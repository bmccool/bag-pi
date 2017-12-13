import pygame
import pygame.midi
from time import sleep
from Embellishments import * 
from bww_reader import BWWReader
import logging

logger = logging.getLogger(__name__)
FORMAT = "[%(filename)-14s:%(lineno)-3s - %(funcName)-15s():%(levelname)-8s ] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

# Parameters that you can change
instrument = 109 
velocity = 127
emb_length = .050 #embelishment note length
WHOLE_NOTE = 1.5 

ng = 55
na = 57
nb = 59
nc = 61
nd = 62
ne = 64
nf = 66
nG = 67
nA = 69



def transpose(delta):
    global ng
    global na
    global nb
    global nc
    global nd
    global ne
    global nf
    global nG
    global nA
    ng = ng + delta
    na = na + delta
    nb = nb + delta
    nc = nc + delta
    nd = nd + delta
    ne = ne + delta
    nf = nf + delta
    nG = nG + delta
    nA = nA + delta
    notes["g"] = ng
    notes["a"] = na
    notes["b"] = nb
    notes["c"] = nc
    notes["d"] = nd
    notes["e"] = ne
    notes["f"] = nf
    notes["G"] = nG
    notes["A"] = nA

notes = {"g" : ng,  
         "a" : na,
         "b" : nb,
         "c" : nc, 
         "d" : nd, 
         "e" : ne, 
         "f" : nf, 
         "G" : nG,
         "A" : nA}
velocity = 127


def get_fraction(duration):
    return "1/" + str(int((WHOLE_NOTE / duration)))

def play_note(note, duration=1.000, embellishment=None):
    if not embellishment: logger.info ("Playing: " + str(note) + ", " + get_fraction(duration))
    else: logger.info ("Playing: " + str(note) + ", " + get_fraction(duration) + ", Embellishment: " + str(embellishment.notes))

    played = 0
    if embellishment is not None: #Play embellishment...
        for emb_note in embellishment.notes:
            midiOutput.note_on(notes[emb_note], velocity)
            sleep(emb_length)
            midiOutput.note_off(notes[emb_note], velocity)
            played = played + emb_length
    # Then play the note
    midiOutput.note_on(notes[note], velocity)
    sleep(duration - played)
    midiOutput.note_off(notes[note], velocity) 


def play_file(filename):
    song = BWWReader(filename)
    embellishment = None
    note = None
    while(True):
        part = song.interpret_next()
        if part is not None:
            if part.split()[0] == "Embellishment":
                logger.debug("Found Embellishment: " + str(part.split()[1]))
                embellishment = getattr(Embellishments, part.split()[1])
            elif part.split()[0] == "note":
                logger.debug("Found a note!")
                note = [part.split()[1], part.split()[2]] #[Pitch, duration]
        else: 
            break
        if note is not None:
            logger.debug("Found something to play")
            play_note(note[0], WHOLE_NOTE / int(note[1]), embellishment)
            embellishment = None
            note = None

# Initialize the Pygame and pygame.midi modules
pygame.init()
pygame.midi.init()

# This port number seems the only one to work
port = 2  
latency = 0 

# Set parameters
midiOutput = pygame.midi.Output(port, latency)
midiOutput.set_instrument(instrument)

transpose(3)

try:
#    song_itchy_fingers(.200)
    logger.info("Playing file")
    play_file("itchy_fingers_stripped.bww")

except (KeyboardInterrupt, SystemExit):
    # close the handler and quit midi
    del midiOutput
    pygame.midi.quit()

# close the handler and quit midi
del midiOutput
pygame.midi.quit()
