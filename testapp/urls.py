from django.urls import path
from . import views

app_name='testapp'
urlpatterns=[
    path('',views.index_template,name='index_template'),
    path('change',views.change_graph,name='change_graph'),
]