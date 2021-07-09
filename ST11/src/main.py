import matplotlib.pyplot as plt


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    signal = [0, 1, 3, 0, 1, 3, 0, 1, 3, 0]

    reverse_signal = reverse(signal)
    result_signal = apply_AMDF(reverse_signal, signal)
    show_results(result_signal)


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


def show_results(samples):
    print("AMDF: {0}\nF1: {1} at position {2}.".
          format(
              samples,
              None if (len(samples) %
                       2) == 0 else samples[int(len(samples)/2)],
              None if (len(samples) % 2) == 0 else int(
                  len(samples)/2) + 1,
          ))

    plt.plot(samples)
    plt.show()


if __name__ == '__main__':
    main()
