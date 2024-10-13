import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(ticker, interval, period_days, ma_window):
    processed_dir = 'data/processed/'
    filename = f"{ticker}_{interval}_{period_days}d.csv"
    filepath = os.path.join(processed_dir, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError("처리된 데이터가 없습니다.")
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df


def display_sidebar():
    st.sidebar.header("설정")
    ticker = st.sidebar.text_input("티커 심볼", value="BTC-USD")
    strategy = st.sidebar.selectbox("전략", options=['Basic', 'VRB'])
    interval = st.sidebar.selectbox("데이터 간격", options=['1h', '1d'], index=1)
    period_days = st.sidebar.number_input("데이터 기간 (일수)", min_value=30, max_value=365, value=360)
    ma_window = st.sidebar.number_input("이동 평균 윈도우", min_value=1, max_value=100, value=20)
    update = st.sidebar.button("데이터 업데이트")
    return ticker, strategy, interval, period_days, ma_window, update
