import streamlit as st

# List of 10 technical indicators with formulas
technical_indicators = [
    {
        "name": "Moving Average Convergence Divergence (MACD)",
        "description": "Shows the relationship between two moving averages of a security’s price.",
        "formula": "MACD = EMA_{12} - EMA_{26}"
    },
    {
        "name": "Relative Strength Index (RSI)",
        "description": "A momentum oscillator that measures the speed and change of price movements.",
        "formula": r"RSI = 100 - \left( \frac{100}{1 + RS} \right), \text{ where } RS = \frac{\text{Average Gain}}{\text{Average Loss}}"
    },
    {
        "name": "Bollinger Bands",
        "description": "A volatility indicator that consists of a middle band (SMA) and upper/lower bands that track price deviation.",
        "formula": r"Upper\ Band = SMA + (k \times \sigma), \ Lower\ Band = SMA - (k \times \sigma)"
    },
    {
        "name": "Exponential Moving Average (EMA)",
        "description": "Places greater weight on recent prices to react more quickly to price changes.",
        "formula": r"EMA_t = Price_t \times \frac{\alpha}{1 + n} + EMA_{t-1} \times \left(1 - \frac{\alpha}{1 + n}\right)"
    },
    {
        "name": "Simple Moving Average (SMA)",
        "description": "Calculates the average of a selected range of prices over a defined period.",
        "formula": r"SMA = \frac{\sum_{i=1}^{n} Price_i}{n}"
    },
    {
        "name": "Stochastic Oscillator",
        "description": "A momentum indicator that compares a closing price to its price range over a specific period.",
        "formula": r"Stochastic\ %K = \frac{(Current\ Close - Lowest\ Low)}{(Highest\ High - Lowest\ Low)} \times 100"
    },
    {
        "name": "Average Directional Index (ADX)",
        "description": "Used to quantify trend strength, ranging from 0 to 100.",
        "formula": r"ADX = 100 \times \frac{\sum_{i=1}^{n} DX_i}{n}, \text{ where } DX = \frac{|+DI - -DI|}{+DI + -DI} \times 100"
    },
    {
        "name": "On-Balance Volume (OBV)",
        "description": "A volume-based indicator that measures buying and selling pressure.",
        "formula": r"OBV = OBV_{prev} + Volume, \text{ when price closes higher; } OBV_{prev} - Volume, \text{ when price closes lower}"
    },
    {
        "name": "Fibonacci Retracement",
        "description": "Identifies potential reversal levels by using horizontal lines at key Fibonacci levels.",
        "formula": r"Levels: 0\%, 23.6\%, 38.2\%, 50\%, 61.8\%, \text{ and } 100\% \text{ of the price range}"
    },
    {
        "name": "Ichimoku Cloud",
        "description": "Provides support and resistance levels, momentum, and trend direction.",
        "formula": r"\text{Components include: } Tenkan\text{-}sen = \frac{(Highest\ High + Lowest\ Low)}{2} \text{ over the last 9 periods, } Kijun\text{-}sen = \frac{(Highest\ High + Lowest\ Low)}{2} \text{ over the last 26 periods, etc.}"
    }
]

# Streamlit app interface
st.title("Technical Indicators List")
st.write("Here are 10 commonly used technical indicators in financial analysis with their formulas:")

# Display the technical indicators
for indicator in technical_indicators:
    st.subheader(indicator["name"])
    st.write(indicator["description"])
    st.markdown(f"**Formula:**\n\n${indicator['formula']}$", unsafe_allow_html=True)
