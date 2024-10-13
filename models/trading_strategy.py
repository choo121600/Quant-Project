import pandas as pd

from dataclasses import dataclass
from models.tradingStrategy.vrb_strategy import volatility_range_breakout_strategy
from models.tradingStrategy.basic_strategy import basic_strategy


@dataclass
class TradingStrategy:
    moving_average: float
    max_drawdown_threshold: float = 0.1

    def generate_signal(self, status: int, prev_row: pd.Series, row: pd.Series, mdd: float, trading_strategy: str):
        """
        트레이딩 신호를 생성합니다.

        Parameters:
        - status (int): 현재 포지션 상태 (0: 포지션 없음, 1: 포지션 보유)
        - prev_row (pd.Series): 이전 행
        - row (pd.Series): 현재 행
        - mdd (float): 최대 낙폭
        - trading_strategy (str): 트레이딩 전략

        Returns:
        - int: 신호 (1: 매수, -1: 매도, 0: 유지)
        """
        if trading_strategy == 'Basic':
            signal = basic_strategy(status, row['Close'], mdd, self.moving_average, self.max_drawdown_threshold)
        elif trading_strategy == 'VRB':
            k = 0.001 # 변동성 계수
            signal = volatility_range_breakout_strategy(status, prev_row, row, k)

        return signal
