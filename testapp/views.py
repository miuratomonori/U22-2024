from django.views.generic import TemplateView
from django.shortcuts import render
#莉･荳玖ｨｭ螳�
import pandas as pd             #繝�繝ｼ繧ｿ隗｣譫舌Λ繧､繝悶Λ繝ｪ

from PIL import Image           #逕ｻ蜒丞�ｦ逅�繝ｩ繧､繝悶Λ繝ｪ
from django.contrib.auth.models import User

import copy                     #繧ｳ繝斐�ｼ縺ｧ縺阪ｋ(繝�繧｣繝ｼ繝励さ繝斐�ｼ)

from django.shortcuts import render
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index_template(request):
    df = pd.read_csv('C:\\Users\\user\\Desktop\\testncc\\static\\csv\\year_date.csv')
    plt.figure(figsize=(10,5))
    plt.plot(df['date'],df['average'])
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.grid()


    graph = get_image()
    return render(request, 'index.html',{'graph': graph})

def graph_create(x_top,x_end,y_select,df):

    views_df = df[df["date"] >= int(x_top)] & df[["date"] <= int(x_end)]
    plt.figure(figsize=(10,5))
    plt.plot(views_df["date"],views_df[y_select])

    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.grid()


    graph = get_image()
    return(graph)

def change_graph(request):
    if request.method == 'POST':
        x_top = request.POST['x_top']
        x_end = request.POST['x_end']
        x_option = request.POST['x_option']
        y_select = request.POST['y_select']

        if x_option == "year":
            df = pd.read_csv('C:/Users/user/Downloads/python-2023/python-2023/testproject/static/csv/year_date.csv')
        elif x_option == "month":
            df = pd.read_csv('C:/Users/user/Downloads/python-2023/python-2023/testproject/static/csv/mth_average.csv')
        elif x_option == "day":
            df = pd.read_csv('C:/Users/user/Downloads/python-2023/python-2023/testproject/static/csv/day_average.csv')

        if y_select == "average":
            grath = graph_create(x_top,x_end,y_select,df)
        elif y_select == "max_average":
            grath = graph_create(x_top,x_end,y_select,df)
        elif y_select == "min_average":
            grath = graph_create(x_top,x_end,y_select,df)
        elif y_select == "max":
            grath = graph_create(x_top,x_end,y_select,df)
        elif y_select == "min":
            grath = graph_create(x_top,x_end,y_select,df)
    
    graph = get_image()
    return render(request, 'index.html',{'graph': graph})    

def get_image():
 buffer = io.BytesIO()
 plt.savefig(buffer, format='png')
 image_png = buffer.getvalue()
 graph = base64.b64encode(image_png)
 graph = graph.decode('utf-8')
 buffer.close()
 return graph