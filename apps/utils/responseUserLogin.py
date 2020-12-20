'''
     自定义jwt认证成功返回数据
     :token  返回的jwt
     :user   当前登录的用户信息[对象]
     :request 当前本次客户端提交过来的数据
     :role 角色
     '''
from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None, role=None):

    if user.first_name:
        name = user.first_name
    else:
        name = user.username
    return {
        'code': 200,
        'success': True,
        'msg': "success",
        'status': status.HTTP_200_OK,
        'data': {
            "authenticated": True,
            'id': user.id,
            'name': name,
            'fxId':user.last_name,
            'username': user.username,
            'email': user.email,
            'isStaff':user.is_staff,
            'token': token,
            'gender':user.gender,
            'phone':user.phone
        }

    }
