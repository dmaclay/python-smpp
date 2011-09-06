# -*- coding: utf-8 -*-
import unittest, collections
from datetime import datetime, timedelta

from smpp.esme import *
from smpp.clickatell import *
from smpp import pdu
import credentials_test
try:import credentials_priv
except:pass

from test.pdu import pdu_objects
from test import pdu_asserts
from test.pdu_hex import pdu_hex_strings
from test import pdu_hex_asserts


def unpack_hex(pdu_hex):
    """Unpack PDU hex string and return it as a dictionary"""
    return unpack_pdu(binascii.a2b_hex(hexclean(pdu_hex)))

def hexclean(dirtyhex):
    """Remove whitespace, comments & newlines from hex string"""
    return re.sub(r'\s','',re.sub(r'#.*\n','\n',dirtyhex))

def prettydump(pdu_obj):
    """Unpack PDU dictionary and dump it as a JSON formatted string"""
    return json.dumps(pdu_obj, indent=4, sort_keys=True)

def hex_to_named(dictionary):
    """
    Recursive function to convert values in test dictionaries to
    their named counterparts that unpack_pdu returns
    """
    clone = dictionary.copy()
    for key, value in clone.items():
        if isinstance(value, collections.Mapping):
            clone[key] = hex_to_named(value)
        else:
            lookup_table = pdu.maps.get('%s_by_hex' % key)
            if lookup_table:
                # overwrite with mapped value or keep using
                # default if the dictionary key doesn't exist
                clone[key] = lookup_table.get("%.2d" % value, value)
    return clone

def create_pdu_asserts():
    pdu_index = 0
    for pdu in pdu_objects:
        pdu_index += 1
        pstr  = "\n########################################\n"
        pstr += "pdu_json_"
        pstr += ('%010d' % pdu_index)
        pstr += " = '''"
        pstr += prettydump(unpack_pdu(pack_pdu(pdu)))
        pstr += "'''"
        print pstr


def create_pdu_hex_asserts():
    pdu_index = 0
    for pdu_hex in pdu_hex_strings:
        pdu_index += 1
        pstr  = "\n########################################\n"
        pstr += "pdu_json_"
        pstr += ('%010d' % pdu_index)
        pstr += " = '''"
        pstr += prettydump(unpack_hex(pdu_hex))
        pstr += "'''"
        print pstr


## :w|!python % > test/pdu_asserts.py
#create_pdu_asserts()
#quit()

## :w|!python % > test/pdu_hex_asserts.py
#create_pdu_hex_asserts()
#quit()


class PduTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assertDictEquals(self, dictionary1, dictionary2, depth=[]):
        """
        Recursive dictionary comparison, will fail if any keys and values
        in the two dictionaries don't match. Displays the key chain / depth 
        and which parts of the two dictionaries didn't match.
        """
        d1_keys = dictionary1.keys()
        d1_keys.sort()
        
        d2_keys = dictionary2.keys()
        d2_keys.sort()
        
        self.failUnlessEqual(d1_keys, d2_keys, 
            "Dictionary keys do not match, %s vs %s" % (
                d1_keys, d2_keys))
        for key, value in dictionary1.items():
            if isinstance(value, collections.Mapping):
                # go recursive
                depth.append(key)
                self.assertDictEquals(value, dictionary2[key], depth)
            else:
                self.failUnlessEqual(value, dictionary2[key], 
                    "Dictionary values do not match for key '%s' " \
                    "(%s vs %s) at depth: %s.\nDictionary 1: %s\n" \
                    "Dictionary 2: %s\n" % (
                        key, value, dictionary2[key], ".".join(depth),
                        prettydump(dictionary1), prettydump(dictionary2)))
    
    def test_pack_unpack_pdu_objects(self):
        print ''
        """
        Take a dictionary, pack and unpack it and dump it as JSON correctly
        """
        pdu_index = 0
        for pdu in pdu_objects:
            pdu_index += 1
            padded_index = '%010d' % pdu_index
            print '...', padded_index
            self.assertEquals(
                    re.sub('\n *','',
                        prettydump(unpack_pdu(pack_pdu(pdu)))),
                    re.sub('\n *','',
                        eval('pdu_asserts.pdu_json_'+padded_index)))


    def test_pack_unpack_pdu_hex_strings(self):
        print ''
        """
        Read the hex data, clean it, and unpack it to JSON correctly
        """
        pdu_index = 0
        for pdu_hex in pdu_hex_strings:
            pdu_index += 1
            padded_index = '%010d' % pdu_index
            print '...', padded_index
            self.assertEquals(
                    re.sub('\n *','',
                        prettydump(unpack_hex(pdu_hex))),
                    re.sub('\n *','',
                        eval('pdu_hex_asserts.pdu_json_'+padded_index)))


    def test_pack_unpack_performance(self):
        print ''
        """
        Pack & unpack 500 submit_sm PDUs in under 1 second
        """
        submit_sm = {
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
                    'short_message':'',
                },
            },
        }
        start = datetime.now()
        for x in range(500):
            x += 1
            submit_sm['header']['sequence_number'] = x
            sm = 'testing: x = '+str(x)+''
            submit_sm['body']['mandatory_parameters']['short_message'] = sm
            u = unpack_pdu(pack_pdu(submit_sm))
        delta = datetime.now() - start
        print '... 500 pack & unpacks in:', delta
        self.assertTrue(delta < timedelta(seconds=1))

    def test_pack_unpack_of_unicode(self):
        """
        SMPP module should be able to pack & unpack unicode characters
        without a problem
        """
        submit_sm = {
            'header': {
                'command_length': 67,
                'command_id': 'submit_sm',
                'command_status': 'ESME_ROK',
                'sequence_number': 0,
            },
            'body': {
                'mandatory_parameters': {
                    'service_type':'',
                    'source_addr_ton':'international',
                    'source_addr_npi':'unknown',
                    'source_addr':'',
                    'dest_addr_ton':'international',
                    'dest_addr_npi':'unknown',
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
                    'sm_length':34,
                    'short_message':u'Vumi says: أبن الشرموطة'.encode('utf-8'),
                },
            },
        }
        self.assertDictEquals(
            hex_to_named(submit_sm),
            unpack_pdu(pack_pdu(submit_sm))
        )

    def test_pack_unpack_of_ascii_and_unicode_8_16_32(self):
        """
        SMPP module should be able to pack & unpack unicode characters
        without a problem
        """
        submit_sm = {
            'header': {
                'command_length': 65,
                'command_id': 'submit_sm',
                'command_status': 'ESME_ROK',
                'sequence_number': 0,
            },
            'body': {
                'mandatory_parameters': {
                    'service_type':'',
                    'source_addr_ton':'international',
                    'source_addr_npi':'unknown',
                    'source_addr':'',
                    'dest_addr_ton':'international',
                    'dest_addr_npi':'unknown',
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
                    'sm_length':32,
                    'short_message':u'a \xf0\x20\u0373\u0020\u0433\u0020\u0533\u0020\u05f3\u0020\u0633\u0020\u13a3\u0020\u16a3 \U0001f090'.encode('utf-8'),
                },
            },
        }
        self.assertDictEquals(
            hex_to_named(submit_sm),
            unpack_pdu(pack_pdu(submit_sm))
        )

class PduBuilderTestCase(unittest.TestCase):

    def test_true(self):
        print ''
        self.assertTrue(True)



if __name__ == '__main__':
    print '\n##########################################################\n'
    #deliv_sm_resp = DeliverSMResp(23)
    #print deliv_sm_resp.get_obj()
    #print deliv_sm_resp.get_hex()
    #enq_lnk = EnquireLink(7)
    #print enq_lnk.get_obj()
    #print enq_lnk.get_hex()
    #sub_sm = SubmitSM(5, short_message='testing testing')
    #print sub_sm.get_obj()
    #print sub_sm.get_hex()
    #sub_sm.add_message_payload('01020304')
    #print sub_sm.get_obj()
    #print sub_sm.get_hex()
    #print unpack_pdu(sub_sm.get_bin())
    print '\n##########################################################\n'

    esme = ESME()
    esme.loadDefaults(clickatell_defaults)
    esme.loadDefaults(credentials_test.logica)
    print esme.defaults
    esme.bind_transmitter()
    print esme.state
    start = datetime.now()
    for x in range(1):
        esme.submit_sm(
                short_message = 'gobbledygook',
                destination_addr = '555',
                )
        print esme.state
    for x in range(1):
        esme.submit_multi(
                short_message = 'gobbledygook',
                dest_address = ['444','333'],
                )
        print esme.state
    for x in range(1):
        esme.submit_multi(
                short_message = 'gobbledygook',
                dest_address = [
                    {'dest_flag':1, 'destination_addr':'111'},
                    {'dest_flag':2, 'dl_name':'list22222'},
                    ],
                )
        print esme.state
    delta = datetime.now() - start
    esme.disconnect()
    print esme.state
    print 'excluding binding ... time to send messages =', delta


#if __name__ == '__main__':
    #unittest.main()

