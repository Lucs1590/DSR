import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    amplitute_variation = [1.01, 0.99]
    frequency_variation = [0.06, 0]
    transition_band = [(0.45*math.pi), (0.15*math.pi)]
    (passband, stopband, transition_band_diff) = set_diffs(
        amplitute_variation, frequency_variation, transition_band)
    omega_c = np.mean(transition_band)
    # - dB transform
    dB = to_dB(stopband)
    # - set min flutuation 1:47:14
    # - choose window type
    flutuation_type = chose_window_type(dB)
    # - set magnetude
    M = get_magnetude(transition_band_diff)
    # - create filter
    result_filter = create_filter()
    print('h[n] = {0}'.format(result_filter))


def set_diffs(amp, freq, trans):
    return (
        np.diff(amp)[0],
        np.diff(freq)[0],
        np.diff(trans)[0]
    )


def to_dB(frequency, base=20):
    return base * math.log10(frequency)


def chose_window_type(frequency):
    ...


def get_magnetude(transition_band_diff):
    ...


def create_filter():
    ...


if __name__ == '__main__':
    main()
