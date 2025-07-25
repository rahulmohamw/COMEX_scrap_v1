import yfinance as yf
import pandas as pd
from datetime import datetime

# Constants
TICKER = "HG=F"
START_DATE = "2008-01-01"
END_DATE = datetime.now().strftime("%Y-%m-%d")
CSV_FILE = "comex_copper_historical_data.csv"

# Download Copper Futures data
print(f"Downloading data for {TICKER} from {START_DATE} to {END_DATE}")
data = yf.download(TICKER, start=START_DATE, end=END_DATE)

# Filter and format
df = data[['Close', 'Volume']].reset_index()
df['date'] = df['Date'].dt.strftime('%-m/%-d/%Y')
df.drop(columns=['Date'], inplace=True)
df.columns = ['close', 'volume', 'date']
df = df[['date', 'close', 'volume']]

# Convert to required metrics
df['COMEX Cu $/MT'] = df['close'] * 2204.62
df['volume cu in MT'] = df['volume'] * 11.34

# Round off values
df = df.round({'COMEX Cu $/MT': 2, 'volume cu in MT': 0})

# Save to CSV
df.to_csv(CSV_FILE, index=False)
print(f"Saved to {CSV_FILE}")
