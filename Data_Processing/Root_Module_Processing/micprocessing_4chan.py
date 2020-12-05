#%%
import csv
import os 
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fft import rfft, rfftfreq
import time 
# %%

data = np.loadtxt('./processed_data/b_processed.txt',delimiter=',',dtype=np.int32)
# %%
tic = time.perf_counter()
d0 = np.array(np.zeros(int(len(data)/8),dtype=np.int32))
d1 = np.array(np.zeros(int(len(data)/8),dtype=np.int32))
d2 = np.array(np.zeros(int(len(data)/8),dtype=np.int32))
d3 = np.array(np.zeros(int(len(data)/8),dtype=np.int32))
i = 0
index = 0
while i < len(data):
    temp0 = data[i] * 256 + data[i+1]
    if temp0 > 2047: 
        temp0 = temp0 - 4095
    
    temp1 = data[i+2] * 256  + data[i+3]
    if temp1 > 2047: 
        temp1 = temp1 - 4095
    
    temp2 = data[i+4] * 256  + data[i+5]
    if temp2 > 2047: 
        temp2 = temp2 - 4095

    temp3 = data[i+6] * 256  + data[i+7]
    if temp3 > 2047: 
        temp3 = temp3 - 4095 

    d0[index] = temp0
    d1[index] = temp1
    d2[index] = temp2
    d3[index] = temp3
    index = index + 1 
    i = i + 8
toc = time.perf_counter()
print(f'Took {toc-tic:0.4f} seconds')

# %%
sample_rate = 100000
n = len(d0)
x = np.linspace(0, n/sample_rate, n)

fig1, ax1 = plt.subplots(figsize = [10,5])
ax1.plot(x,d0)

ax1_ins = ax1.inset_axes([0.5, 0.5, 0.47, 0.47])
ax1_ins.plot(x[4000:6000], d0[4000:6000])
ax1_ins.set_xticklabels('') 
ax1_ins.set_yticklabels('') 

ax1.indicate_inset_zoom(ax1_ins)

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('ADC Code')
ax1.set_title('Sample Recording')
plt.show()
# %%
sample_rate = 100000
n = 8192
win = np.hamming(n)
samp_sig = d0[0:8192]-np.round(np.mean(d0[0:8192])) * win
yf = rfft(samp_sig)
xf = rfftfreq(n,1/sample_rate)
ref = 4096
yf_mag = np.abs(yf) * 2 / np.sum(win)

yf_dbfs = 20 * np.log10(yf_mag/ref)

fig2, ax2 = plt.subplots(figsize = [10,5])

ax2.semilogx(xf, yf_dbfs)
ax2.grid(True)
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('Amplitude [dBfs]')
ax2.set_title('FFT of Sample Signal')

peakf = xf[np.argmax(yf)]
peakamp = yf_dbfs[np.argmax(yf)]
xdisp, ydisp = ax2.transData.transform_point((peakf, peakamp))
bbox = dict(boxstyle ='round',fc='0.8')
arrowprops = dict(
    arrowstyle = '->',
    connectionstyle = 'angle,angleA=0,angleB=90,rad=10'
)
offset = 72

ax2.annotate(
    'Peakf = %.1f Hz \n Peaka = %.1f dBfs'%(peakf,peakamp),
    (peakf,peakamp),
    xytext=(offset,-offset/2),
    textcoords='offset points',
    bbox = bbox,
    arrowprops = arrowprops
)
# %%
