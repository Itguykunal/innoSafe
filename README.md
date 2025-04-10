```markdown
# LocalLink - innoSafe

**innoSafe** is a real-time chat monitoring application designed to detect and alert on unsafe or harmful interactions, especially to protect children from online abuse. It leverages NLP and machine learning to assess the severity of conversations and integrates OCR to extract text from images.

---

## 🔧 Features

- 🚨 **Real-time Danger Detection** using BERT-based model
- 🧠 **Contextual NLP Analysis** to assess threat levels
- 👁️ **OCR Integration** to detect harmful content in images
- 📈 **Severity Level Classification** (0–10)
- 📡 **Web Interface** for chat monitoring
- 📁 **Chat Logs Archiving**

---

## 📁 Project Structure

```
LocalLink/
│
├── chatLogs/               # Stored chat conversations
├── node_modules/           # Node.js dependencies
├── public/                 # Static frontend assets
│
├── package.json            # Node.js project config
├── package-lock.json       # Node.js dependency lock file
│
├── server.js               # Node.js server for frontend/backend API
├── app.py                  # Python backend handling ML inference
├── BERT3.ipynb             # Model training notebook (BERT)
├── CLEANcorpus4.docx       # Dataset file for chat training
│
├── LICENSE                 # Project license
└── README.md               # This file
```

---

## 🚀 How to Run

### 1. Train the BERT Model

First, train the classification model using the notebook:

```bash
# Open the notebook and execute cells
jupyter notebook BERT3.ipynb
```

### 2. Run the Python Backend (Model Inference)

Start the backend server that handles conversation classification:

```bash
python app.py
```

### 3. Start the Node.js Server (Frontend/API)

Launch the Node.js server to serve the frontend and expose APIs:

```bash
node server.js
```

---

## 📌 Notes

- Ensure Python dependencies are installed (`transformers`, `torch`, `flask`, etc.).
- Node.js is required for running the frontend (`express`, etc.).
- The system uses a shared interface between `app.py` and `server.js` for real-time interaction and classification.
- Under development, more features to be added soon.

---

## 🛡️ Under Development

We are constantly improving innoSafe for better performance, accuracy, and coverage of unsafe conversations. Future improvements will include:

- Multilingual support
- Advanced OCR filtering
- Parent/admin dashboard
- More datasets for diverse training

---

## 📄 License

MIT License
```