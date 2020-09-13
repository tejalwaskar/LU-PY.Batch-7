'''
this is the test file in which we are going to check out the py file with the help of unittest
'''
import unittest
import capitalizeText

class testPrimeNumber(unittest.TestCase):
    def testOne(self):
        result = capitalizeText.capText("tejal waskar")
        self.assertEqual(result,"Tejal Waskar")
    def testSecond(self):
        resul = capitalizeText.capText("this is a test string to test the unittest on a file")
        self.assertEqual(result,"This Is A Test String To Test The Unittest On A File")
if __name__ == "__main__":
    unittest.main()
