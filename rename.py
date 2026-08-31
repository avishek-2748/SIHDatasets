import os

# Mapping of old filenames to clean, structured filenames
rename_map = {
    "Baltic Dry Index Historical Data(15years).csv": "1_freight_bdi_daily.csv",
    "Baltic Dry Index Historical Data(15 years weekly).csv": "1_freight_bdi_weekly.csv",
    "dataset_1_freight_proxies.csv": "1_freight_vessel_proxies.csv",
    "Newcastle Coal Futures Historical Data(15 years daily).csv": "2_macro_coal_newcastle_daily.csv",
    "Newcastle Coal Futures Historical Data(15 years weekly).csv": "2_macro_coal_newcastle_weekly.csv",
    "Iron ore fines 62% Fe CFR Futures Historical Data(15 years daily).csv": "2_macro_iron_ore_daily.csv",
    "Iron ore fines 62% Fe CFR Futures Historical Data(15 years weekly).csv": "2_macro_iron_ore_weekly.csv",
    "Brent Oil Futures Historical Data(15 years daily).csv": "2_macro_brent_oil_daily.csv",
    "Brent Oil Futures Historical Data(15 years weekly).csv": "2_macro_brent_oil_weekly.csv",
    "US Dollar Index Historical Data(15 years).csv": "2_macro_dxy_usd_index.csv"
}

for old_name, new_name in rename_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")

print("\nAll datasets for Category 1 & Category 2 renamed successfully!")