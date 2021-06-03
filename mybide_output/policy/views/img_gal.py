from policy.views.image_data import image
from flask import Blueprint,request,jsonify
from flask.templating import render_template
from pymongo import MongoClient
# from .app_id import search_image
from .pp import s3_image_path
from .hash_func import hashTag
from flask import Blueprint, url_for, render_template, flash, request, session

# from os import pipe, replace
# from warnings import showwarning
# from werkzeug.utils import redirect
# import os
# import re

bp = Blueprint('img_gallery', __name__, url_prefix='/image')
client = MongoClient('localhost', 27017)

@bp.route('/')
def home():
    return render_template('image_gal/gallery.html')
    
@bp.route('/gallery', methods=['POST'])
def post_articles():
    # 1. 검색 키워드 받기
    global url_receive
    
    url_receive = request.form['url_give'] # fix-it
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


@bp.route('/gallery', methods=['GET'])
def read_articles():
    
    global url_receive # 검색 키워드 

    image_list = [] # 해시태그를 가진 사진들
    hash_tag = [] # 해당하는 사진의 해시태그들
    images_path = [] # 웹에 반환할 이미지

    all_image = s3_image_path() # user_image에 있는 모든 사진 list 가져오기
    #이미지 전체 리스트
    
    if url_receive is not None:
        # image_list = hashTag().search_pic_of_tag(url_receive) # 태그 포함된 이미지가 반환
        user_id = [session.get('user_id')]
        print('회원 아이디',user_id)

        search = url_receive # 검색어
        print(len(image_list))
        # image_list = search_image(user_id,search)
        image_list = ['1.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '2.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg']
        print('검색어에 대한 리스트',image_list)

        print('S# 전체 데이터  \n\n',all_image)
        print('image타입',type(image_list))

    
    else:
        pass
    # 검색어 받음(str)

    for image_ in image_list:
        if image_ in all_image:
            images_path.append(image_)
            hash_tag.append(hashTag().show_all_hashtag(image_))

        
    print(images_path)
    print(image_list)
    return jsonify({'result': 'success', 'image_list':images_path,'hash_tag':hash_tag})



