from bs4 import BeautifulSoup
from requests import get, ConnectionError
import sys


def crawl(url: str, depth: int, visited: list, max_depth: int=3):
	if depth >= max_depth:
		pass
	elif url in visited:
		pass
	else:
		depth += 1
		visited.append(url)
		try:
			soup = BeautifulSoup(get(url).text, 'html.parser')
			html_lines = soup.prettify().split()
			urls_to_test = [line for line in html_lines if 'href' in line]
			correct_urls = url_verify(url, urls_to_test)
			print('\t' * depth + url)
			for url in correct_urls:
				print("URL: ", url)
				crawl(url, depth, visited, max_depth)
		except ConnectionError:
			print(f"Unable to reach URL {url}")


def url_verify(base_url, url_list):

	if '//' in base_url:  # https stuff still there
		base_url = (base_url.split('//'))[1].split('/')[0] + ((base_url.split('//'))[0])  # gets https and root up to .com/
	for i in range(len(url_list)):
		if base_url not in url_list[i]:
			url_list[i] = base_url + url_list[i]
	return url_list


def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print('\tUSAGE: python3.6 web_crawler.py ABSOLUTE_URL [MAX_SEARCH_DEPTH]')
		sys.exit(1)

	elif len(sys.argv) == 2:
		crawl(sys.argv[1], 0, [])

	else:
		crawl(sys.argv[1], 0, [], int(sys.argv[2]))


if __name__ == '__main__':
	main()
