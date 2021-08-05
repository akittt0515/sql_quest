from functools import singledispatch
import sql_quest_app
from django.shortcuts import render
from django.http import HttpResponse
from .models import std_data
from .forms import sql_form
from QA.models import QA
import sqlite3

def index(request):
    params={
        'title':'Hello/Index',
    }
    return render(request,'sql_quest_app/index.html',params)

def chapter1(request):
    if (request.method == 'POST'):
        msg = request.POST['sql_syntax']
        form = sql_form(request.POST)
        sql ='SELECT * FROM sql_quest_app_std_data'
        sql2 ='CREATE TABLE test2 AS SELECT * FROM QA_qa'
        sql3 ='DROP TABLE test2;'
        if (msg == "aaa"):
            sql += ' where ' + msg
# ----------------------------------------------
            dbname = 'db_QA.sqlite3'
            conn = sqlite3.connect(dbname)

            # SQLiteを操作するためのカーソルを作成
            cur = conn.cursor()

            # テーブルのコピー
            cur.execute(sql2)

            conn.close()
# ----------------------------------------------
            data=std_data.objects.all()
            msg = "ok"
        elif (msg == "bbb"):
            sql += ' where ' + msg
# ----------------------------------------------
            dbname = 'db_QA.sqlite3'
            conn = sqlite3.connect(dbname)

            # SQLiteを操作するためのカーソルを作成
            cur = conn.cursor()

            # テーブルのコピー
            cur.execute(sql3)

            conn.close()
# ----------------------------------------------
            data=std_data.objects.all()
            msg = "ok"
        elif (msg == "ccc"):
            sql += ' where ' + msg
# ----------------------------------------------
            # DBに接続する。なければDBを作成する。
            conn = sqlite3.connect('example.db')
            
            # カーソルを取得する
            c = conn.cursor()
            
            # 1. カーソルをイテレータ (iterator) として扱う
            c.execute('select * from articles')
            for row in c:
                # rowオブジェクトでデータが取得できる。タプル型の結果が取得
                print(row)
            
            # 2. fetchallで結果リストを取得する
            c.execute('select * from articles')
            for row in c.fetchall():
                print(row)
            
            # 3. fetchoneで1件ずつ取得する
            c.execute('select * from articles')
            print(c.fetchone()) # 1レコード目が取得
            print(c.fetchone()) # 2レコード目が取得
            
            
            # コネクションをクローズする
            conn.close()
# ----------------------------------------------
            data=std_data.objects.all()
            msg = "ok"
        elif (msg != ""):
            sql += ' where ' + msg
            data=std_data.objects.raw(sql)
            msg = sql
    else:
        msg = 'search words...'
        form = sql_form()
        # sql ='SELECT * FROM sql_quest_app_std_data where name="アレックス"'
        data = QA.objects.all()
    params = {
        'title':'1章',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'sql_quest_app/chapter1.html',params)





# test


# Create your views here.
