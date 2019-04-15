from bs4 import BeautifulSoup
import requests
import sys


def crawl(url: str, depth: int, visited: list, max_depth: int=3):
	if depth >= max_depth:
		pass
	elif url in visited:
		pass
	else:
		depth += 1
		visited.append(url)
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		html_lines = soup.prettify().split()
		urls_to_test = [line for line in html_lines if 'href' in line]
		url_snatcher(url, urls_to_test)
		scanned = False
		while not scanned:
			pass


def url_snatcher(base_url, url_list):
	if '//' in base_url:  # https stuff still there
		base = (base_url.split('//'))[1].split('/')[0] + ((base_url.split('//'))[0])  # gets https and root up to .com/


def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print('USAGE: python3.6 web_crawler.py ABSOLUTE_URL [MAX_SEARCH_DEPTH]')
		sys.exit(1)

	elif len(sys.argv) == 2:
		crawl(sys.argv[1], 0, [])

	elif len(sys.argv) == 3:
		crawl(sys.argv[1], 0, [], int(sys.argv[2]))

	else:
		pass


if __name__ == '__main__':
	main()
