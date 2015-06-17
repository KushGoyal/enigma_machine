from reflector import Reflector
import string

class TestReflector:

    def testReflect(self):
    
        reflector = Reflector(1,1,'A')
        position = reflector.reflect(8)
        reflection = string.ascii_uppercase[position]
        assert(reflection == 'P')
        position = reflector.reflect(string.ascii_uppercase.index('M'))
        reflection = string.ascii_uppercase[position]
        assert(reflection == 'O')
        print('Reflect passed')
        

def main():

    testReflector = TestReflector()
    testReflector.testReflect()
    

if __name__ == '__main__':
    main()
