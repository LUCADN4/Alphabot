from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import socket
import AlphaBot
import time

alpha = AlphaBot.AlphaBot()
dizio = {"s": alpha.stop,"f":alpha.forward,"b":alpha.backward,"l":alpha.left,"r":alpha.right}
app = Flask(__name__)


def validate(username, password):
    completion = False
    con = sqlite3.connect('./TabellaRaspberryPi.db')
    #with sqlite3.connect('static/db.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM UTENTI")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[1]
        dbPass = row[2]
        if dbUser==username:
            completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route('/secret', methods=['GET', 'POST'])
def secret():
    if request.method == 'POST':
        if request.form.get('action1') == 'AVANTI':
                alpha.forward(50)
                time.sleep(1)
                alpha.stop()

        elif  request.form.get('action2') == 'INDIETRO':
            alpha.backward(50)
            time.sleep(1)
            alpha.stop()

        elif request.form.get('action3') == 'SINISTRA':
            alpha.left()
            time.sleep(1)
            alpha.stop()
        elif request.form.get('cmd') == 'cmd':
            dato = int(request.form['comando'])
            con = sqlite3.connect("./TabellaRaspberryPi.db")
            cur = con.cursor()
            res = cur.execute(f"SELECT Movimento FROM TABELLA_MOVIMENTI WHERE ID={dato}")
            dati =str(res.fetchone()[0]).split(";")
            for dato in dati:
                dati = dato.split(",")
                print(dato,dati)
                dizio[dati[0]]()
                time.sleep(float(dati[1]))
                alpha.stop()
                time.sleep(0.5)
        elif request.form.get('action4') == 'DESTRA':
            alpha.right()
            time.sleep(1)
            alpha.stop()
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html')
    

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)
