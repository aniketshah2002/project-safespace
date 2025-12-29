# 🛡️ SafeSpace: Agentic AI Content Moderator for Children's Storytelling

> **An intelligent, context-aware API designed to ensure safe and educational interactions between children and Generative AI tools.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

## 📖 Overview

As Generative AI becomes central to children's entertainment, standard "Block/Allow" filters are no longer sufficient. **SafeSpace** is an **Agentic AI Middleware** designed to sit between a child's prompt and a Generative AI model (like DALL-E or GPT).

Instead of simply rejecting unsafe inputs, SafeSpace acts as an **educational coach**. It identifies specific unsafe categories (Violence, Scary Themes, Bullying) and provides **constructive, agentic suggestions** to guide the child toward positive storytelling.

### 🚀 Key Features

* **Multi-Class Threat Detection:** Classifies content into specific categories: *Safe, Violence, Scary Theme, Bullying, Sexual Content*.
* **Agentic Feedback Loop:** Unlike static filters, it returns actionable suggestions to "fix" the story (e.g., transforming "fighting" into "resolving a conflict").
* **High-Performance API:** Built with **FastAPI** for low-latency integration into real-time applications.
* **Explainable AI:** Provides confidence scores and clear categorization logic.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **API Framework:** FastAPI (Asynchronous Server)
* **Machine Learning:** Scikit-Learn (Logistic Regression with TF-IDF Vectorization)
* **Data Processing:** Pandas, NumPy
* **Server:** Uvicorn

---

## ⚡ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/aniketshah2002/project-safespace.git](https://github.com/aniketshah2002/project-safespace.git)
cd project-safespace

2. Install Dependencies
pip install fastapi uvicorn scikit-learn pandas

3. Train the Model
python train_model.py
Output: "Models trained and saved successfully!"

4. Run the API Server
uvicorn main:app --reload
The API will be live at http://127.0.0.1:8000.

🔌 API Usage
You can test the API using the interactive Swagger UI at http://127.0.0.1:8000/docs, or use curl.
POST /analyze
{
  "text": "The monster punched the villager in the face."
}

Example Response (Agentic Output)
{
  "text": "The monster punched the villager in the face.",
  "is_safe": false,
  "confidence_score": 0.89,
  "flagged_category": "Violence",
  "message": "Hold on! This looks a bit too violent. How can they solve this without fighting?",
  "agent_suggestion": "Try using words like 'helped' or 'rescued' instead."
}
🧠 Project Architecture
Input Layer: Receives raw text from the user.

Vectorization: Converts text to numerical format using TF-IDF.

Classification:

Model A (Binary): Determines if the content is Safe vs. Unsafe.

Model B (Categorical): Determines the specific issue (Violence, Bullying, etc.).

Agentic Logic: Maps the identified category to a repository of educational, child-psychology-aligned suggestions.

Response: Returns a JSON object with the verdict and guidance.

🔮 Future Improvements
Transformer Integration: Upgrade the classification backend to use BERT/DistilBERT for deeper contextual understanding.

LLM-Based Suggestions: Replace rule-based suggestions with a small LLM to generate dynamic, story-specific rewrites.

Feedback Loop: Implement a mechanism to log user corrections to improve the model over time.

👨‍💻 Author
[Aniket Shah] AI & Machine Learning Engineer [https://www.linkedin.com/in/aniketcu/]
