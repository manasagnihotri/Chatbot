import streamlit as st

def basic_chatbot(question):
    question = question.lower()  # Convert input to lowercase for easier comparison

    if "hello" in question or "hi" in question:
        return "Hi there! How can I help you today?"

    elif "how are you" in question:
        return "I'm just a chatbot, but I'm doing well! How about you?"

    elif "bye" in question or "goodbye" in question:
        return "Goodbye! Have a great day!"

    elif "what is your name" in question:
        return "I'm a basic chatbot."

    else:
        return "I'm sorry, I don't understand that. Can you ask something else?"

# Streamlit UI
st.title("Basic Chatbot")
st.write("Welcome! Type your questions below.")

user_input = st.text_input("You: ")  # User input field

if st.button("Ask"):
    if user_input.strip() != "":
        response = basic_chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100)
    else:
        st.warning("Please ask something!")
