from lxml import html
import requests

page = requests.get('http://mikebozee.com')
tree = html.fromstring(page.content)

for i in tree:
    print(i)