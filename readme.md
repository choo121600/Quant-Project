# Quant Trading	Project

## Introduction
This project is a quantitative trading project that uses statistical strategies to make trading decisions. 



## Data
BTC-USD data is used for this project. The data is obtained from Yahoo Finance. The data is stored in the `data/processed` folder.


## Strategy
The strategy used in this project is a simple moving average strategy.

- Basic Strategy: 
	- Buy: When the short moving average crosses above the long moving average
	- Sell: When the short moving average crosses below the long moving average

- VRB Strategy:
	- Buy: When the short moving average crosses above the long moving average and the volume is increasing
	- Sell: When the short moving average crosses below the long moving average and the volume is decreasing


## Backtesting


