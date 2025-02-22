import yfinance as yf
from app.schemas.api_schemas import Price_Schema

async def get_currencies_price() -> list[Price_Schema] | None:
    try:
        all_tickers = {"RUB=X": "Доллар", "BTC-USD": "Биткоин"}
        exchange_rates = []
        for ticker in all_tickers.keys():
            data = yf.download(ticker, period="1d", interval="1m")
            price = round(float(data['Close'].iloc[-1]), 2)
            exchange_rates.append(
                Price_Schema(title=all_tickers[ticker],
                            ticker=ticker,
                            price=f'{'$' if 'usd' in ticker.lower() else '₽'}{price}')) 

        return exchange_rates
    except Exception as e:
        print(f"Ошибка при получении курса валют: {e}")
