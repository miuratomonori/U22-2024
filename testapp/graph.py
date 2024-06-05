#グラフ表示・操作プログラム
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

sns.set()
japanize_matplotlib.japanize()  #日本語フォントの設定

#CSVの読込
#year_data = pd.read_csv('C:\Users\user\python-2023\testproject\testapp\data\年\year_date.csv')
#month_data = pd.read_csv('C:\Users\user\python-2023\testproject\testapp\data\月\mth_date.csv')
#day_data = pd.read_csv('C:\Users\user\python-2023\testproject\testapp\data\日\day_date.csv')


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

