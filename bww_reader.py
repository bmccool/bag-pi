bww_dict = {"&": "NewMeasure TrebelClef",
	   "sharpf": "Key Signature F#",
	   "sharpc": "Key Signature C#",
  
           # TIME SIGNATURES
	   "2_4": "Two Four Time",
	   "C_":  "Cut Time",

	   # MEASURE MARKINGS
	   "I!\'\'": "NewPart OpenReapeat",
	   "\'\'!I": "EndPart CloseRepeat",
           "I!": "NewPart",
           "!I": "EndPart",
	   "!": "NewMeasure",
	   "\'1": "Ending 1",
	   "\'22": "Ending 2 of 2",
	   "!t": "End Line",

	   # Embelishments
           # - Grace Notes
	   "gg": "Grace G",
	   "eg": "Grace E",
           # - Single Strike
	   "strla": "Strike Low A",
	   "strlg": "Strike Low G",
           # - Doublings
           # - - Regular Doubling
	   "dbc": "Doubling C",
	   "dbe": "Doubling E",
	   "dbhg": "Doubling High G",
	   "dbha": "Doubling High A",
           # - - Half Doubling
	   "hdbe": "Half Doubling E",
           # Birls
	   "brl": "Birl",
	   "abr": "Birl Low A",
	   "gbr": "Birl Low G",
	   "tbr": "Birl High G",
	   "thrd": "D throw",
	   "lgstd": "lemolougghlin",
	   "dg": "D grace note",
	   "grp": "grip",
	   "hdbf": "Nope",
	   "tar": "taorloughg",
	   "gstb": "!!!!!!1",
	   "gstd": "!!!!!!",
	   "tg": "!",
	   "strhg": "!",
    
           # Notes
	   "LA_4": 	"note a 4"            ,
	   "LAr_16": 	"note a 16 Flag_right",
	   "LAl_16": 	"note a 16 Flag_left" ,
	   "LAr_32": 	"note a 32 Flag_right",
	   "LAl_8": 	"note a 8  Flag_left" ,
	   "LAr_8": 	"note a 8  Flag_right",
	   "B_4": 	"note B 4"            ,
	   "Br_32": 	"note B 32 Flag_right",
	   "Bl_16": 	"note B 16 Flag_left" ,
	   "Bl_32": 	"note B 32 Flag_left" ,
	   "Br_8": 	"note B 8  Flag_right",
	   "Bl_8": 	"note B 8  Flag_left" ,
	   "C_4": 	"note C 4"            , 
	   "Cr_32": 	"note C 32 Flag_right",
	   "Cl_32": 	"note C 32 Flag_left" ,
	   "Cr_16":	"note C 16 Flag_right",
	   "Cl_8": 	"note C 8  Flag_left" ,
	   "Cr_8": 	"note C 8  Flag_right",
	   "Dr_8": 	"note D 8  Flag_right",
	   "Dr_16": 	"note D 16 Flag_right",
	   "Dl_8": 	"note D 8  Flag_left" ,
	   "Dl_32": 	"note D 32 Flag_left" ,
	   "Dl_16": 	"note D 16 Flag_left" ,
	   "D_8": 	"note D 8"            ,
	   "El_8": 	"note E 8  Flag_left" ,
	   "Er_16": 	"note E 16 Flag_right",
	   "El_32": 	"note E 32 Flag_left" ,
	   "Er_8": 	"note E 8  Flag_right",
	   "E_4": 	"note E 4"            ,
	   "E_8": 	"note E 8"            ,
	   "Fr_8": 	"note F 8  Flag_right",
	   "Fr_16": 	"note F 16 Flag_right",
	   "Fl_32": 	"note F 32 Flag_left" ,
	   "Fr_32": 	"note F 32 Flag_right",
	   "Fl_16": 	"note F 16 Flag_left" ,
	   "Fl_8":	"note F 8  Flag_left" ,
	   "HGl_32": 	"note G 32 Flag_left" ,
	   "HGr_8": 	"note G 8  Flag_right",
	   "HGr_32": 	"note G 32 Flag_right",
	   "HA_4": 	"note A 4"            ,
	   "HAr_16": 	"note A 16 Flag_right",
	   "HAr_8":	"note A 8  Flag_right",
	   "HAl_8":	"note A 8  Flag_left" ,
  
           # Dots
	   "\'la": "Dot last low a",
	   "\'f" : "Dot last f",
	   "\'ha": "Dot last High A",
	   "\'e" : "Dot last e",
	   "\'d" : "Dot last d",
	   "\'b" : "Dot last b",
	   "\'c" : "Dot last c",
   

           # END
	   "END": "END"}

class BWWReader():
    """Class provides interface for reading and parsing bww bagpipe player file """

    def __init__(self, bww_file):
        self.file_name = bww_file
        self.elements = []
        self.index = 0
        bww = open(self.file_name)
        
        for line in bww:
            parts = line.split()
            for part in parts:
                self.elements.append(part)
        bww.close()

    def next():
        if self.index < len(self.elements):
            self.index = self.index + 1
            #TODO: Is there a built in type, iterator maybe, that can keep track of this for me?
            return self.elements[self.index - 1]
        else:
            self.index = 0
            return None

    def interpret_file(self):
        for element in self.elements:
            if element in bww_dict:
                print bww_dict[element]
            else:
                print "No element " + element + " in dictionary!"

    def unknown_elements(self):
        unknown_elements = 0
        print "Unknown Elements:"
        for element in self.elements:
            if element not in bww_dict:
                print element
                unknown_elements = unknown_elements + 1
        print str(unknown_elements) + " unknown elements found."
