import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import pandas as pd

from sqlalchemy import create_engine

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv('MODEL_NAME')

model = ChatOpenAI(api_key=openai_key, model=model_name)

df = pd.read_csv("./data/salaries_2023.csv").fillna(value=0)

# from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

print(SQLDatabaseToolkit)