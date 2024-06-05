src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
crossorigin="anonymous"
    const modal = document.getElementById('easyModal');
    const buttonClose = document.getElementsByClassName('modalClose')[0];

    // ボタンがクリックされた時
    function modalOpen() {
        modal.style.display = 'block';
    }

    // バツ印がクリックされた時
    buttonClose.addEventListener('click', modalClose);
        function modalClose() {
            modal.style.display = 'none';
        }

    // モーダルコンテンツ以外がクリックされた時
    addEventListener('click', outsideClose);
        function outsideClose(e) {
            if (e.target == modal) {
                modal.style.display = 'none'
        }
    }
    //月毎の日数
    let month_days =[31,28,31,30,31,30,31,31,30,31,30,31];
    //フォームの取得
    const form = document.forms.checkes;   
    
    var vals = []; // 配列を定義

    //↓平均が選択された場合、平均以外と日単位の期間を選択できなくする

    //各Chekboxのドキュメント
    let average = document.getElementById("average");
    let max_average = document.getElementById("max_average");
    let min_average = document.getElementById("min_average");
    let max = document.getElementById("max");
    let min = document.getElementById("min");
    //平均グループと平均以外のグループ
    let averages = document.getElementById('averages');
    let day_date = document.getElementById('day_date');
    
    //checkboxをクリックしたときに呼ばれる関数
    //例：if->max,minにクラスhiddenを追加、変数valsに値を追加。elseif->max,minのhiddenを削除、変数valsから値を削除
    average.onchange=function(){
        average_if();
        if(average.checked){
            vals.push(average.value);
        }else if(vals.indexOf(average.value) !== -1){
            vals.splice(vals.indexOf(average.value),1);
        }
        arry_clear();
        console.log(vals);
    }
    max_average.onchange=function(){
        average_if();
        if(max_average.checked){
            vals.push(max_average.value);
        }else if(vals.indexOf(max_average.value) !== -1){
            vals.splice(vals.indexOf(max_average.value),1);
        }
        console.log(vals);
        arry_clear();
    }
    min_average.onchange=function(){
        average_if();
        if(min_average.checked){
            vals.push(min_average.value);
        }else if(vals.indexOf(min_average.value) !== -1){
            vals.splice(vals.indexOf(min_average.value),1);
        }
        arry_clear();
        console.log(vals);
    }
    max.onchange=function(){
        day_date_if();
        if(max.checked){
            vals.push(max.value);
        }else if(vals.indexOf(max.value) !== -1){
            //delete vals[vals.indexOf(max.value)];
            vals.splice(vals.indexOf(max.value),1);
        }
        arry_clear();
        console.log(vals);
    } 
    min.onchange=function(){
        day_date_if();
        if(min.checked){
            vals.push(min.value);
        }else if(vals.indexOf(min.value) !== -1){
            vals.splice(vals.indexOf(min.value),1);
        }
        arry_clear();
        console.log(vals);
    }    

    //チェックボックスが押されたら呼び出し
    function average_if(){
        if(average.checked || max_average.checked || min_average.checked){
            max.classList.add('hidden');
            min.classList.add('hidden');
            day_date.classList.add('hidden');
        }
        else if(!average.checked && !max_average.checked && !min_average.checked){
            if(max.classList.contains('hidden')){
                max.classList.remove('hidden');
                day_date.classList.remove('hidden');
            }
            if(min.classList.contains('hidden')){
                min.classList.remove('hidden');
                day_date.classList.remove('hidden');
            }
        }
    }

    function day_date_if(){
        if(max.checked || min.checked){
            average.classList.add('hidden');
            max_average.classList.add('hidden');
            min_average.classList.add('hidden');
            averages.classList.add('hidden');
        }
        else if(!max.checked && !min.checked){
            average.classList.remove('hidden');
            max_average.classList.remove('hidden');
            min_average.classList.remove('hidden');
            averages.classList.remove('hidden');
        }
    }
    //radio.y_dataが一つも選択されていなければ配列を初期化
    function arry_clear(){
        let count = 0;
        for(var i=0; i<form.y_data.length-1;i++){
            if(form.y_data[i].checked){ 
                count++;
            }
        }
        if(count == 0){
            vals=[];
        }
    }

    //データのフラグ(0=年,1=年月,2=年月日)
    let data_flag;
    //年月日データの取得
    let x_date_top = document.getElementById('y_top');
    let x_date_last = document.getElementById('y_last');

    //top側の変数
    let top_arry = [];   

    //last側の変数
    let last_arry = [];

    //テキストボックスの内容が変わったら
    x_date_top.onchange=function(){
        top_arry = x_date_top.value.split('/');

        for(var i=0; i < top_arry.length; i++){
            if(i == 0){
                if(top_arry[i] < 1946 || top_arry[i] > 2022 || top_arry[i].match(/^[0-9]*$/) == null){
                    console.log('入力エラー');
                }
            }
            else if(top_arry.length >= 2 && i == 1){
                if(top_arry[i] < 1 || top_arry[i] > 12 || top_arry[i].match(/^[0-9]*$/) == null){
                    console.log('入力エラー');
                }
            }
            else if(top_arry.length == 3 && i == 2){
                if(top_arry[i] < 1 || top_arry[i].match(/^[0-9]*$/) != null){
                    console.log('入力エラー');
                }
            }
        }
        console.log(top_arry.length);
    }

    x_date_last.onchange=function(){
        last_arry = x_date_last.value.split('/');

        for(var i=0; i < last_arry.length; i++){
            if(i == 0 ){
                if(last_arry[i] < 1946 || last_arry[i] > 2022 || last_arry[i].match(/^[0-9]*$/) == null){
                    console.log('入力エラー');
                }
            }
            else if(last_arry.length >= 2 && i == 1){
                if(last_arry[i] < 1 || last_arry[i] > 12 || last_arry[i].match(/^[0-9]*$/) == null){
                    console.log('入力エラー');
                }
            }
            else if(last_arry.length == 3 && i == 2){
                if( last_arry[i] < 1 || last_arry[i].match(/^[0-9]*$/) == null){
                    console.log('入力エラー');
                }   
            }
        }
        console.log(last_arry);
    }
    
    function graphDataSet(){
        $.ajax({
            'url':'{% url "test:graphCreatData %}',
            'type':'POST',
            'data':{
                'y_data':vals,
                'x_top_data':top_arry,
                'x_last_data':last_arry,
            },
            'dataType': 'json'
        })
    }

    document.getElementById('log').onclick=function(){
        console.log(x_date_top);
    }
    