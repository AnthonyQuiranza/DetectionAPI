from django import views
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Test_img
from .models import Result_img
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
class TestView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #MÉTODO GET
    def get(self,request):
        test= list(Test_img.objects.values())
        if len(test)>0:
            datos={'message':'success','test':test}
        else:
            datos={'message':'Images not found...'}
        return JsonResponse(datos)

    #MÉTODO POST
    def post(self,request):
        jd= json.loads(request.body)
        Test_img.objects.create(url=jd['url'])
        datos={'message':'success'}
        return JsonResponse(datos)

    #MÉTODO PUT
    def put(self,request):
        pass

    #MÉTODO DELETE
    def delete(self,request):
        pass

class ResultView(View):
    def get(self,request):
        result= list(Result_img.objects.values())
        if len(result)>0:
            datos={'message':'success','result':result}
        else:
            datos={'message':'Images not found...'}
        return JsonResponse(datos)
    def pos(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass

