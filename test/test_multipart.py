
import unittest, collections

from smpp.pdu_builder import *
from smpp.pdu_inspector import *


class MultipartTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_formats(self):
        """
        Testing TLV vs SAR vs CSM vs CSM16
        """
        tlv = DeliverSM(1, short_message='the first message part')
        tlv.set_sar_msg_ref_num(65017)
        tlv.set_sar_total_segments(2)
        tlv.set_sar_segment_seqnum(1)
        sar = DeliverSM(1, short_message='\x00\x03\xff\x02\x01the first message part')
        csm = DeliverSM(1, short_message='\x05\x00\x03\xff\x02\x01the first message part')
        csm16 = DeliverSM(1, short_message='\x06\x00\x04\xff\xff\x02\x01the first message part')
        non_multi = DeliverSM(1, short_message='whatever')
        none_short_message = DeliverSM(1, short_message=None)

        self.assertEquals(detect_multipart(unpack_pdu(tlv.get_bin()))['multipart_type'], 'TLV')
        self.assertEquals(detect_multipart(unpack_pdu(sar.get_bin()))['multipart_type'], 'SAR')
        self.assertEquals(detect_multipart(unpack_pdu(csm.get_bin()))['multipart_type'], 'CSM')
        self.assertEquals(detect_multipart(unpack_pdu(csm16.get_bin()))['multipart_type'], 'CSM16')
        self.assertEquals(detect_multipart(unpack_pdu(none_short_message.get_bin())), None)


    def test_ordering(self):
        """
        Out of order pieces must be re-assembled in-order
        """
        sar_1 = DeliverSM(1, short_message='\x00\x03\xff\x04\x01There she was just a')
        sar_2 = DeliverSM(1, short_message='\x00\x03\xff\x04\x02 walking down the street,')
        sar_3 = DeliverSM(1, short_message='\x00\x03\xff\x04\x03 singing doo wa diddy')
        sar_4 = DeliverSM(1, short_message='\x00\x03\xff\x04\x04 diddy dum diddy do')

        multi = MultipartMessage()
        multi.add_pdu(sar_3.get_obj())
        multi.add_pdu(sar_4.get_obj())
        multi.add_pdu(sar_2.get_obj())
        multi.add_pdu(sar_1.get_obj())
        self.assertEquals(multi.get_completed()['message'],
                'There she was just a walking down the street, singing doo wa diddy diddy dum diddy do')


    def test_real_csm_data(self):
        """
        Test with real-world data which uses the CSM format.
        """

        asif_1 = {'body': {'mandatory_parameters': {'priority_flag': 0, 'source_addr': '261xxx720371', 'protocol_id': 0, 'replace_if_present_flag': 0, 'registered_delivery': 0, 'dest_addr_ton': 'international', 'source_addr_npi': 'ISDN', 'schedule_delivery_time': '', 'dest_addr_npi': 'ISDN', 'sm_length': 159, 'esm_class': 64, 'data_coding': 0, 'service_type': '', 'source_addr_ton': 'international', 'sm_default_msg_id': 0, 'validity_period': '', 'destination_addr': '261xxx782943', 'short_message': '\x05\x00\x03\x1a\x02\x01I try to send sms testing vumi sms sms sms sms msm sms sms sms sms sms sms sms sms sms ssms sms smS sms sms sms sms sms sms sms sns sns sms sms sms sms s'}, 'optional_parameters': [{'length': 2, 'tag': 'user_message_reference', 'value': 91}, {'length': 16, 'tag': 'dest_subaddress', 'value': 'a0000410020601030303070802090403'}]}, 'header': {'command_status': 'ESME_ROK', 'command_length': 242, 'sequence_number': 23, 'command_id': 'deliver_sm'}}

        asif_2 = {'body': {'mandatory_parameters': {'priority_flag': 1, 'source_addr': '261xxx720371', 'protocol_id': 0, 'replace_if_present_flag': 0, 'registered_delivery': 0, 'dest_addr_ton': 'international', 'source_addr_npi': 'ISDN', 'schedule_delivery_time': '', 'dest_addr_npi': 'ISDN', 'sm_length': 78, 'esm_class': 64, 'data_coding': 0, 'service_type': '', 'source_addr_ton': 'international', 'sm_default_msg_id': 0, 'validity_period': '', 'destination_addr': '261xxx782943', 'short_message': '\x05\x00\x03\x1a\x02\x02mns again again again again again again again again sms sms sms sms sms '}, 'optional_parameters': [{'length': 2, 'tag': 'user_message_reference', 'value': 92}, {'length': 16, 'tag': 'dest_subaddress', 'value': 'a0000410020601030303070802090403'}]}, 'header': {'command_status': 'ESME_ROK', 'command_length': 161, 'sequence_number': 24, 'command_id': 'deliver_sm'}}

        multi = MultipartMessage()
        self.assertEquals(multi.get_partial(), {'to_msisdn': '', 'from_msisdn': '', 'message': ''})
        self.assertEquals(multi.get_completed(), None)
        self.assertEquals(multi.get_key(), None)
        multi.add_pdu(asif_2)
        self.assertEquals(multi.get_partial(), {'to_msisdn': '261xxx782943', 'from_msisdn': '261xxx720371', 'message': 'mns again again again again again again again again sms sms sms sms sms '})
        self.assertEquals(multi.get_completed(), None)
        self.assertEquals(multi.get_key(), '261xxx720371_261xxx782943_26_2')
        multi.add_pdu(asif_1)
        self.assertEquals(multi.get_completed()['message'], 'I try to send sms testing vumi sms sms sms sms msm sms sms sms sms sms sms sms sms sms ssms sms smS sms sms sms sms sms sms sms sns sns sms sms sms sms smns again again again again again again again again sms sms sms sms sms ')
        self.assertEquals(multi.get_key(), '261xxx720371_261xxx782943_26_2')

