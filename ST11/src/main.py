import matplotlib.pyplot as plt


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    signal = [0, 1, 3, 0, 1, 3, 0, 1, 3, 0]
    samples_second = 8_000

    reverse_signal = reverse(signal)
    result_signal = apply_AMDF(reverse_signal, signal)
    show_results(result_signal, samples_second)


def reverse(audio_arr):
    """ ## Reverse

    Args:
        audio_arr (numpy.ndarray): audio data in numpy array type.

    Returns:
        numpy.ndarray: reversed array.
    """
    return audio_arr[::-1]


def apply_AMDF(signal_1, signal_2):
    results = []
    final_size = (len(signal_1) + len(signal_2)) - 1

    for idx, i in enumerate(signal_2):
        aux = []
        for j in signal_1:
            aux.append(abs(i-j))
        aux = complete_with_zeros(reverse(aux), final_size, idx)
        results.append(aux)

    return [sum(i) for i in zip(*results)]


def complete_with_zeros(signal, final_size, idx):
    for i in range(idx):
        signal.append(0)

    while len(signal) < final_size:
        signal.insert(0, 0)

    return signal


def find_period(samples_second):
    samples_period = 4
    return samples_period / samples_second


def show_results(samples, samples_second):
    print("\
    Samples per Second: {4}\n\
    T: {5}\n\
    AMDF: {0}\n\
    F0: {3}\n\
    Min Value: {1} at position {2} (center)".
        format(
            samples,
            None if (len(samples) %2) == 0 else samples[int(len(samples)/2)],
            None if (len(samples) % 2) == 0 else int(len(samples)/2) + 1,
            1 / find_period(samples_second),
            samples_second,
            find_period(samples_second)
        ))

    plt.plot(samples)
    plt.show()


if __name__ == '__main__':
    main()
