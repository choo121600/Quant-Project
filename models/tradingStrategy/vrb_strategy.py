def volatility_range_breakout_strategy(status, prev_row, current_row, k):
    """
    변동성 범위 돌파 전략을 적용합니다.
    변동성 돌파 전략은 가격이 일정 기간 동안 형성된 가격 범위에서 벗어날 때 거래 신호로 인식하여 매매하는 전략
    
    거래에 사용되는 주요 지표
    - ATR (Average True Range): 가격 변동성을 측정하는 지표
    - 볼린저 밴드: 가격의 표준편차를 기반으로 상한선과 하한선을 계산하는 지표
    - 이동평균선: 일정 기간 동안의 가격 평균을 계산하는 지표
    
    장점:
    - 단순함
    - 변동성이 높을 때 유용함
    
    단점:
    - 변동성이 낮을 때 거래 신호가 발생하지 않음
    - 거짓 신호가 발생할 수 있음
    - 리스크 관리가 필요함

    Parameters:
    - status (int): 현재 포지션 상태 (0: 포지션 없음, 1: 포지션 보유)
    - prev_row (pd.Series): 이전 시점의 데이터
    - current_row (pd.Series): 현재 시점의 데이터
    - k (float): 변동성 계수

    Returns:
    - int: 신호 (1: 매수, -1: 매도, 0: 유지)
    """
    signal = 0

    try:
        prev_high = prev_row['High']
        prev_low = prev_row['Low']
        prev_open = prev_row['Open']
        prev_close = prev_row['Close']

        range_ = prev_high - prev_close
        breakout_buy = prev_open + range_ * k

        current_open = current_row['Open']

        if status == 0:
            if current_open > breakout_buy:
                signal = 1
        elif status == 1:
            if current_open < prev_low:
                signal = -1 

    except KeyError as e:
        print(f"KeyError: {e} - 데이터에 필요한 열이 누락되었습니다.")
    except Exception as e:
        print(f"예상치 못한 에러 발생: {e}")

    return signal
