
from pdu import *

class PDU(object):
    def __init__(self,
            command_id,
            command_status,
            sequence_number,
            **kwargs):
        super(PDU, self).__init__()
        self.obj = {}
        self.obj['header'] = {}
        self.obj['header']['command_length'] = 0
        self.obj['header']['command_id'] = command_id
        self.obj['header']['command_status'] = command_status
        self.obj['header']['sequence_number'] = sequence_number


    def __add_optional_parameter(self, tag, value):
        if self.obj.get('body') == None:
            self.obj['body'] = {}
        if self.obj['body'].get('optional_parameters') == None:
            self.obj['body']['optional_parameters'] = []
        self.obj['body']['optional_parameters'].append({
            'tag':tag,
            'length':0,
            'value':value,
            })

    def set_sar_msg_ref_num(self, value):
        self.__add_optional_parameter('sar_msg_ref_num', value)

    def set_sar_segment_seqnum(self, value):
        self.__add_optional_parameter('sar_segment_seqnum', value)

    def set_sar_total_segments(self, value):
        self.__add_optional_parameter('sar_total_segments', value)


    def get_obj(self):
        return self.obj


    def get_hex(self):
        return encode_pdu(self.obj)


    def get_bin(self):
        return pack_pdu(self.obj)


class Bind(PDU):
    def __init__(self,
            command_id,
            sequence_number,
            system_id = '',
            password = '',
            system_type = '',
            interface_version = '34',
            addr_ton = 0,
            addr_npi = 0,
            address_range = '',
            **kwargs):
        super(Bind, self).__init__(
                command_id,
                'ESME_ROK',
                sequence_number,
                )
        self.obj['body'] = {}
        self.obj['body']['mandatory_parameters'] = {}
        self.obj['body']['mandatory_parameters']['system_id'] = system_id
        self.obj['body']['mandatory_parameters']['password'] = password
        self.obj['body']['mandatory_parameters']['system_type'] = system_type
        self.obj['body']['mandatory_parameters']['interface_version'] = interface_version
        self.obj['body']['mandatory_parameters']['addr_ton'] = addr_ton
        self.obj['body']['mandatory_parameters']['addr_npi'] = addr_npi
        self.obj['body']['mandatory_parameters']['address_range'] = address_range


class BindTransmitter(Bind):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(BindTransmitter, self).__init__('bind_transmitter', sequence_number, **kwargs)


class BindReceiver(Bind):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(BindReceiver, self).__init__('bind_receiver', sequence_number, **kwargs)


class BindTransceiver(Bind):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(BindTransceiver, self).__init__('bind_transceiver', sequence_number, **kwargs)


class BindResp(PDU):
    def __init__(self,
            command_id,
            command_status,
            sequence_number,
            system_id = '',
            **kwargs):
        super(BindResp, self).__init__(
                command_id,
                command_status,
                sequence_number,
                )
        self.obj['body'] = {}
        self.obj['body']['mandatory_parameters'] = {}
        self.obj['body']['mandatory_parameters']['system_id'] = system_id


class BindTransmitterResp(BindResp):
    def __init__(self,
            sequence_number,
            command_status="ESME_ROK",
            **kwargs):
        super(BindTransmitterResp, self).__init__('bind_transmitter_resp', command_status, sequence_number, **kwargs)


class BindReceiverResp(BindResp):
    def __init__(self,
            sequence_number,
            command_status="ESME_ROK",
            **kwargs):
        super(BindReceiverResp, self).__init__('bind_receiver_resp', command_status, sequence_number, **kwargs)


class BindTransceiverResp(BindResp):
    def __init__(self,
            sequence_number,
            command_status="ESME_ROK",
            **kwargs):
        super(BindTransceiverResp, self).__init__('bind_transceiver_resp', command_status, sequence_number, **kwargs)


class Unbind(PDU):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(Unbind, self).__init__('unbind', 'ESME_ROK', sequence_number, **kwargs)


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
            **kwargs):
        super(SM1, self).__init__(
                command_id,
                'ESME_ROK',
                sequence_number,
                )
        self.obj['body'] = {}
        self.obj['body']['mandatory_parameters'] = {}
        self.obj['body']['mandatory_parameters']['service_type'] = service_type
        self.obj['body']['mandatory_parameters']['source_addr_ton'] = source_addr_ton
        self.obj['body']['mandatory_parameters']['source_addr_npi'] = source_addr_npi
        self.obj['body']['mandatory_parameters']['source_addr'] = source_addr
        self.obj['body']['mandatory_parameters']['esm_class'] = esm_class
        self.obj['body']['mandatory_parameters']['protocol_id'] = protocol_id
        self.obj['body']['mandatory_parameters']['priority_flag'] = priority_flag
        self.obj['body']['mandatory_parameters']['schedule_delivery_time'] = schedule_delivery_time
        self.obj['body']['mandatory_parameters']['validity_period'] = validity_period
        self.obj['body']['mandatory_parameters']['registered_delivery'] = registered_delivery
        self.obj['body']['mandatory_parameters']['replace_if_present_flag'] = replace_if_present_flag
        self.obj['body']['mandatory_parameters']['data_coding'] = data_coding
        self.obj['body']['mandatory_parameters']['sm_default_msg_id'] = sm_default_msg_id
        self.obj['body']['mandatory_parameters']['sm_length'] = sm_length
        self.obj['body']['mandatory_parameters']['short_message'] = short_message


    def add_message_payload(self, value):
        self.obj['body']['mandatory_parameters']['sm_length'] = 0
        self.obj['body']['mandatory_parameters']['short_message'] = None
        self._PDU__add_optional_parameter('message_payload', value)


class SubmitMulti(SM1):
    def __init__(self,
            sequence_number,
            number_of_dests = 0,
            dest_address = [],
            **kwargs):
        super(SubmitMulti, self).__init__('submit_multi', sequence_number, **kwargs)
        mandatory_parameters = self.obj['body']['mandatory_parameters']
        mandatory_parameters['number_of_dests'] = number_of_dests
        mandatory_parameters['dest_address'] = [] + dest_address

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
    def __init__(self,
            sequence_number,
            **kwargs):
        super(SubmitSM, self).__init__('submit_sm', sequence_number, **kwargs)


class SubmitSMResp(PDU):
    def __init__(self,
            sequence_number,
            message_id,
            command_status = 'ESME_ROK',
            **kwargs):
        super(SubmitSMResp, self).__init__(
                'submit_sm_resp',
                command_status,
                sequence_number,
                **kwargs)
        self.obj['body'] = {}
        self.obj['body']['mandatory_parameters'] = {}
        self.obj['body']['mandatory_parameters']['message_id'] = message_id


class DeliverSM(SM2):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(DeliverSM, self).__init__('deliver_sm',sequence_number,  **kwargs)


class DeliverSMResp(PDU):
    def __init__(self,
            sequence_number,
            message_id = '',
            command_status = 'ESME_ROK',
            **kwargs):
        super(DeliverSMResp, self).__init__(
                'deliver_sm_resp',
                command_status,
                sequence_number,
                **kwargs)
        self.obj['body'] = {}
        self.obj['body']['mandatory_parameters'] = {}
        self.obj['body']['mandatory_parameters']['message_id'] = ''


class EnquireLink(PDU):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(EnquireLink, self).__init__(
                'enquire_link',
                'ESME_ROK',
                sequence_number,
                **kwargs)


class EnquireLinkResp(PDU):
    def __init__(self,
            sequence_number,
            **kwargs):
        super(EnquireLinkResp, self).__init__(
                'enquire_link_resp',
                'ESME_ROK',
                sequence_number,
                **kwargs)


class QuerySM(PDU):
    def __init__(self,
            sequence_number,
            message_id,
            source_addr = '',
            source_addr_ton = 0,
            source_addr_npi = 0,
            **kwargs):
        super(QuerySM, self).__init__(
                'query_sm',
                'ESME_ROK',
                sequence_number,
                **kwargs)
        self.obj['body'] = {}
        self.obj['body']['mandatory_parameters'] = {}
        self.obj['body']['mandatory_parameters']['message_id'] = message_id
        self.obj['body']['mandatory_parameters']['source_addr'] = source_addr
        self.obj['body']['mandatory_parameters']['source_addr_ton'] = source_addr_ton
        self.obj['body']['mandatory_parameters']['source_addr_npi'] = source_addr_npi


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
