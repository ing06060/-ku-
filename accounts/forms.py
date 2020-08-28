from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, AuthenticationForm)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    re_password = forms.CharField(label='re_password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'major', 'grade', 'email', 'nickname']

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

        return cd['re_password']
"""
class ProfileCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('first_name', 'last_name', 'username', 'email', 'nickname', 'major', 'grade')

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
"""

"""
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'major', 'major_one', 'major_two', 'grade']
"""