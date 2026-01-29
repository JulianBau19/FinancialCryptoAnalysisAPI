# TREND DETECTION PROYECT FROM X ( API INGESTION )



API: coinGecko







### Steps:



1. Get crypto currency infomation
2. Ingestion mode: BATCH every n MINS 
3. INGESTION
4. Data contract + RAW storage desing



## STEP 1: main.py

## STEP 2: src/transform.py

RAW TO STG (transform.py)
We transform CoinGecko RAW JSON files into a structured STG CSV.

STG schema:

id, symbol, name, current_price, market_cap, total_volume

price_change_percentage_24hs, market_cap_change_percentage_24hs

last_updated (timestamp from API)

Logic:

Validate RAW exists: if no data/raw/crypto_raw_*.json, raise an exception.

Read the latest RAW file and json.load() into data.

Convert JSON → DataFrame: df = pd.DataFrame(data).

Select required columns with columns_wanted and create df_stg.

Standardize column names (rename the 24h fields to *_24hs).

Ensure data/stg/ exists and write df_stg to data/stg/crypto_stg.csv.
