import itertools
import requests

chars = 'abcdef0123456789'

def all_possible(chars, length):
    yield from itertools.product( *([chars] * length))

for p in all_possible(chars, 3):
    short_hash = 'e' + ''.join(p)
    url = f"https://github.com/lukasew/nothing2see/commit/{short_hash}"
    r = requests.get(url)

    print(f"trying {short_hash}...")

    if r.status_code != 404:
        print(f'Short hash {short_hash} gave status {r.status_code} for URL {r.url}')
        break
