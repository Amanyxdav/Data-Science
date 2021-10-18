"""In this we are going to learn how to handle missing value in data"""


import pandas as pd

"""df = pd.read_csv("weather_data.csv")"""
'''print(type(df.day[0]))'''

df = pd.read_csv('weather_data.csv', parse_dates=['day'])
print(type(df.day[0]))
print('Original Dataframe')
print(df)
print('-'*50)
print('Data frame after index set to dates')
df.set_index('day', inplace=True)
print(df)
print('-'*50)

# Fill Na or Empty
print('Data frame after filling Empty values with 0')
new_df = df.fillna(0)
print(new_df)
print('-'*50)

print('Dataframe after filling Empty values with 0\n***And Empty events with No Event Using Dictionaries***')
new_df = df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'No Event'

})
print(new_df)
print('-'*50)

# Forward Fill
print('Data Frame after using forward fill')
new_df = df.fillna(method='ffill')
print(new_df)
print('-'*50)

# Backward Fill
print('DataFrame after using backward fill')
new_df = df.fillna(method='bfill')
print(new_df)
print('-'*50)

# Limiter for Forward Fill
print('Using Limiter in Forwarfill of Empty Values')
new_df = df.fillna(method='ffill', limit=1)
print(new_df)
print('-'*50)

# Backward Fill Applying On Columns
print('Backward fill applying on columns')
new_df = df.fillna(method='bfill', axis='columns')
print(new_df)
print('-'*50)

# Interpolate for Data Frame
print('***Using Interpolate On Data Frame for Empty Data Prediction***')
new_df = df.interpolate()
print(new_df)
print('*'*50)

# Methods for Interpolate Data
print('***Using Interpolate On Data Frame for Empty Data Prediction and methods such as time***')
new_df = df.interpolate(method='time')
print(new_df)
print('*'*50)

# Using DropNa for rows to drop the empty row
new_df = df.dropna()
print(new_df)
print('*'*50)

# Using DropNA for different methods such as How
print('Using methods for condition such As DropNa by condition such as How=All')
new_df = df.dropna(how='all')
print(new_df)
print('-'*50)

# Using DropNA for different methods such as Threshold Value
print('Using methods for condition such As DropNa by using conditions such as threshold values are given 0,1,2,3')
new_df = df.dropna(thresh=2)
print(new_df)
print('-'*50)

# Using Date Range function for proper indexing of Dates
print('||| Using datetime.index and asigning it as new index will provide the missing dates of the month |||')
dt = pd.date_range('01-01-2017', '01-11-2017')
idx = pd.DatetimeIndex(dt)
new_df = df.reindex(idx)
print(new_df)
print('|'*50)
