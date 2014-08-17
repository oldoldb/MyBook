__author__ = 'VeryBigMan'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import cgi
import webbrowser
import BookInfo
import os
from global_list import bookinfo
from bs4 import BeautifulSoup
import BookInfoController


print 'Content-Type: text/html\n\n'
form = cgi.FieldStorage()
bookName = form['bookname'].value
bookKind = form['bookkind'].value
bookinfo = BookInfo.BookInfo()
bookinfo.kind = bookKind
bookinfo.name = bookName
bookinfo.initialConnection()

fin = open("cgi-bin/book.html")
data = fin.read()
fin.close()

soup = BeautifulSoup(data)
divContent = soup.find(id='contents')
BookInfoController.addbookinfo(divContent, soup, bookinfo)

fout = file("cgi-bin/book.html", "w")
fout.write(soup.prettify())
fout.close()

path = "file:///" + os.getcwd().replace('\\', '/') + "/cgi-bin/book.html"
webbrowser.open_new_tab(path)
print 'Success'