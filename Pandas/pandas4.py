import pandas as pd
df = pd.read_csv('/Numpy /nyc_taxi.csv')
print(df)


df.to_csv('new.csv', columns=['pickup_year','pickup_dayofweek'], header=False)


df.to_csv('new.csv', columns=['pickup_year','pickup_dayofweek'], header=False, index=False)


df.to_csv('new.csv', columns=['pickup_year','pickup_dayofweek'])

# For Excel type data file

'''
df.to_excel('new.xlsx', columns=['pickup_year','pickup_dayofweek'])'''

