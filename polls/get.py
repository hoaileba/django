from bs4 import BeautifulSoup
import urllib.request

url =  'https://www.spoj.com/PTIT/users/lebahoailamson/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
# print(soup)
new_feed = soup.find('table', class_='table table-condensed').find_all('a')
prob = [new_feed]
print(len(new_feed))
# text = new_feed.get('text')
# print(len(new_feed))
# for p in len:
#     print(p,end='\n')
# print(text)
# title = new_feed.get('title')
num_prob = 0
for p in new_feed:
    link = p.get('href')
    str = p.string
    if not str:
        continue
    num_prob+=1;    
    print('Link: {}'.format( str))
print(num_prob)


