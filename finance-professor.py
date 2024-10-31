import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Model defined in .env

# Define the system prompt for finance education
system_prompt = """You are a finance professor who explains every term in simple language. For each term, provide:
- A clear, simple but detailed definition
- Related concepts and terms
- Real-world use cases
- Include LaTeX for any formulas (e.g., RSI = 100 - \\left( \\frac{100}{1 + RS} \\right))
- Practical examples"""

# Initialize session state for conversation history
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = [
        {"role": "system", "content": system_prompt}
    ]

# Function to get a response from OpenAI
def get_response(user_input):
    st.session_state["conversation_history"].append({"role": "user", "content": user_input})
    
    # Send the entire conversation history to OpenAI
    response = openai.ChatCompletion.create(
        model=openai_model,
        messages=st.session_state["conversation_history"]
    )
    
    # Get the response content
    response_content = response.choices[0].message['content']
    st.session_state["conversation_history"].append({"role": "assistant", "content": response_content})
    
    return response_content

# Streamlit app interface
st.title("Finance Professor Chatbot")
latex=st.latex(r"RSI = 100 - \left( \frac{100}{1 + RS} \right)")
st.write(latex)
# Sidebar contact information
with st.sidebar:
    st.header("Lam Hoang Cat Vy")
    st.subheader("IT - Young Talents - VPBank")
    st.write("**Actual working roles:** Business Analyst, System Analyst, CloudOps, Algorithmic trading Developer, Automation Test Developer, Tester")
    st.write("**Email:** vylhc@vpbank.com.vn | catvyisworking@gmail.com")
    st.write("**Contact:** 0898177342")

# Chat input for user questions
user_input = st.text_input("Ask a finance question:", placeholder="e.g., What is Net Present Value?")

# Generate response if there's user input
if user_input:
    try:
        # Get response from the finance professor chatbot
        response_content = get_response(user_input)
        
        # Display the conversation history in chat format
        for message in st.session_state["conversation_history"]:
            if message["role"] == "user":
                st.write(f"**You:** {message['content']}")
            elif message["role"] == "assistant":
                st.write(f"**Finance Professor:** {message['content']}")

    except Exception as e:
        st.error(f"Error: {e}")

# Option to reset the conversation history
if st.button("Reset Conversation"):
    st.session_state["conversation_history"] = [{"role": "system", "content": system_prompt}]
    st.success("Conversation reset.")


# I want ot have one professor as a chatbot to help me learn everything about finance, every terms need to be explained in an easy to understand manner, with use case, related terms, formula, example, use cases, examples, and very much more, strucutred my requiremnt to prompt and change  my app.
# - The placeholder to add at the bottom of the page
# - The response answer
# - The formula response that is format I can read maybe use funciton calling in latex
