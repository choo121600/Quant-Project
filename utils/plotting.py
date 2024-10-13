import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def visualize_portfolio(portfolio_df):
    st.header("포트폴리오 자산 분배")
    pie_fig = go.Figure()
    pie_fig.add_trace(go.Pie(labels=['Cash Asset', 'Coin Asset', 'Coin Amount', 'Sub'], values=portfolio_df.iloc[-1].values, hole=0.5))
    pie_fig.update_layout(title="포트폴리오 자산 분배", annotations=[dict(text='자산 분배', showarrow=False)])
    st.plotly_chart(pie_fig, use_container_width=True)


def visualize_trades(trade_df):
    st.header("거래 내역")
    st.dataframe(trade_df.style.format({"Buy": "{}", "Sell": "{}", "Hold": "{}"}))

    st.subheader("매수/매도 거래량")
    trade_fig = go.Figure()
    trade_fig.add_trace(go.Scatter(x=trade_df['Datetime'], y=trade_df['Buy'],
                                mode='markers', name='Buy', marker=dict(color='green', symbol='triangle-up')))
    trade_fig.add_trace(go.Scatter(x=trade_df['Datetime'], y=trade_df['Sell'],
                                mode='markers', name='Sell', marker=dict(color='red', symbol='triangle-down')))
    trade_fig.update_layout(title="매수/매도 거래량", xaxis_title="날짜", yaxis_title="금액")
    st.plotly_chart(trade_fig, use_container_width=True)

def visualize_overview(df, trade_df, ma_window):
    st.header("종합 그래프")

    # 가격과 이동 평균을 그리는 Figure 생성
    price_fig = go.Figure()
    price_fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='현재 가격', line=dict(color='blue')))
    price_fig.add_trace(go.Scatter(x=df.index, y=df[f'ma_{ma_window}'], mode='lines', name=f'{ma_window}-기간 이동 평균', line=dict(color='orange')))

    # 매수 시점 필터링
    trade_buy_df = trade_df[trade_df['Buy'] > 0]
    # 매도 시점 필터링
    trade_sell_df = trade_df[trade_df['Sell'] > 0]

    # 매수 시점의 가격 데이터 병합
    trade_buy_merged = trade_buy_df.merge(df[['Close']], left_on='Datetime', right_index=True, how='left')
    # 매도 시점의 가격 데이터 병합
    trade_sell_merged = trade_sell_df.merge(df[['Close']], left_on='Datetime', right_index=True, how='left')

    # 매수 마커 추가
    price_fig.add_trace(go.Scatter(
        x=trade_buy_merged['Datetime'],
        y=trade_buy_merged['Close'],
        mode='markers',
        name='매수',
        marker=dict(color='green', symbol='triangle-up', size=12)
    ))

    # 매도 마커 추가
    price_fig.add_trace(go.Scatter(
        x=trade_sell_merged['Datetime'],
        y=trade_sell_merged['Close'],
        mode='markers',
        name='매도',
        marker=dict(color='red', symbol='triangle-down', size=12)
    ))

    price_fig.update_layout(title="가격과 이동 평균 및 매수/매도 시점", xaxis_title="날짜", yaxis_title="가격")
    st.plotly_chart(price_fig, use_container_width=True)
