#_*_ coding:utf-8 _*_

import sys
sys.path.insert(0,'..')

from traceback import format_exc
from utils.root import Root



'''
用于获取某一本书的全部章节名及其url
'''


class Item(Root):

    def __init__(self,book_id,local=None,logger=None):
        '''
        book summary url like :     https://www.aavbook.fun/book-2578.html
        book item list url like :   https://www.aastory.club/archive.php?id=2578
        '''

        self.book_id=book_id
        url=u'https://www.aastory.club/archive.php?id=%s'%(self.book_id)
        Root.__init__(self,url=url,local=local,logger=logger)


    def get_item(self,):
        ##获取book下章节信息

        tags=self.root.findall('.//div[@class="page_main"]//li/a')
        for tag in tags:
            title=tag.text
            href=tag.get('href')
            item_id = href.rsplit('-',1)[-1].rsplit('.',1)[0]
            message=u'from url=%s get title=%s ,href=%s'%(self.url,title,href)
            self.logger.info(message)
            yield dict(title=title,item_id=int(item_id))

    def get_xingzhi(self,):

        self.book_url=u'https://www.aavbook.fun/book-%s.html'%(self.book_id)
        root=Root(url=self.book_url,logger=self.logger)
        # print root.html
        img=root.root.find('.//img[@class="book_xingzhi"]')
        src=img.get('src')
        message=u'from book_url=%s get src=%s'%(self.book_url,src)
        self.logger.info(message)

        if u'wanjie' in src :

            xingzhi=1

        elif u'lianzai' in src:
            xingzhi=0

        else:
            xingzhi=-1

        message=u'get xingzhi=%s'%xingzhi
        self.logger.info(message)

        return xingzhi

        ##xingzhi=1，表示已完结；xingzhi=0，表示连载；-1表示其他未知状态        


def test():

    url='https://www.aavbook.fun/archive.php?id=3623'
    book=Item(book_id=2858)
    status=book.get_xingzhi()
    info=book.get_item()
    import json 
    for item in info:
        print json.dumps(item,ensure_ascii=False)
        pass



if __name__=='__main__':

    test()