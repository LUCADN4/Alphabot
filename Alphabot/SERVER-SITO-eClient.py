import socket
import AlphaBot
import time
import sqlite3
# importazione del modulo Flask e di alcune sue funzioni
from flask import Flask, render_template, request
# creazione dell'istanza dell'applicazione Flask
app = Flask(__name__)
# definizione della rotta '/' per la gestione delle richieste GET e POST
@app.route("/", methods=['GET', 'POST'])
def index():
        # verifica se la richiesta è di tipo POST
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

        elif request.form.get('action4') == 'DESTRA':
            alpha.right()
            time.sleep(1)
            alpha.stop()
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")
con = sqlite3.connect("./TabellaRaspberryPi.db")
cur = con.cursor()
alpha = AlphaBot.AlphaBot()

def MovimentoDatabase(dato):
    res = cur.execute(f"SELECT Movimento FROM TABELLA_MOVIMENTI WHERE ID={dato}")
    dati =str(res.fetchone()[0]).split(";")
    for dato in dati:
        dati = dato.split(",")
        print(dato,dati)
        dizio[dati[0]]()
        time.sleep(float(dati[1]))
        alpha.stop()
        time.sleep(0.5)


dizio = {"s": alpha.stop,"f":alpha.forward,"b":alpha.backward,"l":alpha.left,"r":alpha.right}
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",5000))
    print("Sto ascoltando...")
    s.listen()
    connection,address = s.accept()
    while True:
        dato = connection.recv(4096).decode().lower()
        print(dato)
        if "," in dato:
            dati = dato.split(",")
            print("1")
            if dati[0]== "id":
                    print("2")
                    MovimentoDatabase(int(dati[1]))
            else:
                    dizio[dati[0]]()
                    time.sleep(float(dati[1]))
                    dizio["s"]()
        else:
                time.sleep(float(dati[1]))
                dizio["s"]()
    s.close()
        
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
    main()
