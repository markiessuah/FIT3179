import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_csv('game_revenue_country.csv')
df2 = pd.read_csv('country_coor.csv')

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = 'country')
df3.set_index('country', inplace = True)

# Write it to a new CSV file
df3.to_csv('coor_country_new.csv')