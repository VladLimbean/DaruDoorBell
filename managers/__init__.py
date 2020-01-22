from .audio_manager import AudioManager
from .event_manager import EventManager 
from .profile_manager import ProfileManager

# make constants public
from .audio_manager import FFMPEG, NODISPLAY, AUTOEXIT, EXIT_M, NOSTATS, HIDEBANNER, SEEK, DURATION, VOLUME, LOOP

manager = AudioManager()
profile = ProfileManager()