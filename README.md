# 🤖 AI Conversational Agent: Open-Source LLM Integration
(# [My OpenSource AI])
![Interface Demo](./screenshots/chatbot_demo.png)


## 📌 Project Overview
This repository contains a full-stack implementation of a conversational AI chatbot. The system utilizes a distilled Large Language Model (LLM) to generate human-like responses in real-time via a web-based interface. 

The primary objective of this project was to bridge the gap between raw machine learning models and a user-facing application, implementing a complete end-to-end NLP (Natural Language Processing) pipeline.

---

## ⚙️ Technical Architecture

### 1. The AI Core (The Brain)
The application is powered by the **`facebook/blenderbot-400M-distill`** model.
- **Architecture:** A Sequence-to-Sequence (Seq2Seq) Transformer.
- **Capability:** Optimized for open-domain conversation, allowing the bot to maintain a persona and handle diverse topics.
- **Distillation:** By using a distilled model, the application achieves a high balance between inference speed and response quality, making it viable for local execution.

### 2. The NLP Pipeline
Every interaction follows a strict professional pipeline:
**`User Input`** $\rightarrow$ **`Tokenization`** $\rightarrow$ **`Context Injection`** $\rightarrow$ **`Model Inference`** $\rightarrow$ **`Detokenization`** $\rightarrow$ **`UI Rendering`**

- **Contextual Memory:** The bot implements a "Sliding Window" memory system, keeping track of the last 6 conversational turns to ensure continuity and coherence.
- **Sampling Strategy:** To prevent robotic responses, I implemented **Nucleus Sampling (Top-P)** and **Temperature scaling**, allowing the model to be creative yet grounded.

### 3. The Tech Stack
| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript | Responsive UI & Asynchronous API calls |
| **Backend** | Python, Flask | API Routing & Model Management |
| **AI Engine** | PyTorch, Transformers | Model Loading, Tokenization & Generation |
| **Environment** | venv, pip | Dependency Isolation & Version Control |

---

## 🚀 Installation & Local Setup

Follow these steps to deploy the chatbot on your local machine.

### 📋 Prerequisites
- Python 3.10+ installed.
- Minimum 8GB RAM.

### 🛠 Step-by-Step Guide
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Amritanshkumarpandey/my-ai-chatbot.git 
   cd my-ai-chatbot
