__author__ = 'VeryBigMan'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def addbookinfo(divcontent, soup, bookinfo):
    targetdiv = divcontent.find(id=bookinfo.kind)

    divsection = soup.new_tag('div')
    divsection.attrs['class'] = 'section'

    divcolleft = soup.new_tag('div')
    divcolleft.attrs['class'] = 'col'

    h2 = soup.new_tag('h2')
    h2.string = bookinfo.name

    p = soup.new_tag('p')
    p.string = bookinfo.details

    h4 = soup.new_tag('h4')
    h4.string = 'Douban Rating : ' + str(bookinfo.rating)

    divRating = soup.new_tag('div')
    divRating.attrs['class'] = 'rating'
    divRating.attrs['data-average'] = bookinfo.rating * 2
    divRating.attrs['data-id'] = '1'

    divcolright = soup.new_tag('div')
    divcolright.attrs['class'] = 'col'

    blockquote = soup.new_tag('blockquote')

    img = soup.new_tag('img')
    img.attrs['src'] = bookinfo.img

    blockquote.insert(0, img)
    divcolright.insert(0, blockquote)

    divcolleft.insert(0, h2)
    divcolleft.insert(1, p)
    divcolleft.insert(2, h4)
    divcolleft.insert(3, divRating)

    divsection.insert(0, divcolleft)
    divsection.insert(1, divcolright)

    targetdiv.insert_after(divsection)