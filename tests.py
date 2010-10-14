from unittest import TestCase
from datetime import datetime
from smpp.esme import *
from smpp import pdu
import collections

def unpack(pdu_hex):
    """Unpack PDU and return it as a dictionary"""
    return unpack_pdu(binascii.a2b_hex(hexclean(pdu_hex)))

def prettydump(pdu_hex):
    """Unpack PDU and dump it as a JSON formatted string"""
    return json.dumps(unpack_pdu(pdu_hex), indent=4, sort_keys=True)

def hexclean(dirtyhex):
    """Remove whitespace, comments & newlines from hex string"""
    return re.sub(r'\s','',re.sub(r'#.*\n','\n',dirtyhex))

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
                        'value':0,
                        'length':1
                    }
                ]
            }
        }
    
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
                        dictionary1, dictionary2))
    
    
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
        
        self.assertDictEquals(unpack(x), {
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
        self.assertDictEquals(unpack(x), {
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
        self.assertDictEquals(unpack(x), {
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

    def test_packing_and_unpacking_of_dictionary(self):
        """
        It should take a dictionary, pack and unpack it and dump
        it as JSON correctly.
        """
        dictionary = self.dictionary.copy()
        self.assertDictEquals(
            hex_to_named(dictionary),
            unpack_pdu(pack_pdu(dictionary))
        )
    
    def test_packing_of_100000_sequence(self):
        """Test time to pack & unpack 10000 dictionaries"""
        dictionary = self.dictionary.copy()
        start = datetime.now()
        for x in range(100000):
            dictionary['header']['sequence_number'] = x
            u = unpack_pdu(pack_pdu(dictionary))
        print x+1, ':', datetime.now() - start
    


