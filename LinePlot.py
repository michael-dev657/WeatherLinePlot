import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('city_temperature.csv', low_memory=False)
cairo_data = df[df['City'] == 'Cairo'].copy()
week_data = cairo_data[(cairo_data['Year'] == 2010) & (cairo_data['Month'] == 3) & (cairo_data['Day'] >= 7) & (cairo_data['Day'] <= 13)].copy()
week_data = week_data[week_data['AvgTemperature'] > -50].copy()
# Formula: C = (F - 32) * 5/9
week_data['Temp_Celsius'] = (week_data['AvgTemperature'] - 32) * 5/9
plt.figure(figsize=(10, 5))
plt.plot(week_data['Day'], week_data['Temp_Celsius'], marker='o', color='violet', linestyle='--')
plt.title('Average Temperature in Cairo (March 7-13, 2010)')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.show()