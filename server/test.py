import sys
import socket
import threading
import SocketServer
import time
import traceback

SERVER_ADDRESS = file("server.txt", "r").read().strip()


if __name__ == '__main__':
    while True:
        try:
            time.sleep(1)
            print "PRESEND: {}".format(time.time())
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print "SENDING: {} to {}".format(time.time(), SERVER_ADDRESS)
            s.sendto("{}|{}|{}".format("testing","9999",time.time()), (SERVER_ADDRESS, 4756))
        except(Exception):
            traceback.print_exc()
            pass
