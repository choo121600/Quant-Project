import pandas as pd
from utils.mdd_calculate import calculate_mdd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    데이터 클리닝을 진행합니다.

    :param df:
    - 원시 데이터프레임
    :return:
    - pd.Dataframe: 클리닝이 진행된 데이터프레임
    """

    # 결측치 제거
    df = df.dropna()

    # TODO: 필요시 몇 가지의 클리닝 기법 사용

    return df


def calculate_moving_average(df: pd.DataFrame, window: int) -> pd.DataFrame:
    """
    이동평균을 계산하여 데이터프레임에 추가합니다.

    :param df: 클리닝된 데이터 프레임을 넣어줍니다.
    :param window: 이동평균의 윈도우 크기
    :return:
    - pd.Dataframe: 이동평균이 추가된 데이터 프레임
    """

    df[f'ma_{window}'] = df['Close'].rolling(window=window).mean().fillna(method='bfill')

    return df

def add_mdd(df: pd.DataFrame) -> pd.DataFrame:
    """
    최대 낙폭(Max Drawdown)을 계산하여 데이터 프레임에 추가합니다.

    :param df:
    :return:
    """

    df['MDD'] = calculate_mdd(df['Close'])
    return df
