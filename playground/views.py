from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def SayHello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', { 'name': 'mason' })