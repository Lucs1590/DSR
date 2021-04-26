from scipy.io import wavfile as wv
import os
import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    audio_a = generate_audio(2)
    audio_b = generate_audio(time=4, frequence=400)
    audio_y1 = convolve_audio(audio_b, audio_a)
    save_audio(audio_a, 'base_audio_1.wav', 'ST2/audios')
    save_audio(audio_b, 'base_audio_2.wav', 'ST2/audios')
    save_audio(audio_y1, 'audio_1.wav', 'ST2/results')

    audio_y2 = convolve_audio(audio_y1, audio_y1)
    save_audio(audio_y2, 'audio_2.wav', 'ST2/results')
    print(
        'The general formula to audios size is n = (n1 + n2)-1.\n \
        For example, audio 1 has {0} samples and audio 2 has {1} samples.\n \
        The convolution result has {2} samples.'.format(
            len(audio_a),
            len(audio_b),
            (len(audio_a)+len(audio_b))-1
        )
    )


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


def save_audio(file, name, path):
    """ ## Save Audio

    Args:
        file (numpy.ndarray): audio array.
        name (string): file name.
        path (string): path to save the file.
    """
    if len(file):
        _path = os.path.abspath(path)
        if os.path.isfile('{}/{}'.format(_path, name)):
            os.remove('{}/{}'.format(_path, name))
            wv.write('{}/{}'.format(_path, name),
                     44100, (file).astype(np.int16))
        else:
            wv.write('{}/{}'.format(_path, name),
                     44100, (file).astype(np.int16))


if __name__ == '__main__':
    main()
