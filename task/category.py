#_*_ coding:utf-8 _*_

import sys
sys.path.insert(0,'..')
from traceback import format_exc
from utils.root import Root

'''
获取网站分类及其url
'''
class Category(Root):

    def __init__(self,url='https://www.aastory.club/category.php',local=None,logger=None):

        Root.__init__(self,url=url,local=local,logger=logger)


    def get_category(self,):

        # print self.html
        
        tags=self.root.findall('.//div[@class="sub_nav_inner"]//a')

        for tag in tags: 

            category=tag.text
            href=tag.get('href')
            keyword = href.rsplit('=',1)[-1]
            message=u'from url=%s get category=%s ,keyword=%s'%(self.url,category,keyword)
            self.logger.info(message)

            yield dict(category=category,keyword=keyword)


            

def test():

    url='https://www.aastory.club/category.php'
    book=Category(url=url)
    category=book.get_category()
    import json
    for item in category:
        print json.dumps(item,ensure_ascii=False)




if __name__=='__main__':

    test()