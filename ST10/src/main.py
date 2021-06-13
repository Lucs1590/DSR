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
    zcr_list = []
    i = 0

    while i < len(signal):
        values = signal[i:i + delay]
        energy_list.append(calc_energy(values))
        zcr_list.append(calc_zcr(values))
        i += int(i / overlap)

    return (energy_list, zcr_list)


def calc_energy(frame):
    return np.sum(np.power(frame, 2))


def calc_zcr(frame):
    i = 0
    aux = 0
    while i < len(frame):
        aux += 1 if (frame[i] * frame[i+1]) < 0 else 0
        i += 1
    return aux


if __name__ == '__main__':
    main()
