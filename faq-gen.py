import os
import docx
import pandas as pd
import streamlit as st
import openai
from io import BytesIO
from dotenv import load_dotenv
import re

# Load environment variables from a .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai_model = "gpt-4o-mini"  # You can set your model here

# Function to extract text from a DOCX file
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

# Function to generate FAQ based on document content
def generate_faq(doc_content):
    system_prompt = """You are an assistant that creates FAQs from documents. You always use Vietnamese. You must generate a list of questions \
and answers based on the content of the provided document. The questions should be concise and directly related to the context, and the answers should be derived strictly from the text."""
    
    user_prompt = f"""Document content:\n\n{doc_content}\n\nGenerate FAQs based on this document. Format it in json so that I can load from dataframe. Only return faq_data."""

    response = openai.ChatCompletion.create(
        model=openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    # Split the generated text into questions and answers
    faqs = response.choices[0].message['content'].strip().split("\n")
    faq_data = []
    for i in range(0, len(faqs), 2):
        if i + 1 < len(faqs):
            question = faqs[i].replace("Q: ", "")
            answer = faqs[i + 1].replace("A: ", "")
            faq_data.append([question, answer])
    return faq_data

# Function to convert the FAQ  into a DataFrame
def create_faq_dataframe(faq_data):
    faq_data = str(faq_data)
    # Use regex to find all questions and answers
    questions = re.findall(r'"question": "(.*?)"', faq_data)
    answers = re.findall(r'"answer": "(.*?)"', faq_data)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Question': questions,
        'Answer': answers
    })
    
    return df


# Function to convert DataFrame to Excel for download
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='FAQ')
        writer.close()
    processed_data = output.getvalue()
    return processed_data

# Streamlit app interface
st.title("FAQ Generator from Document")

# Upload DOCX file
docx_file = st.file_uploader("Upload a DOCX file", type="docx")

# If a DOCX file is uploaded, read and process it
if docx_file is not None:
    try:
        # Extract the text from the DOCX file
        doc_content = extract_text_from_docx(docx_file)
        st.write("Extracting content from the DOCX file...")
        
        # Generate FAQ
        faq_data = generate_faq(doc_content)
        st.write("FAQ faq_data", faq_data)
        # Create DataFrame from FAQ data
        df = create_faq_dataframe(faq_data)
        
        # Display the editable table
        edited_df = st.data_editor(df, use_container_width=True)
        
        # Convert the edited DataFrame to Excel for download
        excel_data = convert_df_to_excel(edited_df)
        st.download_button(label="Download FAQ as Excel", 
                           data=excel_data, 
                           file_name="faq.xlsx", 
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please upload a DOCX file to generate FAQs.")
