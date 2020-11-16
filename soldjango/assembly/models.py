from django.db import models

# Create your models here.
#국회의원 Name이라는 속성 한 개를 DB에 저장을 할 것입니다.

class Member(models.Model):  #Model 대문자는 클래스 이름이구나 ^.^
    name = models.CharField(max_length=20) #Char 쓴 이유는 NAME은 글자니깐 ^ㅅ^
    
    def __str__(self):
        return self.name
