from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('chapter1',views.chapter1,name='chapter1'),
]
