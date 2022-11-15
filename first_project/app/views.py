from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import os

# Create your views here.
def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }


    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list_of_directories = os.listdir()
    message = f'Список файлов: {list_of_directories}'
    return HttpResponse(message)