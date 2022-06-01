import unittest
import articles

class Test_test_url_T(unittest.TestCase):
    def test_A(self):
        correct_urls = ["https://gmail.com", "http://alaska.net", "https://ohio.com",
                        "https://trustFond.de", "https://unite4freedom.by",
                        "https://amazon.com", "https://oregon.net/portland_timbers",
                        "https://masChu.com/livinginboston", "http://maryland.net/tonight_show",
                        "https://texas.com", "https://cali.net",
                        "https://sacramentotoday.com", "http://www.dailymirror.com/where_to_rest_uk",
                        "https://sun.us/rest_in_reace"]

        for url in correct_urls:
            self.assertTrue(articles.isUrlValid(url))
            print("OK")

if __name__ == '__main__':
    unittest.main()
