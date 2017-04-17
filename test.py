import urllib.request
from bs4 import BeautifulSoup

site= 'https://seword.com/2016/08/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def traverseSeword():
  site='https://seword.com/2016'
  for i in range(8,12):
    getListArticle(site + '/'+ str(i) +'/')

#kalo niat return array haruse  
def getListArticle(site):
  j=1
  try:
    while(True):
      if(j > 1):
        newSite= site+"page/"+ str(j)
      else:
        newSite= site
      req = urllib.request.Request(newSite, headers=hdr)
      with urllib.request.urlopen(req) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
      j=j+1
      for article in soup.find_all('article'):
        href = article.find('a', {"class":"image-link"})['href']
        if ("politik" in href):
          print(href)
          content = getDetailedArticleText(href)
  except urllib.error.HTTPError:
    print("nothing to worries")


def getDetailedArticleText(site):
  req = urllib.request.Request(site, headers=hdr)
  with urllib.request.urlopen(req) as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
  content = soup.find('div', {"class": "post-content"})
  text = '';
  for p in content.find_all('p'):
    text += ' ' + p.text
  return text
      
traverseSeword()
