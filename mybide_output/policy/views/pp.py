from policy.views.image_data import image
import boto3
def s3_image_path():
    __aws_access_key_id__ = '' # 자신의 ACCESS_KEY로 대체
    __aws_secret_access_key__ = '' # 자신의 SECRET_ACCESS_KEY로 대체

    s3 = boto3.client(
    's3', # 사용할 서비스 이름, ec2이면 'ec2', s3이면 's3', dynamodb이면 'dynamodb'
    aws_access_key_id=__aws_access_key_id__, # 액세스 키
    aws_secret_access_key=__aws_secret_access_key__) # 비밀 엑세스 키

    # 동형암호화..

    paginator = s3.get_paginator('list_objects_v2')

    response_iterator = paginator.paginate(
        Bucket='mybide',
        Prefix='user_image'
    )
    image_names = []
    print(response_iterator)
    for page in response_iterator:
        for content in page['Contents']:
            d = content['Key'].replace('user_image/','')
            image_names.append(d)
            # print(d )
    del image_names[0]
    return image_names
print(type( s3_image_path()))
