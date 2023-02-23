import socket
lettere=["f","b","l","r","s","id"]

def main():
    # Crea un'istanza di socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connette il socket all'indirizzo IP e alla porta specificati
    s.connect(("192.168.1.128",5000))
    # Stampa a video i comandi disponibili
    print("COMANDI  f b l r s id")
    # Ciclo infinito che legge in input un comando e lo invia al server tramite il socket
    while True:
        comando = input("inserisci comando e tempo con vigola: ")
        s.sendall("".join(comando).encode())

if __name__ == "__main__":
    main()