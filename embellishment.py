class Embellishment(object):
    """
    A class used to represent all embelishments (small notes) capable of being
    played on bagpipes.  Embellishments have the following properties:

    Attributes:
        notes:
        beat: 0-based index which note of the embellishment is on the beat
        before: how many notes in this embellishment come befre the beat
        after: how many notes in this embellishment come after the beat
            NOTE: the beat is considered on the front edge of the beat note
            That means the beat and all note following are considered AFTER
    """


    def __init__(self, notes, beat):
        """Return a Embellishment using the provided notes and alignment"""
        self.notes = notes
        self.beat = beat
        self.num_notes = 0
        for note in notes: self.num_notes += 1
        self.after = self.num_notes - self.beat

    def play(self, play_func, note_length):
        """Play each note in the embellishment using the play_func function and note_length"""
        for note in self.notes:
            play_func(note, note_length)

    def length(self, note_length):
        length = 0
        for note in self.notes:
            length = length + note_length
        return note_length

"""
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
"""
