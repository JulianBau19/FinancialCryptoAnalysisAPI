from pathlib import Path
import json
import pandas as pd

raw_dir = Path("data/raw") ## bing the dir
raw_files = sorted(raw_dir.glob("crypto_raw_*.json"))  ## bring the file


if not raw_files:
    raise SystemExit("No raw files found in data/raw. Run main.py first to upload from API")

latest_file = raw_files[-1]

print("Latest raw file: ",latest_file)

## now load JSON from that last_file raw

with open(latest_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Type:", type(data))
print("Items:", len(data))
print("First keys:", list(data[0].keys())[:15])


## convert json into pandas df

df = pd.DataFrame(data)

print("Shape:", df.shape)
print("Columns:", list(df.columns))


columns_wanted = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume",
    "price_change_percentage_24h",
    "market_cap_change_percentage_24h",
    "last_updated"
]

df_stg = df[columns_wanted].copy() ## final dataframe 
print(df_stg.head())


## STANDARDIZE NAMES AND SAVE STG

# rename to your schema naming
df_stg.rename(columns={
    "price_change_percentage_24h": "price_change_percentage_24hs",
    "market_cap_change_percentage_24h": "market_cap_change_percentage_24hs"
}, inplace=True)

# ensure STG folder exists 
Path("data/stg").mkdir(parents=True, exist_ok=True)

output_path = Path("data/stg/crypto_stg.csv")
df_stg.to_csv(output_path, index=False) ## TRANSFORM the .json file into a CSV

print("STG saved to:", output_path)
print(df_stg.head())
