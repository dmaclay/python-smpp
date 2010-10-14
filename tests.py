from datetime import datetime

from smpp.esme import *


def prettydump(pdu_hex):
    return json.dumps(unpack_pdu(binascii.a2b_hex(hexclean(x))), indent=4, sort_keys=True)

def hexclean(dirtyhex):
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
                'short_message':'', # TODO actual msg
            },
        },
    },
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
        # submit_sm can have no body on failure
    },
    # TODO submit_multi
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
                'no_unsuccess':0,
                #'unsuccess_sme':'', TODO
            },
        },
    },
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
                'short_message':'', # TODO actual msg
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
                'short_message':'', # TODO actual msg
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
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'esme_addr_ton':1,
                'esme_addr_npi':1,
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


#start = datetime.now()
#for x in range(100000):
    #b['header']['sequence_number'] = x
    #u = unpack_pdu(pack_pdu(b))
#print stars, x+1, ':', datetime.now() - start



