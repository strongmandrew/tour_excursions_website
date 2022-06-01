import unittest
import articles

class Test_test_mail_F(unittest.TestCase):
    def test_A(self):
        incorrect_mails = ["qv9uvqfuv.ru", "@csooqq88).com", "233...@@.ru",
                           "Sorry! I cannot remember", ",,mail.ru",
                           "Great articles, btw", "My name is John", "11.dot-__.com", "alajd-&mail.ru",
                           ".comm.isposableunit@gmail@com.ru", "htt__@_0@mail.com", 
                           "MaryRobins@mail@...gmail.com",
                           "tryF111indMe.ru@mail", "mail.gmail@andrew666", "Rona,ldReagan^mail.com",
                           "TrustMe@_mailru", "jack-cliff2003@mail,,,com"]
        
        for mail in incorrect_mails:
            self.assertFalse(articles.isMailValid(mail))

if __name__ == '__main__':
    unittest.main()
