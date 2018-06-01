from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.renderers import JSONRenderer
from user.models import Users


def is_login(func):

    def check_login(request):

        ticket = request.COOKIES.get('ticket')

        if not ticket:

            return HttpResponseRedirect(reverse('user:login'))

        user = Users.objects.filter(ticket=ticket)

        if not user:

            return HttpResponseRedirect(reverse('user:login'))

        # request.user = user

        return func(request)

    return check_login


# class CustomJsonRenderer(JSONRenderer):
#
#     """
#     返回结果
#     {
#         'data': {result},
#         'code': 200,
#         'msg' : '请求成功'
#     }
#     """
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#
#         if renderer_context:
#
#             if isinstance(data, dict):
#                 code = data.pop('code', 0)
#                 msg = data.pop('msg', '请求成功')
#
#             else:
#                 code = 0
#                 msg = '请求成功'
#             res = {
#                 'code': code,
#                 'msg': msg,
#                 'data': data
#             }
#             return super().render(res, accepted_media_type, renderer_context)
#
#         else:
#             return super().render(data, accepted_media_type, renderer_context)
