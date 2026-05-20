import streamlit as st
import google.generativeai as genai
import config

SYSTEM_PROMPT = """
You are an advanced, intelligent, and highly professional Engineering Career Assistant and Mentor. 
Your goal is to guide students based on their engineering branch, interests, skills, career goals, and preferred technologies.
You support all engineering domains (CSE, AI/ML, Data Science, Cybersecurity, Mechanical, Civil, Electrical, ECE, Robotics, Biotechnology, etc.).
You can provide roadmap guidance, learning paths, project ideas, certification suggestions, GATE/Placement preparation strategies, and internship advice.
Be conversational, professional, friendly, and concise. Format your responses using markdown, bullet points, and bold text for readability.
Do not hallucinate links. If you suggest resources, make sure they are widely known (like Coursera, freeCodeCamp, MIT OCW).
"""

def setup_gemini():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.9,
            "max_output_tokens": 2048,
        }
        
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config=generation_config,
            system_instruction=SYSTEM_PROMPT
        )
        return model
    except Exception as e:
        st.error(f"Failed to initialize Gemini API. Make sure GEMINI_API_KEY is set in .streamlit/secrets.toml. Error: {e}")
        return None

def inject_chat_css():
    st.markdown("""
        <style>
            /* Chat container adjustments */
            .stChatMessage {
                background: rgba(15, 23, 42, 0.4);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 15px 20px;
                margin-bottom: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
            }
            .stChatMessage:hover {
                box-shadow: 0 4px 20px rgba(0, 242, 254, 0.15);
                border-color: rgba(0, 242, 254, 0.3);
            }
            /* User message specific style */
            [data-testid="stChatMessage"]:nth-child(even) {
                background: rgba(0, 242, 254, 0.05);
                border-color: rgba(0, 242, 254, 0.1);
            }
            /* Quick action buttons */
            .quick-btn > button {
                width: 100%;
                background: rgba(30, 41, 59, 0.5) !important;
                border: 1px solid rgba(0, 242, 254, 0.2) !important;
                color: var(--text) !important;
                border-radius: 8px !important;
                padding: 8px !important;
                font-size: 0.85rem !important;
                transition: all 0.2s ease !important;
                text-align: left !important;
                justify-content: flex-start !important;
            }
            .quick-btn > button:hover {
                background: rgba(0, 242, 254, 0.1) !important;
                border-color: var(--primary) !important;
                color: var(--primary) !important;
                transform: translateX(4px);
            }
        </style>
    """, unsafe_allow_html=True)

def render(domains_data):
    st.title("🤖 AI Career Mentor")
    st.markdown("<p style='color: var(--muted); font-size: 1.1rem; max-width: 800px;'>Your personal engineering guide powered by Gemini. Ask me about roadmaps, skills, GATE preparation, internships, and more.</p>", unsafe_allow_html=True)
    
    inject_chat_css()
    
    if "gemini_model" not in st.session_state or st.session_state.gemini_model is None:
        st.session_state.gemini_model = setup_gemini()
        
    if "chat_session" not in st.session_state and st.session_state.gemini_model:
        st.session_state.chat_session = st.session_state.gemini_model.start_chat(history=[])
        
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
        greeting = "Hello! I'm your AI Engineering Mentor. Which branch are you studying, and what are your career goals?"
        st.session_state.messages.append({"role": "assistant", "content": greeting})
    
    with st.sidebar:
        st.markdown("### 💡 Quick Suggestions")
        st.markdown("<p style='font-size: 0.8rem; color: var(--muted);'>Click to ask</p>", unsafe_allow_html=True)
        
        prompts = [
            "Best roadmap for AI Engineer",
            "How to prepare for GATE CSE",
            "Skills needed for Robotics",
            "Best projects for Data Science",
            "Roadmap to become a Cybersecurity Engineer",
            "How to secure a Google Internship"
        ]
        
        clicked_prompt = None
        for p in prompts:
            st.markdown('<div class="quick-btn">', unsafe_allow_html=True)
            if st.button(f"💬 {p}", key=f"btn_{p}"):
                clicked_prompt = p
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown("---")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            if st.session_state.gemini_model:
                st.session_state.chat_session = st.session_state.gemini_model.start_chat(history=[])
            st.rerun()

    for msg in st.session_state.messages:
        avatar = "🤖" if msg["role"] == "assistant" else "🧑‍💻"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])
            
    user_input = st.chat_input("Ask about your engineering career...")
    prompt = clicked_prompt if clicked_prompt else user_input

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)
            
        if st.session_state.gemini_model:
            with st.chat_message("assistant", avatar="🤖"):
                with st.spinner("Analyzing your request..."):
                    try:
                        response = st.session_state.chat_session.send_message(prompt)
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    except Exception as e:
                        error_msg = f"Sorry, I encountered an error: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.warning("AI model is not initialized. Please check your API key configuration.")
