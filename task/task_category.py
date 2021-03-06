#_*_ coding:utf-8 _*_

from category import Category
from sql.table import Table
from utils.log import Log
from utils.tools import putty
import json



def task_category(logger,is_test=False):

    sql_connect = Table(logger=logger)
    sql_connect.create_table_category()
    category = Category(logger=logger)
    category_info = category.get_category()
    for each in category_info:
        category = each.get('category')
        keyword = each.get('keyword')

        category = putty(category)
        if is_test:
            message = json.dumps(dict(category=category,keyword=keyword),ensure_ascii=False)
            logger.debug(message)
        else:
            sql_connect.insert_table_category(category=category,keyword=keyword)

    sql_connect.close()




def test_task_category():

    log = Log(mode='w')
    logger = log.Logger

    task_category(logger=logger,is_test=True)


if __name__ =='__main__':

    test_task_category()