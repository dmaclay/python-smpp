
from smpp.esme import *

def prettydump(pdu_hex):
    return json.dumps(unpack_pdu(binascii.a2b_hex(hexclean(x))), indent=4, sort_keys=True)

def hexclean(dirtyhex):
    return re.sub(r'\s','',re.sub(r'#.*\n','\n',dirtyhex))

lines = "\n==================================================================\n"



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
print lines, prettydump(x)


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
print lines, prettydump(x)


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
print lines, prettydump(x)




b = {
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

print '**********************************************************'
print json.dumps(unpack_pdu(pack_pdu(b)), indent=4, sort_keys=True)

print "'''''"
for x in range(10000):
    b['header']['sequence_number'] = x
    u = unpack_pdu(pack_pdu(b))
    print u['header']['sequence_number']
print "'''''"
