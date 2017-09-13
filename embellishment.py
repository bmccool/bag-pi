class Embellishment(object):
    """
    A class used to represent all embelishments (small notes) capable of being
    played on bagpipes.  Embellishments have the following properties:

    Attributes:
        notes:
        alignment:
    """


    def __init__(self, notes, alignment):
        """Return a Embellishment using the provided notes and alignment"""
        self.notes = notes
        self.alignment = alignment

    def play(self, play_func, note_length):
        """Play each note in the embellishment using the play_func function and note_length"""
        for note in self.notes:
            play_func(note, note_length)

    def length(self, note_length):
        length = 0
        for note in self.notes:
            length = length + note_length
        return note_length
