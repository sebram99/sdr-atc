import numpy as np
import matplotlib.pyplot as plt

def to_db(amplitude):
    return 10**(amplitude/20)

class WaveformGenerator:
    def __init__(self, sample_rate) -> None:
        self.sample_rate = sample_rate
        pass

    def pulse(self, pulse_width: float, amplitude_db: float):
        pulse = pulse_width*self.sample_rate
        pulse = np.ones(int(pulse))

        return pulse * to_db(amplitude_db)
