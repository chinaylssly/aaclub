#_*_ coding:utf-8 _*_

import sys
sys.path.insert(0,'..')
from utils.mysql import MySQL



class Table_Summary(MySQL):

    def __init__(self,logger=None):
        super(Table_Summary,self).__init__(logger=logger)

    def create_table_category(self,):
        ##创建table category

        query='''create table if not exists %s.category(
                category varchar(20) not null primary key,
                url varchar(100),
                book_count int not null default '0',
                create_time timestamp default current_timestamp
                )default charset utf8'''%(self.db)

        self.execute(query=query)




def test():

    table_category=Table_Category()
    table_category.create_table_category_n()
    table_category.test_insert()


   


if __name__=='__main__':

    test()

    pass




