from django.contrib import admin
from .models import Member #Member 클래스를 .models에 등록을 한다.
# Register your models here.
admin.site.register(Member) #Member을 admin에 등록한다.
