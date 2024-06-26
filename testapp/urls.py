from django.urls import path
from . import views

app_name='nccapp'
urlpatterns=[
    path('',views.index_template,name='index_template'),
    path('change_graph/',views.change_graph,name='change_graph'),
]