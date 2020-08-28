from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
"""
class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields']+=('nickname', 'major', 'major_one', 'major_two', 'grade')
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('nickname', 'major', 'major_one', 'major_two', 'grade')}),
    )
"""
admin.site.register(Profile)#, CustomUserAdmin)
# Register your models here.

