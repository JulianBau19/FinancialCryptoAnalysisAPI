import requests
import json
from datetime import datetime
from pathlib import Path

# CoinGecko endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"

# What we ask?
params = {
    "vs_currency": "usd",
    "order": "volume_desc",
    "per_page": 20,
    "page": 1,
    "price_change_percentage": "1h,24h"
}



resp = requests.get(url, params=params, timeout=30) ## send the request to coingecko and store in resp variable

print("STATUS:", resp.status_code)

if resp.status_code != 200:         ## basic API error handling ( 200 = ok, anything else = error)
    print("ERROR:", resp.text)
    raise SystemExit("Request failed")

data = resp.json()   ## list of dictionaries
print("Coins received:", len(data))
print("Example coin:\n", data[0])




#  SAVE DATA into RAW LAYER and create a timestamp
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
Path("data/raw").mkdir(parents=True, exist_ok=True)

filepath = f"data/raw/crypto_raw_{timestamp}.json"   ## save the data into raw folder with the timestamp in the name

with open(filepath, "w", encoding="utf-8") as f: ## Open the file, use it, and automatically close it after
    json.dump(data, f, indent=2) ## convert python object to JSON text and save to file.

print("RAW data saved to:", filepath) 



