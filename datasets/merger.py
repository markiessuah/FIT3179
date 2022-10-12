import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_csv('game_popular_country.csv')
df2 = pd.read_csv('game_playtime.csv')

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = 'game', how='left')
df3.set_index('game', inplace = True)

# Write it to a new CSV file
df3.to_csv('game_country_new.csv')