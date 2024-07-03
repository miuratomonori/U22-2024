src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
crossorigin="anonymous"

//月毎の日数
let month_days =[31,28,31,30,31,30,31,31,30,31,30,31];
//フォームの取得
const form = document.forms.checkes;   

var vals = []; // 配列を定義

//↓平均が選択された場合、平均以外と日単位の期間を選択できなくする

//各radiobuttonのドキュメント
let average = document.getElementById("average");
let max_average = document.getElementById("max_average");
let min_average = document.getElementById("min_average");
let max = document.getElementById("max");
let min = document.getElementById("min");
let averages = document.getElementById('averages');
let day_date = document.getElementById('day_date');

document.getElementById('log').onclick=function(){
    console.log(x_date_top);
}

//プルダウンメニュー
const selectBox1 = document.getElementById('topyearSelect');
const selectBox2 = document.getElementById('endyearSelect');
const selectBox3 = document.getElementById('topmonthSelect');
const selectBox4 = document.getElementById('endmonthSelect');
const startYear = 1946;
const endYear = 2022;
const startMonth = 1;
const endMonth = 12;

//初めの年のプルダウンメニュー
for(let year = startYear; year <= endYear; year++){
    const option1 = document.createElement('option');
    option1.value = year;
    option1.textContent = year;
    selectBox1.appendChild(option1);

//終わりの年のプルダウンメニュー
    const option2 = document.createElement('option');
    option2.value = year;
    option2.textContent = year;
    selectBox2.appendChild(option2);
}

//初めの月のプルダウンメニュー
for(let month = startMonth; month <= endMonth; month++){
    const option1 = document.createElement('option');
    option1.value = month;
    option1.textContent = month;
    selectBox3.appendChild(option1);

//終わりの月のプルダウンメニュー
    const option2 = document.createElement('option');
    option2.value = month;
    option2.textContent = month;
    selectBox4.appendChild(option2);
}