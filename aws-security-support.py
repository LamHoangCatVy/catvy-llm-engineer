import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load environment variables in a file called .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Use the model defined in .env

# Function to summarize transcript content with streaming
def summarize_content(transcript):
    system_prompt = """You are a training expert about security. You are tasked with summarizing lessons on AWS about security specialty certification. 
    Generate a summary of the main topics covered in the lesson in an easy-to-understand format, but it should be detailed enough for the user to pass the exam and provide a basic AWS code example.
    Additionally, generate a few review questions based on the content of the lesson."""
    
    user_prompt = f"Transcript content: {transcript}\n\nSummarize the content and generate an AWS example with review questions."

    # Placeholder in Streamlit for streaming response
    response_placeholder = st.empty()
    reply = ""

    # Stream the response
    for chunk in openai.ChatCompletion.create(
        model=openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        stream=True
    ):
        # Check if content exists in the chunk
        if 'content' in chunk.choices[0].delta:
            reply += chunk.choices[0].delta.content
            response_placeholder.markdown(reply.replace("```", "").replace("markdown", ""))

# Streamlit app interface
st.title("Tool Summarizer Script AWS")
transcript = st.text_area("Paste your transcript here")

# Sidebar information
with st.sidebar:
    st.header("Lam Hoang Cat Vy")
    st.subheader("IT - Young Talents - VPBank")
    st.write("**Roles:** Business Analyst, System Analyst, CloudOps, AWS Developer, etc.")
    st.write("**Email:** vylhc@vpbank.com.vn | catvyisworking@gmail.com")
    st.write("**Contact:** 0898177342")

# Process if transcript is provided
if transcript:
    try:
        st.write("Generating Summary, Code Example, and Review Questions:")
        summarize_content(transcript)  # Streamed summary display

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please paste your transcript to generate a summary, code example, and review questions.")
