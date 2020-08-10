from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://search.naver.com/search.naver?where=nexearch&amp;query=%EA%B0%90%EA%B8%B0&amp;sm=top_lve.ag20sgrpma0sipenpspm&amp;ie=utf8"')
soup = BeautifulSoup(response, 'html.parser')

i = 1
f = open("새파일.txt", 'w')
for anchor in soup.select("span.keyword"):
    if i == 1:
        i = i+1
    else:
        data = str(i-1)  + "위 : " + anchor.get_text()[1:]+"\n"
        i = i+1
        print(data)
        f.write(data)
f.close()