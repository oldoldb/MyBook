__author__ = 'VeryBigMan'
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
from bs4 import BeautifulSoup


class BookInfo:
    def __init__(self):
        self.kind = ""
        self.name = ""
        self.details = ""
        self.rating = 0
        self.img = ""

    def initialConnection(self):
        targetName = self.name.replace(' ', '+')
        initialUrl = 'http://book.douban.com/subject_search?search_text=' + targetName + '&cat=1001'

        initialR = urllib2.urlopen(initialUrl)
        initialSoup = BeautifulSoup(initialR)
        targetA = initialSoup.find(attrs={'title': self.name})
        targetUrl = targetA.attrs['href']
        targetR = urllib2.urlopen(targetUrl)
        targetSoup = BeautifulSoup(targetR)
        targetStrong = targetSoup.find(attrs={'class': 'll rating_num '})
        targetRating = float(targetStrong.get_text())
        self.rating = targetRating
        targetDiv = targetSoup.find_all(attrs={'class': 'intro'})
        targetDivSingle = targetDiv[0]
        tempStr = targetDivSingle.get_text()
        if "展开全部" in tempStr:
            targetDivSingle = targetDiv[1]
        targetIntro = targetDivSingle.get_text()
        self.details = targetIntro


        targetName = self.name.replace(' ', '%20')
        initialUrl = 'http://search.jd.com/Search?keyword=' + targetName + '&enc=utf-8'
        initialR = urllib2.urlopen(initialUrl)
        initialSoup = BeautifulSoup(initialR)
        targetDiv = initialSoup.find(attrs={'class': 'p-name'})
        targetUrl = targetDiv.a.attrs['href']
        targetR = urllib2.urlopen(targetUrl)
        targetSoup = BeautifulSoup(targetR)
        targetStrong = targetSoup.find(id='spec-n1')
        targetImg = targetStrong.img
        targetSrc = targetImg['src']
        path = 'bookimg/' + self.name + '.jpg'

        img = urllib2.urlopen(targetSrc).read()
        fout = file('cgi-bin/' + path, 'wb')
        fout.write(img)
        fout.close()
        self.img = path




