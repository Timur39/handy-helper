import yfinance as yf

async def get_currencies_price():
    all_tickers = {"RUB=X": "Доллар", 
                   "BTC-USD": "Биткоин"}
    exchange_rates = []
    for ticker in all_tickers.keys():
        data = yf.download(ticker, period="1d", interval="1m")

        exchange_rates.append({'title': all_tickers[ticker], 
                               'ticker': ticker,
                               'price': f'{'$' if 'usd' in ticker.lower() else '₽'}{round(float(data['Close'].iloc[-1]), 2)}'})


    return exchange_rates
