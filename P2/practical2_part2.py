import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("SAA2_WC_2017_metocean_10min_avg.csv")

print(df.head())

#Indexing the CSV:

df = pd.read_csv("SAA2_WC_2017_metocean_10min_avg.csv", parse_dates=["TIME_SERVER"], index_col="TIME_SERVER")
print(df.head())


#selecting data for july 4th:
plot_data = df.loc["2017/07/04"]

print(plot_data.head())

#Plot time series: Temperature 

plt.style.use('grayscale')
plt.plot(plot_data.index, plot_data['TSG_TEMP'], label='Temperature', color='black')
plt.title('Time Series of Temperature on July 4, 2017')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S')) #for just hours on x axis 
plt.tight_layout()
plt.savefig('temperature_timeseries.png')  
plt.show()

#Plot histogram for salinity: 
plt.hist(plot_data['TSG_SALINITY'], bins=np.arange(30, 35.5, 0.5), color='gray', edgecolor='black')
plt.title('Salinity Distribution on July 4, 2017')
plt.xlabel('Salinity (psu)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('salinity_histogram.png')  # Save as PNG
plt.show()

#Working out the statistics: 

temperature_mean = plot_data['TSG_TEMP'].mean()
temperature_std = plot_data['TSG_TEMP'].std()
temperature_iqr = plot_data['TSG_TEMP'].quantile(0.75) - plot_data['TSG_TEMP'].quantile(0.25)

salinity_mean = plot_data['TSG_SALINITY'].mean()
salinity_std = plot_data['TSG_SALINITY'].std()
salinity_iqr = plot_data['TSG_SALINITY'].quantile(0.75) - plot_data['TSG_SALINITY'].quantile(0.25)

# Display the results in a table
stats_df = pd.DataFrame({
    'Temperature': [temperature_mean, temperature_std, temperature_iqr],
    'Salinity': [salinity_mean, salinity_std, salinity_iqr]
}, index=['Mean', 'Standard Deviation', 'IQR'])

print(stats_df)

#Scatter plot:
plt.figure(figsize=(10, 6))
plt.scatter(plot_data['WIND_SPEED_TRUE'], plot_data['AIR_TEMPERATURE'], c=plot_data['LATITUDE'], cmap='viridis', s=50, edgecolor='black')
plt.colorbar(label='Latitude')
plt.title('Scatter Plot of Wind Speed vs. Air Temperature (Latitude Encoded in Color)')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Air Temperature (°C)')
plt.tight_layout()
plt.savefig('wind_speed_air_temp_scatter.png', dpi=300)  
plt.show()

