#!/usr/bin/env python
from socket import socket

def main():
    s = socket()
    s.connect(("190.145.70.83", 8000))
    
    while True:
        f = open("./build.xml", "rb")
        content = f.read(1024)
        
        while content:
            # Enviar contenido.i
            print "Intentando enviar"
            s.send(content)
            content = f.read(1024) 
        break

    try:
        s.send(chr(1))
    except TypeError:
        s.send(bytes(chr(1), "utf-8"))

    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")
if __name__ == "__main__":
    print "Start client socket"
    main()
