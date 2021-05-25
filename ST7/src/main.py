from functools import reduce
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    amplitute_variation = [1.01, 0.99]
    frequence_variation = [0.06, 0]
    transition_band = [(0.45*math.pi), (0.15*math.pi)]

    passband = np.diff(amplitute_variation)[0]
    stopband = np.diff(frequence_variation)[0]
    omega_c = np.mean(transition_band)
    print('test')


if __name__ == '__main__':
    main()
