import socket

from pdu_builder import *


class ESME:

    def __init__(self):
        self.state = 'CLOSED'
        self.sequence_number = 1
        self.conn = None
        self.system_id = None
        self.password = None


    def connect(self, host='127.0.0.1', port=2775):
        if self.state in ['CLOSED']:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.connect((host, port))
            self.state = 'OPEN'


    def disconnect(self):
        if self.state in ['BOUND_TX', 'BOUND_RX', 'BOUND_TRX']:
            self.__unbind()
        if self.state in ['OPEN']:
            self.conn.close()
            self.state = 'CLOSED'


    def do_recv(self):
        resp_pdu = None
        length_bin = self.conn.recv(4)
        #print 'length_bin', len(length_bin), length_bin
        if len(length_bin) == 4:
            length = int(binascii.b2a_hex(length_bin),16)
            rest_bin = self.conn.recv(length-4)
            resp_pdu = unpack_pdu(length_bin + rest_bin)
            print '...', resp_pdu['header']['sequence_number'],
            print '>',   resp_pdu['header']['command_id'],
            print '...', resp_pdu['header']['command_status']
        return resp_pdu


    def __is_ok(self, pdu, id_check=None):
        if (isinstance(pdu, dict)
                and pdu.get('header',{}).get('command_status') == 'ESME_ROK'
                and (id_check == None
                    or id_check == pdu['header'].get('command_id'))):
            return True
        else:
            return False


    def bind_transmitter(self, system_id=None, password=None):
        if self.state in ['OPEN']:
            if system_id != None: self.system_id = system_id
            if password != None: self.password = password
            pdu = BindTransmitter(sequence_number = self.sequence_number,
                    system_id = self.system_id,
                    password = self.password)
            self.conn.send(pdu.get_bin())
            self.sequence_number +=1
            if self.__is_ok(self.do_recv(), 'bind_transmitter_resp'):
                self.state = 'BOUND_TX'


    def __unbind(self):
        if self.state in ['BOUND_TX', 'BOUND_RX', 'BOUND_TRX']:
            pdu = Unbind(sequence_number = self.sequence_number)
            self.conn.send(pdu.get_bin())
            self.sequence_number +=1
            if self.__is_ok(self.do_recv(), 'unbind_resp'):
                self.state = 'OPEN'


    def unbind(self): # will probably be deprecated
        self.__unbind()


    def submit_sm(self, message=''):
        if self.state in ['BOUND_TX', 'BOUND_TRX']:
            pdu = SubmitSM(sequence_number = self.sequence_number,
                    short_message = message)
            self.conn.send(pdu.get_bin())
            self.sequence_number +=1
            submit_sm_resp = self.do_recv()
            #print self.__is_ok(submit_sm_resp, 'submit_sm_resp')


