

def basic_strategy(status, current_price, max_drawdown, moving_average, max_drawdown_threshold=0.1):
		"""
		기본적인 트레이딩 전략을 적용합니다.

		Parameters:
		- status (int): 현재 포지션 상태 (0: 포지션 없음, 1: 포지션 보유)
		- current_price (float): 현재 가격
		- max_drawdown (float): 최대 낙폭
		- moving_average (float): 이동평균선
		- max_drawdown_threshold (float): 최대 낙폭 임계값

		Returns:
		- int: 신호 (1: 매수, -1: 매도, 0: 유지)
		"""
		signal = 0
		if status == 0:
				if current_price > moving_average:
						signal = 1
		elif status == 1:
				if max_drawdown > max_drawdown_threshold:
						signal = -1
				elif current_price < moving_average:
						signal = -1
		return signal