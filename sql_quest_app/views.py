from functools import singledispatch
import sql_quest_app
from django.shortcuts import render
from django.http import HttpResponse
from .models import std_data,QA_data,SQL_syntax,QA,QC
from .forms import sql_form
import sqlite3
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm  # 追記
from django.urls import reverse_lazy # 追記
import shutil
import sqlite3
import os

sql_Q=[[""],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'', '', '','');",
            "insert into Quest_table values(2,'', '', '','');",
            "insert into Quest_table values(3,'', '', '','');",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'オルカ', 25, '勇者',4);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'カースト', 23, '踊り子',5);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'オルカ', 25, '勇者',4);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'カースト', 23, '踊り子',5);",
            "insert into Quest_table values(4,'アレックス', 42, '勇者',7);",
            "insert into Quest_table values(5,'ゴードン', 33, '武闘家',6);",
            "insert into Quest_table values(6,'ミレー', 29, '踊り子',5);",
            "insert into Quest_table values(7,'ラーマ', 10, '魔法使い',2);",
            "insert into Quest_table values(8,'シャーリー', 15, '僧侶',3);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'リュー', 9, '勇者見習い',1);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ローラ', 5, '盗賊見習い',5);",
            "insert into Quest_table values(4,'アレックス', 42, '勇者',7);",
            "insert into Quest_table values(5,'ゴードン', 33, '武闘家',6);",
            "insert into Quest_table values(6,'ミレー', 29, '踊り子',5);",
            "insert into Quest_table values(7,'シュン', 3, '僧侶見習い',2);",
            "insert into Quest_table values(8,'シャーリー', 15, '僧侶',3);",
            "insert into Quest_table values(9,'レイ', 7, '侍',3);",
            "insert into Quest_table values(10,'セレン', 8, '魔導士',3);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'オルカ', 25, '勇者',4);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'カースト', 23, '踊り子',5);",
            "insert into Quest_table values(4,'アレックス', 4, '勇者',1);",
            "insert into Quest_table values(5,'ゴードン', 33, '武闘家',6);",
            "insert into Quest_table values(6,'ミレー', 29, '踊り子',5);",
            "insert into Quest_table values(7,'ラーマ', 10, '魔法使い',2);",
            "insert into Quest_table values(8,'シャーリー', 15, '僧侶',3);",
            "insert into Quest_table values(9,'レイ', 7, '侍',1);",
            "insert into Quest_table values(10,'セレン', 8, '魔導士',2);",
        ],
        ]
sql_A=[[""],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'アレックス', 25, '勇者',4);",
            "insert into Quest_table values(2,'ゴードン', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ミレー', 23, '踊り子',5);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'オルカ', 25, '勇者',4);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'カースト', 23, '踊り子',5);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'オルカ', 25, '勇者',4);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'カースト', 23, '踊り子',5);",
            "insert into Quest_table values(4,'アレックス', 42, '勇者',7);",
            "insert into Quest_table values(5,'ゴードン', 33, '武闘家',6);",
            "insert into Quest_table values(6,'ミレー', 29, '踊り子',5);",
            "insert into Quest_table values(7,'ラーマ', 10, '魔法使い',2);",
            "insert into Quest_table values(8,'シャーリー', 15, '僧侶',3);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'リュー', 9, '勇者見習い',1);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ローラ', 5, '盗賊見習い',5);",
            "insert into Quest_table values(4,'アレックス', 42, '勇者',7);",
            "insert into Quest_table values(5,'ゴードン', 33, '武闘家',6);",
            "insert into Quest_table values(6,'ミレー', 29, '踊り子',5);",
            "insert into Quest_table values(7,'シュン', 3, '僧侶見習い',2);",
            "insert into Quest_table values(8,'シャーリー', 15, '僧侶',3);",
        ],
        [
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'オルカ', 25, '勇者',4);",
            "insert into Quest_table values(2,'マレー', 28, '武闘家',6);",
            "insert into Quest_table values(3,'カースト', 23, '踊り子',5);",
            "insert into Quest_table values(4,'アレックス', 4, '勇者',1);",
            "insert into Quest_table values(5,'ゴードン', 33, '武闘家',6);",
            "insert into Quest_table values(6,'ミレー', 29, '踊り子',5);",
            "insert into Quest_table values(7,'ラーマ', 10, '魔法使い',2);",
            "insert into Quest_table values(8,'シャーリー', 15, '僧侶',3);",
            "insert into Quest_table values(9,'レイ', 7, '侍',1);",
            "insert into Quest_table values(10,'セレン', 8, '魔導士',2);",
        ],
        ]
#正解SQL文
ans_SQL=["",
        "select * from Quest_table",
        "select name,job from Quest_table",
        "select * from Quest_table where job='勇者'",
        "select * from Quest_table where job like '%見習い'",
        "select * from Quest_table order by Lv limit 4",
        ]

#正解確認関数　yがユーザー解答
def check(x,y,z):
    if z == 3:
        flag=2
        for a in y:
            if "オルカ" in a or "アレックス" in a:
                flag-=1
            else:
                flag+=1
        print(f"正解3は",{flag})
        return flag
    else:
        flag=0
        if len(x) != len(y):
            flag+=1
        for (a,b) in zip(x,y):
            if a!=b:
                flag+=1
        print(f"正解は",{flag})
        return flag

def index(request):
    params={
        'title':User,
    }
    return render(request,'sql_quest_app/index.html',params)

@login_required(login_url='/accounts/login/')
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
        msg = request.user
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


# class IndexView(TemplateView):
#     template_name = "sql_quest_app/SQ_overview.html"
@login_required(login_url='/accounts/login/')
def SQ_overview(request,):
    data = QA_data.objects.all()
    form = sql_form()
    params={
        'title':User,
        'data':data,
        'form':form,
    }
    return render(request,'sql_quest_app/SQ_overview.html',params)

###############################################################################1
@login_required(login_url='/accounts/login/')
# def SQ_Quest(request,QA_No):
def SQ_Quest1(request,):
    if (request.method == 'POST'):
        msg = request.POST.get('sql_syntax')
        sql_p = request.POST.get('sql_syntax')
        print(msg)
        name=request.session.session_key
        shutil.copy('playground.sqlite3', './user_folder/'+name+'playground.sqlite3')
        dbname = './user_folder/'+name+'playground.sqlite3'
        conn = sqlite3.connect(dbname)
        sqls=[
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'アレックス', 25, '勇者',4);",
            "insert into Quest_table values(2,'ゴードン', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ミレー', 23, '踊り子',5);",
            ]
        cur = conn.cursor()
        for sql in sqls:
            cur.execute(sql)
        conn.commit()
        # ind=[]
        # indexs=cur.execute("PRAGMA TABLE_INFO (Quest_table)")
        # for index in indexs:
        #     ind.append(index[1])
        # print(ind)
        # vol=len(ind)
        try:
            res = cur.execute(sql_p)
            ind = [col[0] for col in cur.description]
            ls=[]
        except:
            res = []
            ind = []
            ls=[["error"]]
        for row in res:
            ls.append(row)
        data = QA_data.objects.all()
        for row in data:
            print(row)

        form = sql_form()

        params={
            # 'title':'Quest'+str(QA_No),
            'title':msg,
            'test':request.session.session_key,
            'data':data,
            'ls':ls,
            'form':form,
            'ind':ind,
            # 'ls1':ls1,
            # 'ls2':ls2,
        }
        conn.close()
        # return render(request,'sql_quest_app/SQ_Quest'+str(QA_No)+'.html',params)
        return render(request,'sql_quest_app/SQ_Answer1.html',params)

    else:
        name=request.session.session_key
        shutil.copy('playground.sqlite3', './user_folder/'+name+'playground.sqlite3')

        # アプリの中で実行してもベースディレクトリで動く
        # sql = "CREATE TABLE Quest_table (id integer NOT NULL, name	text,age INTEGER,job TEXT,PRIMARY KEY(id AUTOINCREMENT))"
        # # sql = "CREATE TABLE test(id INTEGER PRIMARY KEY,name TEXT NOT NULL,age INTEGER NOT NULL,created_datetime TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')))"
        # sql2 = "insert into Quest_table values(1,'アレックス', 19, '勇者');"
        # sql3 = "insert into Quest_table values(2,'ゴードン', 25, '武闘家');"
        # sql4 = "insert into Quest_table values(3,'ミレー', 18, '踊り子');"
        dbname = './user_folder/'+name+'playground.sqlite3'
        conn = sqlite3.connect(dbname)

        # test = SQL_syntax.objects.get(id=1).syntax
        sqls=[
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'アレックス', 25, '勇者',4);",
            "insert into Quest_table values(2,'ゴードン', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ミレー', 23, '踊り子',5);",
            ]
        

        # SQLiteを操作するためのカーソルを作成
        cur = conn.cursor()
        # cur.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')

        # # Insert実行
        # cur.execute("INSERT INTO articles VALUES (1,'今朝のおかず','魚を食べました','2020-02-01 00:00:00')")
        # cur.execute("INSERT INTO articles VALUES (2,'今日のお昼ごはん','カレーを食べました','2020-02-02 00:00:00')")
        # cur.execute("INSERT INTO articles VALUES (3,'今夜の夕食','夕食はハンバーグでした','2020-02-03 00:00:00')")

        # テーブルのコピー
        for sql in sqls:
            cur.execute(sql)
        # cur.execute(sql2)
        # cur.execute(sql3)
        # cur.execute(sql4)
        conn.commit()
        # ind=[]
        # indexs=cur.execute("PRAGMA TABLE_INFO (Quest_table)")
        # for index in indexs:
        #     ind.append(index[1])
        # print(ind)
        # vol=len(ind)

        res = cur.execute("select * from Quest_table")
        ind = [col[0] for col in cur.description]
        ls=[]
        for row in res:
            ls.append(row)
        #     dict = {list[i]:list[i + 1] for i in range(0, len(list), 2)}
        #     print(list)
        #     print(dict)
        # di1=dict(ls)
        # print(di1)

        # ls1,ls2,ls3,ls4=[],[],[],[]
        # for row in res:
        #     ls1.append(row[1])
        #     ls2.append(row[2])
        #     ls3.append(row[3])
        # ls=list(zip(ls1,ls2,ls3))

        # ls=[('アレックス', 19, '勇者'), ('ゴードン', 25, '武闘家'), ('ミレー', 18, '踊り子')]
        print(ls)


        data = QA_data.objects.all()
        for row in data:
            print(row)

        form = sql_form()

        params={
            # 'title':'Quest'+str(QA_No),
            'title':'Quest1',
            'test':request.session.session_key,
            'data':data,
            'ls':ls,
            'form':form,
            'ind':ind,
            # 'ls1':ls1,
            # 'ls2':ls2,
        }
        conn.close()
        # return render(request,'sql_quest_app/SQ_Quest'+str(QA_No)+'.html',params)
        return render(request,'sql_quest_app/SQ_Quest1.html',params)
###############################################################################################2
@login_required(login_url='/accounts/login/')
# def SQ_Quest(request,QA_No):
def SQ_Quest2(request,):
    if (request.method == 'POST'):
        msg = request.POST.get('sql_syntax')
        sql_p = request.POST.get('sql_syntax')
        print(msg)
        name=request.session.session_key
        shutil.copy('playground.sqlite3', './user_folder/'+name+'playground.sqlite3')
        dbname = './user_folder/'+name+'playground.sqlite3'
        conn = sqlite3.connect(dbname)
        sqls=[
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'アレックス', 25, '勇者',4);",
            "insert into Quest_table values(2,'ゴードン', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ミレー', 23, '踊り子',5);",
            ]
        cur = conn.cursor()
        for sql in sqls:
            cur.execute(sql)
        conn.commit()

        res = cur.execute("select * from Quest_table")
        ind0 = [col[0] for col in cur.description]
        ls0=[]
        for row in res:
            ls0.append(row)

        try:
            res = cur.execute(sql_p)
            ind = [col[0] for col in cur.description]
            ls=[]
        except:
            res = []
            ind = []
            ls=[["error"]]
        for row in res:
            ls.append(row)
        data = QA_data.objects.all()
        for row in data:
            print(row)

        form = sql_form()

        params={
            # 'title':'Quest'+str(QA_No),
            'title':msg,
            'test':request.session.session_key,
            'data':data,
            'ls':ls,
            'form':form,
            'ind':ind,
            'ind0':ind0,
            'ls0':ls0,
            # 'ls1':ls1,
            # 'ls2':ls2,
        }
        conn.close()
        # return render(request,'sql_quest_app/SQ_Quest'+str(QA_No)+'.html',params)
        return render(request,'sql_quest_app/SQ_Answer2.html',params)

    else:
        name=request.session.session_key
        shutil.copy('playground.sqlite3', './user_folder/'+name+'playground.sqlite3')
        dbname = './user_folder/'+name+'playground.sqlite3'
        conn = sqlite3.connect(dbname)
        sqls=[
            "CREATE TABLE Quest_table (id integer NOT NULL, name text,lv INTEGER,job TEXT,rank INTEGER ,PRIMARY KEY(id AUTOINCREMENT))",
            "insert into Quest_table values(1,'アレックス', 25, '勇者',4);",
            "insert into Quest_table values(2,'ゴードン', 28, '武闘家',6);",
            "insert into Quest_table values(3,'ミレー', 23, '踊り子',5);",
            ]
        
        # SQLiteを操作するためのカーソルを作成
        cur = conn.cursor()

        # テーブルのコピー
        for sql in sqls:
            cur.execute(sql)
        conn.commit()

        res = cur.execute("select * from Quest_table")
        ind = [col[0] for col in cur.description]
        ls=[]
        for row in res:
            ls.append(row)

        data = QA_data.objects.all()
        for row in data:
            print(row)

        form = sql_form()

        params={

            'title':'Quest1',
            'test':request.session.session_key,
            'data':data,
            'ls':ls,
            'form':form,
            'ind':ind,

        }
        conn.close()
        # return render(request,'sql_quest_app/SQ_Quest'+str(QA_No)+'.html',params)
        return render(request,'sql_quest_app/SQ_Quest2.html',params)
##########################################################################################################
@login_required(login_url='/accounts/login/')
def SQ_Quest(request,QA_No):
    if (request.method == 'POST'):
        msg = request.POST.get('sql_syntax')
        sql_p = request.POST.get('sql_syntax')
        print(QA_No)
        name=request.session.session_key
        shutil.copy('playground.sqlite3', './user_folder/'+name+'playground.sqlite3')
        dbname = './user_folder/'+name+'playground.sqlite3'
        conn = sqlite3.connect(dbname)
#問題文テーブル呼び出し、作成
        # sqls=sql_Q[int(QA_No)]
        sqls_=(QA.objects.all()[int(QA_No)].quest_table)
        sqls=sqls_.split('@')
        cur = conn.cursor()
        for sql in sqls:
            cur.execute(sql)
        conn.commit()

#問題文テーブルのクエリ化と変数格納
        res = cur.execute("select * from Quest_table")
        ind0 = [col[0] for col in cur.description]
        ls0=[]
        for row in res:
            ls0.append(row)

#問題文テーブルの削除
        cur.execute("drop table Quest_table")
#正解確認よう変数の格納
        # sqls=sql_A[int(QA_No)]
        sqls_=(QA.objects.all()[int(QA_No)].answer_table)
        sqls=sqls_.split('@')       
        cur = conn.cursor()
        for sql in sqls:
            cur.execute(sql)
        conn.commit()

        # res = cur.execute(ans_SQL[int(QA_No)])
        res = cur.execute(QA.objects.all()[int(QA_No)].sql_syn)
        ls1=[]
        for row in res:
            ls1.append(row)
        print("aaaaaaaaaaaaaaaaaaaaaaaaa")
        print(ls1)

#問題文テーブルの削除
        cur.execute("drop table Quest_table")

#解答用問題テーブル呼び出し、作成
        # sqls=sql_A[int(QA_No)]
        sqls_=(QA.objects.all()[int(QA_No)].answer_table)
        sqls=sqls_.split('@')        
        cur = conn.cursor()
        for sql in sqls:
            cur.execute(sql)
        conn.commit()

#フォームのSQL文を反映
        try:
            res = cur.execute(sql_p)
            print("BBBBBBBBBBBBBBb")
            print(sql_p)
            print(type(sql_p))
            ind = [col[0] for col in cur.description]
            ls=[]
        except:
            res = []
            ind = []
            ls=[["error"]]
        for row in res:
            ls.append(row)
        data = QA_data.objects.all()
        for row in data:
            print(row)

        form = sql_form(request.POST)
        Q = QA.objects.all()[int(QA_No)].quest

        print("aaaaaaaaaaaaaaaaaaaaaaaaa")
        # User.first_name="ok"
        print(str(User.first_name))
        # flag=0
        # for (a,b) in zip(ls1,ls):
        #     if a!=b:
        #         flag+=1
        # print(f"正解は",{flag})

        flag=check(ls1,ls,QA_No)

        params={
            # 'title':'Quest'+str(QA_No),
            'title':msg,
            'test':request.session.session_key,
            'data':data,
            'ls':ls,
            'form':form,
            'ind':ind,
            'ind0':ind0,
            'ls0':ls0,
            'Q':Q,
            'No':str(QA_No),
            'flag':flag,
            'Next':str(QA_No+1),
        }
        conn.close()
        # return render(request,'sql_quest_app/SQ_Quest'+str(QA_No)+'.html',params)
        return render(request,'sql_quest_app/SQ_Answer.html',params)
    elif(QA_No > len(QA_data.objects.all())):
        data = QA_data.objects.all()
        form = sql_form()
        params={
        'title':User,
        'data':data,
        'form':form,
        }
        return render(request,'sql_quest_app/SQ_overview.html',params)
    else:
        name=request.session.session_key
        shutil.copy('playground.sqlite3', './user_folder/'+name+'playground.sqlite3')
        dbname = './user_folder/'+name+'playground.sqlite3'
        conn = sqlite3.connect(dbname)
        # sqls=sql_Q[int(QA_No)]
        sqls_=(QA.objects.all()[int(QA_No)].quest_table)
        sqls=sqls_.split('@')
        # SQLiteを操作するためのカーソルを作成
        cur = conn.cursor()

        # テーブルのコピー
        for sql in sqls:
            cur.execute(sql)
        conn.commit()

        res = cur.execute("select * from Quest_table")
        ind = [col[0] for col in cur.description]
        ls=[]
        for row in res:
            ls.append(row)

        data = QA_data.objects.all()
        for row in data:
            print(row)

        form = sql_form()
        Q = QA.objects.all()[int(QA_No)].quest
        print(Q)

        params={

            'title':'Quest'+str(QA_No),
            'test':request.session.session_key,
            'data':data,
            'ls':ls,
            'form':form,
            'ind':ind,
            'Q':Q,
            'No':str(QA_No)
        }
        conn.close()
        # return render(request,'sql_quest_app/SQ_Quest'+str(QA_No)+'.html',params)
        return render(request,'sql_quest_app/SQ_Quest.html',params)



    # test


    # Create your views here.
        # # DBに接続する。なければDBを作成する。
        # dbname = './user_folder/test.sqlite3'
        # conn = sqlite3.connect(dbname)
        # conn = sqlite3.connect('example.db')
        # conn.row_factory = sqlite3.Row # row_factoryにsqlite3.Rowを設定
        
        # # カーソルオブジェクトを取得する
        # c = conn.cursor()
        
        # c.execute('select * from articles')
        # for row in c:
        #     print(row['id']) # カラム名でアクセスすることができる。n
        
        # # コネクションをクローズする
        # conn.close()

    # {% for item in data %}
    # <tr>
    # <th scope="row"><a href='{% url "SQ_Quest" QA_No=item.QA_No %}' class="text-dark text-decoration-none">◆</a></th>
    # <th scope="row"><a href='{% url "SQ_Quest" QA_No=item.QA_No %}' class="text-dark text-decoration-none">Quest{{item.QA_No}}</a></th>
    # <th scope="row"><a href='{% url "SQ_Quest" QA_No=item.QA_No %}' class="text-dark text-decoration-none">{{item.OV}}</a></th>
    # </tr>
    # {% endfor %}
