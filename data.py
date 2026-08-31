import pandas as pd
import yfinance as yf

def fetch_datasets():
    print("1. Downloading Coal & Oil Data from FRED...")
    
    # Download Coal Price Index
    df_coal = pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCOALAUUSDM")
    df_coal.rename(columns={"DATE": "Date", "PCOALAUUSDM": "Coal_Price_USD"}, inplace=True)
    
    # Download Brent Oil Index
    df_oil = pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=POILBREUSDM")
    df_oil.rename(columns={"DATE": "Date", "POILBREUSDM": "Brent_Oil_USD"}, inplace=True)
    
    # Save macro commodity files
    df_coal.to_csv("dataset_2_coal_prices.csv", index=False)
    df_oil.to_csv("dataset_2_brent_oil.csv", index=False)
    print("   -> Saved dataset_2_coal_prices.csv")
    print("   -> Saved dataset_2_brent_oil.csv")

    print("2. Downloading Shipping Proxies from Yahoo Finance...")
    
    # Pull proxies individually to prevent multi-header errors
    tickers = {"Capesize_Proxy_GNK": "GNK", "Panamax_Proxy_EDRY": "EDRY", "Supramax_Proxy_SBLK": "SBLK"}
    proxy_dfs = []

    for name, symbol in tickers.items():
        data = yf.download(symbol, start="2011-01-01", progress=False)[['Close']].reset_index()
        # Flatten column names
        data.columns = ['Date', name]
        proxy_dfs.append(data.set_index('Date'))

    # Combine shipping proxy columns cleanly
    freight_proxies = pd.concat(proxy_dfs, axis=1).reset_index()
    freight_proxies.to_csv("dataset_1_freight_proxies.csv", index=False)
    print("   -> Saved dataset_1_freight_proxies.csv")

if __name__ == "__main__":
    fetch_datasets()