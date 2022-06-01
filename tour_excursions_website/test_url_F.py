import unittest
import articles

class Test_test_url_F(unittest.TestCase):
    def test_A(self):
        incorrect_urls = ["ftp:/august/mail.com", "ftp//wash/resorts.mail",
                          "ww.makingspospers.com", ".//washingtonpost.com/floridaresorts",
                          "dailymirror//why so many alcoholics", "eugen@mail.com",
                          "httpss:/mail.spb.ru/voyna_v_irake", "http:/gm.es//franko.ru",
                          "htpp://tranding.net//youth_tendecies", "://appolo.uk\trial",
                          "https:\\reaarange.com/make_that", "ftp:?\roosevelt.ua//kogda vse konchitsa"]
        for url in incorrect_urls:
            self.assertFalse(articles.isUrlValid(url))
            print("OK!")


if __name__ == '__main__':
    unittest.main()
