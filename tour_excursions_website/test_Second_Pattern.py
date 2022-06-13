import unittest
import re
class Test_test_Second_Pattern(unittest.TestCase):
    
    def test_A(self):
        pattern = "^\+7(\s+)?\(?[0-9]{3}\)?(\s+)?[0-9]{3}?(\s+)?[0-9]{2}-?[0-9]{2}$"
        wrongNumbers = ["8998765677","  ","+8 (986) 765 87-42","+7 (987) 765 87-443"]
        for number in wrongNumbers:
            self.assertFalse(re.match(pattern,number))
    def test_B(self):
        pattern = "^\+7(\s+)?\(?[0-9]{3}\)?(\s+)?[0-9]{3}?(\s+)?[0-9]{2}-?[0-9]{2}$"
        rightNumbers = ["+7 (965) 234 34-21", "+798676565-45","+7(877)876 87-76"]
        for number in rightNumbers:
            self.assertTrue(re.match(pattern,number))

if __name__ == '__main__':
    unittest.main()
