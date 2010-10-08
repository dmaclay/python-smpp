import socket

from pdu import *


class ESME:

    def __init__(self):
        self.conn = None

    def connect_SMSC(self, host='127.0.0.1', port=2775):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, port))

    def disconnect_SMSC(self):
        self.conn.close()


    def bind_SMSC(self):
        out_hex = re.sub(' ','','00 00 00 2F 00 00 00 02 00 00 00 00 00 00 00 01 53 4D 50 50 33 54 45 53 54 00 73 65 63 72 65 74 30 38 00 53 55 42 4D 49 54 31 00 00 01 01 00')
        print out_hex
        out_bin = binascii.a2b_hex(out_hex)
        self.conn.send(out_bin)
        length_bin = self.conn.recv(4)
        length = int(binascii.b2a_hex(length_bin),16)
        rest_bin = self.conn.recv(length-4)
        unpack_pdu(length_bin + rest_bin)


#esme = ESME()
#esme.connect_SMSC('localhost')
#esme.bind_SMSC()
#esme.disconnect_SMSC()

