# DaruDoorBell

Your friends come over to your place. They press the button to your door ringy dingy thingy.

The backing track to Sandstorm fades in. Each button press will play a "DU-DU-DU-DU-DU!" After a few of those, the main track plays on a loop for a few times.

Everyone gets a laugh and you have yourself a nice practical joke and possibly some copyright infringement. 

# Usage

`python3 darudoorbell.py`

press `a` to DUDUDUD

press `q` to quit and terminate the script

Future implementation wil feature a GPIO button listener. Stay tuned.

# Current implementation requirements

Since it is supposed to be portable, I implemented this on a RaspberryPi 3.
You will need ffmpeg as part of your environment variables, or a local binary.

Actually building ffmpeg is pretty time consuming and tedious. [Here's how](https://stackoverflow.com/questions/5000385/playing-audio-with-ffmpeg/58703126#58703126) you do it. 
As an alternative, RaspberryPi 4 has ffmpeg inbuilt.

# TODOs

Implement GPIO button listener for an actuall ringer and not a keyboard button.
Do some polish on the audio sequencing and timing. Right now it's pretty hack 'n slash.
Get a bluetooth speaker and test it out in the field.
Take pictures once I make the whole hting and be amazed that I did it :)

# Known issues

The implementation implies a bunch of audio processes playing some files stored locally. Each process played is stored locally inside a manager class in a list. This list does not get populated to save its life in the current commit.

It is a non critical issue, since the core functionality is still there. However, it makes polishing this code a bit of a nuisance. Will fix as soon as I figure out what I'm doing wrong (might be the raspbian, who knows??)
