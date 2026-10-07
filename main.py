import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin"
params = {
    "localization": "false",
    "tickers": "false",
    "market_data": "true",
    "community_data": "false",
    "developer_data": "false",
    "sparkline": "false",
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()["market_data"]

price = data["current_price"]["usd"]
change = data["price_change_percentage_24h"]
high = data["high_24h"]["usd"]
low = data["low_24h"]["usd"]

print("=== Market Tools v1.1 ===")
print(f"BTC/USD: ${price:,.2f}")
print(f"24h Change: {change:+.2f}%")
print(f"24h High: ${high:,.2f}")
print(f"24h Low: ${low:,.2f}")
