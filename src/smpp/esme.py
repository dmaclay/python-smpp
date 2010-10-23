import socket

from pdu_builder import *


class ESME:

    def __init__(self):
        self.sequence_number = 1
        self.conn = None
        self.system_id = None
        self.password = None

    def connect_SMSC(self, host='127.0.0.1', port=2775):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, port))

    def disconnect_SMSC(self):
        self.conn.close()


    def bind_SMSC(self, system_id=None, password=None):
        if system_id != None: self.system_id = system_id
        if password != None: self.password = password
        bind = BindTransmitter(
                sequence_number = self.sequence_number,
                system_id = self.system_id,
                password = self.password)
        self.conn.send(bind.get_bin())
        self.sequence_number +=1

        length_bin = self.conn.recv(4)
        length = int(binascii.b2a_hex(length_bin),16)
        rest_bin = self.conn.recv(length-4)
        print '<<<<', unpack_pdu(length_bin + rest_bin)


