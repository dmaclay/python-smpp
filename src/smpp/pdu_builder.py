
from pdu import *

class PDU(object):
    def __init__(self,
            command_id,
            command_status,
            sequence_number,
            ):
        self.obj = {}
        header = {}
        self.obj['header'] = header
        header['command_length'] = 0
        header['command_id'] = command_id
        header['command_status'] = command_status
        header['sequence_number'] = sequence_number


    def __add_optional_parameter(self, tag, value):
        optional_parameters = self.obj['body'].get('optional_parameters')
        if optional_parameters == None:
            optional_parameters = []
            self.obj['body']['optional_parameters'] = optional_parameters
        optional_parameters.append({
            'tag':tag,
            'length':0,
            'value':value,
            })


    def get_obj(self):
        return self.obj


    def get_hex(self):
        return encode_pdu(self.obj)


    def get_bin(self):
        return pack_pdu(self.obj)


class BindTransmitter(PDU):
    def __init__(self,
            sequence_number,
            system_id = '',
            password = '',
            system_type = '',
            interface_version = '',
            addr_ton = 0,
            addr_npi = 0,
            address_range = '',
            ):
        super(BindTransmitter, self).__init__(
                'bind_transmitter',
                'ESME_ROK',
                sequence_number,
                )
        body = {}
        self.obj['body'] = body
        mandatory_parameters = {}
        body['mandatory_parameters'] = mandatory_parameters
        mandatory_parameters['system_id'] = system_id
        mandatory_parameters['password'] = password
        mandatory_parameters['system_type'] = system_type
        mandatory_parameters['interface_version'] = interface_version
        mandatory_parameters['addr_ton'] = addr_ton
        mandatory_parameters['addr_npi'] = addr_npi
        mandatory_parameters['address_range'] = address_range


class Unbind(PDU):
    def __init__(self,
            sequence_number,
            ):
        super(Unbind, self).__init__(
                'unbind',
                'ESME_ROK',
                sequence_number,
                )


class SM1(PDU):
    def __init__(self,
            command_id,
            sequence_number,
            service_type = '',
            source_addr_ton = 0,
            source_addr_npi = 0,
            source_addr = '',
            esm_class = 0,
            protocol_id = 0,
            priority_flag = 0,
            schedule_delivery_time = '',
            validity_period = '',
            registered_delivery = 0,
            replace_if_present_flag = 0,
            data_coding = 0,
            sm_default_msg_id = 0,
            sm_length = 0,
            short_message = None,
            ):
        super(SM1, self).__init__(
                command_id,
                'ESME_ROK',
                sequence_number,
                )
        body = {}
        self.obj['body'] = body
        mandatory_parameters = {}
        body['mandatory_parameters'] = mandatory_parameters
        mandatory_parameters['service_type'] = service_type
        mandatory_parameters['source_addr_ton'] = source_addr_ton
        mandatory_parameters['source_addr_npi'] = source_addr_npi
        mandatory_parameters['source_addr'] = source_addr
        mandatory_parameters['esm_class'] = esm_class
        mandatory_parameters['protocol_id'] = protocol_id
        mandatory_parameters['priority_flag'] = priority_flag
        mandatory_parameters['schedule_delivery_time'] = schedule_delivery_time
        mandatory_parameters['validity_period'] = validity_period
        mandatory_parameters['registered_delivery'] = registered_delivery
        mandatory_parameters['replace_if_present_flag'] = replace_if_present_flag
        mandatory_parameters['data_coding'] = data_coding
        mandatory_parameters['sm_default_msg_id'] = sm_default_msg_id
        mandatory_parameters['sm_length'] = sm_length
        mandatory_parameters['short_message'] = short_message


    def add_message_payload(self, value):
        self.obj['body']['mandatory_parameters']['sm_length'] = 0
        self.obj['body']['mandatory_parameters']['short_message'] = None
        self._PDU__add_optional_parameter('message_payload', value)


class SubmitMulti(SM1):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(SubmitMulti, self).__init__('submit_multi', sequence_number, **kwargs)
        mandatory_parameters = self.obj['body']['mandatory_parameters']
        mandatory_parameters['number_of_dests'] = 0
        mandatory_parameters['dest_address'] = []

    def addDestinationAddress(self,
            destination_addr,
            dest_addr_ton = 0,
            dest_addr_npi = 0,
            ):
        if isinstance(destination_addr, str) and len(destination_addr) > 0:
            new_entry = {
                    'dest_flag':1,
                    'dest_addr_ton':dest_addr_ton,
                    'dest_addr_npi':dest_addr_npi,
                    'destination_addr':destination_addr,
            }
            mandatory_parameters = self.obj['body']['mandatory_parameters']
            mandatory_parameters['dest_address'].append(new_entry)
            mandatory_parameters['number_of_dests'] = len(
                    mandatory_parameters['dest_address'])
            return True
        else:
            return False

    def addDistributionList(self,
            dl_name,
            ):
        if isinstance(dl_name, str) and len(dl_name) > 0:
            new_entry = {
                    'dest_flag':2,
                    'dl_name':dl_name,
            }
            mandatory_parameters = self.obj['body']['mandatory_parameters']
            mandatory_parameters['dest_address'].append(new_entry)
            mandatory_parameters['number_of_dests'] = len(
                    mandatory_parameters['dest_address'])
            return True
        else:
            return False


class SM2(SM1):
    def __init__(self,
            command_id,
            sequence_number,
            dest_addr_ton = 0,
            dest_addr_npi = 0,
            destination_addr = '',
            **kwargs):
        super(SM2, self).__init__(command_id, sequence_number, **kwargs)
        mandatory_parameters = self.obj['body']['mandatory_parameters']
        mandatory_parameters['dest_addr_ton'] = dest_addr_ton
        mandatory_parameters['dest_addr_npi'] = dest_addr_npi
        mandatory_parameters['destination_addr'] = destination_addr


class SubmitSM(SM2):
    def __init__(self, sequence_number, **kwargs):
        super(SubmitSM, self).__init__('submit_sm', sequence_number, **kwargs)

class DeliverSM(SM2):
    def __init__(self, sequence_number, **kwargs):
        super(DeliverSM, self).__init__('deliver_sm',sequence_number,  **kwargs)


#bind = BindTransmitter(system_id='test_id', password='abc123')
#print bind.get_obj()
#print bind.get_hex()
#print bind.get_bin()
##print json.dumps(bind.get_obj(), indent=4, sort_keys=True)
##print json.dumps(decode_pdu(bind.get_hex()), indent=4, sort_keys=True)
#print json.dumps(unpack_pdu(bind.get_bin()), indent=4, sort_keys=True)

#sm = SubmitSM(short_message='testing testing')
#print json.dumps(unpack_pdu(sm.get_bin()), indent=4, sort_keys=True)
#sm.add_message_payload('616263646566676869')
#print json.dumps(unpack_pdu(sm.get_bin()), indent=4, sort_keys=True)
