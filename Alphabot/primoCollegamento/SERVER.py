import socket   #importa il modulo socket per la comunicazione di rete
import AlphaBot #importa il modulo AlphaBot
import time     #importa il modulo time per gestire i tempi di attesa
import sqlite3  #importa il modulo sqlite3 per l'interfacciamento con il database

con = sqlite3.connect("./TabellaRaspberryPi.db")  #si connette al database
cur = con.cursor()                                #crea un cursore per eseguire le query sul database
alpha = AlphaBot.AlphaBot()                       #crea un oggetto di tipo AlphaBot per controllare il robot

#funzione per eseguire i movimenti presenti nel database
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

#dizionario dei comandi e dei corrispondenti metodi da chiamare
dizio = {"s": alpha.stop,"f":alpha.forward,"b":alpha.backward,"l":alpha.left,"r":alpha.right}
#funzione principale per la gestione della comunicazione di rete

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #crea un oggetto socket
    s.bind(("0.0.0.0",5000)) #associa l'oggetto socket all'indirizzo IP del server e alla porta specificata
    print("Sto ascoltando...")
    s.listen() #mette in ascolto l'oggetto socket
    connection,address = s.accept() #accetta una connessione in entrata
    while True:
        dato = connection.recv(4096).decode().lower() #riceve il messaggio in entrata e lo decodifica
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
    
        
if __name__=="__main__":
    main()