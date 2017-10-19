import pygame
import pygame.midi
from time import sleep
from embellishment import * 

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

notes = [ng, na, nb, nc, nd, ne, nf, nG, nA]
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
    print "play_note"
    if embellishment is not None: #Play embellishment...
        for emb_note in embellishment.notes:
            midiOutput.note_on(emb_note, velocity)
            print "playing embellishment: " + str(emb_note)
            sleep(emb_length)
            midiOutput.note_off(emb_note, velocity)
            played = played + emb_length
    midiOutput.note_on(note, velocity)
    print "playing note: " + str(note)
    sleep(duration - played)
    midiOutput.note_off(note, velocity) 

def song_itchy_fingers(eigth=.300):
    g_g = Embellishment([nG], 0)
    g_a = Embellishment([na], 0)
    g_d = Embellishment([nd], 0)
    g_e = Embellishment([ne], 0)
    g_gef = Embellishment([nG, ne, nf], 0)    
    g_gbd = Embellishment([nG, nb, nd], 0)
    g_gcd = Embellishment([nG, nc, nd], 0)
    g_dThrow = Embellishment([ng, nd, nc], 0)
    g_birl = Embellishment([nG, na, ng, na, ng], 0)
    g_grip = Embellishment([ng, nd, ng], 0)
    


    quarter = eigth * 2
    play_note(nc, eigth, g_g)
    play_note(nd, eigth)
    play_note(ne, quarter, g_gef)
    play_note(ne, eigth, g_a)
    play_note(nf, eigth)
    play_note(ne, eigth, g_g)
    play_note(na, eigth)
    play_note(nc, eigth)
    play_note(ne, eigth)
    play_note(nf, eigth, g_g)
    play_note(na, eigth)
    play_note(nd, eigth)
    play_note(nf, eigth)
    play_note(ne, quarter, g_gef)
    play_note(nc, eigth, g_g)
    play_note(nd, eigth)
    play_note(ne, quarter, g_gef)
    play_note(ne, eigth, g_a)
    play_note(nf, eigth)
    play_note(ne, eigth, g_g)
    play_note(na, eigth)
    play_note(nc, eigth)
    play_note(ne, eigth)
    play_note(nc, eigth, g_g)
    play_note(na, eigth, g_d)
    play_note(nd, eigth, g_g)
    play_note(nc, eigth)
    play_note(nb, quarter, g_gbd)
    play_note(nc, eigth, g_g)
    play_note(nd, eigth)
    play_note(ne, quarter, g_gef)
    play_note(ne, eigth, g_a)
    play_note(nf, eigth)
    play_note(ne, eigth, g_g)
    play_note(na, eigth)
    play_note(nc, eigth)
    play_note(ne, eigth)
    play_note(nf, eigth, g_g)
    play_note(na, eigth)
    play_note(nd, eigth)
    play_note(nf, eigth)
    play_note(ne, quarter, g_gef)
    play_note(nc, eigth, g_g)
    play_note(ne, eigth)
    play_note(nd, eigth, g_g)
    play_note(nc, eigth)
    play_note(nc, eigth, g_g)
    play_note(nb, eigth)
    play_note(nb, eigth, g_g)
    play_note(nf, eigth)
    play_note(ne, eigth, g_g)
    play_note(nb, eigth)
    play_note(nc, quarter, g_gcd)
    play_note(na, quarter, g_e)
    play_note(na, quarter, g_birl) 

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
