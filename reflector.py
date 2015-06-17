from rotor import Rotor
import string

WIRING_REFLECTOR = ['EJMZALYXVBWFCRQUONTSPIKHGD', 
                    'YRUHQSLDPXNGOKMIEBFZCWVJAT'
                    'FVPJIAOYEDRZXWGCTKUQSBNMHL']


class Reflector(Rotor):

    def setWiring(self,reflectorName):
        """ sets the reflector wiring"""
        
        self.wiring = WIRING_REFLECTOR[reflectorName]
    
    def reflect(self,position):
        """reflects back the position sent in"""
        
        #get the reflector alphabet
        alphabet = self.innerContacts[position]
        #get the position of the the reflector alphabet on normal ABCD
        alphabetPosition = string.ascii_uppercase.index(alphabet)
        #get the reflected alphabet
        reflectedAlphabet = self.wiring[position]
        #return the position of reflected alphabet
        return self.innerContacts.index(reflectedAlphabet)
        
