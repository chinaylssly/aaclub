#_*_ coding:utf-8 _*_

import sys
sys.path.insert(0,'..')
from utils.mysql import MySQL



class Table_Category(MySQL):

    def __init__(self,logger=None):
        super(Table_Category,self).__init__(logger=logger)


    def create_table_category(self,):
        '''
        创建表category 书籍分类
        columns --> category   :    书籍所属类名
        columns --> keyword    :    类名关键字   
        columns --> book_count :    分类书籍数
        columns --> insert_time:    入库时间
        columns --> update_time:    更新时间
        '''
        query = u'''create table if not exists %s.category(
                    category varchar(20) not null,
                    keyword varchar(20) not null primary key,
                    book_count int not null default '0',
                    insert_time timestamp default current_timestamp,
                    update_time timestamp default current_timestamp )
                    default charset utf8'''%(self.db)
        self.execute(query)


    def test_insert(self,):
        query = u'insert ignore into category\
                    (category,keyword,book_count,insert_time,update_time) \
                     values \
                    ("category","keyword",default,default,current_timestamp)'
        self.execute(query)


    def check_table_category(self,):
        ##查询category url

        query='select category,keyword from category'
        return self.execute(query=query)



    def insert_table_category(self,category,keyword):
        ##category 插入数据

        query=u'insert ignore into category (category,keyword) values("%s","%s")'%(category,keyword)
        self.execute(query=query)


    def update_table_category_book_count(self,book_count,category):
        ##更新category book_count,同时同步update_time

        query=u'update category set book_count="%s",update_time=current_timestamp where category="%s" '%(book_count,category)
        self.execute(query=query)

    def insert_db_aaclub_category(self,category,keyword,book_count,insert_time='default',update_time=u'default'):


        if insert_time == u'default':
            pass
        else:
            insert_time = u'"%s"'%(insert_time)

        if update_time == u'default':
            pass
        else:
            update_time = u'"%s"'%(update_time)

        query = u'insert ignore into aaclub.category values("%s","%s","%s",%s,%s)'\
                        %(category,keyword,book_count,insert_time,update_time)

        self.execute(query)



def test():

    table_category=Table_Category()
    table_category.create_table_category()
    # table_category.test_insert()


   


if __name__=='__main__':

    test()

    pass




