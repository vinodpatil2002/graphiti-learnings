
# 📊 Graphiti GST Fraud Detection (AI + Graph DB)

This project demonstrates an AI-powered GST fraud detection system using:

* 🧠 LLM (via Ollama)
* 🔗 Graph Database (Neo4j)
* 🧾 Graphiti Memory Engine
* 🔍 Semantic search over investigation data

---

## 🚀 Features

* Store investigation data as **episodes**
* Automatically build **graph relationships**
* Detect suspicious patterns (dealer clusters, fake billing, etc.)
* Perform **natural language search** over stored data
* Fully local LLM support via **Ollama**

---

## 🛠️ Tech Stack

* Python (Async)
* Neo4j (Graph Database)
* Graphiti Core
* Ollama (LLM + embeddings)
* dotenv (env management)

---

## 📁 Project Structure

```
GRAPHITI_GST/
│
├── gst_memory.py        # Main script
├── llm_cache/           # Cached LLM responses (ignored)
├── venv/                # Virtual environment (ignored)
├── .env                 # Secrets (ignored)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/graphiti-gst.git
cd graphiti-gst
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup `.env`

Create a `.env` file:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_API_KEY=ollama
```

---

## 🧠 Start Required Services

### 🔹 Start Neo4j

Make sure Neo4j is running locally:

* Default: `bolt://localhost:7687`
* Username: `neo4j`
* Password: (your password)

---

### 🔹 Start Ollama

Run:

```bash
ollama serve
```

Pull required models:

```bash
ollama pull mistral
ollama pull nomic-embed-text
```

---

## ▶️ Run the Project

```bash
python gst_memory.py
```

---

## 🔍 Example Query

The system runs:

```text
Which dealers are suspicious in Karnataka?
```

And returns relevant insights from stored investigation episodes.

---

## 📌 What This Project Does

* Converts investigation notes into structured **graph knowledge**
* Links dealers based on:

  * Similarity
  * Invoice patterns
  * Registration anomalies
* Uses embeddings + LLM to enable **intelligent search**

---

## ⚠️ Important Notes

* `.env`, `venv/`, `llm_cache/` are ignored in Git
* Never commit API keys or passwords
* If exposed → rotate credentials immediately

---

## 🚀 Future Improvements

* Web dashboard for visualization
* Real-time fraud detection pipeline
* Integration with GST datasets
* Graph analytics (centrality, clustering)
* Alert system for high-risk dealers

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 📬 Contact

* GitHub: [https://github.com/vinodpatil2002](https://github.com/vinodpatil2002)
* LinkedIn: [https://linkedin.com/in/vinod-n-patil](https://linkedin.com/in/vinod-n-patil)

---

## ⭐ If you like this project

Give it a star ⭐ — helps a lot!

---

If you want next:

