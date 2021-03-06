import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    M = 5
    cutoff_frequencies = [2_500, 3_500]
    samples_p_second = 10_000
    band_stop = True

    low_pass_filter = create_filter(
        M, cutoff_frequencies[0], samples_p_second, False)

    high_pass_filter = create_filter(
        M, cutoff_frequencies[1], samples_p_second, True)
    high_pass_filter = to_high_pass_filter(M, high_pass_filter)

    result_filter = join_filters(low_pass_filter, high_pass_filter, band_stop)
    print(
        'Low-pass filter: {0}\nHigh-pass filter: {1}\n {2} filter: {3}'.format(
            low_pass_filter,
            high_pass_filter,
            'Band-stop'if band_stop else 'Band-pass',
            result_filter
        )
    )


def create_filter(size, passing_freq, samples_sec, high_pass):
    """ # Creating a Filter (FIR)

    Args:
        size (int): number of samples.
        passing_freq (int): cut out frequency value.
        samples_sec (int): sample rate.
        high_pass (bool): is high pass filter?

    Returns:
        list: list with the filter values.
    """
    filter = []
    max_freq = samples_sec / 2

    cut_value_divisor = define_cutoff(max_freq, passing_freq, high_pass)

    for n in range(size+1):
        filter.append(
            math.sin(cut_value_divisor * (n - (size/2))) /
            (math.pi * (n - (size/2)))
        )

    return filter


def define_cutoff(max_freq, passing_freq, high_pass):
    """ # Define Cutoff Value

    Args:
        max_freq (int): the max frequency allowed
        passing_freq (int): the cutoff value
        high_pass (bool): if is a high pass filter

    Returns:
        float: the cutoff value to subtitute wc
    """
    cut_value_divisor = (math.pi / (max_freq / passing_freq))
    if high_pass:
        cut_value_divisor = (math.pi / (max_freq / passing_freq)) \
            if passing_freq >= (max_freq*0.3) \
            else (math.pi - (math.pi/(max_freq/passing_freq)))
    return cut_value_divisor


def to_high_pass_filter(M, low_pass_filter: list):
    """# To High Pass

    Args:
        M (int): the filter magnetude.
        low_pass_filter (list): the filter.

    Raises:
        ValueError: Filter with odd magnetude.

    Returns:
        list: the high pass filter.
    """
    if (M % 2) == 0:
        raise ValueError('''You can't use even magnetude.''')
    low_pass_filter = np.array(low_pass_filter)
    low_pass_filter = low_pass_filter[::-1]
    result = [None]*(len(low_pass_filter))
    result[::2] = low_pass_filter[::2]
    result[1::2] = low_pass_filter[1::2] * -1
    return result


def join_filters(filter_1, filter_2, band_stop):
    """ # Join Filters

    Args:
        filter_1 (list): list with first filter
        filter_2 (list): list with second filter
        band_stop (bool): if the result is band-stop filter

    Returns:
        list: band-stop filter or band-pass filter
    """
    filter_1 = np.array(filter_1)
    filter_2 = np.array(filter_2)
    return (filter_1 + filter_2).tolist() if band_stop else (filter_1 - filter_2).tolist()


if __name__ == '__main__':
    main()
