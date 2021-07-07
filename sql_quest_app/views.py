import sql_quest_app
from django.shortcuts import render
from django.http import HttpResponse
from .models import std_data

def index(request):
    params={
        'title':'Hello/Index',
    }
    return render(request,'sql_quest_app/index.html',params)

def chapter1(request):
    data=std_data.objects.all()
    params={
        'title':'1章',
        'data':data
    }
    return render(request,'sql_quest_app/chapter1.html',params)
# test


# Create your views here.
