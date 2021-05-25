from functools import reduce
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    amplitute_variation = [1.01, 0.99]
    frequence_variation = [0.06, 0]
    transition_band = [(0.45*math.pi), (0.15*math.pi)]
    # - fuction to set diffs
    # (passband, stopband, transition_band_diff) = set_diffs(amplitute_variation, frequence_variation, transition_band)
    passband = np.diff(amplitute_variation)[0]
    stopband = np.diff(frequence_variation)[0]
    transition_band_diff = np.diff(transition_band)[0]

    omega_c = np.mean(transition_band)
    # - dB transform
    # - set min flutuation 1:47:14
    # - choose window type
    # - set magnetude
    # - create filter
    M = get_magnetude(transition_band_diff)
    print('test')


def get_magnetude(transition_band_diff):
    ...


if __name__ == '__main__':
    main()
