import pandas as pd
df = pd.read_csv('weather_by_cities_pandas7.csv')
print(df)

print('Grouping the dataframe by using df.groupby')
g = df.groupby('city')
print(g)
print('-'*50)


print('Printing by iterating through the Data Frame')
for city, city_df in g:
    print(city)
    print(city_df)
print('-'*50)


print('Printing grouped By using g.get_group("_____")')
print(g.get_group('mumbai'))
print(g.max)
print('-'*50)

#SELECT * from city_data GROUP BY city
print('Maximum Temperature In the Grouped Data Set By Cities')
print(g.max())
print('-'*50)

print('Mean Temperature In the Grouped Data Set By Cities')
print(g.mean)
print('-'*50)

print('To describe all the details of the Data Set')
print(g.describe())
print('-'*50)

print('To plot a chort of the given data')
print(g.plot())
print('-'*50)
