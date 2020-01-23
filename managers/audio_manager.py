import time
from threading import Thread
from threading import Event
from threading import Lock

from player import AudioProcess

### OPTION DEFINITION ###
FFMPEG    = 'ffplay'
NODISPLAY = '-nodisp'
AUTOEXIT  = '-autoexit'
SEEK      = '-ss'               # takes an argument of where to start playing from
DURATION  = '-t'                # takes number of seconds
VOLUME    = '-volume'           # 0 - 100
LOOP      = '-loop'             # how many loops, 0 means forever
EXIT_M    = '-exitonmousedown'
EXIT_K    = '-exitonkeydown'
NOSTATS   = '-nostats'
HIDEBANNER = '-hide_banner'

global options, arg_options
options     = [FFMPEG, NODISPLAY, AUTOEXIT, EXIT_M, NOSTATS, HIDEBANNER, LOOP]
arg_options = [SEEK, DURATION, VOLUME, LOOP]

class AudioManager(Thread):
    """Handles audio process creation and options
    
    Takes a list of tuples or strings

    This class is treated as a singleton
    """

    def __init__(self):
        Thread.__init__(self)
        self.setName('AudioManager')
        self.stop_event = Event()
        self.lock       = Lock()

        self.process_options = []
        self.audio_procs     = [] # holds all audio processes

    #------------------------------------------------------------------------------------[AUDIO PROCESS INIT]

    def init_audio_process(self, path, config=list):
        self.lock.acquire()
        
        for itm in config:
            #allow strings
            if type(itm) == str:
                itm = tuple(itm)
            elif itm[0] not in options or itm[0] not in arg_options:
                print('Error: Unkown option')
                return
            elif type(itm) != tuple:
                print('Error: Option item is not a tuple')
                return
        self.process_options.append(FFMPEG)

        for itm in config:
            self.__set_process_option(itm)
        try:
            _proc = AudioProcess(audio_path=path, options=self.process_options)
            #print('config list >>> {}'.format(self.process_options))
            #print('Process initialized')

            # TODO: figure out why the process never registers in the list
            self.audio_procs.append(_proc)
            self.reset_process_options()
        except:
            print('WTF?')
        self.lock.release()
        
    def __set_process_option(self, option=tuple):
        res_config = ''
        
        # set options with args
        if len(option) == 2 and option[0] in arg_options:    
            #res_config = '{} {}'.format(option[0], option[1])
            self.process_options.append(option[0])
            self.process_options.append(str(option[1]))
            return

        # set options w/o args
        elif option in options:
            res_config = option 
            self.process_options.append(res_config)
            return
    
    #------------------------------------------------------------------------------------[UTIL]

    def reset_process_options(self):
        #print("Resetting process options")
        self.process_options = []

    def terminate_all(self):
        self.lock.acquire()
        for proc in self.audio_procs:
            try:
                if proc:
                    proc.stop()
            except:
                raise ProcessLookupError('Somthing happened when trying to close the process')
        self.lock.release()
        print('All processes terminated')

    def update(self):
        """Refreshes the audio process list removing idle processes"""
        kill = []
        for proc in self.audio_procs:
            if proc == None:
                continue

            proc.audio_proc.poll()
            
            if proc.audio_proc.returncode != None:
                kill.append(proc)
        
        for i in kill:
            if i != None:
                i.stop()
                self.audio_procs.remove(i)

        self.state()
    #------------------------------------------------------------------------------------[STATE / EVENTS]
    def state(self):
        """Describes number of processes running.
        
        THIS IS CURRENTLY BROKEN SINCE THE LIST MAGICALLY REFUSES TO REGUSTER ANY APPENDED PROCESSES
        MIGHT BE MY MISTAKE, WILL FIX ASAP
        """
        res = 'Processes playing: {}'.format(len(self.audio_procs))
        print(res, sep='', end='\r', flush=True)

    def is_stopped(self):
        return self.stop_event.is_set()
    
    def stop(self):
        self.terminate_all()
        self.stop_event.set()

    def run(self):
        while not self.is_stopped():
            self.update()
            time.sleep(0.3)

manager = AudioManager()
