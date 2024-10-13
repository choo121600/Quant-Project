
import pandas as pd
from etl.extract import fetch_yahoo_finance_data
from etl.transform import clean_data, calculate_moving_average, add_mdd
from etl.load import save_to_csv


def run_etl(ticker: str, interval: str = '1d', period_days: int = 360, ma_window: int = 20) -> pd.DataFrame:
    """

    :param ticker:
    :param interval:
    :param period_days:
    :param ma_window:
    :return:
    """

    # 데이터 추출
    df = fetch_yahoo_finance_data(ticker, interval, period_days)

    df = clean_data(df)
    df = calculate_moving_average(df, window=ma_window)
    df = add_mdd(df)

    # 데이터 적재
    save_to_csv(df, f"{ticker}_{interval}_{period_days}d.csv")

    return df
