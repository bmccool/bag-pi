import pygame
import pygame.midi
from time import sleep
from Embellishments import * 

# Parameters that you can change
instrument = 109 
velocity = 127
emb_length = .050 #embelishment note length

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


def play_note(note, duration=1.000, embellishment=None):
    """played = 0
    if embelishment is not None: played = embelishment()
    midiOutput.note_on(note, velocity)
    print "playing note: " + str(note)
    sleep(duration - played)
    midiOutput.note_off(note, velocity)
    """
    played = 0
    if embellishment is not None: #Play embellishment...
        for emb_note in embellishment.notes:
            midiOutput.note_on(notes[emb_note], velocity)
            print "playing embellishment: " + str(emb_note)
            sleep(emb_length)
            midiOutput.note_off(notes[emb_note], velocity)
            played = played + emb_length
    midiOutput.note_on(notes[note], velocity)
    print "playing note: " + str(note)
    sleep(duration - played)
    midiOutput.note_off(notes[note], velocity) 

def song_itchy_fingers(eigth=.300):
    quarter = eigth * 2
    play_note("c", eigth, g_g)
    play_note("d", eigth)
    play_note("e", quarter, g_gef)
    play_note("e", eigth, g_a)
    play_note("f", eigth)
    play_note("e", eigth, g_g)
    play_note("a", eigth)
    play_note("c", eigth)
    play_note("e", eigth)
    play_note("f", eigth, g_g)
    play_note("a", eigth)
    play_note("d", eigth)
    play_note("f", eigth)
    play_note("e", quarter, g_gef)
    play_note("c", eigth, g_g)
    play_note("d", eigth)
    play_note("e", quarter, g_gef)
    play_note("e", eigth, g_a)
    play_note("f", eigth)
    play_note("e", eigth, g_g)
    play_note("a", eigth)
    play_note("c", eigth)
    play_note("e", eigth)
    play_note("c", eigth, g_g)
    play_note("a", eigth, g_d)
    play_note("d", eigth, g_g)
    play_note("c", eigth)
    play_note("b", quarter, g_gbd)
    play_note("c", eigth, g_g)
    play_note("d", eigth)
    play_note("e", quarter, g_gef)
    play_note("e", eigth, g_a)
    play_note("f", eigth)
    play_note("e", eigth, g_g)
    play_note("a", eigth)
    play_note("c", eigth)
    play_note("e", eigth)
    play_note("f", eigth, g_g)
    play_note("a", eigth)
    play_note("d", eigth)
    play_note("f", eigth)
    play_note("e", quarter, g_gef)
    play_note("c", eigth, g_g)
    play_note("e", eigth)
    play_note("d", eigth, g_g)
    play_note("c", eigth)
    play_note("c", eigth, g_g)
    play_note("b", eigth)
    play_note("b", eigth, g_g)
    play_note("f", eigth)
    play_note("e", eigth, g_g)
    play_note("b", eigth)
    play_note("c", quarter, g_gcd)
    play_note("a", quarter, g_e)
    play_note("a", quarter, g_birl) 

def play_file(filename):
    file = open(filename, "r")
    for line in file:
        parts = line.split()
        if parts.length() > 0:
            for part in parts:
                if part.length() > 0: decode_bww(part)


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
    song_itchy_fingers(.200)
#    play_file("itchy_fingers_stripped.bww")

except (KeyboardInterrupt, SystemExit):
    # close the handler and quit midi
    del midiOutput
    pygame.midi.quit()

# close the handler and quit midi
del midiOutput
pygame.midi.quit()
