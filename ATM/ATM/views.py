from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Card
from rest_framework.response import Response
import time

class InsertCard(APIView):
    def get(self,request):
        return render(request,"main.html")

class cardCheck(APIView):
    def post(self, request):
        card = request.data.get('card_num',None)
        if Card.objects.filter(card_num=card).exists():  # 카드가 DB에 있는지 확인
            request.session['card_num']=card  # 카드 정보 세션에 저장
            return Response(status=200)
        return Response(status=404)


class PINcheck(APIView):
    def get(self,request):
        return render(request,"pin.html")
    
    def post(self, request):
        card = '1000100010001000'     #!수정 필요!#
        pin = request.data.get('pin',None)
        request.session['pin']=pin  # 세션 저장
        user=Card.objects.filter(card_num=card).first()

        if user is None:
            return Response(status=400,data=dict(message="system error"))
        
        if user.pin==pin:
            return Response(status=200)
        else:
            return Response(status=401,data=dict(message="pin is wrong"))
        
class selectAccount(APIView):
    def get(self,request):
        return render(request,"account.html")
    

    
    # def checkpin(request):
    #     pin=Card.objects.filter(card_number='').values_list('pin', flat=True).first()

