import cv2
import socket
import serial
import sys
import traceback
from threading import Thread

TCP_IP = 'localhost' #GANTI IP JURI (COACH)
TCP_PORT = 28097

print "Loading, wait for 5 seconds."

try:
    BUFFER_SIZE = 1024
    MESSAGE = "Saitama"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
except:
    print "Error, Check COACH IP."
    sys.exit(-1)
    
print "Coach Mode = Success"

try: 
    ser = serial.Serial('COM3', 9600) #Ganti COM BLUETOOTH
except:
    print "Gagal Koneksi Ke Saitama. Ulangi Lagi."
    sys.exit(-1)

print "Berhasil Konek Ke Saitama Robot."

print "Menunggu Data Juri"

#s.close() #close UDP

##    if(data == 'S'):
##        #ser.write("R")
##
##    if(data == 'k'):
##        #ser.write("L")
            
def prog1(): #Baca Data Server
    while 1:
        data = s.recv(BUFFER_SIZE)
        print "Data:", data
        if data == 'S':
            print "asik"
        if data == 'k':
            print "miuw"
        return True
        
def prog2(): #Kendali Saitama Jarak Jauh
    while 1:
        
        if cv2.waitKey() == ord('a'):
            print "START"
        if cv2.waitKey() == ord('d'):
            print "STOP"
        return True

if __name__ == '__main__':
    Thread(target=prog2).start()
    Thread(target=prog1).start()

cv2.destroyAllWindows()
