from django import forms

class SearchForm(forms.Form):
    number = forms.IntegerField(label='강의번호')