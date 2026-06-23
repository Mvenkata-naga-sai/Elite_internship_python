import nltk
import random
from nltk.tokenize import TreebankWordTokenizer

# Initialize tokenizer (no punkt needed)
tokenizer = TreebankWordTokenizer()

# Knowledge Base (intents & responses)
knowledge_base = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm fine, thanks!", "Doing great!", "All good!"],
    "your name": ["I'm your NLP chatbot.", "You can call me SmartBot."],
    "what is python": ["Python is a programming language.", "Python is used for AI, web, and more."],
    "what is ai": ["AI means Artificial Intelligence."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day."]
}

# Preprocessing using NLP (Tokenization)
def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    return tokens

# Response Generator
def get_response(user_input):
    tokens = preprocess(user_input)

    for key in knowledge_base:
        key_tokens = preprocess(key)

        # NLP matching (intent detection)
        if set(key_tokens).issubset(set(tokens)):
            return random.choice(knowledge_base[key])

    return "Sorry, I don't understand. Can you rephrase?"

# Chatbot Loop
def chatbot():
    print("🤖 NLP Chatbot is running! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)

# Run chatbot
if __name__ == "__main__":
    chatbot()