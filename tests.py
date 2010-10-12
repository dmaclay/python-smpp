
from smpp.esme import *

#esme = ESME()
#esme.connect_SMSC()

#print str(binascii.a2b_hex(re.sub(' ','','00 00 00 3C 00 00 00 04 00 00 00 00 00 00 00 05 00 02 08 35 35 35 00 01 01 35 35 35 35 35 35 35 35 35 00 00 00 00 00 00 00 00 00 00 0F 48 65 6C 6C 6F 20 77 69 6B 69 70 65 64 69 61')))




print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

test_bin = binascii.a2b_hex(re.sub(' ','','00 00 00 3C 00 00 00 04 00 00 00 00 00 00 00 05 00 02 08 35 35 35 00 01 01 35 35 35 35 35 35 35 35 35 00 00 00 00 00 00 00 00 00 00 0F 48 65 6C 6C 6F 20 77 69 6B 69 70 65 64 69 61 00000000 00000000'))
unpack_pdu(test_bin)

test_bin = binascii.a2b_hex(re.sub(' ','','00000000 00000021 00000000 00000000 00 00 00 00 02 0101016500 026600 00 00 00 00 00 00 00 00 00 00 0000000000000000000000000000000000000000000000000000000000 00000000 00000000 0000'))
print unpack_pdu(test_bin)

test_bin = binascii.a2b_hex(re.sub(' ','','00000000 80000021 00000000 00000000 00 02 01016565650000000000 01016666660000000000'))
print unpack_pdu(test_bin)

pack_pdu('generic_nack','ESME_ROK',1,'00112233445566778899')
pack_pdu()
print unpack_pdu(pack_pdu())


j = {
    'header': {
        'command_length': 16,
        'command_id': 'bind_transmitter',
        'command_status': 'ESME_ROK',
        'sequence_number': 0
    },
    'body': {
        'optional_parameters': [
            {
                'tag':'payload_type',
                'value':0
            }
        ]
    }
}

json_to_pdu(j)
