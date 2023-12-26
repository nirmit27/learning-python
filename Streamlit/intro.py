import yfinance as yf
import streamlit as st
import streamlit_utils.utils as utils

st.set_page_config(layout='wide', page_title='Streamlit Intro', page_icon="📈")

# Heading ...
utils.heading(title="Simple Stock Price App",
              sub_title="Shown below are the stock <b>closing price</b> and <b>volume</b>of Google from <b>May, "
                        "2010</b> to <b>May, 2020</b>.",
              title_color="lightblue"
              )

utils.line_break(2)

# Accessing the ticker data ...
ticker_symbol = "GOOGL"
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

# Charts ...
st.subheader('''Closing Price''')
utils.line_break(1)
st.line_chart(ticker_df.Close)

utils.line_break(1)

st.subheader('''Volume''')
utils.line_break(1)
st.line_chart(ticker_df.Volume)
