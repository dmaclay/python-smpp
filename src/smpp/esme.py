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

    def do_recv(self):
        length_bin = self.conn.recv(4)
        length = int(binascii.b2a_hex(length_bin),16)
        rest_bin = self.conn.recv(length-4)
        print '...',
        print unpack_pdu(length_bin + rest_bin)['header']['sequence_number'],
        print '>',
        print unpack_pdu(length_bin + rest_bin)['header']['command_id'],
        print '...',
        print unpack_pdu(length_bin + rest_bin)['header']['command_status']

    def bind_SMSC(self, system_id=None, password=None):
        if system_id != None: self.system_id = system_id
        if password != None: self.password = password
        pdu = BindTransmitter(sequence_number = self.sequence_number,
                system_id = self.system_id,
                password = self.password)
        self.conn.send(pdu.get_bin())
        self.sequence_number +=1
        self.do_recv()


    def unbind_SMSC(self, system_id=None, password=None):
        if system_id != None: self.system_id = system_id
        if password != None: self.password = password
        pdu = Unbind(sequence_number = self.sequence_number)
        self.conn.send(pdu.get_bin())
        self.sequence_number +=1
        self.do_recv()


    def submit_sm(self, message=''):
        pdu = SubmitSM(sequence_number = self.sequence_number,
                short_message = message)
        self.conn.send(pdu.get_bin())
        self.sequence_number +=1
        self.do_recv()


