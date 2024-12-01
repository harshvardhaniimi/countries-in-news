import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('data/gdelt-2024-11-20-000000000000.csv')[['SQLDATE', 'Actor1CountryCode', 'Actor2CountryCode', 'AvgTone']]

actors = np.unique(np.concatenate((df['Actor1CountryCode'].unique(), df['Actor2CountryCode'].unique())))

tones = np.zeros((len(actors), len(actors)))
for i in range(len(actors)):
  for j in range(len(actors)):
    tones[i][j] = df.loc[(df['Actor1CountryCode'] == actors[i]) & (df['Actor2CountryCode'] == actors[j])]['AvgTone'].mean()
tones = np.nan_to_num(tones)
avg_tones_a1 = np.mean(tones, axis=0)
avg_tones_a2 = np.mean(tones, axis=1)
avg_tones_all = np.sum(tones, axis=0) + np.sum(tones, axis=1)
for i in range(len(avg_tones_all)):
  avg_tones_all[i] -= tones[i][i]
avg_tones_all / len(avg_tones_all)

# average tone over time
df['DateTime'] = pd.to_datetime(df['SQLDATE'].astype(str), format='%Y%m%d')
time_tones = np.array([])
dates = np.array([])
year_min = df['DateTime'].dt.year.min()
year_max = df['DateTime'].dt.year.max()
for y in range(year_min, year_max + 1):
  for m in range(1, 13):
      found = df.loc[(df['DateTime'].dt.year == y) & (df['DateTime'].dt.month == m)]
      time_tones = np.append(time_tones, found['AvgTone'].mean())
      dates = np.append(dates, f"{y}-{m}")
  
# matrix of average tone for each relationship
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

# bar graph of country average tones by actor
width = 0.35
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
num = np.arange(len(actors))
rectsa1 = ax.bar(num - width/2, avg_tones_a1, width, label='Actor1')
rectsa2 = ax.bar(num + width/2, avg_tones_a2, width, label='Actor2')
ax.set_ylabel('Average Tone')
ax.set_title('Country Average Tone')
ax.set_xticks(num)
ax.set_xticklabels(actors)
ax.legend(loc='lower right')
plt.show()

# plot of average tone over time of news a country is involved in
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.plot(time_tones)
ax.set_xticklabels(dates)
ax.xaxis.set_major_locator(ticker.MultipleLocator(6))
formatter = ax.xaxis.get_major_formatter()
formatter.seq = formatter.seq[::6]
plt.show()