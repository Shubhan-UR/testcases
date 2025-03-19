import streamlit as st
import random

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "weather": "I can't check real-time weather, but it's always a great day to chat!",
        "joke": random.choice([
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised!",
            "Why don’t programmers like nature? It has too many bugs!"
        ]),
        "default": "I'm not sure how to respond to that. Can you try something else?"
    }
    return responses.get(user_input.lower(), responses["default"])

# Streamlit UI
st.title("Enhanced Chatbot")
st.write("Ask me something! I can respond to greetings, jokes, and weather inquiries.")
user_input = st.text_input("You:")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", value=response, height=100, disabled=True)
