import unittest
import crawler

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_crawler_init(self):
        c = crawler.Crawler("test_url", 2)
        self.assertEqual(c.root_url, "test_url")
        self.assertEqual(c.depth, 2)

    def test_url_init(self):
        u = crawler.Url("url_string","parent")
        self.assertEqual(u.url, "url_string")
        self.assertEqual(u.parent, "parent")

    def test_url_get_full_url(self):
        u = crawler.Url("https://github.com/muralisc/dotfiles", None)
        self.assertEqual(u.get_full_url(), "https://github.com/muralisc/dotfiles")
        u = crawler.Url("/muralisc/dotfiles","https://github.com")
        self.assertEqual(u.get_full_url(), "https://github.com/muralisc/dotfiles")
        u = crawler.Url("/muralisc/dotfiles", None)
        self.assertEqual(u.get_full_url(), "/muralisc/dotfiles")


if __name__ == '__main__':
    unittest.main()
