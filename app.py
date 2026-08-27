import streamlit as st
from google import genai
from google.genai.types import HttpOptions

# 1. Set up the page title
st.title("🎓 My Personal Study Buddy")
st.caption("Ask me anything! I'm here to help you learn.")

# 2. Initialize the AI and Chat Memory (only runs once)
if "chat" not in st.session_state:
    client = genai.Client(
        api_key="AQ.Ab8RN6IJ8-QRQ2EHv2DatTAv2buFXATkDBsG5jDS6W6tEOTYkA",
        http_options=HttpOptions(api_version="v1")
    )
    st.session_state.chat = client.chats.create(
        model="gemini-3.5-flash",
        config={
            "system_instruction": "You are a friendly, helpful study buddy who explains things simply and encourages learning."
        }
    )
    st.session_state.messages = []

# 3. Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle new user messages
if prompt := st.chat_input("Ask me a question..."):
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI response
    response = st.session_state.chat.send_message(prompt)
    
    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
