from django.db import models

# Create your models here.
class Card(models.Model):
    card_num=models.TextField()    # 카드 번호
    pin=models.TextField()   # Pin 번호
    S_account=models.TextField()   # savings 계좌 번호
    S_balance=models.TextField()   # 남은 잔액
    D_account=models.TextField()   # deposit 계좌 번호
    D_balance=models.TextField()   # 남은 잔액
