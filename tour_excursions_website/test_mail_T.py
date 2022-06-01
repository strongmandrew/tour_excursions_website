import unittest
import articles

class Test_test_mail_T(unittest.TestCase):
    def test_A(self):
        correct_mails = ["hello@mail.com", "byebye@yandex.com", "barbos22@gmail.com", 
                         "aza@mail.ru", "maihf13@gmaiul.com", "treq@aw.ru", "hhgy@rambler.by", "andrewjackson@mail.com",
                        "ivansergeev087@yandex.ru", "erinvlad@ya.ru", 
                         "maximenko@ya.com", "strana@rambler.ua" , "vladimirTd@mail.com", "saintGeorge@mail.ru",
                         "inteeru1717@gmail.by", "wowMaili@gmail.com", "vesti@rambler.dot",
                         "gnuSystems@ya.su", "realiza908@vk.com", "a33mozilla@mail.com"]
        for mail in correct_mails:
            self.assertTrue(articles.isMailValid(mail))

if __name__ == '__main__':
    unittest.main()
