# 🌍 AI Travel Itinerary Planner System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?style=for-the-badge&logo=kubernetes)

**An intelligent AI-powered travel planner that generates personalized day trip itineraries using LLaMA 3.3 via Groq API**

</div>

---

## ✨ Features

- 🤖 **AI-Powered** — Uses LLaMA 3.3 (70B) via Groq for intelligent itinerary generation
- 🎯 **Personalized** — Tailored itineraries based on your city and interests
- 📅 **Structured Output** — Morning, Afternoon & Evening schedule with tips
- 💬 **Chat History** — Tracks full conversation using LangChain messages
- 🐳 **Dockerized** — Fully containerized for easy deployment
- ☸️ **Kubernetes Ready** — Deployed on GCP using Minikube
- 📊 **ELK Monitoring** — Real-time log monitoring with Filebeat, Logstash, Elasticsearch & Kibana

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Groq + LLaMA 3.3** | AI Brain — Itinerary Generation |
| **LangChain** | LLM Framework & Prompt Management |
| **Streamlit** | Frontend UI |
| **Docker** | Containerization |
| **Kubernetes + Minikube** | Orchestration & Deployment |
| **GCP VM** | Cloud Infrastructure |
| **Filebeat** | Log Collection |
| **Logstash** | Log Processing |
| **Elasticsearch** | Log Storage & Indexing |
| **Kibana** | Log Visualization Dashboard |
| **GitHub** | Source Code Management |

---

## 📁 Project Structure

```
AI_Travel_using_filebeat/
│
├── app.py                  # Streamlit UI
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
│
└── src/
    ├── chains/
    │   └── itinerary_chain.py    # LLM chain logic
    │
    ├── config/
    │   └── config.py             # API keys & model config
    │
    ├── core/
    │   └── planer.py             # TravelPlanner class (main logic)
    │
    └── utils/
        ├── logger.py             # Custom logger
        └── custom_exception.py   # Custom exception handler
```

---

## 🔄 System Architecture

```
User Input (City + Interests)
          ↓
    Streamlit UI (app.py)
          ↓
  TravelPlanner Class (planer.py)
          ↓
  LangChain Prompt Template
          ↓
  Groq API → LLaMA 3.3 (70B)
          ↓
  Generated Itinerary ✅
          ↓
  ┌─────────────────────────┐
  │     ELK Stack           │
  │  Filebeat → Logstash    │
  │  → Elasticsearch        │
  │  → Kibana Dashboard     │
  └─────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Docker
- Groq API Key (Free at [console.groq.com](https://console.groq.com))

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mtoqeer-shahzad/AI_TRAVEL_ITINEARY_PLANNER_SYSTEM.git
cd AI_TRAVEL_ITINEARY_PLANNER_SYSTEM
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\Activate.ps1       # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

Open browser at `http://localhost:8501` 🎉

---

## 🐳 Docker Deployment

```bash
# Build image
docker build -t ai-travel-planner .

# Run container
docker run -p 8501:8501 ai-travel-planner
```

---

## ☸️ Kubernetes Deployment (GCP)

```bash
# Start Minikube
minikube start --driver=docker

# Deploy application
kubectl apply -f k8s/deployment.yaml

# Port forward
kubectl port-forward service/travel-planner 8501:8501
```

---

## 📊 ELK Stack Monitoring

```bash
# Deploy ELK stack
kubectl apply -f k8s/filebeat-deployment.yaml
kubectl apply -f k8s/logstash-deployment.yaml
kubectl apply -f k8s/elasticsearch-deployment.yaml
kubectl apply -f k8s/kibana-deployment.yaml

# Access Kibana Dashboard
kubectl port-forward service/kibana 5601:5601
```

---

## 💡 How It Works

1. **User Input** — Enter city name and interests (comma separated)
2. **Processing** — TravelPlanner class processes input
3. **AI Generation** — LLaMA 3.3 generates personalized itinerary
4. **Output** — Structured day trip plan with Morning/Afternoon/Evening slots
5. **Monitoring** — All logs captured by ELK stack

---

## 📸 Sample Output

```
📅 DAY TRIP ITINERARY — PARIS
🎯 Interests: Art, Food, History

🌅 MORNING (8:00 AM - 12:00 PM)
• 📍 Eiffel Tower — Arrive early to avoid crowds!
• 📍 Louvre Museum — Pre-book tickets online

☀️ AFTERNOON (12:00 PM - 5:00 PM)
• 📍 Notre Dame Cathedral
• 📍 Seine River Walk

🌆 EVENING (5:00 PM - 9:00 PM)
• 📍 Montmartre — Beautiful sunset views!
• 📍 Local French Restaurant

🍽️ MUST TRY: Croissants, Crepes, French Wine
🚗 TRANSPORT: Metro Line 6 recommended
```

---

## 🔧 Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model_name` | `llama-3.3-70b-versatile` | Groq LLM model |
| `temperature` | `0.5` | Creativity level (0-1) |
| `port` | `8501` | Streamlit port |

---

## 👨‍💻 Author

**Muhammad Toqeer**

[![GitHub](https://img.shields.io/badge/GitHub-mtoqeer--shahzad-black?style=flat&logo=github)](https://github.com/mtoqeer-shahzad)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

⭐ **If you found this helpful, please give it a star!** ⭐

</div>
