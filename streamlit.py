from main import ChatBot
import streamlit as st
import base64

bot = ChatBot()

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
        /* Migros brand colors and styling */
        :root {
            --migros-orange: #FF6600;
            --migros-dark: #333333;
            --light-gray: #f5f5f5;
        }
        
        .stApp {
            background-color: var(--light-gray);
        }
        
        h1, h2, h3 {
            color: var(--migros-dark);
        }
        
        .chat-message-user {
            background-color: #e6f7ff;
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 10px;
            border-left: 5px solid #1E88E5;
        }
        
        .chat-message-assistant {
            background-color: white;
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 10px;
            border-left: 5px solid var(--migros-orange);
        }
        
        .stButton>button {
            background-color: var(--migros-orange);
            color: white;
        }
        
        .welcome-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            border-left: 5px solid var(--migros-orange);
        }
        
        .sidebar-content {
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Migros Chatbot", 
    page_icon=":shopping_trolley:", 
    layout="wide",
)

# Apply custom CSS
local_css()

# Main content area
st.markdown("<h1 style='text-align: center; color: #FF6600;'>Migros Tasty Bytes Chat</h1>", unsafe_allow_html=True)

# Function for generating LLM response
def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Willkommen bei Migros! Wie kann ich Ihnen heute helfen?"}]

# Display welcome message on first load
if len(st.session_state.messages) == 1:
    st.markdown("#### 👋 Willkommen beim Migros Chatbot!")
    st.markdown("Stellen Sie Fragen zum Eistee.")

# Display chat messages with enhanced styling
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧑‍💻" if message["role"] == "user" else "🛒"):
        message_class = "chat-message-user" if message["role"] == "user" else "chat-message-assistant"
        st.markdown(f"<div class='{message_class}'>{message['content']}</div>", unsafe_allow_html=True)

# User-provided prompt
if input := st.chat_input("Stellen Sie Ihre Frage hier..."):
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(f"<div class='chat-message-user'>{input}</div>", unsafe_allow_html=True)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant", avatar="🛒"):
        with st.spinner("Ihre Antwort wird vorbereitet..."):
            response = generate_response(input) 
            st.markdown(f"<div class='chat-message-assistant'>{response}</div>", unsafe_allow_html=True)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)