import streamlit as st
import pandas as pd

from models.trading_strategy import TradingStrategy
from models.trade_action import TradeAction
from etl.load import save_to_csv

def run_simulation(df, strategy_name, ma_window, initial_amount):
    strategy = TradingStrategy(moving_average=df[f'ma_{ma_window}'].iloc[-1])

    status = 0
    cash_asset = initial_amount
    coin_asset = 0.0
    coin_amount = 0.0
    trade_history = []
    prev_row = df.iloc[0]
    trade_action = TradeAction()

    for index, row in df.iterrows():
        # 현재 최대 낙폭
        mdd = abs(row['MDD'])

        signal = strategy.generate_signal(status, prev_row, row, mdd, trading_strategy=strategy_name)

        prev_row = row

        # 매매 실행
        trade, status, cash_asset, coin_amount = trade_action.execute(
            status=status, 
            signal=signal, 
            cash_asset=cash_asset, 
            coin_amount=coin_amount, 
            price=row['Close'],
            datetime=index
        )


        # 현재 코인 자산 가치
        coin_asset = coin_amount * row['Close']

        # 매매 내역 기록
        trade_history.append({
            'Datetime': trade.date_time,
            'Signal': signal,
            'Status': status,
            'Buy': trade.buy,
            'Sell': trade.sell,
            'Hold': trade.hold,
            'Cash': cash_asset,
            'Coin_Amount': coin_amount,
            'Coin_Asset': coin_asset,
            'Total_Asset': cash_asset + coin_asset
        })

    # 매매 내역 데이터프레임 생성
    trade_df = pd.DataFrame(trade_history)
    trade_df = trade_df.dropna(subset=['Datetime'])

    # trade_df 에서 signal과 status 가 모두 0인 경우 제거
    trade_df = trade_df[(trade_df['Signal'] != 0) | (trade_df['Status'] != 0)]

    return trade_df
