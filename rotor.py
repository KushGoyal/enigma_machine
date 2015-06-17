import string
import copy

NUM_ABCD = 26

R_I = 0
R_II = 1
R_III = 2
R_IV = 3
R_V = 4
R_VI = 5
R_VII = 6
R_VIII = 7

WIRING = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
          'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
          'VZBRGITYUPSDNHLXAWMJQOFECK', 'JPGVOUMFYQBENHZRDKASXLICTW',
          'NZJHGRCXMYSWBOUFAIVLPEKQDT', 'FKQHTLXOCBJSPDZRAMEWNIUYGV']

NOTCHES = ['Q','E','V','J','Z','ZM']

class Rotor:
    """ the rotor class"""
    
    notch = ''
    wiring = ''
    innerContacts = ''
    outerContacts = ''
    ringSetting = 0
    
    def __init__(self,rotorNumber,position,letter):
        """ rotor constructor based on rotor number, ring setting 
            and initial orientation"""
        self.setNotch(rotorNumber)
        self.setWiring(rotorNumber)
        self.setRingSetting(position)
        self.setOrientation(letter)
        
    def setRingSetting(self,position):
        """ sets the ring of the rotor to the desired position"""
        self.ringSetting = position-1
    
    def getRingSetting(self):
        """ returns the ring setting of the rotot"""
        return self.ringSetting
    
    def setOrientation (self,letter):
        """ sets the orientation of the rotor to the desired alphabet"""
        alphabets = string.ascii_uppercase
        alphabets = alphabets[alphabets.index(letter):]+alphabets[:alphabets.index(letter)]
        self.innerContacts = copy.copy(alphabets)
        self.outerContacts = alphabets[-self.getRingSetting():]+alphabets[:-self.getRingSetting()]
    
    def getOrientation(self):
        """ returns the current alphabet on the rotor display"""
        return self.innerContacts[0]
        
    def rotate(self):
        """ rotates the rotor by one unit"""
        self.innerContacts = self.innerContacts[1:]+self.innerContacts[:1]
        self.outerContacts = self.outerContacts[1:]+self.outerContacts[:1]
        
    def setWiring(self,rotorNumber):
        """ sets the wiring of the rotor based on it's number"""
        self.wiring = WIRING[rotorNumber]
        
    
    def encode(self,position):
        """ encodes the letter from the outerCoontacts to innerContacts"""
        
        #get the alphabet on the outer contacts
        outerAlphabet = self.outerContacts[position]
        #print(outerAlphabet)
        #get the position of the outer alphabet in normal ABCD for look up in wiring
        outerAlphabetPosition = string.ascii_uppercase.index(outerAlphabet)
        #print(outerAlphabetPosition)
        #encode the outer alphabet into the new alphabet based on wiring
        encodedAlphabet = self.wiring[outerAlphabetPosition]
        #print(encodedAlphabet)
        #get the position of the encoded alphabet and add the ring setting 
        #for the final position to send to the next rotor
        encodedAlphabetPosition= self.innerContacts.index(encodedAlphabet)+self.getRingSetting()
        #print(encodedAlphabetPosition)
        #return the final position after modding by 26
        return self.modBy26(encodedAlphabetPosition)
        
    def decode(self,position):
        """ decodes the letter from innerContacts to outerContacts"""
        
        #convert the position given relative to ring setting
        position = self.modBy26(position - self.getRingSetting())
        #get the inner alphabet on given position
        innerAlphabet = self.innerContacts[position]
        #get the wiring position of this inner alphabet
        wiringPosition = self.wiring.index(innerAlphabet)
        #decode the position back to outer alphabet based on wiring
        outerAlphabet = string.ascii_uppercase[wiringPosition]
        #get the position of the outer alphabet
        return self.outerContacts.index(outerAlphabet)
        
        
        
    def setNotch(self,rotorNumber):
        """ sets the notch value of the rotor based on it's number"""
        
        if rotorNumber == R_VI or rotorNumber == R_VII or rotorNumber == R_VIII:
            self.notch = NOTCHES[R_VI]
        else:
            self.notch = NOTCHES[rotorNumber]
        
    def getNotch(self):
        """ returns the notch value of the rotor"""
        return self.notch
    
    def modBy26(self,position):
        """ mods the position by 26"""
        return position % NUM_ABCD
        
def main():
    rotor = Rotor(R_I,4,'I')
    print(rotor.getNotch())
    print (rotor.innerContacts)
    print(rotor.outerContacts)
    print(rotor.wiring)
    position = rotor.encode(0)
    position = rotor.encode(0)
    position = rotor.encode(0)


if __name__ == '__main__':
    main()
