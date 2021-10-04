#_*_ coding:utf-8 _*_

import sys
sys.path.insert(0,'..')

from traceback import format_exc
from utils.root import Root

'''
用于获取某个分类下某一页的书名
'''



class Book(Root):

    def __init__(self,page=1,keyword=None,url=None,local=None,logger=None):
        '''
        category_url like:url='https://www.aastory.club/category.php?p=4&t=xuanhuan'
        '''
        if url is None:
            url = u'https://www.aastory.club/category.php?p=%d&t=%s'%(page,keyword)
        else:
            url = url

        super(Book,self).__init__(url=url,local=local,logger=logger)


    def get_link(self,):
        ##获取书名及其url

        tags=self.root.findall('.//td[@class="shuming"]//a')

        for tag in tags:

            title=tag.text
            href=tag.get('href')
            '''
            book_url like:url=https://www.aavbook.fun/book-2141.html
            '''

            if 'html' in href:
                book_id = int(href.rsplit('-',1)[-1].rsplit('.',1)[0])
            else:
                book_id = url.rsplit('=',1)[-1]
            
            message=u'from category_url=%s,get title=%s,url=%s'%(self.url,title,href)
            self.logger.info(message)

            yield dict(title=title,book_id=book_id)

    
    def get_summary(self,book_id=2578):

        ## 获取book相关信息，比如是否完结，月点击率，简介等信息(暂时先不抓取)
        

        self.book_id=book_id
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
        return dict(is_finish=xingzhi,)

        ##xingzhi=1，表示已完结；xingzhi=0，表示连载；-1表示其他未知状态        

      

    def get_next(self):
        ##获取下一页url

        tags=self.root.findall('.//div[@id="page"]//a')
        href=None
        for tag in tags:
            text=tag.text
            if text ==u'下一页':
                href=tag.get('href')
                break

        if href:
            url=u'%s%s'%(self.host,href)
            message=u'from catrgory_url= %s get next page url =%s'%(self.url,url)
            self.logger.info(message)
            return url

        else:
            message=u'cant get next page from url= %s'%(self.url,)
            self.logger.info(message)
            return None




def test():

    url='https://www.aastory.club/category.php?t=xuanhuan'
    url='https://www.aastory.club/category.php?t=gudian'
    url='https://www.aastory.club/category.php?p=1&t=dushi'
    link=Book(url=url)
    links=link.get_link()
    import json
    for item in links:
        print json.dumps(item,ensure_ascii=False)
    next_url=link.get_next()
    
    link.get_summary()


if __name__ =='__main__':

    test()