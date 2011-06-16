import binascii
import re
try:
    import json
except:
    import simplejson as json




maps = {} # Inserting certain referenced dicts in here means they can be declared in the same order as in the spec.


# SMPP PDU Definition - SMPP v3.4, section 4, page 45

mandatory_parameter_lists = {
    'bind_transmitter':[ # SMPP v3.4, section 4.1.1, table 4-1, page 46
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None},
        {'name':'password',                'min':1, 'max':9,   'var':True,              'type':'string',        'map':None},
        {'name':'system_type',             'min':1, 'max':13,  'var':True,              'type':'string',        'map':None},
        {'name':'interface_version',       'min':1, 'max':1,   'var':False,             'type':'hex',           'map':None},
        {'name':'addr_ton',                'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'addr_npi',                'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'address_range',           'min':1, 'max':41,  'var':True,              'type':'string',        'map':None}
    ],
    'bind_transmitter_resp':[ # SMPP v3.4, section 4.1.2, table 4-2, page 47
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None}
    ],
    'bind_receiver':[ # SMPP v3.4, section 4.1.3, table 4-3, page 48
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None},
        {'name':'password',                'min':1, 'max':9,   'var':True,              'type':'string',        'map':None},
        {'name':'system_type',             'min':1, 'max':13,  'var':True,              'type':'string',        'map':None},
        {'name':'interface_version',       'min':1, 'max':1,   'var':False,             'type':'hex',           'map':None},
        {'name':'addr_ton',                'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'addr_npi',                'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'address_range',           'min':1, 'max':41,  'var':True,              'type':'string',        'map':None}
    ],
    'bind_receiver_resp':[ # SMPP v3.4, section 4.1.4, table 4-4, page 50
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None}
    ],
    'bind_transceiver':[ # SMPP v3.4, section 4.1.5, table 4-5, page 51
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None},
        {'name':'password',                'min':1, 'max':9,   'var':True,              'type':'string',        'map':None},
        {'name':'system_type',             'min':1, 'max':13,  'var':True,              'type':'string',        'map':None},
        {'name':'interface_version',       'min':1, 'max':1,   'var':False,             'type':'hex',           'map':None},
        {'name':'addr_ton',                'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'addr_npi',                'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'address_range',           'min':1, 'max':41,  'var':True,              'type':'string',        'map':None}
    ],
    'bind_transceiver_resp':[ # SMPP v3.4, section 4.1.6, table 4-6, page 52
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None}
    ],
    'outbind':[ # SMPP v3.4, section 4.1.7.1, page 54
        {'name':'system_id',               'min':1, 'max':16,  'var':True,              'type':'string',        'map':None},
        {'name':'password',                'min':1, 'max':9,   'var':True,              'type':'string',        'map':None}
    ],
    'unbind':[ # SMPP v3.4, section 4.2.1, table 4-7, page 56
    ],
    'unbind_resp':[ # SMPP v3.4, section 4.2.2, table 4-8, page 56
    ],
    'generic_nack':[ # SMPP v3.4, section 4.3.1, table 4-9, page 57
    ],
    'submit_sm':[ # SMPP v3.4, section 4.4.1, table 4-10, page 59-61
        {'name':'service_type',            'min':1, 'max':6,   'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'dest_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'dest_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'destination_addr',        'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'esm_class',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'protocol_id',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'priority_flag',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'schedule_delivery_time',  'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'validity_period',         'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'registered_delivery',     'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'replace_if_present_flag', 'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'data_coding',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_default_msg_id',       'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_length',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'short_message',           'min':0, 'max':254, 'var':'sm_length',       'type':'xstring',       'map':None}
    ],
    'submit_sm_resp':[ # SMPP v3.4, section 4.4.2, table 4-11, page 67
        {'name':'message_id',              'min':0, 'max':65,  'var':True,              'type':'string',        'map':None}
    ],
    'submit_multi':[ # SMPP v3.4, section 4.5.1, table 4-12, page 69-71
        {'name':'service_type',            'min':1, 'max':6,   'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'number_of_dests',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'dest_address',            'min':0, 'max':0,   'var':'number_of_dests', 'type':'dest_address',  'map':None},
        {'name':'esm_class',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'protocol_id',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'priority_flag',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'schedule_delivery_time',  'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'validity_period',         'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'registered_delivery',     'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'replace_if_present_flag', 'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'data_coding',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_default_msg_id',       'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_length',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'short_message',           'min':0, 'max':254, 'var':'sm_length',       'type':'xstring',       'map':None}
    ],
    'dest_address':[ # SMPP v3.4, section 4.5.1.1, table 4-13, page 75
        {'name':'dest_flag',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None}
        # 'sme_dest_address' or 'distribution_list' goes here
    ],
    'sme_dest_address':[ # SMPP v3.4, section 4.5.1.1, table 4-14, page 75
        {'name':'dest_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'dest_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'destination_addr',        'min':1, 'max':21,  'var':True,              'type':'string',        'map':None}
    ],
    'distribution_list':[ # SMPP v3.4, section 4.5.1.2, table 4-15, page 75
        {'name':'dl_name',                 'min':1, 'max':21,  'var':True,              'type':'string',        'map':None}
    ],
    'submit_multi_resp':[ # SMPP v3.4, section 4.5.2, table 4-16, page 76
        {'name':'message_id',              'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'no_unsuccess',            'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'unsuccess_sme',           'min':0, 'max':0,   'var':'no_unsuccess',    'type':'unsuccess_sme', 'map':None}
    ],
    'unsuccess_sme':[ # SMPP v3.4, section 4.5.2.1, table 4-17, page 77
        {'name':'dest_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'dest_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'destination_addr',        'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'error_status_code',       'min':4, 'max':4,   'var':False,             'type':'integer',       'map':None}
    ],
    'deliver_sm':[ # SMPP v3.4, section 4.6.1, table 4-18, page 79-81
        {'name':'service_type',            'min':1, 'max':6,   'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'dest_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'dest_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'destination_addr',        'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'esm_class',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'protocol_id',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'priority_flag',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'schedule_delivery_time',  'min':1, 'max':1,   'var':False,             'type':'string',        'map':None},
        {'name':'validity_period',         'min':1, 'max':1,   'var':False,             'type':'string',        'map':None},
        {'name':'registered_delivery',     'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'replace_if_present_flag', 'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'data_coding',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_default_msg_id',       'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_length',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'short_message',           'min':0, 'max':254, 'var':'sm_length',       'type':'xstring',       'map':None}
    ],
    'deliver_sm_resp':[ # SMPP v3.4, section 4.6.2, table 4-19, page 85
        {'name':'message_id',              'min':1, 'max':1,   'var':False,             'type':'string',        'map':None}
    ],
    'data_sm':[ # SMPP v3.4, section 4.7.1, table 4-20, page 87-88
        {'name':'service_type',            'min':1, 'max':6,   'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'dest_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'dest_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'destination_addr',        'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'esm_class',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'registered_delivery',     'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'data_coding',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None}
    ],
    'data_sm_resp':[ # SMPP v3.4, section 4.7.2, table 4-21, page 93
        {'name':'message_id',              'min':1, 'max':65,  'var':True,              'type':'string',        'map':None}
    ],
    'query_sm':[ # SMPP v3.4, section 4.8.1, table 4-22, page 95
        {'name':'message_id',              'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':21,  'var':True,              'type':'string',        'map':None}
    ],
    'query_sm_resp':[ # SMPP v3.4, section 4.7.2, table 4-21, page 93
        {'name':'message_id',              'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'final_date',              'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'message_state',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'error_code',              'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None}
    ],
    'cancel_sm':[ # SMPP v3.4, section 4.9.1, table 4-24, page 98-99
        {'name':'service_type',            'min':1, 'max':6,   'var':True,              'type':'string',        'map':None},
        {'name':'message_id',              'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'dest_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'dest_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'destination_addr',        'min':1, 'max':21,  'var':True,              'type':'string',        'map':None}
    ],
    'cancel_sm_resp':[ # SMPP v3.4, section 4.9.2, table 4-25, page 100
    ],
    'replace_sm':[ # SMPP v3.4, section 4.10.1, table 4-26, page 102-103
        {'name':'message_id',              'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':21,  'var':True,              'type':'string',        'map':None},
        {'name':'schedule_delivery_time',  'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'validity_period',         'min':1, 'max':17,  'var':False,             'type':'string',        'map':None},
        {'name':'registered_delivery',     'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'replace_if_present_flag', 'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'data_coding',             'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_default_msg_id',       'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'sm_length',               'min':1, 'max':1,   'var':False,             'type':'integer',       'map':None},
        {'name':'short_message',           'min':0, 'max':254, 'var':'sm_length',       'type':'xstring',       'map':None}
    ],
    'replace_sm_resp':[ # SMPP v3.4, section 4.10.2, table 4-27, page 104
    ],
    'enquire_link':[ # SMPP v3.4, section 4.11.1, table 4-28, page 106
    ],
    'enquire_link_resp':[ # SMPP v3.4, section 4.11.2, table 4-29, page 106
    ],
    'alert_notification':[ # SMPP v3.4, section 4.12.1, table 4-30, page 108
        {'name':'source_addr_ton',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'source_addr_npi',         'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'source_addr',             'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
        {'name':'esme_addr_ton',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_ton'},
        {'name':'esme_addr_npi',           'min':1, 'max':1,   'var':False,             'type':'integer',       'map':'addr_npi'},
        {'name':'esme_addr',               'min':1, 'max':65,  'var':True,              'type':'string',        'map':None},
    ]
}
def mandatory_parameter_list_by_command_name(command_name):
    return mandatory_parameter_lists.get(command_name,[])


# Command IDs - SMPP v3.4, section 5.1.2.1, table 5-1, page 110-111

command_id_by_hex = {
    '80000000':{'hex':'80000000', 'name':'generic_nack'},
    '00000001':{'hex':'00000001', 'name':'bind_receiver'},
    '80000001':{'hex':'80000001', 'name':'bind_receiver_resp'},
    '00000002':{'hex':'00000002', 'name':'bind_transmitter'},
    '80000002':{'hex':'80000002', 'name':'bind_transmitter_resp'},
    '00000003':{'hex':'00000003', 'name':'query_sm'},
    '80000003':{'hex':'80000003', 'name':'query_sm_resp'},
    '00000004':{'hex':'00000004', 'name':'submit_sm'},
    '80000004':{'hex':'80000004', 'name':'submit_sm_resp'},
    '00000005':{'hex':'00000005', 'name':'deliver_sm'},
    '80000005':{'hex':'80000005', 'name':'deliver_sm_resp'},
    '00000006':{'hex':'00000006', 'name':'unbind'},
    '80000006':{'hex':'80000006', 'name':'unbind_resp'},
    '00000007':{'hex':'00000007', 'name':'replace_sm'},
    '80000007':{'hex':'80000007', 'name':'replace_sm_resp'},
    '00000008':{'hex':'00000008', 'name':'cancel_sm'},
    '80000008':{'hex':'80000008', 'name':'cancel_sm_resp'},
    '00000009':{'hex':'00000009', 'name':'bind_transceiver'},
    '80000009':{'hex':'80000009', 'name':'bind_transceiver_resp'},
    '0000000b':{'hex':'0000000b', 'name':'outbind'},
    '00000015':{'hex':'00000015', 'name':'enquire_link'},
    '80000015':{'hex':'80000015', 'name':'enquire_link_resp'},
    '00000021':{'hex':'00000021', 'name':'submit_multi'},
    '80000021':{'hex':'80000021', 'name':'submit_multi_resp'},
    '00000102':{'hex':'00000102', 'name':'alert_notification'},
    '00000103':{'hex':'00000103', 'name':'data_sm'},
    '80000103':{'hex':'80000103', 'name':'data_sm_resp'},

               # v4 codes

    '80010000':{'hex':'80010000', 'name':'generic_nack_v4'},
    '00010001':{'hex':'00010001', 'name':'bind_receiver_v4'},
    '80010001':{'hex':'80010001', 'name':'bind_receiver_resp_v4'},
    '00010002':{'hex':'00010002', 'name':'bind_transmitter_v4'},
    '80010002':{'hex':'80010002', 'name':'bind_transmitter_resp_v4'},
    '00010003':{'hex':'00010003', 'name':'query_sm_v4'},
    '80010003':{'hex':'80010003', 'name':'query_sm_resp_v4'},
    '00010004':{'hex':'00010004', 'name':'submit_sm_v4'},
    '80010004':{'hex':'80010004', 'name':'submit_sm_resp_v4'},
    '00010005':{'hex':'00010005', 'name':'deliver_sm_v4'},
    '80010005':{'hex':'80010005', 'name':'deliver_sm_resp_v4'},
    '00010006':{'hex':'00010006', 'name':'unbind_v4'},
    '80010006':{'hex':'80010006', 'name':'unbind_resp_v4'},
    '00010007':{'hex':'00010007', 'name':'replace_sm_v4'},
    '80010007':{'hex':'80010007', 'name':'replace_sm_resp_v4'},
    '00010008':{'hex':'00010008', 'name':'cancel_sm_v4'},
    '80010008':{'hex':'80010008', 'name':'cancel_sm_resp_v4'},
    '00010009':{'hex':'00010009', 'name':'delivery_receipt_v4'},
    '80010009':{'hex':'80010009', 'name':'delivery_receipt_resp_v4'},
    '0001000a':{'hex':'0001000a', 'name':'enquire_link_v4'},
    '8001000a':{'hex':'8001000a', 'name':'enquire_link_resp_v4'},
    '0001000b':{'hex':'0001000b', 'name':'outbind_v4'},
}
def command_id_name_by_hex(x):
    return command_id_by_hex.get(x,{}).get('name')


command_id_by_name = {
    'generic_nack'            :{'hex':'80000000', 'name':'generic_nack'},
    'bind_receiver'           :{'hex':'00000001', 'name':'bind_receiver'},
    'bind_receiver_resp'      :{'hex':'80000001', 'name':'bind_receiver_resp'},
    'bind_transmitter'        :{'hex':'00000002', 'name':'bind_transmitter'},
    'bind_transmitter_resp'   :{'hex':'80000002', 'name':'bind_transmitter_resp'},
    'query_sm'                :{'hex':'00000003', 'name':'query_sm'},
    'query_sm_resp'           :{'hex':'80000003', 'name':'query_sm_resp'},
    'submit_sm'               :{'hex':'00000004', 'name':'submit_sm'},
    'submit_sm_resp'          :{'hex':'80000004', 'name':'submit_sm_resp'},
    'deliver_sm'              :{'hex':'00000005', 'name':'deliver_sm'},
    'deliver_sm_resp'         :{'hex':'80000005', 'name':'deliver_sm_resp'},
    'unbind'                  :{'hex':'00000006', 'name':'unbind'},
    'unbind_resp'             :{'hex':'80000006', 'name':'unbind_resp'},
    'replace_sm'              :{'hex':'00000007', 'name':'replace_sm'},
    'replace_sm_resp'         :{'hex':'80000007', 'name':'replace_sm_resp'},
    'cancel_sm'               :{'hex':'00000008', 'name':'cancel_sm'},
    'cancel_sm_resp'          :{'hex':'80000008', 'name':'cancel_sm_resp'},
    'bind_transceiver'        :{'hex':'00000009', 'name':'bind_transceiver'},
    'bind_transceiver_resp'   :{'hex':'80000009', 'name':'bind_transceiver_resp'},
    'outbind'                 :{'hex':'0000000b', 'name':'outbind'},
    'enquire_link'            :{'hex':'00000015', 'name':'enquire_link'},
    'enquire_link_resp'       :{'hex':'80000015', 'name':'enquire_link_resp'},
    'submit_multi'            :{'hex':'00000021', 'name':'submit_multi'},
    'submit_multi_resp'       :{'hex':'80000021', 'name':'submit_multi_resp'},
    'alert_notification'      :{'hex':'00000102', 'name':'alert_notification'},
    'data_sm'                 :{'hex':'00000103', 'name':'data_sm'},
    'data_sm_resp'            :{'hex':'80000103', 'name':'data_sm_resp'},

                               # v4 codes

    'generic_nack_v4'         :{'hex':'80010000', 'name':'generic_nack_v4'},
    'bind_receiver_v4'        :{'hex':'00010001', 'name':'bind_receiver_v4'},
    'bind_receiver_resp_v4'   :{'hex':'80010001', 'name':'bind_receiver_resp_v4'},
    'bind_transmitter_v4'     :{'hex':'00010002', 'name':'bind_transmitter_v4'},
    'bind_transmitter_resp_v4':{'hex':'80010002', 'name':'bind_transmitter_resp_v4'},
    'query_sm_v4'             :{'hex':'00010003', 'name':'query_sm_v4'},
    'query_sm_resp_v4'        :{'hex':'80010003', 'name':'query_sm_resp_v4'},
    'submit_sm_v4'            :{'hex':'00010004', 'name':'submit_sm_v4'},
    'submit_sm_resp_v4'       :{'hex':'80010004', 'name':'submit_sm_resp_v4'},
    'deliver_sm_v4'           :{'hex':'00010005', 'name':'deliver_sm_v4'},
    'deliver_sm_resp_v4'      :{'hex':'80010005', 'name':'deliver_sm_resp_v4'},
    'unbind_v4'               :{'hex':'00010006', 'name':'unbind_v4'},
    'unbind_resp_v4'          :{'hex':'80010006', 'name':'unbind_resp_v4'},
    'replace_sm_v4'           :{'hex':'00010007', 'name':'replace_sm_v4'},
    'replace_sm_resp_v4'      :{'hex':'80010007', 'name':'replace_sm_resp_v4'},
    'cancel_sm_v4'            :{'hex':'00010008', 'name':'cancel_sm_v4'},
    'cancel_sm_resp_v4'       :{'hex':'80010008', 'name':'cancel_sm_resp_v4'},
    'delivery_receipt_v4'     :{'hex':'00010009', 'name':'delivery_receipt_v4'},
    'delivery_receipt_resp_v4':{'hex':'80010009', 'name':'delivery_receipt_resp_v4'},
    'enquire_link_v4'         :{'hex':'0001000a', 'name':'enquire_link_v4'},
    'enquire_link_resp_v4'    :{'hex':'8001000a', 'name':'enquire_link_resp_v4'},
    'outbind_v4'              :{'hex':'0001000b', 'name':'outbind_v4'}
}
def command_id_hex_by_name(n):
    return command_id_by_name.get(n,{}).get('hex')


# SMPP Error Codes (ESME) - SMPP v3.4, section 5.1.3, table 5-2, page 112-114

command_status_by_hex = {
    '00000000':{'hex':'00000000', 'name':'ESME_ROK',              'description':'No error'},
    '00000001':{'hex':'00000001', 'name':'ESME_RINVMSGLEN',       'description':'Message Length is invalid'},
    '00000002':{'hex':'00000002', 'name':'ESME_RINVCMDLEN',       'description':'Command Length is invalid'},
    '00000003':{'hex':'00000003', 'name':'ESME_RINVCMDID',        'description':'Invalid Command ID'},
    '00000004':{'hex':'00000004', 'name':'ESME_RINVBNDSTS',       'description':'Incorrect BIND Status for given command'},
    '00000005':{'hex':'00000005', 'name':'ESME_RALYBND',          'description':'ESME Already in bound state'},
    '00000006':{'hex':'00000006', 'name':'ESME_RINVPRTFLG',       'description':'Invalid priority flag'},
    '00000007':{'hex':'00000007', 'name':'ESME_RINVREGDLVFLG',    'description':'Invalid registered delivery flag'},
    '00000008':{'hex':'00000008', 'name':'ESME_RSYSERR',          'description':'System Error'},
    '0000000a':{'hex':'0000000a', 'name':'ESME_RINVSRCADR',       'description':'Invalid source address'},
    '0000000b':{'hex':'0000000b', 'name':'ESME_RINVDSTADR',       'description':'Invalid destination address'},
    '0000000c':{'hex':'0000000c', 'name':'ESME_RINVMSGID',        'description':'Message ID is invalid'},
    '0000000d':{'hex':'0000000d', 'name':'ESME_RBINDFAIL',        'description':'Bind failed'},
    '0000000e':{'hex':'0000000e', 'name':'ESME_RINVPASWD',        'description':'Invalid password'},
    '0000000f':{'hex':'0000000f', 'name':'ESME_RINVSYSID',        'description':'Invalid System ID'},
    '00000011':{'hex':'00000011', 'name':'ESME_RCANCELFAIL',      'description':'Cancel SM Failed'},
    '00000013':{'hex':'00000013', 'name':'ESME_RREPLACEFAIL',     'description':'Replace SM Failed'},
    '00000014':{'hex':'00000014', 'name':'ESME_RMSGQFUL',         'description':'Message queue full'},
    '00000015':{'hex':'00000015', 'name':'ESME_RINVSERTYP',       'description':'Invalid service type'},
    '00000033':{'hex':'00000033', 'name':'ESME_RINVNUMDESTS',     'description':'Invalid number of destinations'},
    '00000034':{'hex':'00000034', 'name':'ESME_RINVDLNAME',       'description':'Invalid distribution list name'},
    '00000040':{'hex':'00000040', 'name':'ESME_RINVDESTFLAG',     'description':'Destination flag is invalid (submit_multi)'},
    '00000042':{'hex':'00000042', 'name':'ESME_RINVSUBREP',       'description':"Invalid `submit with replace' request (i.e. submit_sm with replace_if_present_flag set)"},
    '00000043':{'hex':'00000043', 'name':'ESME_RINVESMCLASS',     'description':'Invalid esm_class field data'},
    '00000044':{'hex':'00000044', 'name':'ESME_RCNTSUBDL',        'description':'Cannot submit to distribution list'},
    '00000045':{'hex':'00000045', 'name':'ESME_RSUBMITFAIL',      'description':'submit_sm or submit_multi failed'},
    '00000048':{'hex':'00000048', 'name':'ESME_RINVSRCTON',       'description':'Invalid source address TON'},
    '00000049':{'hex':'00000049', 'name':'ESME_RINVSRCNPI',       'description':'Invalid source address NPI'},
    '00000050':{'hex':'00000050', 'name':'ESME_RINVDSTTON',       'description':'Invalid destination address TON'},
    '00000051':{'hex':'00000051', 'name':'ESME_RINVDSTNPI',       'description':'Invalid destination address NPI'},
    '00000053':{'hex':'00000053', 'name':'ESME_RINVSYSTYP',       'description':'Invalid system_type field'},
    '00000054':{'hex':'00000054', 'name':'ESME_RINVREPFLAG',      'description':'Invalid replace_if_present flag'},
    '00000055':{'hex':'00000055', 'name':'ESME_RINVNUMMSGS',      'description':'Invalid number of messages'},
    '00000058':{'hex':'00000058', 'name':'ESME_RTHROTTLED',       'description':'Throttling error (ESME has exceeded allowed message limits)'},
    '00000061':{'hex':'00000061', 'name':'ESME_RINVSCHED',        'description':'Invalid scheduled delivery time'},
    '00000062':{'hex':'00000062', 'name':'ESME_RINVEXPIRY',       'description':'Invalid message validity period (expiry time)'},
    '00000063':{'hex':'00000063', 'name':'ESME_RINVDFTMSGID',     'description':'Predefined message invalid or not found'},
    '00000064':{'hex':'00000064', 'name':'ESME_RX_T_APPN',        'description':'ESME Receiver Temporary App Error Code'},
    '00000065':{'hex':'00000065', 'name':'ESME_RX_P_APPN',        'description':'ESME Receiver Permanent App Error Code'},
    '00000066':{'hex':'00000066', 'name':'ESME_RX_R_APPN',        'description':'ESME Receiver Reject Message Error Code'},
    '00000067':{'hex':'00000067', 'name':'ESME_RQUERYFAIL',       'description':'query_sm request failed'},
    '000000c0':{'hex':'000000c0', 'name':'ESME_RINVOPTPARSTREAM', 'description':'Error in the optional part of the PDU Body'},
    '000000c1':{'hex':'000000c1', 'name':'ESME_ROPTPARNOTALLWD',  'description':'Optional paramenter not allowed'},
    '000000c2':{'hex':'000000c2', 'name':'ESME_RINVPARLEN',       'description':'Invalid parameter length'},
    '000000c3':{'hex':'000000c3', 'name':'ESME_RMISSINGOPTPARAM', 'description':'Expected optional parameter missing'},
    '000000c4':{'hex':'000000c4', 'name':'ESME_RINVOPTPARAMVAL',  'description':'Invalid optional parameter value'},
    '000000fe':{'hex':'000000fe', 'name':'ESME_RDELIVERYFAILURE', 'description':'Delivery Failure (used for data_sm_resp)'},
    '000000ff':{'hex':'000000ff', 'name':'ESME_RUNKNOWNERR',      'description':'Unknown error'}
}
def command_status_name_by_hex(x):
    return command_status_by_hex.get(x,{}).get('name')

command_status_by_name = {
    'ESME_ROK'             :{'hex':'00000000', 'name':'ESME_ROK',              'description':'No error'},
    'ESME_RINVMSGLEN'      :{'hex':'00000001', 'name':'ESME_RINVMSGLEN',       'description':'Message Length is invalid'},
    'ESME_RINVCMDLEN'      :{'hex':'00000002', 'name':'ESME_RINVCMDLEN',       'description':'Command Length is invalid'},
    'ESME_RINVCMDID'       :{'hex':'00000003', 'name':'ESME_RINVCMDID',        'description':'Invalid Command ID'},
    'ESME_RINVBNDSTS'      :{'hex':'00000004', 'name':'ESME_RINVBNDSTS',       'description':'Incorrect BIND Status for given command'},
    'ESME_RALYBND'         :{'hex':'00000005', 'name':'ESME_RALYBND',          'description':'ESME Already in bound state'},
    'ESME_RINVPRTFLG'      :{'hex':'00000006', 'name':'ESME_RINVPRTFLG',       'description':'Invalid priority flag'},
    'ESME_RINVREGDLVFLG'   :{'hex':'00000007', 'name':'ESME_RINVREGDLVFLG',    'description':'Invalid registered delivery flag'},
    'ESME_RSYSERR'         :{'hex':'00000008', 'name':'ESME_RSYSERR',          'description':'System Error'},
    'ESME_RINVSRCADR'      :{'hex':'0000000a', 'name':'ESME_RINVSRCADR',       'description':'Invalid source address'},
    'ESME_RINVDSTADR'      :{'hex':'0000000b', 'name':'ESME_RINVDSTADR',       'description':'Invalid destination address'},
    'ESME_RINVMSGID'       :{'hex':'0000000c', 'name':'ESME_RINVMSGID',        'description':'Message ID is invalid'},
    'ESME_RBINDFAIL'       :{'hex':'0000000d', 'name':'ESME_RBINDFAIL',        'description':'Bind failed'},
    'ESME_RINVPASWD'       :{'hex':'0000000e', 'name':'ESME_RINVPASWD',        'description':'Invalid password'},
    'ESME_RINVSYSID'       :{'hex':'0000000f', 'name':'ESME_RINVSYSID',        'description':'Invalid System ID'},
    'ESME_RCANCELFAIL'     :{'hex':'00000011', 'name':'ESME_RCANCELFAIL',      'description':'Cancel SM Failed'},
    'ESME_RREPLACEFAIL'    :{'hex':'00000013', 'name':'ESME_RREPLACEFAIL',     'description':'Replace SM Failed'},
    'ESME_RMSGQFUL'        :{'hex':'00000014', 'name':'ESME_RMSGQFUL',         'description':'Message queue full'},
    'ESME_RINVSERTYP'      :{'hex':'00000015', 'name':'ESME_RINVSERTYP',       'description':'Invalid service type'},
    'ESME_RINVNUMDESTS'    :{'hex':'00000033', 'name':'ESME_RINVNUMDESTS',     'description':'Invalid number of destinations'},
    'ESME_RINVDLNAME'      :{'hex':'00000034', 'name':'ESME_RINVDLNAME',       'description':'Invalid distribution list name'},
    'ESME_RINVDESTFLAG'    :{'hex':'00000040', 'name':'ESME_RINVDESTFLAG',     'description':'Destination flag is invalid (submit_multi)'},
    'ESME_RINVSUBREP'      :{'hex':'00000042', 'name':'ESME_RINVSUBREP',       'description':"Invalid `submit with replace' request (i.e. submit_sm with replace_if_present_flag set)"},
    'ESME_RINVESMCLASS'    :{'hex':'00000043', 'name':'ESME_RINVESMCLASS',     'description':'Invalid esm_class field data'},
    'ESME_RCNTSUBDL'       :{'hex':'00000044', 'name':'ESME_RCNTSUBDL',        'description':'Cannot submit to distribution list'},
    'ESME_RSUBMITFAIL'     :{'hex':'00000045', 'name':'ESME_RSUBMITFAIL',      'description':'submit_sm or submit_multi failed'},
    'ESME_RINVSRCTON'      :{'hex':'00000048', 'name':'ESME_RINVSRCTON',       'description':'Invalid source address TON'},
    'ESME_RINVSRCNPI'      :{'hex':'00000049', 'name':'ESME_RINVSRCNPI',       'description':'Invalid source address NPI'},
    'ESME_RINVDSTTON'      :{'hex':'00000050', 'name':'ESME_RINVDSTTON',       'description':'Invalid destination address TON'},
    'ESME_RINVDSTNPI'      :{'hex':'00000051', 'name':'ESME_RINVDSTNPI',       'description':'Invalid destination address NPI'},
    'ESME_RINVSYSTYP'      :{'hex':'00000053', 'name':'ESME_RINVSYSTYP',       'description':'Invalid system_type field'},
    'ESME_RINVREPFLAG'     :{'hex':'00000054', 'name':'ESME_RINVREPFLAG',      'description':'Invalid replace_if_present flag'},
    'ESME_RINVNUMMSGS'     :{'hex':'00000055', 'name':'ESME_RINVNUMMSGS',      'description':'Invalid number of messages'},
    'ESME_RTHROTTLED'      :{'hex':'00000058', 'name':'ESME_RTHROTTLED',       'description':'Throttling error (ESME has exceeded allowed message limits)'},
    'ESME_RINVSCHED'       :{'hex':'00000061', 'name':'ESME_RINVSCHED',        'description':'Invalid scheduled delivery time'},
    'ESME_RINVEXPIRY'      :{'hex':'00000062', 'name':'ESME_RINVEXPIRY',       'description':'Invalid message validity period (expiry time)'},
    'ESME_RINVDFTMSGID'    :{'hex':'00000063', 'name':'ESME_RINVDFTMSGID',     'description':'Predefined message invalid or not found'},
    'ESME_RX_T_APPN'       :{'hex':'00000064', 'name':'ESME_RX_T_APPN',        'description':'ESME Receiver Temporary App Error Code'},
    'ESME_RX_P_APPN'       :{'hex':'00000065', 'name':'ESME_RX_P_APPN',        'description':'ESME Receiver Permanent App Error Code'},
    'ESME_RX_R_APPN'       :{'hex':'00000066', 'name':'ESME_RX_R_APPN',        'description':'ESME Receiver Reject Message Error Code'},
    'ESME_RQUERYFAIL'      :{'hex':'00000067', 'name':'ESME_RQUERYFAIL',       'description':'query_sm request failed'},
    'ESME_RINVOPTPARSTREAM':{'hex':'000000c0', 'name':'ESME_RINVOPTPARSTREAM', 'description':'Error in the optional part of the PDU Body'},
    'ESME_ROPTPARNOTALLWD' :{'hex':'000000c1', 'name':'ESME_ROPTPARNOTALLWD',  'description':'Optional paramenter not allowed'},
    'ESME_RINVPARLEN'      :{'hex':'000000c2', 'name':'ESME_RINVPARLEN',       'description':'Invalid parameter length'},
    'ESME_RMISSINGOPTPARAM':{'hex':'000000c3', 'name':'ESME_RMISSINGOPTPARAM', 'description':'Expected optional parameter missing'},
    'ESME_RINVOPTPARAMVAL' :{'hex':'000000c4', 'name':'ESME_RINVOPTPARAMVAL',  'description':'Invalid optional parameter value'},
    'ESME_RDELIVERYFAILURE':{'hex':'000000fe', 'name':'ESME_RDELIVERYFAILURE', 'description':'Delivery Failure (used for data_sm_resp)'},
    'ESME_RUNKNOWNERR'     :{'hex':'000000ff', 'name':'ESME_RUNKNOWNERR',      'description':'Unknown error'}
}
def command_status_hex_by_name(n):
    return command_status_by_name.get(n,{}).get('hex')


# Type of Number (TON) - SMPP v3.4, section 5.2.5, table 5-3, page 117

maps['addr_ton_by_name'] = {
    'unknown'          :'00',
    'international'    :'01',
    'national'         :'02',
    'network_specific' :'03',
    'subscriber_number':'04',
    'alphanumeric'     :'05',
    'abbreviated'      :'06'
}

maps['addr_ton_by_hex'] = {
    '00':'unknown',
    '01':'international',
    '02':'national',
    '03':'network_specific',
    '04':'subscriber_number',
    '05':'alphanumeric',
    '06':'abbreviated'
}


# Numberic Plan Indicator (NPI) - SMPP v3.4, section 5.2.6, table 5-4, page 118

maps['addr_npi_by_name'] = {
    'unknown'    :'00',
    'ISDN'       :'01',
    'data'       :'03',
    'telex'      :'04',
    'land_mobile':'06',
    'national'   :'08',
    'private'    :'09',
    'ERMES'      :'0a',
    'internet'   :'0e',
    'WAP'        :'12'
}

maps['addr_npi_by_hex'] = {
    '00':'unknown',
    '01':'ISDN',
    '03':'data',
    '04':'telex',
    '06':'land_mobile',
    '08':'national',
    '09':'private',
    '0a':'ERMES',
    '0e':'internet',
    '12':'WAP'
}


# ESM Class bits  - SMPP v3.4, section 5.2.12, page 121

maps['esm_class_bits'] = {
    'mode_mask'                  :'03',
    'type_mask'                  :'3c',
    'feature_mask'               :'c0',

    'mode_default'               :'00',
    'mode_datagram'              :'01',
    'mode_forward'               :'02',
    'mode_store_and_forward'     :'03',

    'type_default'               :'00',
    'type_delivery_receipt'      :'04',
    'type_delivery_ack'          :'08',
    'type_0011'                  :'0a',
    'type_user_ack'              :'10',
    'type_0101'                  :'14',
    'type_conversation_abort'    :'18',
    'type_0111'                  :'1a',
    'type_intermed_deliv_notif'  :'20',
    'type_1001'                  :'24',
    'type_1010'                  :'28',
    'type_1011'                  :'2a',
    'type_1100'                  :'30',
    'type_1101'                  :'34',
    'type_1110'                  :'38',
    'type_1111'                  :'3a',

    'feature_none'               :'00',
    'feature_UDHI'               :'40',
    'feature_reply_path'         :'80',
    'feature_UDHI_and_reply_path':'c0'
}


# Registered Delivery bits - SMPP v3.4, section 5.2.17, page 124

maps['registered_delivery_bits'] = {
    'receipt_mask'         :'03',
    'ack_mask'             :'0c',
    'intermed_notif_mask'  :'80',

    'receipt_none'         :'00',
    'receipt_always'       :'01',
    'receipt_on_fail'      :'02',
    'receipt_res'          :'03',

    'ack_none'             :'00',
    'ack_delivery'         :'04',
    'ack_user'             :'08',
    'ack_delivery_and_user':'0c',

    'intermed_notif_none'  :'00',
    'intermed_notif'       :'10'
}


# submit_multi dest_flag constants - SMPP v3.4, section 5.2.25, page 129
#maps['dest_flag_by_name'] = {
    #'SME Address'           :1,
    #'Distribution List Name':2
#}


# Message State codes returned in query_sm_resp PDUs - SMPP v3.4, section 5.2.28, table 5-6, page 130
maps['message_state_by_name'] = {
    'ENROUTE'      :1,
    'DELIVERED'    :2,
    'EXPIRED'      :3,
    'DELETED'      :4,
    'UNDELIVERABLE':5,
    'ACCEPTED'     :6,
    'UNKNOWN'      :7,
    'REJECTED'     :8
}


# Facility Code bits for SMPP v4

maps['facility_code_bits'] = {
    'GF_PVCY'   :'00000001',
    'GF_SUBADDR':'00000002',
    'NF_CC'     :'00080000',
    'NF_PDC'    :'00010000',
    'NF_IS136'  :'00020000',
    'NF_IS95A'  :'00040000'
}


# Optional Parameter Tags - SMPP v3.4, section 5.3.2, Table 5-7, page 132-133

optional_parameter_tag_by_hex = {
    '0005':{'hex':'0005', 'name':'dest_addr_subunit',            'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.1, page 134
    '0006':{'hex':'0006', 'name':'dest_network_type',            'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.3, page 135
    '0007':{'hex':'0007', 'name':'dest_bearer_type',             'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.5, page 136
    '0008':{'hex':'0008', 'name':'dest_telematics_id',           'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.7, page 137

    '000d':{'hex':'000d', 'name':'source_addr_subunit',          'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.2, page 134
    '000e':{'hex':'000e', 'name':'source_network_type',          'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.4, page 135
    '000f':{'hex':'000f', 'name':'source_bearer_type',           'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.6, page 136
    '0010':{'hex':'0010', 'name':'source_telematics_id',         'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.8, page 137

    '0017':{'hex':'0017', 'name':'qos_time_to_live',             'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.9, page 138
    '0019':{'hex':'0019', 'name':'payload_type',                 'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.10, page 138

    '001d':{'hex':'001d', 'name':'additional_status_info_text',  'type':'string',  'tech':'Generic'},               # SMPP v3.4, section 5.3.2.11, page 139
    '001e':{'hex':'001e', 'name':'receipted_message_id',         'type':'string',  'tech':'Generic'},               # SMPP v3.4, section 5.3.2.12, page 139

    '0030':{'hex':'0030', 'name':'ms_msg_wait_facilities',       'type':'bitmask', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.13, page 140

    '0101':{'hex':'0101', 'name':'PVCY_AuthenticationStr',       'type':None,      'tech':'? (J-Phone)'},           # v4 page 58-62

    '0201':{'hex':'0201', 'name':'privacy_indicator',            'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.14, page 141
    '0202':{'hex':'0202', 'name':'source_subaddress',            'type':'hex',     'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.15, page 142
    '0203':{'hex':'0203', 'name':'dest_subaddress',              'type':'hex',     'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.16, page 143
    '0204':{'hex':'0204', 'name':'user_message_reference',       'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.17, page 143
    '0205':{'hex':'0205', 'name':'user_response_code',           'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.18, page 144

    '020a':{'hex':'020a', 'name':'source_port',                  'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.20, page 145
    '020b':{'hex':'020b', 'name':'destination_port',             'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.21, page 145
    '020c':{'hex':'020c', 'name':'sar_msg_ref_num',              'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.22, page 146
    '020d':{'hex':'020d', 'name':'language_indicator',           'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.19, page 144
    '020e':{'hex':'020e', 'name':'sar_total_segments',           'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.23, page 147
    '020f':{'hex':'020f', 'name':'sar_segment_seqnum',           'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.24, page 147
    '0210':{'hex':'0210', 'name':'sc_interface_version',         'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.25, page 148

    '0301':{'hex':'0301', 'name':'CC_CBN',                       'type':None,      'tech':'V4'},                    # v4 page 70
    '0302':{'hex':'0302', 'name':'callback_num_pres_ind',        'type':'bitmask', 'tech':'TDMA'},                  # SMPP v3.4, section 5.3.2.37, page 156
    '0303':{'hex':'0303', 'name':'callback_num_atag',            'type':'hex',     'tech':'TDMA'},                  # SMPP v3.4, section 5.3.2.38, page 157
    '0304':{'hex':'0304', 'name':'number_of_messages',           'type':'integer', 'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.39, page 158
    '0381':{'hex':'0381', 'name':'callback_num',                 'type':'hex',     'tech':'CDMA, TDMA, GSM, iDEN'}, # SMPP v3.4, section 5.3.2.36, page 155

    '0420':{'hex':'0420', 'name':'dpf_result',                   'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.28, page 149
    '0421':{'hex':'0421', 'name':'set_dpf',                      'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.29, page 150
    '0422':{'hex':'0422', 'name':'ms_availability_status',       'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.30, page 151
    '0423':{'hex':'0423', 'name':'network_error_code',           'type':'hex',     'tech':'Generic'},               # SMPP v3.4, section 5.3.2.31, page 152
    '0424':{'hex':'0424', 'name':'message_payload',              'type':'hex',     'tech':'Generic'},               # SMPP v3.4, section 5.3.2.32, page 153
    '0425':{'hex':'0425', 'name':'delivery_failure_reason',      'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.33, page 153
    '0426':{'hex':'0426', 'name':'more_messages_to_send',        'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.34, page 154
    '0427':{'hex':'0427', 'name':'message_state',                'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.35, page 154
    '0428':{'hex':'0428', 'name':'congestion_state',             'type':None,      'tech':'Generic'},

    '0501':{'hex':'0501', 'name':'ussd_service_op',              'type':'hex',     'tech':'GSM (USSD)'},            # SMPP v3.4, section 5.3.2.44, page 161

    '0600':{'hex':'0600', 'name':'broadcast_channel_indicator',  'type':None,      'tech':'GSM'},
    '0601':{'hex':'0601', 'name':'broadcast_content_type',       'type':None,      'tech':'CDMA, TDMA, GSM'},
    '0602':{'hex':'0602', 'name':'broadcast_content_type_info',  'type':None,      'tech':'CDMA, TDMA'},
    '0603':{'hex':'0603', 'name':'broadcast_message_class',      'type':None,      'tech':'GSM'},
    '0604':{'hex':'0604', 'name':'broadcast_rep_num',            'type':None,      'tech':'GSM'},
    '0605':{'hex':'0605', 'name':'broadcast_frequency_interval', 'type':None,      'tech':'CDMA, TDMA, GSM'},
    '0606':{'hex':'0606', 'name':'broadcast_area_identifier',    'type':None,      'tech':'CDMA, TDMA, GSM'},
    '0607':{'hex':'0607', 'name':'broadcast_error_status',       'type':None,      'tech':'CDMA, TDMA, GSM'},
    '0608':{'hex':'0608', 'name':'broadcast_area_success',       'type':None,      'tech':'GSM'},
    '0609':{'hex':'0609', 'name':'broadcast_end_time',           'type':None,      'tech':'CDMA, TDMA, GSM'},
    '060a':{'hex':'060a', 'name':'broadcast_service_group',      'type':None,      'tech':'CDMA, TDMA'},
    '060b':{'hex':'060b', 'name':'billing_identification',       'type':None,      'tech':'Generic'},

    '060d':{'hex':'060d', 'name':'source_network_id',            'type':None,      'tech':'Generic'},
    '060e':{'hex':'060e', 'name':'dest_network_id',              'type':None,      'tech':'Generic'},
    '060f':{'hex':'060f', 'name':'source_node_id',               'type':None,      'tech':'Generic'},
    '0610':{'hex':'0610', 'name':'dest_node_id',                 'type':None,      'tech':'Generic'},
    '0611':{'hex':'0611', 'name':'dest_addr_np_resolution',      'type':None,      'tech':'CDMA, TDMA (US Only)'},
    '0612':{'hex':'0612', 'name':'dest_addr_np_information',     'type':None,      'tech':'CDMA, TDMA (US Only)'},
    '0613':{'hex':'0613', 'name':'dest_addr_np_country',         'type':None,      'tech':'CDMA, TDMA (US Only)'},

    '1101':{'hex':'1101', 'name':'PDC_MessageClass',             'type':None,      'tech':'? (J-Phone)'},           # v4 page 75
    '1102':{'hex':'1102', 'name':'PDC_PresentationOption',       'type':None,      'tech':'? (J-Phone)'},           # v4 page 76
    '1103':{'hex':'1103', 'name':'PDC_AlertMechanism',           'type':None,      'tech':'? (J-Phone)'},           # v4 page 76
    '1104':{'hex':'1104', 'name':'PDC_Teleservice',              'type':None,      'tech':'? (J-Phone)'},           # v4 page 77
    '1105':{'hex':'1105', 'name':'PDC_MultiPartMessage',         'type':None,      'tech':'? (J-Phone)'},           # v4 page 77
    '1106':{'hex':'1106', 'name':'PDC_PredefinedMsg',            'type':None,      'tech':'? (J-Phone)'},           # v4 page 78

    '1201':{'hex':'1201', 'name':'display_time',                 'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.26, page 148

    '1203':{'hex':'1203', 'name':'sms_signal',                   'type':'integer', 'tech':'TDMA'},                  # SMPP v3.4, section 5.3.2.40, page 158
    '1204':{'hex':'1204', 'name':'ms_validity',                  'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.27, page 149

    '1304':{'hex':'1304', 'name':'IS95A_AlertOnDelivery',        'type':None,      'tech':'CDMA'},                  # v4 page 85
    '1306':{'hex':'1306', 'name':'IS95A_LanguageIndicator',      'type':None,      'tech':'CDMA'},                  # v4 page 86

    '130c':{'hex':'130c', 'name':'alert_on_message_delivery',    'type':None,      'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.41, page 159

    '1380':{'hex':'1380', 'name':'its_reply_type',               'type':'integer', 'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.42, page 159
    '1383':{'hex':'1383', 'name':'its_session_info',             'type':'hex',     'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.43, page 160

    '1402':{'hex':'1402', 'name':'operator_id',                  'type':None,      'tech':'vendor extension'},
    '1403':{'hex':'1403', 'name':'tariff',                       'type':None,      'tech':'Mobile Network Code vendor extension'},
    '1450':{'hex':'1450', 'name':'mcc',                          'type':None,      'tech':'Mobile Country Code vendor extension'},
    '1451':{'hex':'1451', 'name':'mnc',                          'type':None,      'tech':'Mobile Network Code vendor extension'}
}
def optional_parameter_tag_name_by_hex(x):
    return optional_parameter_tag_by_hex.get(x,{}).get('name')

def optional_parameter_tag_type_by_hex(x):
    return optional_parameter_tag_by_hex.get(x,{}).get('type')


optional_parameter_tag_by_name = {
    'dest_addr_subunit'           :{'hex':'0005', 'name':'dest_addr_subunit',            'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.1, page 134
    'dest_network_type'           :{'hex':'0006', 'name':'dest_network_type',            'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.3, page 135
    'dest_bearer_type'            :{'hex':'0007', 'name':'dest_bearer_type',             'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.5, page 136
    'dest_telematics_id'          :{'hex':'0008', 'name':'dest_telematics_id',           'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.7, page 137

    'source_addr_subunit'         :{'hex':'000d', 'name':'source_addr_subunit',          'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.2, page 134
    'source_network_type'         :{'hex':'000e', 'name':'source_network_type',          'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.4, page 135
    'source_bearer_type'          :{'hex':'000f', 'name':'source_bearer_type',           'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.6, page 136
    'source_telematics_id'        :{'hex':'0010', 'name':'source_telematics_id',         'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.8, page 137

    'qos_time_to_live'            :{'hex':'0017', 'name':'qos_time_to_live',             'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.9, page 138
    'payload_type'                :{'hex':'0019', 'name':'payload_type',                 'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.10, page 138

    'additional_status_info_text' :{'hex':'001d', 'name':'additional_status_info_text',  'type':'string',  'tech':'Generic'},               # SMPP v3.4, section 5.3.2.11, page 139
    'receipted_message_id'        :{'hex':'001e', 'name':'receipted_message_id',         'type':'string',  'tech':'Generic'},               # SMPP v3.4, section 5.3.2.12, page 139

    'ms_msg_wait_facilities'      :{'hex':'0030', 'name':'ms_msg_wait_facilities',       'type':'bitmask', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.13, page 140

    'PVCY_AuthenticationStr'      :{'hex':'0101', 'name':'PVCY_AuthenticationStr',       'type':None,      'tech':'? (J-Phone)'},           # v4 page 58-62

    'privacy_indicator'           :{'hex':'0201', 'name':'privacy_indicator',            'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.14, page 141
    'source_subaddress'           :{'hex':'0202', 'name':'source_subaddress',            'type':'hex',     'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.15, page 142
    'dest_subaddress'             :{'hex':'0203', 'name':'dest_subaddress',              'type':'hex',     'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.16, page 143
    'user_message_reference'      :{'hex':'0204', 'name':'user_message_reference',       'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.17, page 143
    'user_response_code'          :{'hex':'0205', 'name':'user_response_code',           'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.18, page 144

    'source_port'                 :{'hex':'020a', 'name':'source_port',                  'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.20, page 145
    'destination_port'            :{'hex':'020b', 'name':'destination_port',             'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.21, page 145
    'sar_msg_ref_num'             :{'hex':'020c', 'name':'sar_msg_ref_num',              'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.22, page 146
    'language_indicator'          :{'hex':'020d', 'name':'language_indicator',           'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.19, page 144
    'sar_total_segments'          :{'hex':'020e', 'name':'sar_total_segments',           'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.23, page 147
    'sar_segment_seqnum'          :{'hex':'020f', 'name':'sar_segment_seqnum',           'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.24, page 147
    'sc_interface_version'        :{'hex':'0210', 'name':'sc_interface_version',         'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.25, page 148

    'CC_CBN'                      :{'hex':'0301', 'name':'CC_CBN',                       'type':None,      'tech':'V4'},                    # v4 page 70
    'callback_num_pres_ind'       :{'hex':'0302', 'name':'callback_num_pres_ind',        'type':'bitmask', 'tech':'TDMA'},                  # SMPP v3.4, section 5.3.2.37, page 156
    'callback_num_atag'           :{'hex':'0303', 'name':'callback_num_atag',            'type':'hex',     'tech':'TDMA'},                  # SMPP v3.4, section 5.3.2.38, page 157
    'number_of_messages'          :{'hex':'0304', 'name':'number_of_messages',           'type':'integer', 'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.39, page 158
    'callback_num'                :{'hex':'0381', 'name':'callback_num',                 'type':'hex',     'tech':'CDMA, TDMA, GSM, iDEN'}, # SMPP v3.4, section 5.3.2.36, page 155

    'dpf_result'                  :{'hex':'0420', 'name':'dpf_result',                   'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.28, page 149
    'set_dpf'                     :{'hex':'0421', 'name':'set_dpf',                      'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.29, page 150
    'ms_availability_status'      :{'hex':'0422', 'name':'ms_availability_status',       'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.30, page 151
    'network_error_code'          :{'hex':'0423', 'name':'network_error_code',           'type':'hex',     'tech':'Generic'},               # SMPP v3.4, section 5.3.2.31, page 152
    'message_payload'             :{'hex':'0424', 'name':'message_payload',              'type':'hex',     'tech':'Generic'},               # SMPP v3.4, section 5.3.2.32, page 153
    'delivery_failure_reason'     :{'hex':'0425', 'name':'delivery_failure_reason',      'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.33, page 153
    'more_messages_to_send'       :{'hex':'0426', 'name':'more_messages_to_send',        'type':'integer', 'tech':'GSM'},                   # SMPP v3.4, section 5.3.2.34, page 154
    'message_state'               :{'hex':'0427', 'name':'message_state',                'type':'integer', 'tech':'Generic'},               # SMPP v3.4, section 5.3.2.35, page 154
    'congestion_state'            :{'hex':'0428', 'name':'congestion_state',             'type':None,      'tech':'Generic'},

    'ussd_service_op'             :{'hex':'0501', 'name':'ussd_service_op',              'type':'hex',     'tech':'GSM (USSD)'},            # SMPP v3.4, section 5.3.2.44, page 161

    'broadcast_channel_indicator' :{'hex':'0600', 'name':'broadcast_channel_indicator',  'type':None,      'tech':'GSM'},
    'broadcast_content_type'      :{'hex':'0601', 'name':'broadcast_content_type',       'type':None,      'tech':'CDMA, TDMA, GSM'},
    'broadcast_content_type_info' :{'hex':'0602', 'name':'broadcast_content_type_info',  'type':None,      'tech':'CDMA, TDMA'},
    'broadcast_message_class'     :{'hex':'0603', 'name':'broadcast_message_class',      'type':None,      'tech':'GSM'},
    'broadcast_rep_num'           :{'hex':'0604', 'name':'broadcast_rep_num',            'type':None,      'tech':'GSM'},
    'broadcast_frequency_interval':{'hex':'0605', 'name':'broadcast_frequency_interval', 'type':None,      'tech':'CDMA, TDMA, GSM'},
    'broadcast_area_identifier'   :{'hex':'0606', 'name':'broadcast_area_identifier',    'type':None,      'tech':'CDMA, TDMA, GSM'},
    'broadcast_error_status'      :{'hex':'0607', 'name':'broadcast_error_status',       'type':None,      'tech':'CDMA, TDMA, GSM'},
    'broadcast_area_success'      :{'hex':'0608', 'name':'broadcast_area_success',       'type':None,      'tech':'GSM'},
    'broadcast_end_time'          :{'hex':'0609', 'name':'broadcast_end_time',           'type':None,      'tech':'CDMA, TDMA, GSM'},
    'broadcast_service_group'     :{'hex':'060a', 'name':'broadcast_service_group',      'type':None,      'tech':'CDMA, TDMA'},
    'billing_identification'      :{'hex':'060b', 'name':'billing_identification',       'type':None,      'tech':'Generic'},

    'source_network_id'           :{'hex':'060d', 'name':'source_network_id',            'type':None,      'tech':'Generic'},
    'dest_network_id'             :{'hex':'060e', 'name':'dest_network_id',              'type':None,      'tech':'Generic'},
    'source_node_id'              :{'hex':'060f', 'name':'source_node_id',               'type':None,      'tech':'Generic'},
    'dest_node_id'                :{'hex':'0610', 'name':'dest_node_id',                 'type':None,      'tech':'Generic'},
    'dest_addr_np_resolution'     :{'hex':'0611', 'name':'dest_addr_np_resolution',      'type':None,      'tech':'CDMA, TDMA (US Only)'},
    'dest_addr_np_information'    :{'hex':'0612', 'name':'dest_addr_np_information',     'type':None,      'tech':'CDMA, TDMA (US Only)'},
    'dest_addr_np_country'        :{'hex':'0613', 'name':'dest_addr_np_country',         'type':None,      'tech':'CDMA, TDMA (US Only)'},

    'PDC_MessageClass'            :{'hex':'1101', 'name':'PDC_MessageClass',             'type':None,      'tech':'? (J-Phone)'},           # v4 page 75
    'PDC_PresentationOption'      :{'hex':'1102', 'name':'PDC_PresentationOption',       'type':None,      'tech':'? (J-Phone)'},           # v4 page 76
    'PDC_AlertMechanism'          :{'hex':'1103', 'name':'PDC_AlertMechanism',           'type':None,      'tech':'? (J-Phone)'},           # v4 page 76
    'PDC_Teleservice'             :{'hex':'1104', 'name':'PDC_Teleservice',              'type':None,      'tech':'? (J-Phone)'},           # v4 page 77
    'PDC_MultiPartMessage'        :{'hex':'1105', 'name':'PDC_MultiPartMessage',         'type':None,      'tech':'? (J-Phone)'},           # v4 page 77
    'PDC_PredefinedMsg'           :{'hex':'1106', 'name':'PDC_PredefinedMsg',            'type':None,      'tech':'? (J-Phone)'},           # v4 page 78

    'display_time'                :{'hex':'1201', 'name':'display_time',                 'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.26, page 148

    'sms_signal'                  :{'hex':'1203', 'name':'sms_signal',                   'type':'integer', 'tech':'TDMA'},                  # SMPP v3.4, section 5.3.2.40, page 158
    'ms_validity'                 :{'hex':'1204', 'name':'ms_validity',                  'type':'integer', 'tech':'CDMA, TDMA'},            # SMPP v3.4, section 5.3.2.27, page 149

    'IS95A_AlertOnDelivery'       :{'hex':'1304', 'name':'IS95A_AlertOnDelivery',        'type':None,      'tech':'CDMA'},                  # v4 page 85
    'IS95A_LanguageIndicator'     :{'hex':'1306', 'name':'IS95A_LanguageIndicator',      'type':None,      'tech':'CDMA'},                  # v4 page 86

    'alert_on_message_delivery'   :{'hex':'130c', 'name':'alert_on_message_delivery',    'type':None,      'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.41, page 159

    'its_reply_type'              :{'hex':'1380', 'name':'its_reply_type',               'type':'integer', 'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.42, page 159
    'its_session_info'            :{'hex':'1383', 'name':'its_session_info',             'type':'hex',     'tech':'CDMA'},                  # SMPP v3.4, section 5.3.2.43, page 160

    'operator_id'                 :{'hex':'1402', 'name':'operator_id',                  'type':None,      'tech':'vendor extension'},
    'tariff'                      :{'hex':'1403', 'name':'tariff',                       'type':None,      'tech':'Mobile Network Code vendor extension'},
    'mcc'                         :{'hex':'1450', 'name':'mcc',                          'type':None,      'tech':'Mobile Country Code vendor extension'},
    'mnc'                         :{'hex':'1451', 'name':'mnc',                          'type':None,      'tech':'Mobile Network Code vendor extension'}
}
def optional_parameter_tag_hex_by_name(n):
    return optional_parameter_tag_by_name.get(n,{}).get('hex')


#### Decoding functions #######################################################

def unpack_pdu(pdu_bin):
    return decode_pdu(binascii.b2a_hex(pdu_bin))


def decode_pdu(pdu_hex):
    hex_ref = [pdu_hex]
    pdu = {}
    pdu['header'] = decode_header(hex_ref)
    command = pdu['header'].get('command_id', None)
    if command != None:
        body = decode_body(command, hex_ref)
        if len(body) > 0:
            pdu['body'] = body
    return pdu


def decode_header(hex_ref):
    pdu_hex = hex_ref[0]
    header = {}
    (command_length, command_id,    command_status,  sequence_number, hex_ref[0]) = \
    (pdu_hex[0:8],   pdu_hex[8:16], pdu_hex[16:24],  pdu_hex[24:32],  pdu_hex[32: ])
    length = int(command_length, 16)
    command = command_id_name_by_hex(command_id)
    status = command_status_name_by_hex(command_status)
    sequence = int(sequence_number, 16)
    header = {}
    header['command_length'] = length
    header['command_id'] = command
    header['command_status'] = status
    header['sequence_number'] = sequence
    return header


def decode_body(command, hex_ref):
    body = {}
    if command != None:
        fields = mandatory_parameter_list_by_command_name(command)
        mandatory = decode_mandatory_parameters(fields, hex_ref)
        if len(mandatory) > 0:
            body['mandatory_parameters'] = mandatory
    optional = decode_optional_parameters(hex_ref)
    if len(optional) > 0:
            body['optional_parameters'] = optional
    return body


def decode_mandatory_parameters(fields, hex_ref):
    mandatory_parameters = {}
    if len(hex_ref[0]) > 1:
        for field in fields:
            #old = len(hex_ref[0])
            data = ''
            octet = ''
            count = 0
            if field['var'] == True or field['var'] == False:
                while (len(hex_ref[0]) > 1
                        and (count < field['min']
                            or (field['var'] == True
                                and count < field['max']+1
                                and octet != '00'))):
                    octet = octpop(hex_ref)
                    data += octet
                    count += 1
            elif field['type'] in ['string', 'xstring']:
                count = mandatory_parameters[field['var']]
                if count == 0:
                    data = None
                else:
                    for i in range(count):
                        if len(hex_ref[0]) > 1:
                            data += octpop(hex_ref)
            else:
                count = mandatory_parameters[field['var']]
            if field['map'] != None:
                mandatory_parameters[field['name']] = maps[field['map']+'_by_hex'].get(data, None)
            if field['map'] == None or mandatory_parameters[field['name']] == None:
                mandatory_parameters[field['name']] = decode_hex_type(data, field['type'], count, hex_ref)
            #print field['type'], (old - len(hex_ref[0]))/2, repr(data), field['name'], mandatory_parameters[field['name']]
    return mandatory_parameters


def decode_optional_parameters(hex_ref):
    optional_parameters = []
    hex = hex_ref[0]
    while len(hex) > 0:
        (tag_hex, length_hex, rest) = (hex[0:4], hex[4:8], hex[8: ])
        tag = optional_parameter_tag_name_by_hex(tag_hex)
        if tag == None:
            tag = tag_hex
        length = int(length_hex, 16)
        (value_hex, tail) = (rest[0:length*2], rest[length*2: ])
        if len(value_hex) == 0:
            value = None
        else:
            value = decode_hex_type(value_hex, optional_parameter_tag_type_by_hex(tag_hex))
        hex = tail
        optional_parameters.append({'tag':tag, 'length':length, 'value':value})
    return optional_parameters


def decode_hex_type(hex, type, count=0, hex_ref=['']):
    if hex == None:
        return hex
    elif type == 'integer':
        return int(hex, 16)
    elif type == 'string':
        return re.sub('00','',hex).decode('hex')
    elif type == 'xstring':
        return hex.decode('hex')
    elif (type == 'dest_address'
            or type == 'unsuccess_sme'):
        list = []
        fields = mandatory_parameter_list_by_command_name(type)
        for i in range(count):
            item = decode_mandatory_parameters(fields, hex_ref)
            if item.get('dest_flag', None) == 1: # 'dest_address' only
                subfields = mandatory_parameter_list_by_command_name('sme_dest_address')
                rest = decode_mandatory_parameters(subfields, hex_ref)
                item.update(rest)
            elif item.get('dest_flag', None) == 2: # 'dest_address' only
                subfields = mandatory_parameter_list_by_command_name('distribution_list')
                rest = decode_mandatory_parameters(subfields, hex_ref)
                item.update(rest)
            list.append(item)
        return list
    else:
        return hex


def octpop(hex_ref):
    octet = None
    if len(hex_ref[0]) > 1:
        (octet, hex_ref[0]) = (hex_ref[0][0:2], hex_ref[0][2: ])
    return octet


#### Encoding functions #######################################################

def pack_pdu(pdu_obj):
    return binascii.a2b_hex(encode_pdu(pdu_obj))


def encode_pdu(pdu_obj):
    header = pdu_obj.get('header', {})
    body = pdu_obj.get('body', {})
    mandatory = body.get('mandatory_parameters', {})
    optional = body.get('optional_parameters', [])
    body_hex = ''
    fields = mandatory_parameter_list_by_command_name(header['command_id'])
    body_hex += encode_mandatory_parameters(mandatory, fields)
    for opt in optional:
        body_hex += encode_optional_parameter(opt['tag'], opt['value'])
    actual_length = 16 + len(body_hex)/2
    command_length = '%08x' % actual_length
    command_id = command_id_hex_by_name(header['command_id'])
    command_status = command_status_hex_by_name(header['command_status'])
    sequence_number = '%08x' % header['sequence_number']
    pdu_hex = command_length + command_id + command_status + sequence_number + body_hex
    return pdu_hex


def encode_mandatory_parameters(mandatory_obj, fields):
    mandatory_hex_array = []
    index_names = {}
    index = 0
    for field in fields:
        param = mandatory_obj.get(field['name'], None)
        param_length = None
        if param != None or field['min'] > 0:
            map = None
            if field['map'] != None:
                map = maps.get(field['map']+'_by_name', None)
            if isinstance(param, list):
                hex_list = []
                for item in param:
                    flagfields = mandatory_parameter_list_by_command_name(field['type'])
                    plusfields = []
                    if item.get('dest_flag', None) == 1:
                        plusfields = mandatory_parameter_list_by_command_name('sme_dest_address')
                    elif item.get('dest_flag', None) == 2:
                        plusfields = mandatory_parameter_list_by_command_name('distribution_list')
                    hex_item = encode_mandatory_parameters(item, flagfields + plusfields)
                    if isinstance(hex_item, str) and len(hex_item) > 0:
                        hex_list.append(hex_item)
                param_length = len(hex_list)
                mandatory_hex_array.append(''.join(hex_list))
            else:
                hex_param = encode_param_type(
                        param, field['type'], field['min'], field['max'], map)
                param_length = len(hex_param)/2
                mandatory_hex_array.append(hex_param)
            index_names[field['name']] = index
            length_index = index_names.get(field['var'], None)
            if length_index != None and param_length != None:
                mandatory_hex_array[length_index] = encode_param_type(
                        param_length,
                        'integer',
                        len(mandatory_hex_array[length_index])/2)
            index += 1
    return ''.join(mandatory_hex_array)


def encode_optional_parameter(tag, value):
    optional_hex_array = []
    tag_hex = optional_parameter_tag_hex_by_name(tag)
    if tag_hex != None:
        value_hex = encode_param_type(
                value,
                optional_parameter_tag_type_by_hex(tag_hex))
        length_hex = '%04x' % (len(value_hex)/2)
        optional_hex_array.append(tag_hex + length_hex + value_hex)
    return ''.join(optional_hex_array)


def encode_param_type(param, type, min=0, max=None, map=None):
    if param == None:
        hex = None
    elif map != None:
        if type == 'integer' and isinstance(param, int):
            hex = ('%0'+str(min*2)+'x') % param
        else:
            hex = map.get(param, ('%0'+str(min*2)+'x') % 0)
    elif type == 'integer':
        hex = ('%0'+str(min*2)+'x') % int(param)
    elif type == 'string':
        hex = param.encode('hex') + '00'
    elif type == 'xstring':
        hex = param.encode('hex')
    elif type == 'bitmask':
        hex = param
    elif type == 'hex':
        hex = param
    else:
        hex = None
    if hex:
        if len(hex) % 2:
            # pad odd length hex strings
            hex = '0' + hex
    #print type, min, max, repr(param), hex, map
    return hex


