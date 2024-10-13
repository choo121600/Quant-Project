import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_yahoo_finance_data(ticker: str, interval: str =  '1h', period_days: int = '730') -> pd.DataFrame:
    """
    Yahoo Finance 에서 티커 심볼에 맞는 데이터를 추출합니다.

    :param ticker: 티커 심볼
    :param interval: 데이터 간(5min, 1h, 1d)
    :param period_days: 가져올 데이터 일수
    :return:
    - pd.Dataframe: 추출된 가격 데이터 프레임
    """

    end_date = datetime.now()
    start_date = end_date - timedelta(days=period_days)

    try:
        data = yf.download(
            tickers= ticker,
            start=start_date.strftime('%Y-%m-%d'),
            end=end_date.strftime('%Y-%m-%d'),
            interval=interval
        )
        if data.empty:
            raise ValueError("Data is Empty. Check parameter")
        else:
            return data

    except Exception as e:
        raise RuntimeError(f"Yahoo Finance에서 데이터를 추출하는 중 오류가 발생했습니다: {e}")
