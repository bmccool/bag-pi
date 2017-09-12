import pygame
import pygame.midi
from time import sleep

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


def play_note(note, duration=1.000, embelishment=None):
    played = 0
    if embelishment is not None: played = embelishment()
    midiOutput.note_on(note, velocity)
    sleep(duration - played)
    midiOutput.note_off(note, velocity)

def g_grip(note_length=emb_length):
    play_note(ng, note_length)
    play_note(nd, note_length)
    play_note(ng, note_length)
    return note_length * 3

def g_birl(note_length=emb_length):
    play_note(nG, note_length)
    play_note(na, note_length)
    play_note(ng, note_length)
    play_note(na, note_length)
    play_note(ng, note_length)
    return note_length * 5

def g_dThrow(note_length=emb_length):
    play_note(ng, note_length)
    play_note(nd, note_length)
    play_note(nc, note_length)
    return note_length * 3

def g_g(note_length=emb_length):
    play_note(nG, note_length)
    return note_length

def g_gef(note_length=emb_length):
    play_note(nG, note_length)
    play_note(ne, note_length)
    play_note(nf, note_length)
    return note_length * 3

def g_a(note_length=emb_length):
    play_note(na, note_length)
    return note_length

def g_d(note_length=emb_length):
    play_note(nd, note_length)
    return note_length

def g_gbd(note_length=emb_length):
    play_note(nG, note_length)
    play_note(nb, note_length)
    play_note(nd, note_length)
    return note_length * 3

def g_gcd(note_length=emb_length):
    play_note(nG, note_length)
    play_note(nc, note_length)
    play_note(nd, note_length)
    return note_length * 3

def g_e(note_length=emb_length):
    play_note(ne, note_length)
    return note_length

def song_itchy_fingers(eigth=.300):
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
    while (True):
        song_itchy_fingers(.200)
#    play_file("itchy_fingers_stripped.bww")

except (KeyboardInterrupt, SystemExit):
    # close the handler and quit midi
    del midiOutput
    pygame.midi.quit()

# close the handler and quit midi
del midiOutput
pygame.midi.quit()
