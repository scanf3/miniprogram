import json
import logging
import os

import requests
from django.http import JsonResponse

logger = logging.getLogger('log')

wx_api_backend = os.environ["WX_API_BACKEND"]
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]


def get_auth(request):
    """
    获取用户权限

     `` request `` 请求对象
    """
    body = json.loads(request.body)
    logging.error(request.body)
    if 'token' not in body:
        return JsonResponse({'code': 0, 'data': '无token'})
    token = body['token']
    res = requests.get(f'{wx_api_backend}/sns/jscode2session?appid={app_id}&'
                       f'secret={app_secret}&js_code={token}&grant_type=authorization_code')
    if res.status_code != 200:
        logger.error(f'获取用户信息失败:{res.text}')
        return JsonResponse({'code': 0, 'data': '用户信息请求失败'})
    logging.error(res)
    return JsonResponse({'code': 1, 'data': '请求成功'})
