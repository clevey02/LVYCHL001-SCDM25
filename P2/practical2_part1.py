import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#converting ddmm to decimal degrees
def ddmm22dd(ddmm):
	thedeg = np.floor(ddmm/100.)
	themin = (ddmm - thedeg*100.)/60.
	return thedeg+ themin

df = pd.read_csv("CTD_processed_Data.csv", sep ="\t") #tab seperated headings 
df.columns = df.columns.str.strip() # Remove any spaces


print(df.columns)  # Check column names

# Use the correct column names
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12, 6))
ax1.plot(df['Temperature (°C)'],df['Depth (m)'], color='blue', label='Temperature')
ax2.plot(df['Salinity (psu)'], df['Depth (m)'], color='red', label='Salinity')
ax1.invert_yaxis() #To chnage depth to orientate according to ocean

ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Temperature (°C)')
ax1.set_title('Temperature Profile')

ax2.set_ylabel('Depth (m)')
ax2.set_xlabel('Salinity (psu)')
ax2.set_title('Salinity Profile')

plt.tight_layout()
plt.savefig('profiles_plot.png')
plt.show()
