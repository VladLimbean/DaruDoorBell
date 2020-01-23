
from .audio_manager import manager, NODISPLAY, AUTOEXIT, NOSTATS, HIDEBANNER, LOOP

class ProfileManager():
    """Determines playing order for Sandstorm
    
    Also a singleton
    """

    def __init__(self):
        self.dududu_counter = 0

    def start_audio(self, asset, options):
        print(">>>> {}".format(options))

        manager.init_audio_process(asset, config=options)

    def play_segment(self):
        asset = ''
        if self.dududu_counter == 0:
            asset = 'assets/background.wav'
            self.start_audio(asset, [(LOOP, 0), NODISPLAY, NOSTATS, HIDEBANNER])
        
        elif self.dududu_counter > 3:
            asset = 'assets/main.mp3'
            self.start_audio(asset, [NODISPLAY, NODISPLAY, NOSTATS, HIDEBANNER, (LOOP, 4), AUTOEXIT])

        elif self.dududu_counter % 2 != 0:
            asset = 'assets/du_s1.wav'
            self.start_audio(asset, [NODISPLAY, AUTOEXIT, NOSTATS, HIDEBANNER])

        elif self.dududu_counter % 2 == 0:
            asset = 'assets/du_s2.wav'
            self.start_audio(asset, [NODISPLAY, AUTOEXIT, NOSTATS, HIDEBANNER])

        

        self.dududu_counter += 1

    def click(self):
        """Plays darude sandstorm in specific, hardcoded order"""
        self.play_segment()
