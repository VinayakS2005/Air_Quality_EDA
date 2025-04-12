import pandas as pd

df = pd.read_csv('REAL_TIME_AIR_QUALITY_INDEX1.csv', encoding='latin-1', on_bad_lines='skip')

df_cleaned = df.fillna(0)

columns_to_drop = ['who_region', 'iso3', 'country_name', 'city', 'year', 'version', 
                   'pm10_concentration', 'pm25_concentration', 'no2_concentration', 
                   'pm10_tempcov', 'pm25_tempcov', 'no2_tempcov', 'type_of_stations', 
                   'reference', 'web_link', 'population', 'population_source', 
                   'latitude', 'longitude', 'who_ms']

df_cleaned = df_cleaned.drop(columns=columns_to_drop)

df_cleaned.to_csv('cleaned.csv', index=False,encoding='latin-1', on_bad_lines='skip')

print("Data cleaned and saved as 'REAL_TIME_AIR_QUALITY_INDEX.csv'")
