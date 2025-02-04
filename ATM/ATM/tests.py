from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.http import HttpResponse
from .models import Card 

class TemplatesTests(TestCase):

    # GET 요청 테스트
    def test_get_request(self):       # main.html 템플릿 사용 여부 확인
        response = self.client.get(reverse('index')) 
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'main.html')  
        print('main 화면 띄우기')
    
    def test_get_pinrequest(self):       # pin.html 템플릿 사용 여부 확인
        response = self.client.get(reverse('pincheck')) 
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'pin.html')  
        print('pin 입력 화면 띄우기')
    
    def test_get_accountrequest(self):       # pin.html 템플릿 사용 여부 확인
        response = self.client.get(reverse('selectAccount')) 
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'account.html')  
        print('account 입력 화면 띄우기')

class cardCheckTestCase(TestCase):
    def setUp(self):
        self.card_number = "1000100010001000"
        self.pin_number = "1234"
        self.card = Card.objects.create(card_num=self.card_number,pin=self.pin_number)  # 카드 데이터 추가
        self.client = APIClient()

    def test_card_exists(self):
        # card_num이 존재하는 경우 테스트
        url = reverse('cardCheck') 
        data = {'card_num': self.card_number}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        print("카드 유효성 성공")
    

    def test_card_not_exists(self):
        url = reverse('cardCheck') 
        data = {'card_num': '1234567890123456'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 404)
        print("카드 유효성 실패")

    def test_PIN_is_right(self):
        self.client.session['card_num'] = self.card_number
        self.client.session.save()  # 세션을 저장

        url = reverse('pincheck') 
        data = {'pin': self.pin_number}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        print("pin 일치")

    def test_PIN_is_wrong(self):
        self.client.session['card_num'] = self.card_number
        self.client.session.save()  # 세션을 저장

        url = reverse('pincheck') 
        data = {'pin': '0000'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)
        print("pin 불일치")
    
    
    # def test_cardrequest(self):       # 
    #     response = self.client.get(reverse('pin')) 
    #     self.assertEqual(response.status_code, 200)  
    #     self.assertTemplateUsed(response, 'pin.html')


