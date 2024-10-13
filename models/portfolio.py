from dataclasses import dataclass

@dataclass
class Portfolio:
    total_amount: float
    cash_asset: float = 0.0
    coin_asset: float = 0.0
    sub_asset: float = 0.0
    coin_amount: float = 0.0

    cash_ratio: float = 0.6
    coin_ratio: float = 0.2
    sub_ratio: float = 0.2

    def adjust(self, market_status: str, current_coin_price: float, coin_amount: float):
        """
        포트폴리오 자산 분배를 조정합니다.

        Parameters:
        - market_status (str): 'up', 'down', 또는 기타 상태

        Returns:
        - dict: 조정된 자산 분배
        """

        coin_amount = coin_amount
        cash_asset = self.total_amount * self.cash_ratio
        coin_asset = self.total_amount * self.coin_ratio - coin_amount * current_coin_price
        sub_asset = self.total_amount * self.sub_ratio

        # if market_status == 'up':
        #     cash_asset = self.total_amount * 0.6
        #     coin_asset = self.total_amount * 0.3
        #     sub_asset = self.total_amount * 0.1
        # elif market_status == 'down':
        #     cash_asset = self.total_amount * 0.6
        #     coin_asset = self.total_amount * 0.1
        #     sub_asset = self.total_amount * 0.3

        return {
            'cash_asset': cash_asset,
            'coin_asset': coin_asset,
            'sub_asset': sub_asset,
            'coin_amount': coin_amount
        }
