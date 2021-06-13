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

    audio = apply_mean_removal(raw_audio)
    delay_spaces = define_delay(samples_second, ms)
    (energy, zcr) = audio_slip(audio, delay_spaces)

    print(
        'The len of pairs is: {0};\nTotal Raw Energy: {1};\nTotal Energy: {2};\n\
Total ZCR: {3};\nEnergy List: {4};\nZCR List: {5}.'.format(
            len(energy),
            calc_energy(raw_audio),
            calc_energy(audio),
            calc_zcr(audio),
            energy,
            zcr
        )
    )


def apply_mean_removal(sample):
    avg = sum(sample) / len(sample)
    return np.array(sample) - avg


def define_delay(ss, ms):
    return int((ss * ms)/1000)


def audio_slip(signal, delay, overlap=0.5):
    signal = np.array(signal)
    energy_list = []
    zcr_list = []
    i = 0

    while i < len(signal):
        values = signal[i:i + delay]
        if len(values) < delay:
            break
        energy_list.append(calc_energy(values))
        zcr_list.append(calc_zcr(values))
        i += int(len(values)*(1-overlap))

    return (energy_list, zcr_list)


def calc_energy(frame):
    return np.sum(np.power(frame, 2))


def calc_zcr(frame):
    i = 1
    aux = 0
    while i < len(frame):
        aux += 1 if (frame[i-1] * frame[i]) < 0 else 0
        i += 1
    return aux


if __name__ == '__main__':
    main()
