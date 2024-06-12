import pandas as pd
from galvani import BioLogic
import matplotlib.pyplot as plt

mpr_file = BioLogic.MPRfile(r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Experiment files\FF068\SOC plot\FF068_nmr_a_C06.mpr")
# Define start and end times
start_time = 4109
end_time = 8200

excel_data = pd.read_excel(r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Experiment files\FF068\SOC plot\chemical_shifts_data.xlsx")
time_excel = excel_data['Time(s)']
chemical_shift_excel = excel_data['Chemical Shift (ppm)']


df = pd.DataFrame(mpr_file.data)
# Filter DataFrame to include rows within the specified start and end times
filtered_df = df[(df['time/s'] >= start_time) & (df['time/s'] <= end_time)]

# Subtract start time from 'time/s' column to reindex it
reind_df = filtered_df.copy()
reind_df['time/s'] = reind_df['time/s'] - start_time

print(df.columns)

time = reind_df['time/s']
voltage = reind_df['Ewe/V']
current = reind_df['I/mA']
charge = reind_df['(Q-Qo)/mA.h']

plt.rcParams.update({'font.size': 14, 'font.weight': 'bold'})
plt.rcParams['axes.labelweight'] = 'bold'

fig, ax1 = plt.subplots(nrows=3, ncols=1, figsize=(12, 10))

# Plot voltage and current on the first subplot
ax1[0].plot(time, voltage, color='b', label='Voltage')
ax1[0].set_ylabel('Voltage (V)', color='b')
ax1[0].tick_params('y', colors='b')

ax2 = ax1[0].twinx()
ax2.plot(time, current, color='r', label='Current')
ax2.set_ylabel('Current (mA)', color='r')
ax2.tick_params('y', colors='r')

# Plot charge on the second subplot
ax1[1].plot(time, charge, color='g', label='Charge')
ax1[1].set_ylabel('(Q-Qo) (mAh)', color='g')
ax1[1].tick_params('y', colors='g')

# Plot chemical shift from Excel data on the third subplot
ax1[2].plot(time_excel, chemical_shift_excel, 'x', color='m', label='Chemical Shift (Excel)')
ax1[2].set_xlabel('Time (s)')
ax1[2].set_ylabel(r'$\delta$OCF$_3$ (ppm)', color='m')
ax1[2].tick_params('y', colors='m')

plt.subplots_adjust(hspace=0)  # Adjust the spacing between subplots
plt.show()




