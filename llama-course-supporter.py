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
    system_prompt = """You are an assistant tasked with summarizing lessons on Llama programming. 
    Generate a summary of the main topics covered in the lesson and provide a basic Llama code example.
    Additionally, generate a few review questions based on the content of the lesson."""
    
    user_prompt = f"Transcript content: {transcript}\n\nSummarize the content and generate a Llama example with review questions."

    response = openai.ChatCompletion.create(
        model=openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message['content']

# Function to convert questions into a pandas DataFrame
# Function to convert the summary content to a README-like text file
def convert_to_text_file(content):
    return content.encode()

# Streamlit app interface
st.title("Tool summarizer script Llama")

# Text area for inputting transcript
transcript = st.text_area("Paste your transcript here")

# If transcript is provided, process it
if transcript:
    try:
        # Generate summary, code example, and review questions
        summary_response = summarize_content(transcript)
        st.write("Generated Summary, Code Example, and Review Questions:")
        st.write(summary_response)  # Display the generated content
        
        # Assuming the response contains questions at the end, you can manually extract and create a DataFrame
        # For example, splitting questions from the response (customize if needed)
        if "Questions:" in summary_response:
            questions = summary_response.split("Questions:")[1].strip() 
                   
        # Download the entire summary as a README-like text file
        text_file_data = convert_to_text_file(summary_response)
        st.download_button(label="📥 Download full response as README", 
                           data=text_file_data, 
                           file_name="README.txt", 
                           mime="text/plain")

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please paste your transcript to generate a summary, code example, and review questions.")
