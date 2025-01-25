import os
import streamlit as st
import openai
import pandas as pd
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables in a file called .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Sử dụng mô hình đã được định nghĩa trong .env

# Function to summarize transcript content
def summarize_content(transcript):
    system_prompt = """You are an training expert about security. You are tasked with summarizing lessons on Java. 
    Generate a summary of the main topics covered in the lesson in an easy to understand format but it should be detailed enough for newcomers to learn Java.
    Additionally, generate a few review questions based on the content of the lesson."""
    
    user_prompt = f"Transcript content: {transcript}\n\nSummarize the content and generate a AWS example with review questions."

    response = openai.ChatCompletion.create(
        model=openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message['content']

# Function to process chat-based follow-up questions
def ask_follow_up(question, conversation_history):
    system_prompt = "You are a helpful assistant that provides answers to follow-up questions based on the previous conversation."
    
    # Include conversation history to maintain context
    messages = [{"role": "system", "content": system_prompt}]
    for entry in conversation_history:
        messages.append({"role": entry['role'], "content": entry['content']})
    
    # Add the user's new question to the chat
    messages.append({"role": "user", "content": question})
    
    response = openai.ChatCompletion.create(
        model=openai_model,
        messages=messages
    )
    return response.choices[0].message['content']


# Function to convert the summary content to a README-like text file
def convert_to_text_file(content):
    return content.encode()

# Streamlit app interface
st.title("Java Technical Homies")
# Text area for inputting transcript
transcript = st.text_area("Paste your transcript here")

# Sidebar information
with st.sidebar:
    st.header("Lam Hoang Cat Vy")
    st.subheader("IT - Young Talents - VPBank")
    st.write("**Actual working roles:** Business Analyst, System Analyst, CloudOps, AWS Developer, Automation Test Developer, Tester")
    st.write("**Email:** vylhc@vpbank.com.vn | catvyisworking@gmail.com")
    st.write("**Contact:** 0898177342")

# If transcript is provided, process it
if transcript:
    try:
        # Generate summary, code example, and review questions
        summary_response = summarize_content(transcript)
        st.write("Generated Summary, Code Example, and Review Questions:")
        st.write(summary_response)  # Display the generated content

        # Initialize conversation history
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []
        
        # Add the system's response to the conversation history
        st.session_state.conversation_history.append({"role": "assistant", "content": summary_response})

        # Download the entire summary as a README-like text file
        st.download_button(label="📥 Download full response as README", 
                           data=text_file_data, 
                           file_name="Java-Summary.txt", 
                           mime="text/plain")

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please paste your transcript to generate a summary, code example, and review questions.")
