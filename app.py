import streamlit as st
import pandas as pd
import openai

# Load the API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create the dashboard
st.title("📱 Social Media Analytics Dashboard")
st.write("Analyze your social media posts with AI-powered insights.")

# Sample DataFrame
data = pd.DataFrame([
    [1, "reel", 148, 49, 13],
    [2, "reel", 338, 63, 44],
    [3, "image", 238, 98, 136]
], columns=['Post ID', 'Type', 'Likes', 'Shares', 'Comments'])

st.write(data)

# Get GPT insights
if st.button("Get AI Insights"):
    prompt = "Give insights on this social media data"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    st.write(response['choices'][0]['text'])
