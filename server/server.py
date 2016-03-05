import sys
import socket
import threading
import SocketServer
import traceback

QUERY_STRING = file("auth.txt", "r").read().strip()

# format (ip,service,port):heartbeat[ts]
bots = {}

class UDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            print "RECEIVING FROM {} dat--".format(self.client_address[0]),
            data = self.request[0].strip().split("|")
            print len(data)
            if len(data)==0: return
            if data[0] == QUERY_STRING:
                self.request[1].sendto(str(bots), self.client_address)
                return
            if len(data) == 3:
                service, port, heartbeat = data
                bots[(self.client_address[0],service,port)] = heartbeat
        except(Exception):
            traceback.print_exc()
            pass

if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 4756
    print "STARTING SERVER"
    server = SocketServer.UDPServer((HOST,PORT), UDPHandler)
    server.serve_forever()
