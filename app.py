import os
import torch
import time
from flask import Flask, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from threading import Thread

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  

SIDE_1_PATH = os.path.join(BASE_DIR, "LocalLink", "chatLogs", "1.txt")  
SIDE_2_PATH = os.path.join(BASE_DIR, "LocalLink", "chatLogs", "2.txt")  
OUTPUT_FILE_PATH = os.path.join(BASE_DIR, "LocalLink", "chatLogs", "Severity.txt")  
ALERT_FILE_PATH = os.path.join(BASE_DIR, "LocalLink", "chatLogs", "alert.txt")  
MODEL_PATH = os.path.join(BASE_DIR, "results", "distilbert-severity-classifier")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH).to(device)
model.eval()

def classify_messages():
    try:
        results = []
        file_changed = False  

        for file_path in [SIDE_1_PATH, SIDE_2_PATH]:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                
                results.append(f"=== Messages from {os.path.basename(file_path)} ===\n")
                for line in lines:
                    line = line.strip()
                    if line:
                        inputs = tokenizer(line, padding="max_length", truncation=True, return_tensors="pt").to(device)
                        with torch.no_grad():
                            outputs = model(**inputs)
                        prediction = torch.argmax(outputs.logits, dim=-1).item()
                        results.append(f"Message: {line}\nSeverity: {prediction}\n")
                        file_changed = True  

        if file_changed:
            with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as output_file:
                output_file.writelines(results)

    except Exception as e:
        print(f"Error during classification: {e}")

def update_alert_file():
    try:
        if os.path.exists(OUTPUT_FILE_PATH):
            with open(OUTPUT_FILE_PATH, "r", encoding="utf-8") as severity_file:
                lines = severity_file.readlines()

            severity_levels = [int(line.split(":")[1].strip()) for line in lines if line.startswith("Severity:")]
            if severity_levels:
                with open(ALERT_FILE_PATH, "w", encoding="utf-8") as alert_file:
                    alert_file.write(f"{max(severity_levels)}\n")

    except Exception as e:
        print(f"Error updating alert file: {e}")

def monitor_files():
    last_modified_1 = os.path.getmtime(SIDE_1_PATH) if os.path.exists(SIDE_1_PATH) else 0
    last_modified_2 = os.path.getmtime(SIDE_2_PATH) if os.path.exists(SIDE_2_PATH) else 0

    while True:
        time.sleep(1)  
        new_modified_1 = os.path.getmtime(SIDE_1_PATH) if os.path.exists(SIDE_1_PATH) else 0
        new_modified_2 = os.path.getmtime(SIDE_2_PATH) if os.path.exists(SIDE_2_PATH) else 0

        if new_modified_1 != last_modified_1 or new_modified_2 != last_modified_2:
            print("Change detected! Running classification...")
            classify_messages()
            update_alert_file()  # 🔹 Now it updates alert.txt automatically
            print("Classification done. Check Severity.txt and alert.txt")
            last_modified_1 = new_modified_1
            last_modified_2 = new_modified_2

@app.route("/run", methods=["GET"])
def run_classification():
    classify_messages()
    update_alert_file()
    return jsonify({"message": "Classification completed"})

if __name__ == "__main__":
    Thread(target=monitor_files, daemon=True).start()
    app.run(host="0.0.0.0", port=5050)
