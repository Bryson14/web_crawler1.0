import unittest
import web_crawler


class TestWebCrawler(unittest.TestCase):
	def setup(self):
		self.urls_1 = []
		self.urls_2 = ['https://www.yahoo.com/']
		self.urls_3 = ['https://www.yahoo.com/', '#Main']
		self.urls_4 = ['google.com', 1]

	def test_is_a_url(self):
		url1 = 'https://addictinggames.com'
		url2 = 'some_url'
		url3 = ''
		url4 = 'waitbutwhy.com'

		self.assertEqual(web_crawler.is_a_url(url1), True)
		self.assertEqual(web_crawler.is_a_url(url2), False)
		self.assertEqual(web_crawler.is_a_url(url3), False)
		self.assertEqual(web_crawler.is_a_url(url4), True)


if __name__ == '__main__':
	unittest.main()
