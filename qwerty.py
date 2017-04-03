import logging
import re
import requests
from bs4 import BeautifulSoup
import os.path
import HTMLParser
from base64 import b16decode
def download(url):
    assert url.startswith('http://www.google.com')
    a=requests.get("http://ww.google.com")
    if a.status_code!= 200:
        raise Exception ("status code problem")
def parsingtext(html):
    b=BeautifulSoup(html)
    return b.select('div-usertext-body')[1].text


def linker():
    for link in BeautifulSoup.find_all('q'):
        print(link.get('href'))

class  crawler(object):
    def __init__(starturl):
        self.starturl=starturl

    def crawl(self):
        logging.debug('starting to get info from page{}'.format(
            self.starturl))

        currentpage=self.starturl
        bs=BeautifulSoup(currentpage)
        allpostlink=bs.findAll('div',attrs={'class','makers'});
        postlinkz=[(crawler.makeabsurl(link['href'])for link in allpostlink)]
        for postlink in postlinkz:
            txt=parsingtext(Downloadcontent(postlink))
            stordtxtfilename=os.path.join(self.storagedir,base64.b16encode())
            ##open afile write data to it
            stordtxtfilename=open('newfile','w')
            stordtxtfilename.write(txt)





            nxtpageurl=bs.find('a',attrs={'rel':'next'})['href']
            logging


