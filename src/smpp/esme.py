import socket

from pdu_builder import *


class ESME:

    def __init__(self):
        self.state = None
        self.sequence_number = 1
        self.conn = None
        self.system_id = None
        self.password = None


    def connect(self, host='127.0.0.1', port=2775):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, port))
        self.state = 'OPEN'


    def disconnect(self):
        if self.state in ['BOUND_TX', 'BOUND_TR', 'BOUND_TRX']:
            self.__unbind()
        self.conn.close()
        self.state = 'CLOSED'


    def do_recv(self):
        length_bin = self.conn.recv(4)
        length = int(binascii.b2a_hex(length_bin),16)
        rest_bin = self.conn.recv(length-4)
        resp_pdu = unpack_pdu(length_bin + rest_bin)
        print '...', resp_pdu['header']['sequence_number'],
        print '>',   resp_pdu['header']['command_id'],
        print '...', resp_pdu['header']['command_status']
        return resp_pdu


    def bind_transmitter(self, system_id=None, password=None):
        if system_id != None: self.system_id = system_id
        if password != None: self.password = password
        pdu = BindTransmitter(sequence_number = self.sequence_number,
                system_id = self.system_id,
                password = self.password)
        self.conn.send(pdu.get_bin())
        self.sequence_number +=1
        self.do_recv()
        self.state = 'BOUND_TX'


    def __unbind(self):
        pdu = Unbind(sequence_number = self.sequence_number)
        self.conn.send(pdu.get_bin())
        self.sequence_number +=1
        self.do_recv()
        self.state = None


    def submit_sm(self, message=''):
        pdu = SubmitSM(sequence_number = self.sequence_number,
                short_message = message)
        self.conn.send(pdu.get_bin())
        self.sequence_number +=1
        self.do_recv()


