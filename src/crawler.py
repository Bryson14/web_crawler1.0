from web_crawler import crawl, is_a_url
import sys


def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print('\tError: No URL supplied\n\tUSAGE: python3.6 crawler.py ABSOLUTE_URL [MAX_SEARCH_DEPTH]')
		sys.exit(1)

	elif len(sys.argv) == 2:
		if is_a_url(sys.argv[1]):
			crawl(sys.argv[1], 0, [])
		else:
			sys.exit(1)

	else:
		crawl(sys.argv[1], 0, [], int(sys.argv[2]))


if __name__ == '__main__':
	main()
