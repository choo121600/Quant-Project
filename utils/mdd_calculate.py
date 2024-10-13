import pandas as pd

def calculate_mdd(close_prices: pd.Series) -> float:
    """
    최대 낙폭을 게산합니다.
    :param close_prices:
    :return:
    """
    cumulative_max = close_prices.cummax()
    drawdown = (close_prices - cumulative_max) / cumulative_max
    mdd = drawdown.min()
    return mdd
