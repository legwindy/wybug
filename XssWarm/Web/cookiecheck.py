
from django.http import HttpResponse

def authcheck(f):
    def wrapper(request,*args,**kwargs):
        cookies = request.get_signed_cookie('logined', salt='hehehe')
        if cookies == 'True':
            return f(request)
        else:
            return HttpResponse('OK')
    return wrapper
