import unittest
import re
class Test_test_One_Pattern_Mail(unittest.TestCase):
    
    def test_A(self):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-z]{3,6}.[a-z]{2,3}$"
        wrongMails = ["","   s@gmail.com","sseq21","agadga@","adgda@kkkkkkk.com","adghfgjfds@dfgd.ddddddddd"]
        for mail in wrongMails:
            self.assertFalse(re.match(pattern,mail))
    def test_B(self):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-z]{3,6}.[a-z]{2,3}$"
        rightMails = ["9876@gmail.com","andrew@mail.com","a@gmail.com","andy@mail.ru"]
        for mail in rightMails:
            self.assertTrue(re.match(pattern,mail))

if __name__ == '__main__':
    unittest.main()
