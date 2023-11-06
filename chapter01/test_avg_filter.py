import numpy as np
import matplotlib.pyplot as plt
from get_volt import get_volt
from avg_filter import AvgFilter

#np.random.seed(0)

# Set the sample interval and generate the time vector
dt = 0.2
t = np.arange(0, 10 + dt, dt)

# Pre-allocate arrays for efficiency
Nsamples = len(t)
Avgsaved = np.zeros(Nsamples)
Xmsaved = np.zeros(Nsamples)

avg_filter = AvgFilter()

# Sampling loop
for k in range(Nsamples):
    xm = get_volt()
    avg = avg_filter.filter(xm)

    Avgsaved[k] = avg
    Xmsaved[k] = xm

# Plotting the results
plt.figure()
plt.plot(t, Xmsaved, '*:r', label='Measured')
plt.plot(t, Avgsaved, 'o-b', label='Average')
plt.legend()
plt.show()