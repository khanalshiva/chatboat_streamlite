import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# .env file बाट API key load गर्ने
load_dotenv()

# Local मा .env बाट, Streamlit Cloud मा secrets बाट key लिने
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Page setup
st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")
st.title("🤖 Simple Q&A Chatbot (Gemini Flash)")
st.write("प्रश्न लेख्नुहोस्, उत्तर पाउनुहोस् — कुनै history/memory छैन।")

# Model select गर्ने
model = genai.GenerativeModel("gemini-3.6-flash")

# User input box
user_question = st.text_input("तपाईंको प्रश्न:")

# Submit button
if st.button("उत्तर पाउनुहोस्"):
    if user_question.strip() == "":
        st.warning("कृपया केही प्रश्न लेख्नुहोस्।")
    else:
        with st.spinner("सोच्दैछु..."):
            # एकदम simple call - कुनै chat session वा history छैन
            response = model.generate_content(user_question)
            st.markdown("### उत्तर:")
            st.write(response.text)