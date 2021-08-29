from django.urls import path
from .import views

urlpatterns = [
    path('',views.SQ_overview,name='SQ_overview'),
    path('chapter1',views.chapter1,name='chapter1'),
    path('SQ_overview/',views.SQ_overview, name="SQ_overview"),
    path('SQ_Quest/<int:QA_No>',views.SQ_Quest, name="SQ_Quest"),
    path('SQ_Quest1',views.SQ_Quest1, name="SQ_Quest1"),
    path('SQ_Quest2',views.SQ_Quest2, name="SQ_Quest2"),
    # path('SQ_Quest<int:d.QA_No>',views.SQ_Quest2, name="SQ_Quest"),
    # path('SQ_Answer1',views.SQ_Quest1, name="SQ_Answer1"),
]
