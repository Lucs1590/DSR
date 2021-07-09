import matplotlib.pyplot as plt
import numpy as np


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    order = 3
    signal = [2, 3, 5, 8, 8, 10, 6]
    signal = complete_with_zeros(signal, order)
    (matrix_A, matrix_B) = define_matrix_A_B(signal, order)


def complete_with_zeros(signal, order):
    for i in range(order):
        signal.append(0)
        signal.insert(0, 0)

    return signal


def define_matrix_A_B(signal, order):
    matrix_a = []
    matrix_b = []
    i = 0

    for i in range(len(signal) - order):
        matrix_a.append(signal[i:i+order])
        matrix_b.append(signal[i+order])

    return matrix_a, matrix_b


if __name__ == '__main__':
    main()
