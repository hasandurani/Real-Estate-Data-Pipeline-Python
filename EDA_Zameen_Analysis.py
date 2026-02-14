import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Zameen_Islamabad_Clean_Data.csv")


df = df[(df['Size_Marla'] > 0) & (df['Price_PKR'] > 0)].copy()


df['Price_per_Marla'] = df['Price_PKR'] / df['Size_Marla']

print(f"Total Houses Valid for Analysis: {len(df)}")


plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.patch.set_facecolor('#0E1628') 


ax1.set_facecolor('#0E1628')
ax1.scatter(df['Size_Marla'], df['Price_PKR']/10000000, color='#00D2D3', alpha=0.7, s=50)
ax1.set_title("Property Size vs. Price (Islamabad)", fontsize=14, fontweight='bold', color='white')
ax1.set_xlabel("Size (in Marla)", fontsize=12, color='#8898AA')
ax1.set_ylabel("Price (in Crores PKR)", fontsize=12, color='#8898AA')
ax1.grid(color='#2A3459', linestyle='--', linewidth=0.5)

ax2.set_facecolor('#0E1628')
ax2.hist(df['Price_per_Marla']/100000, bins=20, color='#00D2D3', edgecolor='white', alpha=0.8)
ax2.set_title("Market Trend: Price Per Marla Distribution", fontsize=14, fontweight='bold', color='white')
ax2.set_xlabel("Price Per Marla (in Lakhs PKR)", fontsize=12, color='#8898AA')
ax2.set_ylabel("Number of Houses", fontsize=12, color='#8898AA')
ax2.grid(color='#2A3459', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig("Zameen_Islamabad_Analysis.png", dpi=300, bbox_inches='tight')
plt.show()
print("\n📁 FILE SAVED: Zameen_Islamabad_Analysis.png")