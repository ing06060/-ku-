from django import forms

class SearchForm(forms.Form):
    number = forms.IntegerField(label='수강인원 현황 조회')