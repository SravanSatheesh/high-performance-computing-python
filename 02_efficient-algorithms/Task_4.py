import numpy as np

def generate_signal(n=10000, anomaly_rate=0.001):
    """Simulates a simple signal with occasional outliers."""
    signal = np.random.normal(0, 1, n)
    anomalies = np.random.choice(n, int(n * anomaly_rate), replace=False)
    signal[anomalies] += np.random.normal(20, 5, len(anomalies))  # starke Ausreißer
    return signal

def detect_anomalies_time(signal, threshold=5.0):
    """Detects outliers in the time domain by simple threshold comparison."""
    anomalies = []
    for i, value in enumerate(signal):
        if abs(value) > threshold:
            anomalies.append(i)
    return anomalies

def detect_anomalies_fft(signal, power_threshold=100):
    """Detects anomalies based on spectral power."""
    spectrum = np.fft.fft(signal)
    power = np.abs(spectrum)**2
    anomalies = np.where(power > power_threshold)[0]
    return anomalies
