import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/gdelt-2024-11-07-000000000000.csv', nrows=1000000)

actor1s = df['Actor1CountryCode'].unique()
actor2s = df['Actor2CountryCode'].unique()
props1ser = df['Actor1CountryCode'].value_counts(normalize=True)
props2ser = df['Actor2CountryCode'].value_counts(normalize=True)

# print(props2ser.head(20))

# plot sorted cumulative sum of actor2 country frequency by number of actor2 countries included
ser = props2ser
props = ser.array.to_numpy()
cum_sum = props.cumsum()
plt.plot(cum_sum)
plt.show()

# get number of times certain actor1-actor2 pairs occur (top level is actor1)
num_keys = 10
num_rows = 10000
keys = list(props1ser.head(num_keys).keys())
keys.extend(list(props2ser.head(num_keys).keys()))
keys = list(set(keys))
mentions: dict[str, dict[str, int]] = dict((a1, dict((a2, 0) for a2 in keys)) for a1 in keys) # (actor1, (actor2, tally))
for index, row in df.head(num_rows).iterrows():
  if row['Actor1CountryCode'] in keys and row['Actor2CountryCode'] in keys:
    mentions[row['Actor1CountryCode']][row['Actor2CountryCode']] += 1
for k in keys:
  print(k, mentions[k])