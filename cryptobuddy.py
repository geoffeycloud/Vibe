# CryptoBuddy - Your AI-Powered Financial Sidekick

# Step 1: Predefined Cryptocurrency Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Step 2: Greeting Message
def greet():
    print("🤖 CryptoBuddy: Hey there! I'm your AI-powered financial sidekick! 💰")
    print("Ask me about trending cryptos, sustainability, or what to invest in for the long term!")
    print("Type 'exit' or 'bye' to end the chat.\n")

# Step 3: Response Logic Based on User Query
def respond(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🤖 CryptoBuddy: Go with {recommend}! 🌱 It’s eco-friendly and has long-term potential!\n")

    elif "trending" in user_query or "rising" in user_query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"🤖 CryptoBuddy: These coins are trending up 📈: {', '.join(trending_coins)}\n")

    elif "long-term" in user_query or "buy" in user_query:
        found = False
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 7:
                print(f"🤖 CryptoBuddy: {coin} is trending up and has a top-tier sustainability score! 🚀\n")
                found = True
                break
        if not found:
            print("🤖 CryptoBuddy: Hmm... Nothing matches that perfectly, but Ethereum is a safe bet. 💡\n")

    elif "energy" in user_query:
        eco_friendly = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        print(f"🤖 CryptoBuddy: These coins use the least energy ⚡: {', '.join(eco_friendly)}\n")

    else:
        print("🤖 CryptoBuddy: Sorry, I didn’t catch that! Ask me about sustainability, trends, or what to invest in.\n")

# Step 4: Chat Loop
def chat():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🤖 CryptoBuddy: See ya! Keep investing smart! 💸")
            break
        respond(user_input)

# Start the chatbot
chat()
