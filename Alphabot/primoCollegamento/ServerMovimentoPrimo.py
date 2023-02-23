import socket
import AlphaBot

robot = AlphaBot.AlphaBot

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 5000))
    s.listen()
    while True:
        connect, address = s.accept()
        print("connesso")
        dati = (connect.recv(4096)).decode()
        if dati == "forward":
            robot.forward()
        elif dati == "back":
            robot.backward()
        elif dati == "left":
            robot.left()
        elif dati == "right":
            robot.right()

  

if __name__ == "__main__":
    main()