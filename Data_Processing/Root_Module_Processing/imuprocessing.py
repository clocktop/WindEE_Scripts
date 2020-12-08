#%%
import csv
import os 
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fft import rfft, rfftfreq
import time 
plt.style.use('./plot_style.mplstyle')
# %%
accel_data = np.loadtxt('./pdata_accel/europa__newser_a.txt',delimiter=',')
# %%
gyro_data = np.loadtxt('./pdata_gyro/europa__newser_g.txt',delimiter=',')
# %%

for idx,row in enumerate(accel_data):
    accel_data[idx,0] = row[0] / 32768 * 1000 * 2 * 1.5
    accel_data[idx,1] = row[1] / 32768 * 1000 * 2 * 1.5
    accel_data[idx,2] = row[2] / 32768 * 1000 * 2 * 1.5

for idx,row in enumerate(gyro_data):
    gyro_data[idx,0] = row[0] / 32768 * 250
    gyro_data[idx,1] = row[1] / 32768 * 250
    gyro_data[idx,2] = row[2] / 32768 * 250
# %%
sample_rate = 600
n = len(accel_data)
x = np.linspace(0, n/sample_rate, n)

fig1,(ax0,ax1,ax2) = plt.subplots(3,1,sharex=True,figsize = [10,5])

ax0.plot(x,accel_data[:,0], label="Accel. X")
#ax0.set_xlabel('Time[s]')
ax0.set_ylabel('Accel.[mG]')

ax1.plot(x,accel_data[:,1], label="Accel. Y")
#ax1.set_xlabel('Time[s]')
ax1.set_ylabel('Accel.[mG]')

ax2.plot(x,accel_data[:,2], label="Accel. X")
ax2.set_xlabel('Time[s]')
ax2.set_ylabel('Accel.[mG]')

fig1.suptitle('Sample Acclerometer Data')
# %%
sample_rate = 600
n = len(gyro_data)
x = np.linspace(0, n/sample_rate, n)
a = '\u00b0'

fig2,(ax0,ax1,ax2) = plt.subplots(3,1,sharex=True,figsize = [10,5])

ax0.plot(x,gyro_data[:,0], label="Gyro. X")
#ax0.set_xlabel('Time[s]')
ax0.set_ylabel(a+'PS')

ax1.plot(x,gyro_data[:,1], label="Gyro. Y")
#ax1.set_xlabel('Time[s]')
ax1.set_ylabel(a+'PS')

ax2.plot(x,gyro_data[:,2], label="Gyro. X")
ax2.set_xlabel('Time[s]')
ax2.set_ylabel(a+'PS')

fig2.suptitle('Sample Acclerometer Data')
