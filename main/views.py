from django.shortcuts import render


def index(request):
    return render(request, 'main/main.html')


def loginmain(request):
    return render(request, 'main/login_main.html')