import matplotlib.pyplot as plt


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    signal = [0, 1, 3, 0, 1, 3, 0, 1, 3, 0]

    reverse_signal = reverse(signal)
    result_signal = apply_AMDF(reverse_signal, signal)
    plot_graph(result_signal)
    print("AMDF: {0}\nF1: {1} at position {2}.".format(
        result_signal,
        None if (len(result_signal) %
                 2) == 0 else result_signal[int(len(result_signal)/2)],
        None if (len(result_signal) % 2) == 0 else int(
            len(result_signal)/2) + 1,
    )
    )


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


def plot_graph(samples):
    plt.plot(samples)
    plt.show()


if __name__ == '__main__':
    main()
