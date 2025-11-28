import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to get Gemini response
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

def main():
    st.set_page_config(page_title="AI Chatbot by Arsh", layout="centered")

    st.markdown("""
<style>
/* MAIN APP BACKGROUND */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    
    
}

/* SIDEBAR BACKGROUND */
section[data-testid="stSidebar"] {
    background-image: url("https://images.unsplash.com/photo-1557682250-8a0b8f0f7a44");
    background-size: cover;
    
   
}
</style>
""", unsafe_allow_html=True)
    
    st.markdown("""
<style>
/* SIDEBAR DARK FROSTED GLASS EFFECT */
section[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.4); /* dark semi-transparent overlay */
    backdrop-filter: blur(5px); /* subtle blur */
    -webkit-backdrop-filter: blur(5px); /* Safari support */
    border-radius: 10px; /* optional rounded corners */
    color: white; /* make text readable */
}
</style>
""", unsafe_allow_html=True)
    
    st.markdown("""
<style>
/* Clear Chat button text color */
div.stButton > button:first-child {
    color: black; /* text color */
    font-weight: bold; /* optional, makes it stand out */
}
</style>
""", unsafe_allow_html=True)


    st.markdown("""
<style>
/* 3D Ice Diamond Button with Glow */
div.stButton > button:first-child {
    background: linear-gradient(145deg, #a8f0ff, #d4f9ff, #ffffff, #b0e0ff);
    background-size: 400% 400%;
    color: #000000;
    font-weight: bold;
    border: 2px solid rgba(255,255,255,0.6); /* outline glow */
    border-radius: 15px;
    padding: 12px 25px;
    cursor: pointer;
    box-shadow: 
        0 5px 15px rgba(0,0,0,0.3), /* depth shadow */
        0 0 15px rgba(255,255,255,0.6) inset, /* inner glow */
        0 0 15px rgba(0,200,255,0.5); /* subtle outer glow */
    transition: all 0.4s ease, background-position 4s ease;
    font-size: 16px;
    text-shadow: 0 1px 2px rgba(255,255,255,0.8);
}

/* Hover effect: lift + glow intensify */
div.stButton > button:first-child:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 
        0 8px 20px rgba(0,0,0,0.4),
        0 0 25px rgba(255,255,255,0.8) inset,
        0 0 25px rgba(0,200,255,0.8); /* stronger outer glow */
    background-position: 100% 0%;
}

/* Animate gradient continuously */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

div.stButton > button:first-child {
    animation: gradientBG 8s ease infinite;
}
</style>
""", unsafe_allow_html=True)


    st.markdown("""
<style>
/* Chat input bar: dark red theme */
div.stTextInput > div > input {
    background: rgba(50, 0, 0, 0.85); /* dark red semi-transparent */
    border: 2px solid rgba(255, 50, 50, 0.8); /* red border */
    border-radius: 12px;
    padding: 12px 15px;
    font-size: 16px;
    color: #fff; /* white text */
    box-shadow: inset 0 0 8px rgba(255,50,50,0.5);
    transition: all 0.3s ease;
    outline: none;
}

/* Hover effect */
div.stTextInput > div > input:hover {
    box-shadow: inset 0 0 12px rgba(255,50,50,0.7), 0 0 8px rgba(255,50,50,0.5);
    border-color: rgba(255,100,100,0.9);
}

/* Focus effect */
div.stTextInput > div > input:focus {
    box-shadow: inset 0 0 16px rgba(255,50,50,0.8), 0 0 12px rgba(255,100,100,0.6);
    border-color: rgba(255,100,100,1);
    background: rgba(70, 0, 0, 0.95);
}

/* Placeholder color */
div.stTextInput > div > input::placeholder {
    color: rgba(255,200,200,0.7);
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)




    # ✅ SIDEBAR PAPER-FOLD ANIMATION
    st.markdown("""
    <style>
    /* SIDEBAR PAPER-FOLD ANIMATION */
    section[data-testid="stSidebar"] {
        transform-origin: left center;
        transform: rotateY(-90deg);
        opacity: 0;
        animation: foldIn 0.8s ease-out forwards;
    }

    @keyframes foldIn {
        0% {
            transform: rotateY(-90deg);
            opacity: 0;
        }
        50% {
            transform: rotateY(-30deg);
            opacity: 0.5;
        }
        100% {
            transform: rotateY(0deg);
            opacity: 1;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
<style>

/* 🕷️ HORROR CLEAR CHAT BUTTON (NO RED, NO GLOW) */
div.stButton > button:first-child {
    position: relative;
    background: linear-gradient(135deg, #2e2e2e, #444444, #5a5a5a);
    color: #ffffff;
    font-weight: bold;
    border-radius: 14px;
    padding: 12px 26px;
    border: 2px solid #777777;
    cursor: pointer;
    text-shadow: none;
    box-shadow: 
        0 6px 14px rgba(0,0,0,0.5),
        inset 0 0 12px rgba(255,255,255,0.15);
    overflow: hidden;
    transition: all 0.3s ease;
}

/* 🕸️ WEB OVERLAY */
div.stButton > button:first-child::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
      radial-gradient(circle at top left, rgba(255,255,255,0.25), transparent 40%),
      radial-gradient(circle at bottom right, rgba(255,255,255,0.18), transparent 40%);
    opacity: 0.35;
    pointer-events: none;
}

/* 🕷️ SPIDER (RED ONLY) */
div.stButton > button:first-child::after {
    content: "🕷️";
    position: absolute;
    top: -20px;
    right: 8px;
    font-size: 22px;
    animation: spiderDrop 2.5s infinite ease-in-out;

    /* ✅ RED SPIDER EFFECT */
    filter: drop-shadow(0 0 2px red)
            drop-shadow(0 0 4px red)
            drop-shadow(0 0 6px darkred);
}

/* 🕷️ Spider movement */
@keyframes spiderDrop {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(18px); }
    100% { transform: translateY(0); }
}

/* 😱 HORROR HOVER SHAKE */
div.stButton > button:first-child:hover {
    animation: shake 0.25s infinite;
    box-shadow:
        0 10px 22px rgba(0,0,0,0.7),
        inset 0 0 18px rgba(255,255,255,0.2);
    background: linear-gradient(135deg, #3a3a3a, #5a5a5a);
}

/* 😱 Shake animation */
@keyframes shake {
    0% { transform: translateX(0); }
    25% { transform: translateX(-2px); }
    50% { transform: translateX(2px); }
    75% { transform: translateX(-2px); }
    100% { transform: translateX(0); }
}

</style>
""", unsafe_allow_html=True)


    st.markdown("<h1 style='text-align: center;'>🗨️AI Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'> By 🌊Arsh ALi Azam🌊</h3>", unsafe_allow_html=True)

    # Chatbot personality selector
    personality = st.sidebar.selectbox(
        "Select Chatbot Personality",
        ("Sakura", "Beerus'God of Disturction'", "Vegeta")
    )
    st.sidebar.write(f"Current personality: {personality}")

    # Initialize all conversations
    if "all_conversations" not in st.session_state:
        st.session_state.all_conversations = []

    # Initialize current chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Clear Chat = Save current chat + start a new one
    if st.sidebar.button("Clear Chat {New Conversation}"):
        if st.session_state.messages:
            st.session_state.all_conversations.append(st.session_state.messages)
        st.session_state.messages = [] 
        st.session_state.current_prompt_behavior = ""
        st.rerun() 

    # Sidebar: Show all past saved conversations
    st.sidebar.markdown("### 📁 Saved Conversations")

    if st.session_state.all_conversations:
        for idx, convo in enumerate(st.session_state.all_conversations, start=1):
            preview = convo[0]["content"][:30]
            with st.sidebar.expander(f"💬 Conversation {idx}: {preview}"):
                for msg in convo:
                    role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
                    st.write(f"**{role}:** {msg['content']}")
    else:
        st.sidebar.write("No saved conversations yet.")

    # Initialize behavior instructions
    if "current_prompt_behavior" not in st.session_state:
        st.session_state.current_prompt_behavior = ""

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask me Buddy😪"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)

        behavior_instruction = f"Befriendly and respond like a {personality} chatbot."

        if st.session_state.current_prompt_behavior != behavior_instruction:
            full_gemini_prompt = f"{behavior_instruction}\n\n{prompt}"
            st.session_state.current_prompt_behavior = behavior_instruction
        else:
            full_gemini_prompt = prompt

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            with st.spinner("Thinking..."):
                full_response = get_gemini_response(full_gemini_prompt)

            timestamp = datetime.now().strftime("%I:%M %p")
            styled_response = f"**{full_response}**  \n\n*{timestamp}*"
            message_placeholder.markdown(styled_response)

            st.session_state.messages.append(
                {"role": "assistant", "content": styled_response}
            )

if __name__ == "__main__":
    main()
