#_*_ coding:utf-8 _*_

import sys
sys.path.insert(0,'..')

from utils.mysql import MySQL
from utils.tools import jprint
from utils.log import Log
from sql.table import Table


def move_book():

    log = Log(name=u'move')
    logger = log.Logger
    table_book = Table(logger=logger)

    query = u'select * from aabook.book '
    result = table.execute(query)
    data_tuple = result.get('data')
    for data in data_tuple:
        book_id = data.get('id')
        book = data.get('book')
        category = data.get('category')
        d_count = data.get('d_count')
        total = data.get('total')
        rate =data.get('rate')
        is_finish =data.get('is_finish')
        insert_time = data.get('create_time')

        table.insert_db_aaclub_book(book_id,book,category,d_count,total,rate,is_finish,str(insert_time))
    table.close()


def move_category():

    log = Log(name=u'move')
    logger = log.Logger
    table = Table(logger=logger)

    query = u'select * from aabook.category '
    result = table.execute(query)
    data_tuple = result.get('data')
    for data in data_tuple:
     
        category = data.get('category')
        url = data.get('url')
        keyword = url.rsplit('=',1)[-1]
        book_count = data.get('book_count')
        insert_time = data.get('create_time')
        insert_time = str(insert_time)
        table.insert_db_aaclub_category(category,keyword,book_count,insert_time,)
        
    table.close()


def move_item():

    log = Log(name=u'move')
    logger = log.Logger
    table = Table(logger=logger)

    query = u'select * from aabook.item '
    result = table.execute(query)
    data_tuple = result.get('data')  
    for data in data_tuple:
        item_id = data.get('id')
        item    = data.get('item')
        book    = data.get('book')
        category = data.get('category')
        book_id     = data.get('book_id')
        is_download = data.get('is_download')
        is_finish = data.get('is_finish')
        insert_time = str(data.get('create_time'))
        table.insert_db_aaclub_item(item_id,item,book,category,book_id,is_download,is_finish,insert_time)


def test():
    
    # move_book()
    # move_category()
    move_item()


    pass


if __name__ == '__main__':

    test()
    pass