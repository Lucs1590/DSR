from functools import reduce
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    amplitute_variation = [0.99, 1.01]
    frequency_variation = [0, 0.06]
    transition_band = [(0.15*math.pi), (0.45*math.pi)]
    (passband, stopband, transition_band_diff) = set_diffs(
        amplitute_variation, frequency_variation, transition_band)
    omega_c = np.mean(transition_band)
    dB = to_dB(stopband)
    windowing_type = choose_window_type(dB)
    M = get_magnetude(transition_band_diff, windowing_type)
    result_filter = create_filter(M, omega_c, windowing_type)
    print('Filter: {0}\nNormalized_filter: {1}'.format(
        result_filter, normalize(result_filter)))
    # - mike difference function
    # - make readme


def set_diffs(amp, freq, trans):
    """ # Set Difference Values

    Args:
        amp (list): amplitutes flutuation list.
        freq (list): frequencies flutuation list.
        trans (list): transition band variation list.

    Returns:
        tuple: tuple with difference value for each input params.
    """
    return (
        np.diff(amp)[0],
        np.diff(freq)[0],
        np.diff(trans)[0]
    )


def to_dB(frequency, base=20):
    """ # To dB

    Args:
        frequency (float): Gain value.
        base (int, optional): Base of log transform. Defaults to 20.

    Returns:
        float: value in dB.
    """
    return base * math.log10(frequency)


def choose_window_type(measure):
    """ # Chose Window Type

    Args:
        measure (float): dB value.

    Returns:
        str: name of window type.
    """
    reference = {
        'rectangular': -21,
        'barlett': -25,
        'hanning': -44,
        'hamming': -53,
        'blackman': -74
    }
    allow_values = list(
        filter(lambda value: value[1] < measure, reference.items()))
    closet_value = sorted(list(map(lambda value: (value[0], abs(
        value[1]-measure)), allow_values)), key=lambda element: element[1])
    return closet_value[0][0]


def get_magnetude(trans_diff, _type):
    """ # Get Magnetude

    Args:
        trans_diff (float): difference value between transition band.
        _type (str): window type name.

    Returns:
        int: the magnetude value.
    """
    reference = {
        'rectangular': 0.9,
        'barlett': 3.0,
        'hanning': 3.1,
        'hamming': 3.3,
        'blackman': 5.5
    }
    magnetude = reference[_type] / to_frequency_domain(trans_diff)
    return int(magnetude)


def to_frequency_domain(omega):
    """ # To Frequency Domain

    Args:
        omega (float): transition band variation with pi value.

    Returns:
        float: transition value in frequency domain.
    """
    return omega / (2 * math.pi)


def create_filter(size, cutoff_freq, windowing_type):
    """ # Create Filter

    Args:
        size (int): the magnetude value.
        cutoff_freq (float): cutoff frequency.
        windowing_type (str): name of window type.

    Returns:
        list: filter list.
    """
    filter = []
    for n in range(size+1):
        try:
            value = math.sin(cutoff_freq * (n - (size/2))) / \
                (math.pi * (n - (size/2)))
            filter.append(value)
        except:
            filter.append(cutoff_freq/math.pi)

    return filter


def normalize(_list):
    """ # Normalize list

    Args:
        signal (list): list of audio or filter.

    Returns:
        list: list of normalized value
    """
    list_sum = reduce((lambda x, y: x + y), _list)
    normalized_signal = list(map(lambda hi: hi/list_sum, _list))
    return normalized_signal


if __name__ == '__main__':
    main()
