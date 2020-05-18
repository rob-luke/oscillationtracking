import numpy as np

def sinusoid(amplitude=1.0, frequency=1.0, phase=0.0, duration=60.0, samplerate=100.0):
    """Generate a sinusoid"""
    t = np.arange(0, duration, 1.0/samplerate)
    d = np.sin(2.0 * np.pi * frequency * t)
    return t, d

