import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Read the wav file
sample_rate, data = wavfile.read('Cnetz_cell_broadcast.wav')

# Compute FFT
fft_result = np.fft.fft(data)
frequencies = np.fft.fftfreq(len(fft_result))

# Compute absolute value, which is the magnitude of the FFT
magnitude = np.abs(fft_result)

# Find the indices of the two highest peaks
indices = (-magnitude).argsort()[:2]

# Calculate FSK deviation
fsk_deviation = np.abs(frequencies[indices[0]] - frequencies[indices[1]]) * sample_rate
print('Estimated FSK deviation: ', fsk_deviation, 'Hz')
plt.plot(frequencies, magnitude)
plt.show()
