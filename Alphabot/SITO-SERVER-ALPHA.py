import socket
import AlphaBot
import time
import sqlite3
# importazione del modulo Flask e di alcune sue funzioni
from flask import Flask, render_template, request
# creazione dell'istanza dell'applicazione Flask
app = Flask(__name__)

alpha = AlphaBot.AlphaBot()
dizio = {"s": alpha.stop,"f":alpha.forward,"b":alpha.backward,"l":alpha.left,"r":alpha.right}


@app.route("/", methods=['GET', 'POST'])
def index():
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
    
    return render_template("index.html")

app.run(debug=True, host='0.0.0.0')
ok = True
