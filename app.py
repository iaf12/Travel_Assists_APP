import streamlit as st
import backend  # This imports the backend code
import pandas as pd

################### Streamlit Interface ###################
def main():
    st.title("Travel Chatbot Assistant")

    st.write("""
    Welcome to your personal travel assistant! Ask me about flights, hotels, trip planning, or general travel inquiries, and I'll help you find the information you need.
    """)

    # Initialize the conversation
    if 'history' not in st.session_state:
        st.session_state.history = []

    # User input for chat
    user_input = st.text_input("You: ", placeholder="Ask me anything related to travel...")

    # If the user submits input
    if st.button("Send"):
        if user_input:
            # Classify the query (using the backend function)
            query_type = backend.classify_travel_query(user_input)

            # Respond based on classification
            if query_type == 'general':
                response = backend.general(user_input)
            elif query_type == 'plan':
                response = backend.plan(user_input)
            elif query_type == "flight":
                response = backend.flight(user_input)
            elif query_type == "hotel":
                response = backend.hotel(user_input)
            else:
                response = "Sorry, I couldn't classify your query. Please ask again."

            # Append to session state history
            st.session_state.history.append(f"You: {user_input}")
            st.session_state.history.append(f"Assistant: {response}")

    # Display conversation history
    for message in st.session_state.history:
        if isinstance(message, pd.DataFrame):
            st.dataframe(message)  # Display DataFrame results properly
        else:
            st.write(message)

if __name__ == '__main__':
    main()
