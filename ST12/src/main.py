import matplotlib.pyplot as plt
import numpy as np


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    order = 3
    signal = [2, 3, 5, 8, 8, 10, 6]
    signal = complete_with_zero(signal, order)
    (matrix_A, matrix_B) = define_matrix_A_B(signal)


def complete_with_zero(signal, order):
    for i in range(order):
        signal.append(0)
        signal.insert(0, 0)

    return signal


def define_matrix_A_B(signal):
    ...


if __name__ == '__main__':
    main()
