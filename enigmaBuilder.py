class EnigmaBuilder:

    def constructM3 (walzenlage):
        """ Walzenlage: Choice and order of wheels
            input walzenlage is three digits in range 1..8 denoting slow,med,fast rotors in that order.
            (digits 1..8 correspond to enigma rotors I..VIII)"""
        pass
    
    def constructM4 (walzenlage):
        """ walezenlage is four digits in range 1..8 denoting slowest,slow,med,fast rotors in
            that order, followed by a letter in range A..C denoting the reflector type."""
        pass

    def constructM4_1 (walzenlage, ringstellung):
        """ ringstellung is the ring settings for each of the 5 wheels (specified in the same
            order as the wheels are given in the walzenlage).
            Notice that the M4 is just the M4_1 with a ringstellung of 'AAAAA' """
        pass
