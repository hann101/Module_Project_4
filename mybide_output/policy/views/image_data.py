from pymongo import MongoClient   
from datetime import datetime      
import csv 


def image():
    client = MongoClient('3.212.70.241', 27017)  
    db = client.mybide                    # 'dbsparta'라는 이름의 db를 만듭니다.

    # now = datetime.now()
    # nowDate = now.strftime('%Y-%m-%d')
    # datetime.now().strftime('%)

    list_field = []
    doc=db.images.find_one()
    for i in doc:
        list_field.append(i)



    cursor = db.images.find ({},{'_id':False})

    cursor = list(cursor)
    with open('image_data.csv', 'w', encoding='utf-8-sig') as outfile:   

        fields = list_field
        write = csv.DictWriter(outfile, fieldnames=fields)
        write.writeheader()
        for x in cursor: 
            # print(x)
            write.writerow(x)
image()