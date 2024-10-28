import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Initialize OpenAI API (Make sure to replace with your key)
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')

# Set the page layout
st.title("Source Code Analyzer")

# File upload widget
uploaded_file = st.file_uploader("Upload your source code file", type=["py", "js", "java", "cpp", "txt"])

if uploaded_file:
    source_code = uploaded_file.read().decode("utf-8")
    
    # Display the original source code
    st.text_area("Source Code", source_code, height=300)
    
    # Chat functionality to ask questions
    question = st.text_input("Ask about this source code:")
    
    if question:
        # AI explanation for the source code
        response = openai.ChatCompletion.create(
            model=openai_model,  # Ensure to use the correct model name
            messages=[
                {"role": "system", "content": "You are an assistant that explains source code."},
                {"role": "user", "content": f"Explain this source code:\n{source_code}\n\n{question}"}
            ],
            max_tokens=150
        )
        answer = response.choices[0].message["content"]
        st.write(f"AI Response: {answer}")
    
    # Editable source code
    edited_code = st.text_area("Edit Source Code", source_code, height=300)

    # Button to download the modified source code
    st.download_button("Download Edited Code", edited_code.encode("utf-8"), file_name="edited_source_code.py")
