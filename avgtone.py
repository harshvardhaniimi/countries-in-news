import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('data/gdelt-2024-11-20-000000000000.csv')[['Actor1CountryCode', 'Actor2CountryCode', 'AvgTone']]

actors = np.unique(np.concatenate((df['Actor1CountryCode'].unique(), df['Actor2CountryCode'].unique())))
print(actors)

tones = np.zeros((len(actors), len(actors)))
for i in range(len(actors)):
  for j in range(len(actors)):
    tones[i][j] = df.loc[(df['Actor1CountryCode'] == actors[i]) & (df['Actor2CountryCode'] == actors[j])]['AvgTone'].mean()
print(np.nanmax(tones), np.nanmin(tones))
  
tick_labels = np.insert(actors, 0, '')
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
mat = ax.matshow(tones, cmap=matplotlib.colormaps.get_cmap('RdBu'))
ax.set_xticklabels(tick_labels)
ax.set_yticklabels(tick_labels)
ax.set_xlabel('Actor2')
ax.set_ylabel('Actor1')
ax.xaxis.set_label_position('top')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_title('Average Tone by Relationship')
fig.colorbar(mat, shrink=0.8)
mat.set_clim(-4, 4)
plt.show()