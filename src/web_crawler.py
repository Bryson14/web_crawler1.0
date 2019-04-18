from bs4 import BeautifulSoup
from requests import get, exceptions
from urllib.parse import urlparse, urljoin


def crawl(url: str, depth: int, visited: set, keyword=None, max_depth: int=3):
	print('\t' * depth + url)
	visited.add(url)
	sites_visited = 1
	if depth >= max_depth:
		return sites_visited
	else:
		depth += 1
		soup = BeautifulSoup(get(url).text, 'html.parser')
		urls = [stuff['href'] for stuff in soup.find_all('a', href=True)]
		more_correct_urls = url_verify(urls)
		for link in more_correct_urls:
			o = urlparse(link)
			if o[0] == '' or o[1] == '':
				new_link = make_absolute_path(url, link)
			else:
				new_link = link
			if is_a_url(new_link) and new_link not in visited:
				sites_visited += crawl(new_link, depth, visited, max_depth)
		return sites_visited


def make_absolute_path(base, relative):
	parent = urlparse(base)
	child = urlparse(relative)
	new_url = urljoin(parent.scheme, parent.netloc, child.path)
	return new_url


def url_verify(url_list):
	end = False
	i = 0
	while not end:
		if not url_list:
			end = True
		elif str(url_list[i]).startswith('#'):
			url_list.pop(i)
			if i == len(url_list):
				end = True
		elif not isinstance(url_list[i], str):
			url_list.pop(i)
			if i == len(url_list):
				end = True
		elif '.' not in url_list[i] or len(url_list[i]) < 3:
			url_list.pop(i)
			if i == len(url_list):
				end = True
		else:
			if i >= len(url_list) - 1:
				end = True
			else:
				i += 1

	return url_list


def is_a_url(url):
	try:
		get(url)
		return True
	except exceptions.ConnectionError:
		print("*Connection Error: URL can't be connected to")
		return False
	except exceptions.MissingSchema:
		print("*Missing Schema: URL does not exist")
		return False
