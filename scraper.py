import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

all_prices = []
all_sizes = []

print("🚀 Data Analyst Bot Started... Getting 5 pages of Data!\n")

for page in range(1, 6):
    url = f"https://www.zameen.com/Homes/Islamabad-3-{page}.html"
    print(f"📡 Scraping Page {page}...")
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    raw_data = soup.find_all("div", class_="d870ae17")
    
    # List slicing
    prices = [item.get_text(strip=True) for item in raw_data[0::2]]
    sizes = [item.get_text(strip=True) for item in raw_data[1::2]]
    
    all_prices.extend(prices)
    all_sizes.extend(sizes)

    time.sleep(2) 

print("\n✅ Scraping Done! Total Homes Found:", len(all_prices))


print("⚙️ Cleaning Data for Analysis...")

def clean_price(price_str):
    price_str = price_str.replace("PKR", "").strip()
    if "Crore" in price_str:
        return int(float(price_str.replace("Crore", "").strip()) * 10000000)
    elif "Lakh" in price_str:
        return int(float(price_str.replace("Lakh", "").strip()) * 100000)
    else:
        try:
            return int(float(price_str.replace(",", "")))
        except:
            return 0

def clean_size(size_str):
    size_str = str(size_str).lower()
    if "kanal" in size_str:
        return float(size_str.replace("kanal", "").strip()) * 20
    elif "marla" in size_str:
        return float(size_str.replace("marla", "").strip())
    else:
        return 0

df = pd.DataFrame({
    "Raw_Price": all_prices,
    "Raw_Size": all_sizes
})

df['Price_PKR'] = df['Raw_Price'].apply(clean_price)
df['Size_Marla'] = df['Raw_Size'].apply(clean_size)

final_df = df[['Price_PKR', 'Size_Marla']].copy()
final_df.to_csv("Zameen_Islamabad_Clean_Data.csv", index=False)

print("\n📁 FILE SAVED: Zameen_Islamabad_Clean_Data.csv")