from rotor import Rotor

class TestRotor:

    def testModBy26(self):
        
        print("Testing mod by 26....")
        rotor = Rotor(1,1,'A')
        number = rotor.modBy26(26)
        assert(number == 0)
        number = rotor.modBy26(-2)
        print(number)
        assert(number == 24)
        print ("modBy26 passed!")
    
    def testSetOrientation(self):
        
        print("Testing set orientation....")
        rotor = Rotor(1,4,'I')
        alphabets1 = 'IJKLMNOPQRSTUVWXYZABCDEFGH'
        alphabets2 = 'FGHIJKLMNOPQRSTUVWXYZABCDE'
        assert(alphabets1 == rotor.innerContacts)
        assert(alphabets2 == rotor.outerContacts)
        rotor = Rotor(0,1,'A')
        rotor.setOrientation('I')
        alphabets1 = 'IJKLMNOPQRSTUVWXYZABCDEFGH'
        alphabets2 = 'IJKLMNOPQRSTUVWXYZABCDEFGH'
        assert(alphabets1 == rotor.innerContacts)
        assert(alphabets2 == rotor.outerContacts)
        print ("set orientation passed!")
    
    def testRotate(self):
        
        print("Testing rotate....")
        rotor = Rotor(1,4,'I')
        alphabets1 = 'KLMNOPQRSTUVWXYZABCDEFGHIJ'
        alphabets2 = 'HIJKLMNOPQRSTUVWXYZABCDEFG'
        rotor.rotate()
        rotor.rotate()
        assert(alphabets1 == rotor.innerContacts)
        assert(alphabets2 == rotor.outerContacts)
        print ("rotate passed!")
        
    def testEncode(self):
    
        print("Testing ecode....")
        rotor = Rotor(2,1,'A')
        rotor.rotate()
        alphabets1 = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
        alphabets2 = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
        position = rotor.encode(0)
        assert(alphabets1 == rotor.innerContacts)
        assert(alphabets2 == rotor.outerContacts)
        assert(position == 2)
        print("Encode passed")
        
    def testDecode(self):
    
        print("Testing decode....")
        rotor = Rotor(2,1,'A')
        rotor.rotate()
        alphabets1 = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
        alphabets2 = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
        position = rotor.decode(4)
        assert(alphabets1 == rotor.innerContacts)
        assert(alphabets2 == rotor.outerContacts)
        assert(position == 1)
        rotor = Rotor(1,1,'A')
        alphabets1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabets2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        position = rotor.decode(18)
        assert(alphabets1 == rotor.innerContacts)
        assert(alphabets2 == rotor.outerContacts)
        assert(position == 4)
        print("Decode passed")
        

def main():

    testRotor = TestRotor()
    testRotor.testModBy26()
    testRotor.testSetOrientation()
    testRotor.testRotate()
    testRotor.testEncode()
    testRotor.testDecode()
    print ("All tests passed!")
    
if __name__ == '__main__':
    main()
