#!/usr/bin/env python
import time,base64,os
from lxml import etree
import xml.etree.ElementTree as ET
from socket import socket, error

def main():
    s = socket()
    
    s.bind(("190.145.70.83", 8000))
    s.listen(0)
    
    conn, addr = s.accept()
    #ruta = "recibido" + time.strftime("%Y-%m-%d_%H_%M")+".txt"
    folder = "recibido"
    
    if os.path.isdir(folder)==False:
        path = os.mkdir(folder)
    

    ruta = folder + "/"+time.strftime("%Y_%m_%d_%H:%M_%S")+".txt"
    f = open(ruta, "wb")
    
    while True:
        try:
            input_data = conn.recv(1024)
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break
     
    print("El archivo se ha recibido correctamente.")
    f.close()

def readXml(ruta):
    
    f = open(ruta, 'r')
    tree = str(f.readlines())   
    archivo = str(tree[tree.find("<?xml"):tree.find("</infoplate>")+12])
    
    root = ET.fromstring(archivo);    
   
    for child in root:
	if child.tag == 'Plate':
	    plate = child.text
	    folder = "/opt/receive/"+time.strftime("%Y-%m-%d")+"/"
	    
    	    if os.path.isdir(folder)==False:
		path = os.mkdir(folder)
	    else:
		path = folder
	
	    path = path + child.text+".jpg"

	
		
	if child.tag=='img':

	    fh = open(path,"wb")
	    fh.write((child.text).decode('base64'))
	    fh.close()
            print child.text
		
	   
	    
	
  
if __name__ == "__main__":
    print "Inicio el socket"
    main()
