import streamlit as st
from datetime import datetime

# 1. Page Config & Styling
st.set_page_config(page_title="Velora Chat", page_icon="🟣")

# Custom CSS to match your image (Dark mode, purple bubbles, rounded corners)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    [data-testid="stChatMessage"] {
        border-radius: 20px;
        padding: 10px;
        margin-bottom: 10px;
    }
    /* User message bubble (Purple) */
    [data-testid="user-chat-message"] {
        background-color: #7B61FF !important;
        color: white !important;
    }
    /* App name header style */
    .velora-header {
        color: #FF4B4B;
        font-weight: bold;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Velora Branding
st.markdown('<p class="velora-header">🔴 Velora-v4</p>', unsafe_allow_html=True)

# 3. Connection to Firestore/Database (The "Social" part)
# For now, we use session_state. To make it "Social" for others, 
# you'll connect a DB in Phase 2 below.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Input Area
if prompt := st.chat_input("Message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Placeholder for 'Active now' response logic
    # In a real social app, this would refresh with other users' data
