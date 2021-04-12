from scipy.io import wavfile as wv
import numpy as np


def main():
    raw_audio = read_audio("ST1/audios/soneto.wav")
    audio_arr = audio_to_arr(raw_audio)
    reversed_audio = reverse(audio_arr)
    save_audio(reversed_audio, "reversed.wav", "ST1/results")


def read_audio(path):
    return wv.read(path)


def audio_to_arr(audio):
    return np.array(audio[1], dtype=float)


def reverse(audio_arr):
    return audio_arr[::-1]


def save_audio(file, name, path):
    wv.write('{}/{}'.format(path, name), 44100, (file).astype(np.int16))


if __name__ == '__main__':
    main()
