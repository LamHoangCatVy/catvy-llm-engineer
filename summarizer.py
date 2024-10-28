import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import streamlit as st
import openai

# Load environment variables in a file called .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')

# A class to represent a Webpage
class Website:
    url: str
    title: str
    text: str

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

# Function to create the system prompt and user prompt
system_prompt = """You are an assistant that analyzes the contents of a website \
and provides a detailed summary for the whole website, including all the knowledge, topics included, even brainstorm questions based on the position of an SA, ignoring text that might be navigation related. \
Respond in markdown.
"""

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}. "
    user_prompt += "The contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Function to summarize the website
def summarize(url):
    website = Website(url)
    response = openai.ChatCompletion.create(
        model = openai_model,  # You can adjust this based on the model available to you
        messages = messages_for(website)
    )
    return response.choices[0].message['content']

# Streamlit app interface
st.title("Summarizer")

# Input field to enter URL
url = st.text_input("Enter the URL of the website you want to summarize:")
with st.sidebar:
    st.header("Lam Hoang Cat Vy")
    st.subheader("IT - Young Talents - VPBank")
    st.write("**Actual working roles:** Business Analyst, System Analyst, CloudOps, Python Developer, Automation Test Developer, Tester")
    st.write("**Email:** vylhc@vpbank.com.vn | catvyisworking@gmail.com")
    st.write("**Contact:** 0898177342")


# If a URL is provided, fetch the summary
if url:
    try:
        st.write("Summarizing the content from:", url)
        summary = summarize(url)
        st.markdown(summary)
        st.download_button(label="📥 Download full response as README", 
            data=summary, 
            file_name=f"{url}.txt", 
            mime="text/plain")

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter a URL to get a summary.")
