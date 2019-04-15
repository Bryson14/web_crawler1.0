from bs4 import BeautifulSoup
import requests


def crawl(url: str, depth: int, visited: list, max_depth: int=3):
	if depth >= max_depth:
		pass
	elif url in visited:
		pass
	else:
		depth += 1
		visited.append(url)
		html_data = requests.get(url).text.split('\n')
		urls_to_test = [line for line in html_data if '<a href' in line]
		url_snatcher(url, urls_to_test)
		scanned = False
		while not scanned:
			pass

def url_snatcher(base_url, url_list):
	



def main():
	pass


if __name__ == '__main__':
	main()
