from web_crawler import crawl, is_a_url
import sys
import time


def main():
	USAGE = 'USAGE: python3.6 crawler.py ABSOLUTE_URL [-f | <KEYWORD>][MAX_SEARCH_DEPTH]'

	if len(sys.argv) < 2 or len(sys.argv) > 5:
		print(f'\tError: Incorrect program call\n\t{USAGE}')
		sys.exit(1)

	elif len(sys.argv) == 2:
		if is_a_url(sys.argv[1]):
			print(f"Crawling from {sys.argv[1]} to a maximum distance of 3 links")
			start = time.time()
			sites_found = crawl(sys.argv[1], 0, {sys.argv[1]})
			print(f"{sites_found} sites visited in {time.time() - start:.3f} seconds.")
			sys.exit(1)
		else:
			print(f"\tPlease supply a valid URL to this program\n\t{USAGE}")
			sys.exit(1)

	elif len(sys.argv) == 3:
		try:
			if is_a_url(sys.argv[1]) and isinstance(int(sys.argv[2]), int):
				print(f"Crawling from {sys.argv[1]} to a maximum distance of {sys.argv[2]}")
				start = time.time()
				sites_found = crawl(sys.argv[1], 0, {sys.argv[1]}, None, int(sys.argv[2]))
				print(f"{sites_found} sites visited in {time.time() - start:.3f} seconds.")
				sys.exit(1)
			else:
				print(f"\tPlease supply a valid URL and keyword to this program\n\t{USAGE}")
				sys.exit(1)
		except ValueError:
			print(f"\tMax_depth_search must be an integer\n\t{USAGE}")
			sys.exit(1)

	elif len(sys.argv) == 4:
		if sys.argv[2] == '-f':
			if is_a_url(sys.argv[1]):
				print(f"Crawling from {sys.argv[1]} to a maximum distance of 3 links\nSearching for {sys.argv[3]}")
				start = time.time()
				sites_found = crawl(sys.argv[1], 0, {sys.argv[1]}, sys.argv[3])
				print(f"{sites_found} sites visited in {time.time() - start:.3f} seconds.")
				sys.exit(1)
			else:
				print(f"\tPlease supply a valid URL and keyword to this program\n\t{USAGE}")
				sys.exit(1)
		else:
			print(f'\tunknown command {sys.argv[2]}\n\t{USAGE}')

	elif len(sys.argv) == 5:
		try:
			if sys.argv[2] == '-f':
				if is_a_url(sys.argv[1]) and isinstance(int(sys.argv[4]), int):
					print(f"Crawling from {sys.argv[1]} to a maximum distance of {sys.argv[4]} links\nSearching for {sys.argv[3]}")
					start = time.time()
					sites_found = crawl(sys.argv[1], 0, {sys.argv[1]}, sys.argv[3], int(sys.argv[4]))
					print(f"{sites_found} sites visited in {time.time() - start:.3f} seconds.")
					sys.exit(1)
				else:
					print(f"\tPlease supply a valid URL to this program\n\t{USAGE}")
					sys.exit(1)
			else:
				print(f'\tunknown command {sys.argv[2]}\n\t{USAGE}')
		except ValueError:
			print(f"\tMax_depth_search must be an integer\n\t{USAGE}")
			sys.exit(1)
	else:
		print(USAGE)


if __name__ == '__main__':
	main()
