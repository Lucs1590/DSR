from scipy.io import wavfile as wv
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    audio_a = generate_audio(2)
    audio_b = generate_audio(4)
    audio_y1 = convolve_audio(audio_a, audio_b)
    save_audio(audio_y1, 'audio_1.wav', 'ST2/results')

    audio_y2 = convolve_audio(audio_y1, audio_y1)
    save_audio(audio_y2, 'audio_2.wav', 'ST2/results')


def generate_audio(time, sample_rate=44100.0, frequence=100):
    """# Generate Audio
    Function to generate audio based on time.

    Args:
        time (int): time of the audio.
        sample_rate (float, optional): sample rate of the audio. Defaults to 44100.0.
        frequence (int, optional): frequence of the audio. Defaults to 100.

    Returns:
        numpy.ndarray: audio with the samples.
    """
    audio = []
    num_samples = (time * 1000) * (sample_rate / 1000.0)
    for x in range(int(num_samples)):
        audio.append(np.iinfo(np.int16).max *
                     math.sin(2 * math.pi * frequence * (x / sample_rate)))
    return np.array(audio)


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
