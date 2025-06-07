# app.py

import streamlit as st
import streamlit.components.v1 as components
from connect_with_llm import call_openrouter

st.set_page_config(page_title="Conversational Code Assistant", layout="wide")
st.title("💬 AI Code Assistant with OpenRouter")

# Sidebar navigation and language selector
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose a mode:", ["💬 Chat Code Assistant", "📂 Analyze Uploaded Code"])
selected_language = st.sidebar.selectbox("Preferred coding language", ["Python", "JavaScript", "C++", "Java"], key="lang")

# Separate session states for each mode
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "analysis_messages" not in st.session_state:
    st.session_state.analysis_messages = []

# Code rendering
def render_code_block(code, language="text"):
    st.code(code, language=language)

# --- Chat-based Code Assistant ---
if app_mode == "💬 Chat Code Assistant":
    st.header("💬 Chat with AI to generate, explain, or fix code")

    # Display past chat
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            if msg["role"] == "assistant" and "" in msg["content"]:
                content = msg["content"]
                start = content.find("") + 3
                end = content.rfind("```")
                lang = content[start:content.find("\n", start)].strip() or "text"
                code = content[content.find("\n", start)+1:end].strip()
                render_code_block(code, language=lang)
            else:
                st.markdown(msg["content"])

    # User input
    if prompt := st.chat_input("Ask me to generate, explain, or fix code..."):
        # Ensure no repeated prompts are sent
        if not st.session_state.chat_messages or st.session_state.chat_messages[-1]["content"] != prompt:
            st.chat_message("user").markdown(prompt)
            st.session_state.chat_messages.append({"role": "user", "content": prompt})

            # Add reinforced system instruction
            system_msg = {
                "role": "system",
                "content": (
                    "You are an expert code assistant. The user prefers responses in "
                    f"{selected_language}. Only respond to the prompt. If unclear, ask a question."
                )
            }

            # Limit message history for clarity
            recent_messages = st.session_state.chat_messages[-5:]
            messages_to_send = [system_msg] + recent_messages

            with st.chat_message("assistant"):
                try:
                    response = call_openrouter(messages_to_send, temperature=0.2)
                except Exception as e:
                    response = f"❌ Error: {str(e)}"
                st.markdown(response)
                st.session_state.chat_messages.append({"role": "assistant", "content": response})

# --- Code File Analysis ---
elif app_mode == "📂 Analyze Uploaded Code":
    st.header("📂 Upload and Analyze Your Code")
    uploaded_file = st.file_uploader("Upload your code file", type=["py", "js", "cpp", "java", "ts", "rb"])

    if uploaded_file:
        code_content = uploaded_file.read().decode("utf-8")
        file_extension = uploaded_file.name.split(".")[-1]
        st.code(code_content, language=file_extension)

        analysis_type = st.selectbox("Choose analysis type:", [
            "Explain the code",
            "Find bugs or issues",
            "Refactor the code",
            "Add comments to the code"
        ])

        if st.button("Analyze Code"):
            prompt = f"{analysis_type}: \n{code_content}"
            st.session_state.analysis_messages.append({"role": "user", "content": prompt})

            # Strong analysis instruction
            system_msg = {
                "role": "system",
                "content": "You are an expert code analyzer. Provide professional insights based on the user's analysis request."
            }
            messages_to_send = [system_msg] + st.session_state.analysis_messages[-5:]

            with st.chat_message("assistant"):
                try:
                    response = call_openrouter(messages_to_send, temperature=0.2)
                except Exception as e:
                    response = f"❌ Error: {str(e)}"
                st.markdown(response)
                st.session_state.analysis_messages.append({"role": "assistant", "content": response})