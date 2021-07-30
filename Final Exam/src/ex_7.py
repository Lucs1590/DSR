import numpy as np


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    order = 3
    signal = [2, 3, 5, 8, 8, 10, 6]
    signal = complete_with_zeros(signal, order)
    (matrix_A, matrix_B) = define_matrix_A_B(signal, order)
    mAtA, mAtB = make_operations(matrix_A, matrix_B)
    coefficients = make_coefficients(mAtA, mAtB)
    show_results(mAtA, mAtB, coefficients)


def complete_with_zeros(signal, order):
    """# Complete with zeros

    Args:
        signal (list): list with audio samples.
        order (int): window size.

    Returns:
        list: list with the zeros after and before.
    """
    for i in range(order):
        signal.append(0)
        signal.insert(0, 0)

    return signal


def define_matrix_A_B(signal, order):
    """ # Define matriz

    Args:
        signal (list): list with audio samples.
        order (int): window size.

    Returns:
        tuple: two matrix with equation incognitas and results
    """
    matrix_a = []
    matrix_b = []
    i = 0

    for i in range(len(signal) - order):
        matrix_a.append(signal[i:i+order])
        matrix_b.append(signal[i+order])

    return np.array(matrix_a), np.array(matrix_b)


def make_operations(matrix_A, matrix_B):
    """ # Make Operations

    Args:
        matrix_A (numpy.ndarray): list with equations values
        matrix_B (numpy.ndarray): list with results values

    Returns:
        tuple: initial matrix mutiplied by first matrix transposed
    """
    matrix_A_transp = matrix_A.transpose()
    mAtA = np.dot(matrix_A_transp, matrix_A)
    mAtB = np.dot(matrix_A_transp, matrix_B)
    return mAtA, mAtB


def make_coefficients(matrix_A, matrix_B):
    """ # Make Coefficients

    Args:
        matrix_A (numpy.ndarray): first matrix multiplied by itself transposed
        matrix_B (numpy.ndarray): second matrix multiplied by first one transposed

    Returns:
        numpy.ndarray: the coefficients of linear equation
    """
    return np.linalg.solve(matrix_A, matrix_B)


def show_results(matrix_A, matrix_B, coefficients):
    """ # Show Results

    Args:
        matrix_A (numpy.ndarray): first matrix multiplied by itself transposed
        matrix_B (numpy.ndarray): second matrix multiplied by first one transposed
        coefficients (numpy.ndarray): the coefficients of linear equation
    """
    print("\n{0} * {1} = {2}\n\n{3}\n".format(
        matrix_A,
        np.array(['a{0}'.format(i+1) for i, j in enumerate(coefficients)]),
        matrix_B,
        "\n".join(['a{0} = {1}'.format(i+1, j)
                  for i, j in enumerate(coefficients)])
    ))


if __name__ == '__main__':
    main()
