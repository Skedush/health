from rest_framework.exceptions import AuthenticationFailed
import jwt
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    # 自定义认证类，重写authenticate方法
    def authenticate(self, request):
        # 认证通过，返回user，auth
        # 认证失败，返回None
        # auth = request.META.get('HTTP_AUTHORIZATION')  # 前台用auth携带token
        # 通过前台传过来的请求头中获取auth
        token = get_authorization_header(request)[4:]

        if not token:
            raise AuthenticationFailed('Authorization 字段是必须的')
        try:
            payload = jwt_decode_handler(token)
        # 出现jwt解析异常，直接抛出异常，代表非法用户，也可以返回None，作为游客处理
        except jwt.ExpiredSignature:
            raise AuthenticationFailed('token已过期')
        except:
            raise AuthenticationFailed('token非法')

        user = self.authenticate_credentials(payload)
        return (user, token)
