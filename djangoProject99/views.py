from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = '<h1>Превед медвед!</h1>'
    text = "Тестовый текст"
    return render(request, './index.html', {
        'a':a,
        'text':text
    })