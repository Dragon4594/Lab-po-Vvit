import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="1",
                        user="postgres",
                        password="1242EefD933",
                        host="",
                        port="5432")

cursor = conn.cursor()

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            if username == '':
                return render_template('login.html', empty_login=True)
            elif password == '':
                return render_template('login.html', empty_password=True)
            try:
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
                records = list(cursor.fetchall())

                return render_template('account.html', full_name=records[0][1],login=records[0][2])
            except IndexError:
                return render_template('login.html', not_in_base=True)
        if request.form.get("registration"):
                return redirect("/registration/")

    return render_template('login.html')
@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        if request.form.get("registration"):
            name = request.form.get('name')
            login = request.form.get('login')
            password = request.form.get('password')
            t=1
            if len(str(password))<=6:
                return render_template('registration.html', insert_name=name, insert_login=login, insert_password='', kor_pass=True)
                t=0
            if name == '' or login == '' or password == '':
                return render_template('registration.html', insert_name=name, insert_login=login, insert_password=password, pusto=True)
                t=0
            cursor.execute("SELECT * FROM service.users WHERE login = %s", (login,))
            if cursor.fetchone():
                return render_template('registration.html', insert_name=name, insert_login='', insert_password=password, registr=True)
                t=0
            if t==1:
                cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',(str(name), str(login), str(password)))
                conn.commit()
                return render_template('account.html', rg=True, log=login, ful_name=name)
        if request.form.get("login"):
            return redirect("/login/")
    return render_template('registration.html')

#Андрей Удалов БВТ2204
#http://localhost:5000/login/
