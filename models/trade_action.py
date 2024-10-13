from dataclasses import dataclass
import pandas as pd

@dataclass
class TradeAction:
    buy: float = 0.0
    sell: float = 0.0
    hold: float = 0.0
    fee: float = 0.005  # 거래 수수료 0.5%
    date_time: pd.Timestamp = pd.NaT

    def execute(self, status: int, signal: int, cash_asset: float, coin_amount: float, price: float, datetime: pd.Timestamp):
        """
        트레이딩 신호에 따라 액션을 설정합니다.

        Parameters:
        - status (int): 현재 포지션 상태 (0: 보유하지 않음, 1: 보유 중)
        - signal (int): 트레이딩 신호 (-1: 매도, 0: 보유, 1: 매수)
        - cash_asset (float): 현재 현금 자산
        - coin_amount (float): 현재 코인 수량
        - price (float): 현재 코인 가격
        - datetime (pd.Timestamp): 현재 시간

        Returns:
        - TradeAction: 실행된 액션
        - int: 업데이트된 상태
        - float: 업데이트된 코인 수량
        """
        # 트레이드 액션 초기화
        self.buy = 0.0
        self.sell = 0.0
        self.hold = 0.0

        self.date_time = datetime

        if status == 1 and signal == -1:
            # 매도: 보유 중인 모든 코인을 매도
            sell_amount = coin_amount * price
            sell_after_fee = sell_amount * (1 - self.fee)
            cash_asset += sell_after_fee
            self.sell = sell_after_fee
            coin_amount = 0.0
            status = 0
        elif status == 1 and signal == 0:
            # 보유 중, 유지
            self.hold = 1.0
            # 자산 변화 없음
        elif status == 0 and signal == 1:
            # 매수: 전체 현금 자산을 사용하여 매수
            if price > 0:  # 가격이 유효한지 확인
                buy_amount = cash_asset / price
                buy_after_fee = buy_amount * (1 - self.fee)
                coin_amount += buy_after_fee
                self.buy = cash_asset
                cash_asset = 0.0
                status = 1
            else:
                print("매수 실패: 가격이 유효하지 않습니다.")
        # 신호가 다른 경우는 아무 동작도 하지 않음


        return self, status, cash_asset, coin_amount