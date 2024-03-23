import json
import logging
import os

import requests
from django.http import JsonResponse

from wxcloudrun.models import AuthUser

logger = logging.getLogger('log')

wx_api_backend = os.environ["WX_API_BACKEND"]
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

def decode_request_data(request):
    return request.body.decode('utf-8')

def get_auth(request):
    """
    获取用户权限

     `` request `` 请求对象
    """
    try:
        body = json.loads(decode_request_data(request))
    except Exception as e:
        logger.error("解析请求body失败")
        return JsonResponse({'code': 0, 'data': '解析请求body失败'})
    if 'code' not in body:
        return JsonResponse({'code': 0, 'data': '无token'})
    code = body['code']
    res = requests.get(f'{wx_api_backend}/sns/jscode2session?appid={app_id}&'
                       f'secret={app_secret}&js_code={code}&grant_type=authorization_code')
    if res.status_code != 200:
        logger.error(f'获取用户信息失败:{res.text}')
        return JsonResponse({'code': 0, 'data': '用户信息请求失败'})
    open_id = res.json()['open_id']
    if AuthUser.objects.filter(open_id=open_id).exists():
        return JsonResponse({'code': 1, 'data': '请求成功'})
    else:
        return JsonResponse({'code': 0, 'data': '非admin用户'})
