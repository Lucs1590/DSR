from scipy.io import wavfile as wv
import numpy as np


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    raw_audio = read_audio("ST1/audios/soneto.wav")
    audio_arr = audio_to_arr(raw_audio)
    reversed_audio = reverse(audio_arr)
    save_audio(reversed_audio, "reversed.wav", "ST1/results")


def read_audio(path):
    """## Read Audio

    Args:
        path (string): audio file path.

    Returns:
        tuple: the read file.
    """
    return wv.read(path)


def audio_to_arr(audio):
    """ ## Audio to Array

    Args:
        audio (tuple): original read audio file.

    Returns:
        numpy.ndarray: array of audio data.
    """
    return np.array(audio[1], dtype=float)


def reverse(audio_arr):
    """ ## Reverse

    Args:
        audio_arr (numpy.ndarray): audio data in numpy array type.

    Returns:
        numpy.ndarray: reversed array.
    """
    return audio_arr[::-1]


def save_audio(file, name, path):
    """ ## Save Audio

    Args:
        file (numpy.ndarray): audio array.
        name (string): file name.
        path (string): path to save the file.
    """
    wv.write('{}/{}'.format(path, name), 44100, (file).astype(np.int16))


if __name__ == '__main__':
    main()
