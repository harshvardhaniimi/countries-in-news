import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('data/gdelt-2024-11-20-000000000000.csv')[['GoldsteinScale', 'AvgTone', 'NumArticles', 'SOURCEURL']]

df['Source'] = df['SOURCEURL'].str.extract(r'(?<=:\/\/)(.*?)(?=\/)')
print(df['Source'].value_counts())
countsdf = df['Source'].value_counts()
sources = countsdf.index.to_numpy()
source_counts = countsdf.values

width = 0.4
num = 50
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.bar(sources[:num], source_counts[:num], width)
ax.set_ylabel('Count')
ax.set_title('News Outlet Frequency')
plt.xticks(rotation=90)
plt.show()

