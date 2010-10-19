from unittest import TestCase
from datetime import datetime

from src.smpp.esme import *

def unpack(pdu_hex):
    """Unpack PDU and return it as a dictionary"""
    return unpack_pdu(binascii.a2b_hex(hexclean(pdu_hex)))

def prettydump(pdu_hex):
    """Unpack PDU and dump it as a JSON formatted string"""
    return json.dumps(unpack_pdu(binascii.a2b_hex(hexclean(x))), indent=4, sort_keys=True)

def hexclean(dirtyhex):
    """Remove whitespace, comments & newlines from hex string"""
    return re.sub(r'\s','',re.sub(r'#.*\n','\n',dirtyhex))

stars = "\n******************************************************************\n"



print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

#esme = ESME()
#esme.connect_SMSC('localhost')
#esme.bind_SMSC()
#esme.disconnect_SMSC()

print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

x = '''
    0000003C # command_length
    00000004 # command_id
    00000000 # command_status
    00000005 # sequence_number
    00
    02
    08
    35353500
    01
    01
    35353535353535353500
    00
    00
    00
    00
    00
    00
    00
    00
    00
    0F
    48656C6C6F2077696B697065646961
    00000000
    001d00026566
'''
print stars, prettydump(x)


x = '''
    00000000 # command_length
    00000021 # command_id
    00000000 # command_status
    00000000 # sequence_number
    00
    00
    00
    00
    02
    01 01 01 6500
    02 6600
    00
    00
    00
    00
    00
    00
    00
    00
    00
    00
    0005 0002 0000
    0000 0004 00000000
'''
print stars, prettydump(x)


x = '''
    00000000
    80000021
    00000000
    00000000
    00
    02
    01016565650000000000
    01016666660000000000
'''
print stars, prettydump(x)


print re.sub('.','@',stars),
print re.sub('.','@',stars),
print re.sub('.','@',stars),
print re.sub('.','@',stars)

minimal_defaults = [
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transmitter',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
                'system_type':'',
                'interface_version':'',
                'addr_ton':1,
                'addr_npi':1,
                'address_range':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transmitter_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_receiver',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
                'system_type':'',
                'interface_version':'',
                'addr_ton':1,
                'addr_npi':1,
                'address_range':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_receiver_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transceiver',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
                'system_type':'',
                'interface_version':'',
                'addr_ton':1,
                'addr_npi':1,
                'address_range':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transceiver_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'outbind',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'unbind',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'unbind_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'generic_nack',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'testing 123',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':0,
                # 'short_message' can be of zero length
            },
        },
    },
#]
#breaker = [
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm_resp',
            'command_status': 'ESME_RSYSERR',
            'sequence_number': 0,
        },
        # submit_sm_resp can have no body for failures
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_multi',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'number_of_dests':0,
                'dest_address':[
                    {
                        'dest_flag':1,
                        'dest_addr_ton':1,
                        'dest_addr_npi':1,
                        'destination_addr':'the address'
                    },
                    {
                        'dest_flag':2,
                        'dl_name':'the list',
                    },
                    {
                        'dest_flag':2,
                        'dl_name':'the other list',
                    },
                    #{}
                    ],
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'testing 123',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_multi_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'no_unsuccess':5,
                'unsuccess_sme':[
                    {
                        'dest_addr_ton':1,
                        'dest_addr_npi':1,
                        'destination_addr':'',
                        'error_status_code':0,
                    },
                    {
                        'dest_addr_ton':3,
                        'dest_addr_npi':1,
                        'destination_addr':'555',
                        'error_status_code':0,
                    },
                ],
            },
        },
    },
#]
#breaker = [
    {
        'header': {
            'command_length': 0,
            'command_id': 'deliver_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'deliver_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'data_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'registered_delivery':0,
                'data_coding':0,
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'data_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'query_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'query_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'final_date':'',
                'message_state':0,
                'error_code':0,
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'cancel_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'message_id':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'cancel_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'replace_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'is this an = sign?',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'replace_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'enquire_link',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'enquire_link_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'alert_notification',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'source_addr_ton':'international',
                'source_addr_npi':1,
                'source_addr':'',
                'esme_addr_ton':9,
                'esme_addr_npi':'',
                'esme_addr':'',
            },
        },
    },
]

for m in minimal_defaults:
    print stars,
    print m['header']['command_id']
    print json.dumps(
            unpack_pdu(pack_pdu(m)),
            indent=4,
            sort_keys=True)


test_submit = {
    'header': {
        'command_length': 0,
        'command_id': 'submit_sm',
        'command_status': 'ESME_ROK',
        'sequence_number': 0,
    },
    'body': {
        'mandatory_parameters': {
            'service_type':'',
            'source_addr_ton':'international',
            'source_addr_npi':1,
            'source_addr':'',
            'dest_addr_ton':9,
            'dest_addr_npi':'',
            'destination_addr':'',
            'esm_class':0,
            'protocol_id':0,
            'priority_flag':0,
            'schedule_delivery_time':'',
            'validity_period':'',
            'registered_delivery':0,
            'replace_if_present_flag':0,
            'data_coding':0,
            'sm_default_msg_id':0,
            'sm_length':1,
            'short_message':'',
        },
    },
}


#start = datetime.now()
#for x in range(1000000):
    #x += 1
    #test_submit['header']['sequence_number'] = x
    #sm = 'testing: x = '+str(x)+''
    ##print stars, repr(sm)
    #test_submit['body']['mandatory_parameters']['short_message'] = sm
    #u = unpack_pdu(pack_pdu(test_submit))
    ##print stars, json.dumps(u, indent=4, sort_keys=True)
#print stars, x, ':', datetime.now() - start


print '\n\n======='
quit()
class PythonSmppTestCase(TestCase):

    def setUp(self):
        # Sample dictionary used for packing & unpacking
        self.dictionary = {
            'header': {
                'command_length': 16,
                'command_id': 'bind_transmitter',
                'command_status': 'ESME_ROK',
                'sequence_number': 0
            },
            'body': {
                'mandatory_parameters': {
                    'system_id':'test_system',
                    'password':'abc123',
                    'system_type':'',
                    'interface_version':'',
                    'addr_ton':1,
                    'addr_npi':1,
                    'address_range':'',
                },
                'optional_parameters': [
                    {
                        'tag':'payload_type',
                        'value':0
                    }
                ]
            }
        }

    def tearDown(self):
        pass

    def test_pretty_dump_1(self):
        """Read the hex data, clean it and display the JSON"""
        x = '''
            0000003C # command_length
            00000004 # command_id
            00000000 # command_status
            00000005 # sequence_number
            00
            02
            08
            35353500
            01
            01
            35353535353535353500
            00
            00
            00
            00
            00
            00
            00
            00
            00
            0F
            48656C6C6F2077696B697065646961
            00000000
            001d00026566
        '''

        self.assertEquals(unpack(x), {
            "body": {
                "mandatory_parameters": {
                    "data_coding": 0,
                    "dest_addr_npi": "ISDN",
                    "dest_addr_ton": "international",
                    "destination_addr": "555555555",
                    "esm_class": 0,
                    "priority_flag": 0,
                    "protocol_id": 0,
                    "registered_delivery": 0,
                    "replace_if_present_flag": 0,
                    "schedule_delivery_time": "",
                    "service_type": "",
                    "short_message": "Hello wikipedia",
                    "sm_default_msg_id": 0,
                    "sm_length": 15,
                    "source_addr": "555",
                    "source_addr_npi": "national",
                    "source_addr_ton": "national",
                    "validity_period": ""
                },
                "optional_parameters": [
                    {
                        "length": 0,
                        "tag": "0000",
                        "value": None
                    },
                    {
                        "length": 2,
                        "tag": "additional_status_info_text",
                        "value": "ef"
                    }
                ]
            },
            "header": {
                "command_id": "submit_sm",
                "command_length": 60,
                "command_status": "ESME_ROK",
                "sequence_number": 5
            }
        })

    def test_pretty_dump_2(self):
        """Read the hex data, clean it and display the JSON"""
        x = '''
            00000000 # command_length
            00000021 # command_id
            00000000 # command_status
            00000000 # sequence_number
            00
            00
            00
            00
            02
            01 01 01 6500
            02 6600
            00
            00
            00
            00
            00
            00
            00
            00
            00
            00
            0005 0002 0000
            0000 0004 00000000
        '''
        self.assertEquals(unpack(x), {
            "body": {
                "mandatory_parameters": {
                    "priority_flag": 0,
                    "number_of_dests": 2,
                    "protocol_id": 0,
                    "dest_address": [{
                        "dest_flag": 1,
                        "dest_addr_npi": "ISDN",
                        "dest_addr_ton": "international",
                        "destination_addr": "e"
                    },
                    {
                        "dest_flag": 2,
                        "dl_name": "f"
                    }],
                    "replace_if_present_flag": 0,
                    "registered_delivery": 0,
                    "source_addr_npi": "unknown",
                    "schedule_delivery_time": "",
                    "sm_default_msg_id": 0,
                    "sm_length": 0,
                    "esm_class": 0,
                    "data_coding": 0,
                    "service_type": "",
                    "source_addr": "",
                    "source_addr_ton": "unknown",
                    "validity_period": "",
                    "short_message": ""
                },
                "optional_parameters": [{
                    "length": 2,
                    "tag": "dest_addr_subunit",
                    "value": 0
                },
                {
                    "length": 4,
                    "tag": "0000",
                    "value": "00000000"
                }]
            },
            "header": {
                "command_status": "ESME_ROK",
                "command_length": 0,
                "sequence_number": 0,
                "command_id": "submit_multi"
            }
        })

    def test_pretty_dump_3(self):
        """Read the hex data, clean it and display the JSON"""
        x = '''
            00000000
            80000021
            00000000
            00000000
            00
            02
            01016565650000000000
            01016666660000000000
        '''
        self.assertEquals(unpack(x), {
            "body": {
                "mandatory_parameters": {
                    "message_id": "",
                    "no_unsuccess": 2,
                    "unsuccess_sme": [{
                        "error_status_code": 0,
                        "dest_addr_npi": "ISDN",
                        "dest_addr_ton": "international",
                        "destination_addr": "eee"
                    },
                    {
                        "error_status_code": 0,
                        "dest_addr_npi": "ISDN",
                        "dest_addr_ton": "international",
                        "destination_addr": "fff"
                    }]
                }
            },
            "header": {
                "command_status": "ESME_ROK",
                "command_length": 0,
                "sequence_number": 0,
                "command_id": "submit_multi_resp"
            }
        })

    def test_packing_of_dictionary(self):
        """
        It should take a dictionary, pack and unpack it and dump
        it as JSON correctly.
        """
        dictionary = self.dictionary.copy()
        print json.dumps(unpack_pdu(pack_pdu(dictionary)), indent=4, sort_keys=True)

    def test_packing_of_100000_sequence(self):
        """Test time to pack & unpack 10000 dictionaries"""
        dictionary = self.dictionary.copy()
        start = datetime.now()
        for x in range(100000):
            dictionary['header']['sequence_number'] = x
            u = unpack_pdu(pack_pdu(dictionary))
            print x+1, ':', datetime.now() - start



