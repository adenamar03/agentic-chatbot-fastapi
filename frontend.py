#Step #1 --> ui setup using streamlit (model provider, model, system_prompt, query and web search)

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("AI CHATBOT AGENTS")
st.write("Create and Interact with AI agents")

system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your prompt here...")

MODEL_NAMES_GROQ=["llama-3.3-70b-versatile","mistral-8x7b-32768"]
MODEL_NAMES_OPENAI=["gpt-4o-mini"]

provider=st.radio("Select Provider:",("Groq","OpenAI"))

if provider=="Groq":
    selected_model=st.selectbox("SELECT GROQ MODEL:", MODEL_NAMES_GROQ)
elif provider=="OpenAI":
    selected_model=st.selectbox("SELECT openai MODEL:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="You can ask Anything :) ")

API_URL="http://127.0.0.1:9999/chat"

if st.button("ASK AGENT !"):
    if user_query.strip():
        import requests
        
# step # 2 ---> connect with backend using url
     

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
            }
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("Agent response")
                    st.markdown(f"**Final Response:** {response_data}")
            else:
                st.error(f"Request failed with status {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to backend. Is FastAPI running on port 9999?")