import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    M = 5
    cutoff_freq = 1_500
    samples_p_second = 24_000
    low_pass_filter = create_low_pass_filter(M, cutoff_freq, samples_p_second)
    high_pass_filter = to_high_pass_filter(M, low_pass_filter)
    print(
        'Low-pass filter: {0}\nHigh-pass filter: {1}'.format(
            low_pass_filter, high_pass_filter)
    )


def create_low_pass_filter(size, passing_freq, samples_sec):
    """ # Creating a Filter (FIR)

    Args:
        size (int): number of samples.
        passing_freq (int): cut out frequency value.
        samples_sec (int): sample rate.

    Returns:
        list: list with the filter values.
    """
    filter = []
    max_freq = samples_sec / 2
    cut_value_divisor = (math.pi / (max_freq / passing_freq)) \
        if passing_freq >= (max_freq*0.3) \
        else (math.pi - (math.pi/(max_freq/passing_freq)))

    for n in range(size+1):
        filter.append(
            math.sin(cut_value_divisor * (n - (size/2))) /
            (math.pi * (n - (size/2)))
        )

    return filter


def to_high_pass_filter(M, low_pass_filter: list):
    if (M % 2) == 0:
        raise ValueError('''You can't use even magnetude.''')
    low_pass_filter = np.array(low_pass_filter)
    low_pass_filter = low_pass_filter[::-1]
    result = [None]*(len(low_pass_filter))
    result[::2] = low_pass_filter[::2]
    result[1::2] = low_pass_filter[1::2] * -1
    return result


if __name__ == '__main__':
    main()
