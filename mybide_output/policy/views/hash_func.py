from os import pipe, replace
from pymongo import MongoClient 
client = MongoClient('3.212.70.241', 27017)
db = client.mybide

import re

class hashTag:
    def show_all_hashtag(self,image_name):
        # 이미지 이름이 input으로 들어오면
        # 해당 이미지 해시태그만 출력
        a = list(db.images.find({"image.image_path":image_name},{"_id":0,"image.image_path":1,"image.tag":1}))
        # print('\na',a)
        a = str(a)
        a = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
        a = a.replace('{','')
        a = a.replace('}','')
        a = a.replace('tag','')
        # print('aa',a,'\n\n')

        a = a.split("image_path")
        b = []

        for i in range(1,len(a)):
            
            if image_name in a[i]:
                b.append(a[i])
                aa = a[i]
                b = aa.split(' ')
                vv = b.count('')
                for p in range(0,vv):
                    b.remove('')

        del b[0]
        b = tuple(b)

        return b

    def search_pic_of_tag(self,keyword):
        # 검색 키워드로 들어온 해시태그가 포함한 이미지 결과물 출력
         
        a = list(db.images.find({},{"_id":0,"image.image_path":1,"image.tag":1})) # all data
        # 전체 목록 가져오기
        # mongodb는 검색이 안됨.. 그러니 파이썬으로..

        a = str(a)
        a = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
        a = a.replace('{','')
        a = a.replace('}','')
        a = a.replace('tag','')

        a = a.split("image_path")

        tag_path = []

        # 태그 검색
        for i in range(1,len(a)):
            
            if keyword in a[i]:
                str_a = str(a[i]) 
                str_a = str_a.split(' ')
                remv = str_a.count('')
                for p in range(0,remv):
                    str_a.remove('')

                if keyword in str_a:
                    tag_path.append(str_a[0])

        return tag_path

