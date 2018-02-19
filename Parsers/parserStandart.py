import urllib.request, re
siteURL = "http://"+input("http://")

with urllib.request.urlopen(siteURL) as url:
	html = url.read().decode('cp1251')

template = r"href\s?=\s?['\"]([^'\"]+)"
result = re.findall(template, html)

for href in result:
	print(href)

# with open("file.html",'w') as file:
# 	file.write(html)