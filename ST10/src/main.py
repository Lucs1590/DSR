from scipy.io import wavfile as wv
from functools import reduce
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    raw_audio = [1, 2, -3, 3, -2, 1, -1, -1, 4, 5, -5, 4]
    samples_second = 8_000
    ms = 0.25

    delay_spaces = define_delay(samples_second, ms)
    (energy, zcr) = audio_slip(raw_audio, delay_spaces)


def define_delay(ss, ms):
    return int((ss * ms)/1000)


def audio_slip(signal, delay, overlap=0.5):
    signal = np.array(signal)
    energy_list = []
    aux = []
    zc = 0
    i = 0

    while i < len(signal):
        values = signal[i:i + delay]
        energy_list.append()
        i += int(i / overlap)

    return aux


def calc_energy(frame):
    return list(map())

if __name__ == '__main__':
    main()
