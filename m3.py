# Created by Kush Goyal
# For COMP2911 design task 6
# resources for enigma machine description:
# http://users.telenet.be/d.rijmenants/en/enigmatech.htm
# http://www.ellsbury.com/enigma2.htm


from rotor import Rotor
from reflector import Reflector
from enigmaMachine import EnigmaMachine
import string
import copy


class M3(EnigmaMachine):
    
    def __init__(self,setting):
        
        self.rotorLeft = Rotor(int(setting[0])-1,1,'A') 
        self.rotorMiddle = Rotor(int(setting[1])-1,1,'A')
        self.rotorRight = Rotor(int(setting[2])-1,1,'A')        
        self.reflector = Reflector(int(setting[3]),1,'A')
    
    def numberOfSettableWheels(self):
        """ returns the number of rotors+reflectors in the machine whose position can be set
            by the operator.  for example for the m3 this will be 3, for the m4 it will be 5.
            this will be the length of the string returned by the set/get indicator methods."""
        return len(self.getCurrentIndicators())
     
    def setIndicators (self,setting):
        """ set the orientation of the rotors (and settable reflectors) to the specified
            characters.  the characters correspond to the rotors (and settable reflector)
            in the same order as the walzenlage string.
            for any valid setting:
            m.getCurrentIndicators(m.setIndicators(setting)).equals(setting)"""
            
        self.rotorLeft.setOrientation(setting[0])
        self.rotorMiddle.setOrientation(setting[1])
        self.rotorRight.setOrientation(setting[2])

    def getCurrentIndicators (self):
        """ refers to the current orientation of the rotors (and settable reflectors)
            ie what are the letters you can currently read thru the windows?
            the output characters should be in the same order as the walzenlage string"""
        indicators = ''
        indicators += self.rotorLeft.getOrientation()
        indicators += self.rotorMiddle.getOrientation()
        indicators += self.rotorRight.getOrientation()
        return indicators
        
    def encipher (self,plaintext):
        ciphertext = ''
        plaintext = plaintext.upper()
        for alphabet in plaintext:
            self.rotateRotors()
            #print(self.getCurrentIndicators())
            #print("Alphabet:",alphabet)
            position = string.ascii_uppercase.index(alphabet)
            position = self.rotorRight.encode(position)
            #print(position)
            position = self.rotorMiddle.encode(position)
            #print(string.ascii_uppercase[position])
            position = self.rotorLeft.encode(position)
            #print(string.ascii_uppercase[position])
            position = self.reflector.reflect(position)
            #print(string.ascii_uppercase[position])
            position = self.rotorLeft.decode(position)
            #print(string.ascii_uppercase[position])
            position = self.rotorMiddle.decode(position)
            #print(string.ascii_uppercase[position])
            position = self.rotorRight.decode(position)
            #print(string.ascii_uppercase[position])
            cipherAlphabet = string.ascii_uppercase[position]
            ciphertext += cipherAlphabet
        return ciphertext

    
    def rotateRotors(self):
        """ rotates the rotors based on conditions"""
        
        if self.rotorRight.getOrientation() == self.rotorRight.getNotch():
            if self.rotorMiddle.getOrientation() == self.rotorMiddle.getNotch():
                self.rotorLeft.rotate()
            self.rotorMiddle.rotate()
        elif self.rotorMiddle.getOrientation() == self.rotorMiddle.getNotch():
            self.rotorMiddle.rotate()
            self.rotorLeft.rotate()
        #elif self.rotorLeft.getOrientation() == self.rotorLeft.getNotch():
            #self.rotorLeft.rotate()
        self.rotorRight.rotate()

def main():


    m3 = M3('1231')
    plaintext = "WHEREEVERYOUGOTHEREYOUAREWHEREEVERYOUGOTHEREYOUAREWHEREEVERYOUGOTHEREYOUAREWHEREEVERYOUGOTHEREYOUAREWHEREEVERYOUGOTHEREYOUAREWHEREEVERYOUGOTHEREYOUARE"
    ciphertext = "KPCURNSYDGLDHCUGTOOMLAQGCDQKHOUMRBNBFXDEKUIKBCJHKVPEGLYXBTKFFATZEYYLTNFQGLDSQXOYKUHSGPLVNJTWCZXXKEFBBZGHPLHKVGIFBPLRSVSQYOIXTNEGPMNPBGVDXYHMUNUUDYYLZX"
    m3.setIndicators('AAA')
    answer = m3.encipher(plaintext)
    if (answer == ciphertext):
        print("you are awesome!!!!")
    else:
        print("error!")
    
    m3 = M3('4511')   
    ciphertext = "BTNJJFJGELCFIPFTLANTCABHGKDFCJWYMPKTFRLWOIQHLBXZCYSBFTIJREAJWHHWQUVLIEVYBANINWFKQYMYRELWPHEYWNSOZCRKIFNDGCNGDQLVTQEWHITLYCNLGCLTJGDLPPWXMTZHNYSLNYMGVOWJQMYEOJAIXYINDUWFGEEIQGXRXKYFMQNLCTQVJEFVGPKUNOXMTMKNJQGGIIKAJZIEHUPVVGZVTNCMSQSWMATLOORQDOXASDTCFBSQDQJPXUCUWTVJEYPNDMGUBBLSRXBINNVOUZZGZRFSCATQWKMCVRBYLEHGVPFXIINZRLMNOWFONLDUGPPQNVNQFTYPIEOCMCXFFQWHNKYTWHFBOFZGQQBYSPNWWSHGULJYFZYBHJAPOQREBQIONTDFFGRWLHHAOLMEJBBZSPXTKDNQYDRFKTGIDVZKPLJZUDELBWQGTURXWJJHCJYXVEMXIQZNAPPDLQKEEBDTGYVBNCNUFKWYFFNETMZLJRBASQTTSTQJTTYQFBLXSGOJXRIXAFCYXMCPBMZQNHHRQTOWIYAMVUGVJGMIGVEWJOTAYXGOLQQCRCQOYCMGZMSSLCLEBMSBIAJKYBLCHCDPYGLPLCKGXTXMKIAKXQWFHYLCGBFGYTQWIKSKOHYHPBJRYBJYAIFGAMGYEMLYOQZONCGXDQSZZIHPQFYXYRTOFOCUVAVEOPXLJUZUXTJUWWDMRDZZAHGTTLNAYCSLVLOFRYYZEDBNPRCIHBYTNVBWYQKJQMEMBJSTLXRDQQFXQBTDMQURKFPYSFQRXIWBZUEALOKHWKCFACIIDVMJVZEZECZYPGNTFZBYMFBEWOPLKKLPZQXGCDIMPMBSVDIUDRRJRBMODKYKHVBOYLMYHOVEMBTVIALAAEFFIAXTHVCMLOFWPVVILTXTAMCSLEBMPDMZMPSPNZVVYFMIXQAPKXRTLVFVUBQULGNJYTXXUWZZOORJQXMMRTSUVJJKYUCKFIXOTOPTQZQQXSYMUBSCHGGELPFZNQSZOYZSLQKWP"
    plaintext = "OURFORMOFGOVERNMENTDOESNOTENTERINTORIVALRYWITHTHEINSTITUTIONSOFOTHERSOURGOVERNMENTDOESNOTCOPYOURNEIGHBORSBUTISANEXAMPLETOTHEMITISTRUETHATWEARECALLEDADEMOCRACYFORTHEADMINISTRATIONISINTHEHANDSOFTHEMANYANDNOTOFTHEFEWBUTWHILETHEREEXISTSEQUALJUSTICETOALLANDALIKEINTHEIRPRIVATEDISPUTESTHECLAIMOFEXCELLENCEISALSORECOGNIZEDANDWHENACITIZENISINANYWAYDISTINGUISHEDHEISPREFERREDTOTHEPUBLICSERVICENOTASAMATTEROFPRIVILEGEBUTASTHEREWARDOFMERITNEITHERISPOVERTYANOBSTACLEBUTAMANMAYBENEFITHISCOUNTRYWHATEVERTHEOBSCURITYOFHISCONDITIONTHEREISNOEXCLUSIVENESSINOURPUBLICLIFEANDINOURPRIVATEBUSINESSWEARENOTSUSPICIOUSOFONEANOTHERNORANGRYWITHOURNEIGHBORIFHEDOESWHATHELIKESWEDONOTPUTONSOURLOOKSATHIMWHICHTHOUGHHARMLESSARENOTPLEASANTWHILEWEARETHUSUNCONSTRAINEDINOURPRIVATEBUSINESSASPIRITOFREVERENCEPERVADESOURPUBLICACTSWEAREPREVENTEDFROMDOINGWRONGBYRESPECTFORTHEAUTHORITIESANDFORTHELAWSHAVINGAPARTICULARREGARDTOTHOSEWHICHAREORDAINEDFORTHEPROTECTIONOFTHEINJUREDASWELLASTHOSEUNWRITTENLAWSWHICHBRINGUPONTHETRANSGRESSOROFTHEMTHEREPROBATIONOFTHEGENERALSENTIMENT"
    m3.setIndicators('IYP')
    answer = m3.encipher(ciphertext)
    #print(answer)
    if (answer == plaintext):
        print("you are awesome!!!!")
    else:
        print("error!")
    

if __name__ == '__main__':
    main()















 
