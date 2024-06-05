from django.views.generic import TemplateView
from django.shortcuts import render
#以下設定
from itertools import chain     #便利なやつ
import numpy as np              #数値計算ライブラリ
import pandas as pd             #データ解析ライブラリ
import django as dj             #フレームワーク
import matplotlib.pyplot as plt #グラフを作れる
import japanize_matplotlib      #日本語対応
import seaborn as sns           #データ可視化ライブラリ。上と同じくグラフ

from PIL import Image           #画像処理ライブラリ
import base64                   #64種類の文字でエンコード・デコード
from io import BytesIO          #バイト列で読込が出来る。要は(pythonにしては)早い

import copy                     #コピーできる(ディープコピー)

from PIL import Image           #画像処理ライブラリ

import copy                     #コピーできる(ディープコピー)

from . import graph

# Create your views here.

#demo_data = pd.read_csv('C:/Users/owner/python-2023/testproject/static/csv/year_date.csv')
#day_data = pd.read_csv('/data/日/day_date.csv')

def index_template(request):

    return render(request, 'index.html')

#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

#グラフをプロットするための関数
def Plot_Graph(x,y,x_label,y_label):
	plt.switch_backend("AGG")        #スクリプトを出力させない
	plt.figure(figsize=(10,5))       #グラフサイズ
	plt.bar(x,y)                     #グラフ作成
	plt.title("気象データ")    #グラフタイトル
	plt.xlabel("年月日")               #xラベル
	plt.ylabel("気温(℃)")             #yラベル
	plt.tight_layout()               #レイアウト
	graph = Output_Graph()           #グラフプロット
	return graph

def graphCreatData(request):
    """
    if '平均気温' in request.POST.get('y_data'):

    elif '最高平均気温' in request.POST.get('y_data'):

    elif '最低平均気温' in request.POST.get('y_data'):

    elif '最高気温' in request.POST.get('y_data')
    
    #グラフオブジェクト
        qs    =   #モデルクラス(ProductAテーブル)読込
        x     = [x.year for x in qs]           #X軸データ
        y     = [y.average for y in qs]        #Y軸データ
        chart = graph.Plot_Graph(x,y)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
    return(context)
    """


