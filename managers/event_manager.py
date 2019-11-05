
import keyboard

# add events

class EventManager():
    """Handles all external events for audio processes"""

    def __init__(self):
        self.subscribed_procs = []

    def notify(self, event):
        for sub in self.subscribed_procs:
            if sub and sub.is_playing():
                sub(event)

    def subscribe(self, process):
        self.subscribed_procs.append(process)

    def unsubscribe(self, process):
        self.subscribed_procs.remove(process)
