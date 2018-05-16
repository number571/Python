from urllib.request import urlopen
from re import findall

def get_link(text):
	pattern = r"href\s*=\s*['\"]([^'\"]+)"
	return findall(pattern, text)

with urlopen("https://www.google.com") as page:
	html = page.read().decode()

[print(x) for x in get_link(html)]
