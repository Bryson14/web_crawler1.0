import unittest
import web_crawler


class TestWebCrawler(unittest.TestCase):
	def setup(self):
		pass

	def test_url_verify(self):
		urls_1 = ['#', '/about/index.php']
		right_1 = ['/about/index.php']
		urls_2 = ['https://www.yahoo.com', 'http://usu.edu/myusu/']
		right_2 = ['https://www.yahoo.com', 'http://usu.edu/myusu/']
		urls_3 = ['https://www.yahoo.com/', '#Main']
		right_3 = ['https://www.yahoo.com/']
		urls_4 = ['google.com', 1, '/']
		right_4 = ['google.com']
		urls_5 = []
		right_5 = []

		self.assertEqual(web_crawler.url_verify(urls_1), right_1)
		self.assertEqual(web_crawler.url_verify(urls_2), right_2)
		self.assertEqual(web_crawler.url_verify(urls_3), right_3)
		self.assertEqual(web_crawler.url_verify(urls_4), right_4)
		self.assertEqual(web_crawler.url_verify(urls_5), right_5)

	def test_is_a_url(self):
		url1 = 'https://addictinggames.com'
		url2 = 'some_url'
		url3 = ''
		url4 = 'http://www.waitbutwhy.com'

		self.assertEqual(web_crawler.is_a_url(url1), True)
		self.assertEqual(web_crawler.is_a_url(url2), False)
		self.assertEqual(web_crawler.is_a_url(url3), False)
		self.assertEqual(web_crawler.is_a_url(url4), True)


if __name__ == '__main__':
	unittest.main()
