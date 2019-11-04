import os

from subprocess import PIPE
from subprocess import Popen
from subprocess import TimeoutExpired

FFMPEG    = 'ffplay'
NODISPLAY = '-nodisp'
AUTOEXIT  = '-autoexit'

class AudioPlayer():
    """Initializes and stops audio tracks with specific flags for ffmpeg"""

    def __init__(self, audio_path):
        self.file       = os.path.abspath(audio_path)
        self.audio_proc = None

        self.playing    = False
    
    def start(self):
        print('Starting: {}'.format(self.file))
        try:
            command = [FFMPEG, self.file, NODISPLAY, AUTOEXIT] 
            self.playing    = True
            
            self.audio_proc = Popen(command, stdout=PIPE, stdin=PIPE, shell=False)
        except:
            print('Cannot play file {}'.format(self.file))

        finally:
            return self

    def stop(self):
        print('Stopping: {}'.format(self.file))
        if self.audio_proc:
            self.audio_proc.terminate()

            try:
                self.audio_proc.wait(0.1)
                print('Audio process terminated')

            except TimeoutExpired:
                print('Could not terminate process')
