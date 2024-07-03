from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse

import pandas as pd
from datetime import datetime as dt

from PIL import Image
from pathlib import Path          
from django.contrib.auth.models import User
import copy                    

from django.shortcuts import render
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

#最初に呼び出される
def index_template(request):
    
    df = pd.read_csv('C:\\Users\\user\\python-2023\\testproject\\static\\csv\\year_date.csv')
    plt.figure(figsize=(10,5))
    plt.plot(df['date'],df['average'])
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.grid()

    graph = get_image()
    return render(request, 'index.html',{'graph': graph})

#グラフを作成
def graph_create(x_top,x_end,y_select,df):

    views_df = df[(df['date'] >= x_top) & (df['date'] <= x_end)]
    plt.figure(figsize=(10,5))
    plt.plot(views_df["date"],views_df[y_select])

    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.grid()

    graph = get_image()
    return graph

#グラフを変える
def change_graph(request):
    x_option = request.POST['x_option']
    y_select = request.POST['y_select']
    x_top = request.POST['x_top']
    x_end = request.POST['x_end']

    if x_option == "year":
        df = pd.read_csv('C:\\Users\\user\\python-2023\\testproject\\static\\csv\\year_date.csv')
        x_top = int(request.POST['x_top'])
        x_end = int(request.POST['x_end'])
    elif x_option == "month":
        df = pd.read_csv('C:\\Users\\user\\python-2023\\testproject\\static\\csv\\mth_date.csv')
        df['date'] = pd.to_datetime(df['date'].astype(str))
        print(x_top)
    elif x_option == "day":
        df = pd.read_csv('C:\\Users\\user\\python-2023\\testproject\\static\\csv\\day_date.csv')
        df['date'] = pd.to_datetime(df['date'].astype(str))

    
    graph = graph_create(x_top, x_end, y_select, df)
    return JsonResponse({'graph': graph})

#画像にする
def get_image():
 buffer = io.BytesIO()
 plt.savefig(buffer, format='png')
 image_png = buffer.getvalue()
 graph = base64.b64encode(image_png)
 graph = graph.decode('utf-8')
 buffer.close()
 return graph