import os
from scipy.io import wavfile as wv
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    sample_rate = 12_000
    signal = [-1, 1, -2, 2, 2]

    filter = create_filter(5, 1_500, sample_rate)
    final_audio = convolve_audio(signal, filter)

    save_audio(final_audio, sample_rate, 'audio_1.wav', 'ST3/results')
    print(
        "The result of convolution between signal ({0}) and filter ({1}) is: \n {2}".
        format(
            signal, filter, final_audio.tolist()
        )
    )


def create_filter(size, passing_freq, samples_sec):
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
    cut_value_divisor = max_freq / passing_freq

    for n in range(size+1):
        filter.append(
            math.sin((math.pi/cut_value_divisor) * (n - (size/2))) /
            (math.pi * (n - (size/2)))
        )

    return filter


def convolve_audio(audio, kernel):
    """# Convolve audio
    Function that make a convolution with audios.

    Args:
        audio (numpy.ndarray): audio to convolve.
        kernel (numpy.ndarray): kernel to convolve.

    Returns:
        numpy.ndarray: result of dot multiplication of audio and kernel
    """
    return np.convolve(audio, kernel)


def save_audio(file, sample_rate, name, path):
    """ ## Save Audio

    Args:
        file (numpy.ndarray): audio array.
        sample_rate (int): sample per second.
        name (string): file name.
        path (string): path to save the file.
    """
    if len(file):
        _path = os.path.abspath(path)
        scaled = np.int16(file/np.max(np.abs(file)) * sample_rate/2)

        if os.path.isfile('{}/{}'.format(_path, name)):
            os.remove('{}/{}'.format(_path, name))
            wv.write('{}/{}'.format(_path, name), sample_rate, scaled)
        else:
            wv.write('{}/{}'.format(_path, name), sample_rate, scaled)


if __name__ == '__main__':
    main()
