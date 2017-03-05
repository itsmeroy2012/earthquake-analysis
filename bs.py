import os, sys
bspath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"BeautifulSoup4")
sys.path.append(bspath)
from bs4 import BeautifulSoup
import urllib2,cookielib

site= "http://quakes.globalincidentmap.com/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

try:
    page = BeautifulSoup(urllib2.urlopen(req).read(),'lxml')
except urllib2.HTTPError, e:
    print e.fp.read()

#content = page.read()

l=[]


tableStats=page.findAll('script')



for row in tableStats:
	for col in row:
		
		l.append(col)
filtered= l[4]+'/var'

filtered2=filtered.split('var earthquakes')[1]
filtered3=filtered2.split('/var')[0]
earthquake=filtered3.split(' = ')[1]
earthquake1=earthquake[0:len(earthquake)-2]
print earthquake1




