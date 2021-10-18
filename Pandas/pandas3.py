import pandas as pd

#Creating Data Fame Using cSv file
'''df = pd.read_csv('/Users/amanyadav/Desktop/new_numpy/nyc_taxi.csv')
print(df)
'''

#Creating Data Fame Using EXCEL file
'''df = pd.red_excel("                  ")
print(df)
'''

#Creating Data Frame Using Dictionarie
'''wheather_data = {
    'day':['1/1/2001', '2/2/2002', '3/1/2002'],
    'temperature':[23, 20, 18],
    'windspeed':[3, 4, 7],
    'event': ['cold', 'chill', 'cold_chill']
}
df = pd.DataFrame(wheather_data)
print(df)
df.set_index('day', inplace=True)
print(df)'''

#Creating Data Frame using Tupple
'''
wheather_data = [
    ('1/1/2002', 32, 6, 'Rain'),
    ('1/2/2002', 35, 7, 'Sunny'),
    ('1/3/2002', 28, 2, 'Snow')
]
df = pd.DataFrame(wheather_data, columns=['day', 'temperature', 'windspeed', 'event'])
print(df)'''

#Creating Data Frame Using Dictionaries
'''weather_data = [
    {'day': '1/1/2002', 'tempearture': '32', 'windspeed': 6, 'event': 'Rain' },
    {'day': '1/2/2002', 'tempearture': '28', 'windspeed': 4, 'event': 'Cold'},
    {'day': '1/3/2002', 'tempearture': '16', 'windspeed': 3, 'event': 'Chill'},
    {'day': '1/4/2002', 'tempearture': '10', 'windspeed': 1, 'event': 'Chilling_cold'},
]
df = pd.DataFrame(weather_data)
print(df)'''