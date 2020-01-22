import os

from subprocess import PIPE
from subprocess import Popen

class AudioProcess():
    """Initializes and stops audio tracks with specific flags for ffmpeg"""

    def __init__(self, audio_path, options):
        self.file       = os.path.abspath(audio_path)
        self.args        = options
        
        # add file to play
        self.args.append(self.file)

        self.audio_proc = None
        self.playing    = False

        self.start()

    #------------------------------------------------------------------------------------[AUDIO PROCESS INIT]
    def start(self):
        print('Starting: {}'.format(self.file))
        #print('Options: {}'.format(self.args))
        try:
            
            self.audio_proc = Popen(self.args, stdout=PIPE, stdin=PIPE, shell=False)
            self.playing    = True
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
                self.playing = False

            except:
                print('Could not terminate process')
    
    #------------------------------------------------------------------------------------[UTIL]

    def is_playing(self):
        return self.playing

    def get_process(self):
        return self

    #------------------------------------------------------------------------------------[EVENT]
    def __call__(self, event):
        print("I have been called")