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
