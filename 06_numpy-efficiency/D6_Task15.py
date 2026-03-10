import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1. Signal generation
# ----------------------------
fs = 1000        # Sampling rate (Hz)
T = 1            # Duration (seconds)
t = np.linspace(0, T, int(fs*T), endpoint=False)  # Time vector
print("Time vector t (first 10 values):", t[:10])

# Frequencies of the sine waves
f1, f2, f3 = 10, 50, 120  

# Generate signal: sum of three sine waves
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t)
print("Signal without noise (first 10 values):", signal[:10])

# Add normally distributed noise
noise = 0.5 * np.random.randn(len(t))
signal += noise
print("Added noise (first 10 values):", noise[:10])
print("Signal with noise (first 10 values):", signal[:10])

# ----------------------------
# 2. Fourier Transform
# ----------------------------
fft_signal = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/fs)

# Only positive frequencies
pos_mask = freqs >= 0
freqs_pos = freqs[pos_mask]
fft_pos = np.abs(fft_signal[pos_mask])

print("FFT magnitude (first 10 values):", fft_pos[:10])
print("Frequencies corresponding to FFT (first 10 values):", freqs_pos[:10])

# Identify dominant frequencies (top 5 peaks)
top_indices = np.argsort(fft_pos)[-5:]  # indices of largest 5 magnitudes
dominant_freqs = freqs_pos[top_indices]
print("Dominant frequencies (Hz):", np.sort(dominant_freqs))

# ----------------------------
# 3. Plotting
# ----------------------------
plt.figure(figsize=(12, 5))

# Time-domain signal
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title("Time-Domain Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Frequency-domain signal
plt.subplot(1, 2, 2)
plt.stem(freqs_pos, fft_pos, basefmt=" ")  # Removed use_line_collection
plt.title("Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.xlim(0, 200)

# Highlight dominant frequencies
for freq in dominant_freqs:
    plt.axvline(freq, color='r', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()


# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task15.py"
# Time vector t (first 10 values): [0.    0.001 0.002 0.003 0.004 0.005 0.006 0.007 0.008 0.009]
# Signal without noise (first 10 values): [0.         1.05635462 1.71114521 1.76691155 1.32507964 0.72123174
#  0.33689382 0.39046836 0.82084904 1.32659746]
# Added noise (first 10 values): [ 0.28310754  0.94549747 -1.40857672  0.0409297  -0.57080769 -0.03618779
#  -0.0900705   0.20327368 -0.40129806  0.83506143]
# Signal with noise (first 10 values): [0.28310754 2.00185209 0.3025685  1.80784125 0.75427195 0.68504396
#  0.24682332 0.59374204 0.41955098 2.16165889]
# FFT magnitude (first 10 values): [ 6.91945821 10.24125871  4.84360919 13.63077533 17.36875208  4.14032315
#  16.65955665  6.81895812 16.98820874 19.00882605]
# Frequencies corresponding to FFT (first 10 values): [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
# Dominant frequencies (Hz): [ 10.  50. 101. 120. 397.]