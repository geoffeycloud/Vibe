Step-by-Step Guide
1. Design the Chatbot’s Personality

Name your bot (e.g., CryptoBuddy).

Define its tone: Friendly, professional, or meme-loving? (e.g., “Hey there! Let’s find you a green and growing crypto!”).

2. Predefined Crypto Data

Use this sample dataset (or create your own):

python

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}  
3. Chatbot Logic

User Inputs: Ask questions like:

“Which crypto is trending up?”

“What’s the most sustainable coin?”

Bot Responses:

Use if-else logic to match queries to data.

Example:

python
if "sustainable" in user_query:  
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])  
    print(f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")  
4. Add Advice Rules

Profitability: Prioritize coins with price_trend = "rising" and market_cap = "high".

Sustainability: Prioritize coins with energy_use = "low" and sustainability_score > 7/10.

5. Test Your Bot

Sample conversation:


You: Which crypto should I buy for long-term growth?  
CryptoBuddy: Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀 

# CO₂ Emissions Analysis and Prediction

## 🌍 SDG Problem
This project addresses SDG 13: Climate Action, analyzing historical CO₂ emissions and predicting future trends to inform policy and awareness.

## 🤖 ML Approach
We used Linear Regression to model historical CO₂ emissions data and predict future emissions over the next 10 years.

## 📊 Results
- R² Score: 0.54 (moderate correlation)
- Emissions predicted to increase steadily if current trends continue

## ⚖️ Ethical Considerations
- Predictions depend heavily on historical data; socioeconomic factors or climate policy changes could disrupt trends
- Important to contextualize findings and avoid overreliance on linear extrapolation

## 📁 Data Source
Kaggle: patricklford/global-co-emissions


# 📘 Practical Implementation Project – Machine Learning, Deep Learning & NLP

This project demonstrates practical applications of machine learning, deep learning, and natural language processing using Python libraries like **scikit-learn**, **TensorFlow/PyTorch**, and **spaCy**. It is divided into three tasks:

---

## 🔹 Task 1: Classical ML with Scikit-learn

**Dataset:** [Iris Species Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
**Goal:** Predict iris flower species using a Decision Tree Classifier.

### ✅ Steps:

* Load and explore the dataset.
* Preprocess the data:

  * Handle missing values (if any).
  * Encode categorical labels.
* Split the data into training and testing sets.
* Train a **Decision Tree Classifier**.
* Evaluate using **accuracy**, **precision**, and **recall**.

### 📦 Deliverable:

* Python script / Jupyter Notebook with code and explanatory comments.

---

## 🔹 Task 2: Deep Learning with TensorFlow or PyTorch

**Dataset:** [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/)
**Goal:** Build a CNN model to classify handwritten digits.

### ✅ Steps:

* Load and normalize the MNIST dataset.
* Build a **Convolutional Neural Network (CNN)** using either TensorFlow or PyTorch.
* Train the model and achieve **>95% test accuracy**.
* Visualize predictions on 5 sample test images.

### 📦 Deliverable:

* Python code showing model architecture, training process, evaluation metrics, and prediction visualizations.


## 🔹 Task 3: NLP with spaCy

**Dataset:** [Amazon Product Reviews – `bittlingmayer/amazonreviews`](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)
**Goal:** Extract product names and brands, and analyze sentiment.

### ✅ Steps:

* Load user reviews from the Amazon review dataset.
* Perform **Named Entity Recognition (NER)** using spaCy to extract:

  * Product names
  * Brand names (ORG, PRODUCT, GPE, etc.)
* Apply a simple **rule-based sentiment analysis** (positive/negative).
* Display the extracted entities and sentiment for each review.


## 🛠️ Requirements

* Python 3.x
* Google collab
* Libraries:

  * `scikit-learn`
  * `pandas`, `numpy`
  * `matplotlib`, `seaborn`
  * `tensorflow` or `torch`
  * `spaCy` (`en_core_web_sm`)
  * `kagglehub`, `bz2` (for Task 3)




## 📌 Notes

* Each task is self-contained and well-commented.
* Datasets are either downloaded from public sources or via `kagglehub`.
* Suitable for coursework or ML/NLP training projects.

  Part 1: Theoretical Analysis (30%)
1. Short Answer Questions

Q1: Explain how AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?

Q2: Compare supervised and unsupervised learning in the context of automated bug detection.

Q3: Why is bias mitigation critical when using AI for user experience personalization?

2. Case Study Analysis

Read the article: AI in DevOps: Automating Deployment Pipelines.

Answer: How does AIOps improve software deployment efficiency? Provide two examples.

Part 2: Practical Implementation (60%)
Task 1: AI-Powered Code Completion

Tool: Use a code completion tool like GitHub Copilot or Tabnine.

Task:

Write a Python function to sort a list of dictionaries by a specific key.

Compare the AI-suggested code with your manual implementation.

Document which version is more efficient and why.

Deliverable: Code snippets + 200-word analysis.

Task 2: Automated Testing with AI

Framework: Use Selenium IDE with AI plugins or Testim.io.

Task:

Automate a test case for a login page (valid/invalid credentials).

Run the test and capture results (success/failure rates).

Explain how AI improves test coverage compared to manual testing.

Deliverable: Test script + screenshot of results + 150-word summary.

Task 3: Predictive Analytics for Resource Allocation

Dataset: Use Kaggle Breast Cancer Dataset.

Goal:

Preprocess data (clean, label, split).

Train a model (e.g., Random Forest) to predict issue priority (high/medium/low).

Evaluate using accuracy and F1-score.

Deliverable: Jupyter Notebook + performance metrics.

Part 3: Ethical Reflection (10%)

Prompt: Your predictive model from Task 3 is deployed in a company. Discuss:

Potential biases in the dataset (e.g., underrepresented teams).

How fairness tools like IBM AI Fairness 360 could address these biases.
