import pymysql
# from pymongo import MongoClient 
# import pandas as pd
# from datetime import datetime

from .image_data import image

from .level1 import main1
from .level2 import main2
from .level3 import main3

conn = pymysql.connect(host='mybide.cutyxjtrt78p.us-east-1.rds.amazonaws.com', user='admin', password='wqend1001', port=3306, db='login', charset='utf8')
cursor = conn.cursor()




def search_image(user_id,search):
# query = 'SELECT lv FROM output_users where id = test'
    query = 'SELECT lv FROM output_users where id = %s'
    cursor.execute(query,user_id)
    conn.commit()

    level = cursor.fetchone()
    print('회원 레벨',level[0])
 

    image()

    if level[0] =='level1':
        return main1(search)
    elif level[0] =='level2':
        return main2(search)
    elif level[0] =='level3':
        return main3(search)

