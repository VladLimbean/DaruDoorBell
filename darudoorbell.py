import os

from audio_player import AudioPlayer

class DaDoorBell:

    def __init__(self):
        pass

if __name__ == '__main__':
    test = 'assets/Darude-Sandstorm.mp3'
    test_player = AudioPlayer(test)
    test_player.start()