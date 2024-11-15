import requests as requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=RELIANCE.BSE&interval=5min&apikey=2USKBNHM7280OSZ4'
r = requests.get(url)
data = r.json()
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=2USKBNHM7280OSZ4'
r = requests.get(url)
data_intra = r.json()
print(data_intra)




