from django.urls import path
from . import views

app_name = 'test'
urlpatterns = [
    path('template/', views.index_template, name='index_template'),
    path('graphCreatData/',views.graphCreatData,name='graphCreatData'),
]