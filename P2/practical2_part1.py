import matplotlib as plt
import pandas as pd
import numpy as np

#converting ddmm to decimal degrees
def ddmm22dd(ddmm):
	thedeg = np.floor(ddmm/100.)
	themin = (ddmm - thedeg*100.)/60.
	return thedeg+ themin

df = pd.read_csv("CTD_processed_Data.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12, 6))
ax1.plot(df['Depth'], df['Temperature (°C)'], color='blue', label='Temperature')
ax2.plot(df['Depth'], df['Salinity (psu)'], color='green', label='Salinity')

ax1.set_xlabel('Depth (m)')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Temperature Profile')

ax2.set_xlabel('Depth (m)')
ax2.set_ylabel('Salinity (psu)')
ax2.set_title('Salinity Profile')

plt.tight_layout()
plt.savefig('profiles_plot.png')
plt.show()
