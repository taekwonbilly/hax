import sys
import socket
import threading
import SocketServer
import time
import traceback

SERVER_ADDRESS = file("server.txt", "r").read().strip()
QUERY_STRING = file("auth.txt", "r").read().strip()
CHUNK_SIZE = 4096

if __name__ == '__main__':
    while True:
        try:
            time.sleep(2)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(QUERY_STRING, (SERVER_ADDRESS, 4756))
            print "SENDING to {}: ".format(SERVER_ADDRESS)
            st = ""
            while True:
                t = s.recv(CHUNK_SIZE)
                st += t
                if len(t) < CHUNK_SIZE: break
            s.close()
            print "RECEIVING: "
            print(st)
        except(Exception):
            traceback.print_exc()
            pass
