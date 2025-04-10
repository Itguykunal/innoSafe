# innoSafe

**innoSafe** is a real-time chat monitoring application designed to detect and alert on unsafe or harmful interactions, especially to protect children from online abuse. It leverages NLP and a fine-tuned BERT model to assess the severity of conversations and broadcasts alerts for high-risk behavior.

---

## 🔧 Features

- 🚨 **Real-time Danger Detection** using BERT-based model
- 🧠 **Contextual NLP Analysis** to assess threat levels
- 📈 **Severity Level Classification** (0–10)
- 📡 **Web Interface** for chat monitoring
- 📁 **Chat Logs Archiving**

---

## 📊 Dataset

Our model is trained on a **realistic, hand-crafted dataset** of chat conversations that simulate actual online interactions. The dataset:

- Includes a wide range of age-based conversations (e.g., teens and adults)
- Covers both **safe** and **toxic/inappropriate** dialogues
- Contains severity labels ranging from **0 (safe)** to **10 (highly dangerous)**
- Was designed specifically to detect:
  - **Grooming**
  - **Predatory behavior**
  - **Inappropriate language**
  - **Emotional manipulation**

> 🧪 The dataset is not sourced from public corpora — it is **fully synthetic**, yet modeled on real-world behavioral patterns to ensure practical effectiveness.

---

## 📁 Project Structure

```
INNOSAFE/
├── LocalLink/
│   ├── chatLogs/              # Chat log dataset (realistically generated)
│   ├── node_modules/          # Node.js dependencies
│   ├── public/                # Static assets for frontend
│   ├── package.json           # Node.js config
│   ├── package-lock.json      # Dependency lock
│   ├── README.md              # Project-specific instructions
│   └── server.js              # Node backend server
├── app.py                     # Python-based AI model API
├── BERT3.ipynb                # Jupyter notebook for BERT model experiments
├── CLEANcorpus4.docx          # Clean and labeled training corpus
├── LICENSE                    # Open source license
└── README.md                  # You are here
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

- Ensure Python dependencies are installed (`transformers`, `torch`, `flask`, etc.)
- Node.js is required for running the frontend (`express`, `socket.io`, etc.)
- The system uses a shared interface between `app.py` and `server.js` for real-time interaction and classification
- **OCR is not currently implemented** — all detection is based on text only

---

## 🛡️ Under Development

We are constantly improving innoSafe for better performance, accuracy, and coverage of unsafe conversations. Future improvements will include:

- Multilingual support
- Admin dashboard for parents
- More datasets for diverse training
- Integration with mobile app monitoring

---

## 📄 License

MIT License
