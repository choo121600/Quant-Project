import streamlit as st
import os
import sys

from data.data_fetcher import run_etl
from models.trading_strategy import TradingStrategy
from utils.helpers import load_data, display_sidebar
from utils.plotting import visualize_portfolio, visualize_trades, visualize_overview
from utils.simulation import run_simulation


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    st.title("포트폴리오 관리 및 트레이딩 대시보드")
    ticker, strategy_name,  interval, period_days, ma_window, update = display_sidebar()

    # ETL 실행 버튼
    if update:
        with st.spinner("데이터를 추출, 변환, 적재하는 중..."):
            try:
                df = run_etl(ticker, interval, period_days, ma_window)
                st.success("데이터 업데이트 완료!")
            except Exception as e:
                st.error(f"ETL 프로세스 중 오류가 발생했습니다: {e}")
                return
    else:
        try:
            df = load_data(ticker, interval, period_days, ma_window)
        except FileNotFoundError:
            st.warning("처리된 데이터가 없습니다. 사이드바에서 데이터를 업데이트하세요.")
            return
        except Exception as e:
            st.error(f"데이터를 로드하는 중 오류가 발생했습니다: {e}")
            return

    # 초기 자본
    amount = 1_000_000_000

    trade_df = run_simulation(df, strategy_name, ma_window, initial_amount=amount)


    # 포트폴리오 상태 시각화
    # visualize_portfolio(portfolio_df)
    visualize_trades(trade_df)
    visualize_overview(df, trade_df, ma_window)

if __name__ == "__main__":
    main()
