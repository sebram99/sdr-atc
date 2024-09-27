import numpy as np
import matplotlib.pyplot as plt
import waveformgen

class SIFWaveform:

    def __init__(self, sample_rate = 50e6) -> None:
        self.sample_rate = sample_rate
        pass

    def make_sif_waveform(self, p1_pulse : dict, p1_p2_spacing, p2_pulse : dict, p1_p3_spacing, p3_pulse : dict):
        """
        Generates a SIF waveform by concatenating three pulses with specified spacings.

        Parameters:
        p1_pulse (dict): Dictionary containing 'Width' and 'Amplitude' for the first pulse.
        p1_p2_spacing (float): Time spacing between the end of the first pulse and the start of the second pulse.
        p2_pulse (dict): Dictionary containing 'Width' and 'Amplitude' for the second pulse.
        p1_p3_spacing (float): Time spacing between the end of the first pulse and the start of the third pulse.
        p3_pulse (dict): Dictionary containing 'Width' and 'Amplitude' for the third pulse.

        Returns:
        numpy.ndarray: Concatenated waveform consisting of the three pulses and their respective spacings.
        """
        waveform = waveformgen.WaveformGenerator(self.sample_rate)
        p1 = waveform.pulse(p1_pulse['Width'], p1_pulse['Amplitude'])
        p1_p2_space = self.sample_rate*(p1_p2_spacing - p1_pulse['Width'])
        p1_p2_space = np.zeros(int(p1_p2_space))

        p2 = waveform.pulse(p2_pulse['Width'], p2_pulse['Amplitude'])
        p1_p3_space = self.sample_rate*(p1_p3_spacing - p1_p2_spacing - p2_pulse['Width'])
        p1_p3_space = np.zeros(int(p1_p3_space))

        p3 = waveform.pulse(p3_pulse['Width'], p3_pulse['Amplitude'])

        return np.concatenate((p1, p1_p2_space, p2, p1_p3_space, p3))

    def make_mode_s_waveform(self, p1_pulse : dict, p1_p2_spacing, p2_pulse : dict, p2_p6_spacing, p6_pulse : dict):
        pass

waveform = SIFWaveform()
p1_pulse = {'Width' : 800e-9, 'Amplitude' : 0}
p2_pulse = {'Width' : 800e-9, 'Amplitude' : 0}
p3_pulse = {'Width' : 800e-9, 'Amplitude' : 0}
waveform = waveform.make_sif_waveform(p1_pulse, 2e-6, p2_pulse, 8e-6, p3_pulse)
waveform *= 2**14

print(waveform)

plt.figure(0)
plt.plot(waveform)
plt.xlabel('Samples')
plt.ylabel('Power (dB)')
plt.show()