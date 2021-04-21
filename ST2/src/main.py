from scipy.io import wavfile as wv
import numpy as np


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    audio_a = generate_audio(2)
    audio_b = generate_audio(4)
    audio_y1 = convolve_audio(audio_a, audio_b)
    save_audio(audio_y1, 'audio_1', 'ST2/results')

    audio_y2 = convolve_audio(audio_y1, audio_y1)
    save_audio(audio_y2, 'audio_2', 'ST2/results')


def generate_audio(time):
    """ # Generate Audio
    Function to generate audio based on time.
    https://stackoverflow.com/a/33913403/10239129
    Args:
        time (int): time of audio (seconds)
    """
    ...


def convolve_audio(*audios):
    """# Convolve audio
    Function that make a convolution with audios.

    Args:
        *audios (): audio lists.
    """
    ...


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
