
from smpp.esme import *

#esme = ESME()
#esme.connect_SMSC()

#print str(binascii.a2b_hex(re.sub(' ','','00 00 00 3C 00 00 00 04 00 00 00 00 00 00 00 05 00 02 08 35 35 35 00 01 01 35 35 35 35 35 35 35 35 35 00 00 00 00 00 00 00 00 00 00 0F 48 65 6C 6C 6F 20 77 69 6B 69 70 65 64 69 61')))




print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

test_bin = binascii.a2b_hex(re.sub(' ','','00 00 00 3C 00 00 00 04 00 00 00 00 00 00 00 05 00 02 08 35 35 35 00 01 01 35 35 35 35 35 35 35 35 35 00 00 00 00 00 00 00 00 00 00 0F 48 65 6C 6C 6F 20 77 69 6B 69 70 65 64 69 61'))
unpack_pdu(test_bin)


pack_pdu('generic_nack','ESME_ROK',1,'00112233445566778899')
pack_pdu()
unpack_pdu(pack_pdu())


j = {'status': 'ESME_ROK', 'body': {'optional_parameters':[{'tag':'payload_type', 'value':0}]}, 'length': 16, 'sequence': 0, 'command': 'bind_transmitter'}

json_to_pdu(j)
