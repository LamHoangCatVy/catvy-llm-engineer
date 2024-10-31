import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

def load_data():
    return pd.read_csv("BTCUSD_Candlestick_1_D_ASK_08.05.2017-16.10.2021.csv")

df = load_data()

st.title("Candlesticks Indicators")

dfpl = df[0:50]
fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                                     open=dfpl['Open'],
                                     high=dfpl['High'],
                                     low=dfpl['Low'],
                                     close=dfpl['Close'],
)])

data = yf.download("BTC-USD", period="max", interval="1d")
data.reset_index(inplace=True)
print(data.tail())

# fig.show()
st.plotly_chart(fig, use_container_width=True)