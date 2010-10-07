import binascii
import re



def octpop(ref):
    octet = None
    if len(ref[0]) > 1:
        (octet, ref[0]) = (ref[0][0:2], ref[0][2: ])
    return octet


def decode_hex_type(data, hex_type):
    if hex_type == 'string':
        return binascii.b2a_qp(binascii.a2b_hex(re.sub('00','',data)))
    if hex_type == 'integer':
        return int(data, 16)
    if hex_type == 'bits':
        return data
    return data


# SMPP Error Codes (ESME) - SMPP v3.4, section 5.1.3, table 5-2, page 112-114

command_status_by_hex = {
    '00000000' : {'hex' : '00000000', 'name' : 'ESME_ROK',              'description' : 'No error'},
    '00000001' : {'hex' : '00000001', 'name' : 'ESME_RINVMSGLEN',       'description' : 'Message Length is invalid'},
    '00000002' : {'hex' : '00000002', 'name' : 'ESME_RINVCMDLEN',       'description' : 'Command Length is invalid'},
    '00000003' : {'hex' : '00000003', 'name' : 'ESME_RINVCMDID',        'description' : 'Invalid Command ID'},
    '00000004' : {'hex' : '00000004', 'name' : 'ESME_RINVBNDSTS',       'description' : 'Incorrect BIND Status for given command'},
    '00000005' : {'hex' : '00000005', 'name' : 'ESME_RALYBND',          'description' : 'ESME Already in bound state'},
    '00000006' : {'hex' : '00000006', 'name' : 'ESME_RINVPRTFLG',       'description' : 'Invalid priority flag'},
    '00000007' : {'hex' : '00000007', 'name' : 'ESME_RINVREGDLVFLG',    'description' : 'Invalid registered delivery flag'},
    '00000008' : {'hex' : '00000008', 'name' : 'ESME_RSYSERR',          'description' : 'System Error'},
    '0000000a' : {'hex' : '0000000a', 'name' : 'ESME_RINVSRCADR',       'description' : 'Invalid source address'},
    '0000000b' : {'hex' : '0000000b', 'name' : 'ESME_RINVDSTADR',       'description' : 'Invalid destination address'},
    '0000000c' : {'hex' : '0000000c', 'name' : 'ESME_RINVMSGID',        'description' : 'Message ID is invalid'},
    '0000000d' : {'hex' : '0000000d', 'name' : 'ESME_RBINDFAIL',        'description' : 'Bind failed'},
    '0000000e' : {'hex' : '0000000e', 'name' : 'ESME_RINVPASWD',        'description' : 'Invalid password'},
    '0000000f' : {'hex' : '0000000f', 'name' : 'ESME_RINVSYSID',        'description' : 'Invalid System ID'},
    '00000011' : {'hex' : '00000011', 'name' : 'ESME_RCANCELFAIL',      'description' : 'Cancel SM Failed'},
    '00000013' : {'hex' : '00000013', 'name' : 'ESME_RREPLACEFAIL',     'description' : 'Replace SM Failed'},
    '00000014' : {'hex' : '00000014', 'name' : 'ESME_RMSGQFUL',         'description' : 'Message queue full'},
    '00000015' : {'hex' : '00000015', 'name' : 'ESME_RINVSERTYP',       'description' : 'Invalid service type'},
    '00000033' : {'hex' : '00000033', 'name' : 'ESME_RINVNUMDESTS',     'description' : 'Invalid number of destinations'},
    '00000034' : {'hex' : '00000034', 'name' : 'ESME_RINVDLNAME',       'description' : 'Invalid distribution list name'},
    '00000040' : {'hex' : '00000040', 'name' : 'ESME_RINVDESTFLAG',     'description' : 'Destination flag is invalid (submit_multi)'},
    '00000042' : {'hex' : '00000042', 'name' : 'ESME_RINVSUBREP',       'description' : "Invalid `submit with replace' request (i.e. submit_sm with replace_if_present_flag set)"},
    '00000043' : {'hex' : '00000043', 'name' : 'ESME_RINVESMCLASS',     'description' : 'Invalid esm_class field data'},
    '00000044' : {'hex' : '00000044', 'name' : 'ESME_RCNTSUBDL',        'description' : 'Cannot submit to distribution list'},
    '00000045' : {'hex' : '00000045', 'name' : 'ESME_RSUBMITFAIL',      'description' : 'submit_sm or submit_multi failed'},
    '00000048' : {'hex' : '00000048', 'name' : 'ESME_RINVSRCTON',       'description' : 'Invalid source address TON'},
    '00000049' : {'hex' : '00000049', 'name' : 'ESME_RINVSRCNPI',       'description' : 'Invalid source address NPI'},
    '00000050' : {'hex' : '00000050', 'name' : 'ESME_RINVDSTTON',       'description' : 'Invalid destination address TON'},
    '00000051' : {'hex' : '00000051', 'name' : 'ESME_RINVDSTNPI',       'description' : 'Invalid destination address NPI'},
    '00000053' : {'hex' : '00000053', 'name' : 'ESME_RINVSYSTYP',       'description' : 'Invalid system_type field'},
    '00000054' : {'hex' : '00000054', 'name' : 'ESME_RINVREPFLAG',      'description' : 'Invalid replace_if_present flag'},
    '00000055' : {'hex' : '00000055', 'name' : 'ESME_RINVNUMMSGS',      'description' : 'Invalid number of messages'},
    '00000058' : {'hex' : '00000058', 'name' : 'ESME_RTHROTTLED',       'description' : 'Throttling error (ESME has exceeded allowed message limits)'},
    '00000061' : {'hex' : '00000061', 'name' : 'ESME_RINVSCHED',        'description' : 'Invalid scheduled delivery time'},
    '00000062' : {'hex' : '00000062', 'name' : 'ESME_RINVEXPIRY',       'description' : 'Invalid message validity period (expiry time)'},
    '00000063' : {'hex' : '00000063', 'name' : 'ESME_RINVDFTMSGID',     'description' : 'Predefined message invalid or not found'},
    '00000064' : {'hex' : '00000064', 'name' : 'ESME_RX_T_APPN',        'description' : 'ESME Receiver Temporary App Error Code'},
    '00000065' : {'hex' : '00000065', 'name' : 'ESME_RX_P_APPN',        'description' : 'ESME Receiver Permanent App Error Code'},
    '00000066' : {'hex' : '00000066', 'name' : 'ESME_RX_R_APPN',        'description' : 'ESME Receiver Reject Message Error Code'},
    '00000067' : {'hex' : '00000067', 'name' : 'ESME_RQUERYFAIL',       'description' : 'query_sm request failed'},
    '000000c0' : {'hex' : '000000c0', 'name' : 'ESME_RINVOPTPARSTREAM', 'description' : 'Error in the optional part of the PDU Body'},
    '000000c1' : {'hex' : '000000c1', 'name' : 'ESME_ROPTPARNOTALLWD',  'description' : 'Optional paramenter not allowed'},
    '000000c2' : {'hex' : '000000c2', 'name' : 'ESME_RINVPARLEN',       'description' : 'Invalid parameter length'},
    '000000c3' : {'hex' : '000000c3', 'name' : 'ESME_RMISSINGOPTPARAM', 'description' : 'Expected optional parameter missing'},
    '000000c4' : {'hex' : '000000c4', 'name' : 'ESME_RINVOPTPARAMVAL',  'description' : 'Invalid optional parameter value'},
    '000000fe' : {'hex' : '000000fe', 'name' : 'ESME_RDELIVERYFAILURE', 'description' : 'Delivery Failure (used for data_sm_resp)'},
    '000000ff' : {'hex' : '000000ff', 'name' : 'ESME_RUNKNOWNERR',      'description' : 'Unknown error'}
}

def command_status_name_by_hex(x):
    return command_status_by_hex.get(x,{}).get('name')

command_status_by_name = {
    'ESME_ROK'              : {'hex' : '00000000', 'name' : 'ESME_ROK',              'description' : 'No error'},
    'ESME_RINVMSGLEN'       : {'hex' : '00000001', 'name' : 'ESME_RINVMSGLEN',       'description' : 'Message Length is invalid'},
    'ESME_RINVCMDLEN'       : {'hex' : '00000002', 'name' : 'ESME_RINVCMDLEN',       'description' : 'Command Length is invalid'},
    'ESME_RINVCMDID'        : {'hex' : '00000003', 'name' : 'ESME_RINVCMDID',        'description' : 'Invalid Command ID'},
    'ESME_RINVBNDSTS'       : {'hex' : '00000004', 'name' : 'ESME_RINVBNDSTS',       'description' : 'Incorrect BIND Status for given command'},
    'ESME_RALYBND'          : {'hex' : '00000005', 'name' : 'ESME_RALYBND',          'description' : 'ESME Already in bound state'},
    'ESME_RINVPRTFLG'       : {'hex' : '00000006', 'name' : 'ESME_RINVPRTFLG',       'description' : 'Invalid priority flag'},
    'ESME_RINVREGDLVFLG'    : {'hex' : '00000007', 'name' : 'ESME_RINVREGDLVFLG',    'description' : 'Invalid registered delivery flag'},
    'ESME_RSYSERR'          : {'hex' : '00000008', 'name' : 'ESME_RSYSERR',          'description' : 'System Error'},
    'ESME_RINVSRCADR'       : {'hex' : '0000000a', 'name' : 'ESME_RINVSRCADR',       'description' : 'Invalid source address'},
    'ESME_RINVDSTADR'       : {'hex' : '0000000b', 'name' : 'ESME_RINVDSTADR',       'description' : 'Invalid destination address'},
    'ESME_RINVMSGID'        : {'hex' : '0000000c', 'name' : 'ESME_RINVMSGID',        'description' : 'Message ID is invalid'},
    'ESME_RBINDFAIL'        : {'hex' : '0000000d', 'name' : 'ESME_RBINDFAIL',        'description' : 'Bind failed'},
    'ESME_RINVPASWD'        : {'hex' : '0000000e', 'name' : 'ESME_RINVPASWD',        'description' : 'Invalid password'},
    'ESME_RINVSYSID'        : {'hex' : '0000000f', 'name' : 'ESME_RINVSYSID',        'description' : 'Invalid System ID'},
    'ESME_RCANCELFAIL'      : {'hex' : '00000011', 'name' : 'ESME_RCANCELFAIL',      'description' : 'Cancel SM Failed'},
    'ESME_RREPLACEFAIL'     : {'hex' : '00000013', 'name' : 'ESME_RREPLACEFAIL',     'description' : 'Replace SM Failed'},
    'ESME_RMSGQFUL'         : {'hex' : '00000014', 'name' : 'ESME_RMSGQFUL',         'description' : 'Message queue full'},
    'ESME_RINVSERTYP'       : {'hex' : '00000015', 'name' : 'ESME_RINVSERTYP',       'description' : 'Invalid service type'},
    'ESME_RINVNUMDESTS'     : {'hex' : '00000033', 'name' : 'ESME_RINVNUMDESTS',     'description' : 'Invalid number of destinations'},
    'ESME_RINVDLNAME'       : {'hex' : '00000034', 'name' : 'ESME_RINVDLNAME',       'description' : 'Invalid distribution list name'},
    'ESME_RINVDESTFLAG'     : {'hex' : '00000040', 'name' : 'ESME_RINVDESTFLAG',     'description' : 'Destination flag is invalid (submit_multi)'},
    'ESME_RINVSUBREP'       : {'hex' : '00000042', 'name' : 'ESME_RINVSUBREP',       'description' : "Invalid `submit with replace' request (i.e. submit_sm with replace_if_present_flag set)"},
    'ESME_RINVESMCLASS'     : {'hex' : '00000043', 'name' : 'ESME_RINVESMCLASS',     'description' : 'Invalid esm_class field data'},
    'ESME_RCNTSUBDL'        : {'hex' : '00000044', 'name' : 'ESME_RCNTSUBDL',        'description' : 'Cannot submit to distribution list'},
    'ESME_RSUBMITFAIL'      : {'hex' : '00000045', 'name' : 'ESME_RSUBMITFAIL',      'description' : 'submit_sm or submit_multi failed'},
    'ESME_RINVSRCTON'       : {'hex' : '00000048', 'name' : 'ESME_RINVSRCTON',       'description' : 'Invalid source address TON'},
    'ESME_RINVSRCNPI'       : {'hex' : '00000049', 'name' : 'ESME_RINVSRCNPI',       'description' : 'Invalid source address NPI'},
    'ESME_RINVDSTTON'       : {'hex' : '00000050', 'name' : 'ESME_RINVDSTTON',       'description' : 'Invalid destination address TON'},
    'ESME_RINVDSTNPI'       : {'hex' : '00000051', 'name' : 'ESME_RINVDSTNPI',       'description' : 'Invalid destination address NPI'},
    'ESME_RINVSYSTYP'       : {'hex' : '00000053', 'name' : 'ESME_RINVSYSTYP',       'description' : 'Invalid system_type field'},
    'ESME_RINVREPFLAG'      : {'hex' : '00000054', 'name' : 'ESME_RINVREPFLAG',      'description' : 'Invalid replace_if_present flag'},
    'ESME_RINVNUMMSGS'      : {'hex' : '00000055', 'name' : 'ESME_RINVNUMMSGS',      'description' : 'Invalid number of messages'},
    'ESME_RTHROTTLED'       : {'hex' : '00000058', 'name' : 'ESME_RTHROTTLED',       'description' : 'Throttling error (ESME has exceeded allowed message limits)'},
    'ESME_RINVSCHED'        : {'hex' : '00000061', 'name' : 'ESME_RINVSCHED',        'description' : 'Invalid scheduled delivery time'},
    'ESME_RINVEXPIRY'       : {'hex' : '00000062', 'name' : 'ESME_RINVEXPIRY',       'description' : 'Invalid message validity period (expiry time)'},
    'ESME_RINVDFTMSGID'     : {'hex' : '00000063', 'name' : 'ESME_RINVDFTMSGID',     'description' : 'Predefined message invalid or not found'},
    'ESME_RX_T_APPN'        : {'hex' : '00000064', 'name' : 'ESME_RX_T_APPN',        'description' : 'ESME Receiver Temporary App Error Code'},
    'ESME_RX_P_APPN'        : {'hex' : '00000065', 'name' : 'ESME_RX_P_APPN',        'description' : 'ESME Receiver Permanent App Error Code'},
    'ESME_RX_R_APPN'        : {'hex' : '00000066', 'name' : 'ESME_RX_R_APPN',        'description' : 'ESME Receiver Reject Message Error Code'},
    'ESME_RQUERYFAIL'       : {'hex' : '00000067', 'name' : 'ESME_RQUERYFAIL',       'description' : 'query_sm request failed'},
    'ESME_RINVOPTPARSTREAM' : {'hex' : '000000c0', 'name' : 'ESME_RINVOPTPARSTREAM', 'description' : 'Error in the optional part of the PDU Body'},
    'ESME_ROPTPARNOTALLWD'  : {'hex' : '000000c1', 'name' : 'ESME_ROPTPARNOTALLWD',  'description' : 'Optional paramenter not allowed'},
    'ESME_RINVPARLEN'       : {'hex' : '000000c2', 'name' : 'ESME_RINVPARLEN',       'description' : 'Invalid parameter length'},
    'ESME_RMISSINGOPTPARAM' : {'hex' : '000000c3', 'name' : 'ESME_RMISSINGOPTPARAM', 'description' : 'Expected optional parameter missing'},
    'ESME_RINVOPTPARAMVAL'  : {'hex' : '000000c4', 'name' : 'ESME_RINVOPTPARAMVAL',  'description' : 'Invalid optional parameter value'},
    'ESME_RDELIVERYFAILURE' : {'hex' : '000000fe', 'name' : 'ESME_RDELIVERYFAILURE', 'description' : 'Delivery Failure (used for data_sm_resp)'},
    'ESME_RUNKNOWNERR'      : {'hex' : '000000ff', 'name' : 'ESME_RUNKNOWNERR',      'description' : 'Unknown error'}
}

def command_status_hex_by_name(n):
    return command_status_by_name.get(n,{}).get('hex')


# Type of Number (TON) - SMPP v3.4, section 5.2.5, table 5-3, page 117

addr_ton_by_name = {
    'unknown'           : '00',
    'international'     : '01',
    'national'          : '02',
    'network_specific'  : '03',
    'subscriber_number' : '04',
    'alphanumeric'      : '05',
    'abbreviated'       : '06'
}

addr_ton_by_hex = {
    '00' : 'unknown',
    '01' : 'international',
    '02' : 'national',
    '03' : 'network_specific',
    '04' : 'subscriber_number',
    '05' : 'alphanumeric',
    '06' : 'abbreviated'
}

# Numberic Plan Indicator (NPI) - SMPP v3.4, section 5.2.6, table 5-4, page 118

addr_npi_by_name = {
    'unknown'     : '00',
    'ISDN'        : '01',
    'data'        : '03',
    'telex'       : '04',
    'land_mobile' : '06',
    'national'    : '08',
    'private'     : '09',
    'ERMES'       : '0a',
    'internet'    : '0e',
    'WAP'         : '12'
}

addr_npi_by_hex = {
    '00' : 'unknown',
    '01' : 'ISDN',
    '03' : 'data',
    '04' : 'telex',
    '06' : 'land_mobile',
    '08' : 'national',
    '09' : 'private',
    '0a' : 'ERMES',
    '0e' : 'internet',
    '12' : 'WAP'
}


# ESM Class bits  - SMPP v3.4, section 5.2.12, page 121

esm_class_bits = {
    'mode_mask'                   : '03',
    'type_mask'                   : '3c',
    'feature_mask'                : 'c0',

    'mode_default'                : '00',
    'mode_datagram'               : '01',
    'mode_forward'                : '02',
    'mode_store_and_forward'      : '03',

    'type_default'                : '00',
    'type_delivery_receipt'       : '04',
    'type_delivery_ack'           : '08',
    'type_0011'                   : '0a',
    'type_user_ack'               : '10',
    'type_0101'                   : '14',
    'type_conversation_abort'     : '18',
    'type_0111'                   : '1a',
    'type_intermed_deliv_notif'   : '20',
    'type_1001'                   : '24',
    'type_1010'                   : '28',
    'type_1011'                   : '2a',
    'type_1100'                   : '30',
    'type_1101'                   : '34',
    'type_1110'                   : '38',
    'type_1111'                   : '3a',

    'feature_none'                : '00',
    'feature_UDHI'                : '40',
    'feature_reply_path'          : '80',
    'feature_UDHI_and_reply_path' : 'c0'
}


# Registered Delivery bits - SMPP v3.4, section 5.2.17, page 124

registered_delivery_bits = {
    'receipt_mask'          : '03',
    'ack_mask'              : '0c',
    'intermed_notif_mask'   : '80',

    'receipt_none'          : '00',
    'receipt_always'        : '01',
    'receipt_on_fail'       : '02',
    'receipt_res'           : '03',

    'ack_none'              : '00',
    'ack_delivery'          : '04',
    'ack_user'              : '08',
    'ack_delivery_and_user' : '0c',

    'intermed_notif_none'   : '00',
    'intermed_notif'        : '10'
}


# submit_multi dest_flag constants - SMPP v3.4, section 5.2.25, page 129
dest_flag_by_name = {
    'SME_Address' : 1,
    'dist_list'   : 2
}


# Message State codes returned in query_sm_resp PDUs - SMPP v3.4, section 5.2.28, table 5-6, page 130
message_state_by_name = {
    'ENROUTE'       : 1,
    'DELIVERED'     : 2,
    'EXPIRED'       : 3,
    'DELETED'       : 4,
    'UNDELIVERABLE' : 5,
    'ACCEPTED'      : 6,
    'UNKNOWN'       : 7,
    'REJECTED'      : 8
}



# Facility Code bits for SMPP v4

facility_code_bits = {
    'GF_PVCY'    : '00000001',
    'GF_SUBADDR' : '00000002',
    'NF_CC'      : '00080000',
    'NF_PDC'     : '00010000',
    'NF_IS136'   : '00020000',
    'NF_IS95A'   : '00040000'
}


# Optional Parameter Tags - SMPP v3.4, section 5.3.2, Table 5-7, page 132-133

optional_parameter_tag_by_hex = {
    '0005' : {'hex' : '0005', 'name' : 'dest_addr_subunit',            'technology' : 'GSM'},
    '0006' : {'hex' : '0006', 'name' : 'dest_network_type',            'technology' : 'Generic'},
    '0007' : {'hex' : '0007', 'name' : 'dest_bearer_type',             'technology' : 'Generic'},
    '0008' : {'hex' : '0008', 'name' : 'dest_telematics_id',           'technology' : 'GSM'},

    '000d' : {'hex' : '000d', 'name' : 'source_addr_subunit',          'technology' : 'GSM'},
    '000e' : {'hex' : '000e', 'name' : 'source_network_type',          'technology' : 'Generic'},
    '000f' : {'hex' : '000f', 'name' : 'source_bearer_type',           'technology' : 'Generic'},
    '0010' : {'hex' : '0010', 'name' : 'source_telematics_id',         'technology' : 'GSM'},

    '0017' : {'hex' : '0017', 'name' : 'qos_time_to_live',             'technology' : 'Generic'},
    '0019' : {'hex' : '0019', 'name' : 'payload_type',                 'technology' : 'Generic'},
    '001d' : {'hex' : '001d', 'name' : 'additional_status_info_text',  'technology' : 'Generic'},
    '001e' : {'hex' : '001e', 'name' : 'receipted_message_id',         'technology' : 'Generic'},
    '0030' : {'hex' : '0030', 'name' : 'ms_msg_wait_facilities',       'technology' : 'GSM'},

    '0101' : {'hex' : '0101', 'name' : 'PVCY_AuthenticationStr',       'technology' : '? (J-Phone)'}, # v4 page 58-62

    '0201' : {'hex' : '0201', 'name' : 'privacy_indicator',            'technology' : 'CDMA,TDMA'},
    '0202' : {'hex' : '0202', 'name' : 'source_subaddress',            'technology' : 'CDMA,TDMA'}, # v4 page 65-67
    '0203' : {'hex' : '0203', 'name' : 'dest_subaddress',              'technology' : 'CDMA,TDMA'}, # v4 page 65-67
    '0204' : {'hex' : '0204', 'name' : 'user_message_reference',       'technology' : 'Generic'},
    '0205' : {'hex' : '0205', 'name' : 'user_response_code',           'technology' : 'CDMA,TDMA'},
    '020a' : {'hex' : '020a', 'name' : 'source_port',                  'technology' : 'WAP'},
    '020b' : {'hex' : '020b', 'name' : 'destination_port',             'technology' : 'WAP'},
    '020c' : {'hex' : '020c', 'name' : 'sar_msg_ref_num',              'technology' : 'Generic'},
    '020d' : {'hex' : '020d', 'name' : 'language_indicator',           'technology' : 'CDMA,TDMA'},
    '020e' : {'hex' : '020e', 'name' : 'sar_total_segments',           'technology' : 'Generic'},
    '020f' : {'hex' : '020f', 'name' : 'sar_segment_seqnum',           'technology' : 'Generic'},
    '0210' : {'hex' : '0210', 'name' : 'sc_interface_version',         'technology' : 'Generic'},

    '0301' : {'hex' : '0301', 'name' : 'CC_CBN',                       'technology' : 'V4'}, # v4 page 70
    '0302' : {'hex' : '0302', 'name' : 'callback_num_pres_ind',        'technology' : 'TDMA'}, # v4 page 71
    '0303' : {'hex' : '0303', 'name' : 'callback_num_atag',            'technology' : 'TDMA'}, # v4 page 71
    '0304' : {'hex' : '0304', 'name' : 'number_of_messages',           'technology' : 'CDMA'}, # v4 page 72
    '0381' : {'hex' : '0381', 'name' : 'callback_num',                 'technology' : 'CDMA,TDMA,GSM,iDEN'},

    '0420' : {'hex' : '0420', 'name' : 'dpf_result',                   'technology' : 'Generic'},
    '0421' : {'hex' : '0421', 'name' : 'set_dpf',                      'technology' : 'Generic'},
    '0422' : {'hex' : '0422', 'name' : 'ms_availability_status',       'technology' : 'Generic'},
    '0423' : {'hex' : '0423', 'name' : 'network_error_code',           'technology' : 'Generic'},
    '0424' : {'hex' : '0424', 'name' : 'message_payload',              'technology' : 'Generic'},
    '0425' : {'hex' : '0425', 'name' : 'delivery_failure_reason',      'technology' : 'Generic'},
    '0426' : {'hex' : '0426', 'name' : 'more_messages_to_send',        'technology' : 'GSM'},
    '0427' : {'hex' : '0427', 'name' : 'message_state',                'technology' : 'Generic'},
    '0428' : {'hex' : '0428', 'name' : 'congestion_state',             'technology' : 'Generic'},

    '0501' : {'hex' : '0501', 'name' : 'ussd_service_op',              'technology' : 'GSM (USSD)'},

    '0600' : {'hex' : '0600', 'name' : 'broadcast_channel_indicator',  'technology' : 'GSM'},
    '0601' : {'hex' : '0601', 'name' : 'broadcast_content_type',       'technology' : 'CDMA, TDMA, GSM'},
    '0602' : {'hex' : '0602', 'name' : 'broadcast_content_type_info',  'technology' : 'CDMA, TDMA'},
    '0603' : {'hex' : '0603', 'name' : 'broadcast_message_class',      'technology' : 'GSM'},
    '0604' : {'hex' : '0604', 'name' : 'broadcast_rep_num',            'technology' : 'GSM'},
    '0605' : {'hex' : '0605', 'name' : 'broadcast_frequency_interval', 'technology' : 'CDMA, TDMA, GSM'},
    '0606' : {'hex' : '0606', 'name' : 'broadcast_area_identifier',    'technology' : 'CDMA, TDMA, GSM'},
    '0607' : {'hex' : '0607', 'name' : 'broadcast_error_status',       'technology' : 'CDMA, TDMA, GSM'},
    '0608' : {'hex' : '0608', 'name' : 'broadcast_area_success',       'technology' : 'GSM'},
    '0609' : {'hex' : '0609', 'name' : 'broadcast_end_time',           'technology' : 'CDMA, TDMA, GSM'},
    '060a' : {'hex' : '060a', 'name' : 'broadcast_service_group',      'technology' : 'CDMA, TDMA'},
    '060b' : {'hex' : '060b', 'name' : 'billing_identification',       'technology' : 'Generic'},
    '060d' : {'hex' : '060d', 'name' : 'source_network_id',            'technology' : 'Generic'},
    '060e' : {'hex' : '060e', 'name' : 'dest_network_id',              'technology' : 'Generic'},
    '060f' : {'hex' : '060f', 'name' : 'source_node_id',               'technology' : 'Generic'},
    '0610' : {'hex' : '0610', 'name' : 'dest_node_id',                 'technology' : 'Generic'},
    '0611' : {'hex' : '0611', 'name' : 'dest_addr_np_resolution',      'technology' : 'CDMA, TDMA (US Only)'},
    '0612' : {'hex' : '0612', 'name' : 'dest_addr_np_information',     'technology' : 'CDMA, TDMA (US Only)'},
    '0613' : {'hex' : '0613', 'name' : 'dest_addr_np_country',         'technology' : 'CDMA, TDMA (US Only)'},

    '1201' : {'hex' : '1201', 'name' : 'display_time',                 'technology' : 'CDMA,TDMA'},
    '1203' : {'hex' : '1203', 'name' : 'sms_signal',                   'technology' : 'TDMA'},
    '1204' : {'hex' : '1204', 'name' : 'ms_validity',                  'technology' : 'CDMA,TDMA'},

    '1304' : {'hex' : '1304', 'name' : 'IS95A_AlertOnDelivery',        'technology' : 'CDMA'}, # v4 page 85
    '1306' : {'hex' : '1306', 'name' : 'IS95A_LanguageIndicator',      'technology' : 'CDMA'}, # v4 page 86
    '130c' : {'hex' : '130c', 'name' : 'alert_on_message_delivery',    'technology' : 'CDMA'},
    '1380' : {'hex' : '1380', 'name' : 'its_reply_type',               'technology' : 'CDMA'},
    '1383' : {'hex' : '1383', 'name' : 'its_session_info',             'technology' : 'CDMA Korean [KORITS]'},

    '1402' : {'hex' : '1402', 'name' : 'operator_id',                  'technology' : 'vendor extension'},
    '1403' : {'hex' : '1403', 'name' : 'tariff',                       'technology' : 'Mobile Network Code vendor extension'},
    '1450' : {'hex' : '1450', 'name' : 'mcc',                          'technology' : 'Mobile Country Code vendor extension'},
    '1451' : {'hex' : '1451', 'name' : 'mnc',                          'technology' : 'Mobile Network Code vendor extension'},

    '1101' : {'hex' : '1101', 'name' : 'PDC_MessageClass',             'technology' : '? (J-Phone)'}, # v4 page 75
    '1102' : {'hex' : '1102', 'name' : 'PDC_PresentationOption',       'technology' : '? (J-Phone)'}, # v4 page 76
    '1103' : {'hex' : '1103', 'name' : 'PDC_AlertMechanism',           'technology' : '? (J-Phone)'}, # v4 page 76
    '1104' : {'hex' : '1104', 'name' : 'PDC_Teleservice',              'technology' : '? (J-Phone)'}, # v4 page 77
    '1105' : {'hex' : '1105', 'name' : 'PDC_MultiPartMessage',         'technology' : '? (J-Phone)'}, # v4 page 77
    '1106' : {'hex' : '1106', 'name' : 'PDC_PredefinedMsg',            'technology' : '? (J-Phone)'} # v4 page 78
}

def optional_parameter_tag_name_by_hex(x):
    return optional_parameter_tag_by_hex.get(x,{}).get('name')

optional_parameter_tag_by_name = {
    'dest_addr_subunit'            : {'hex' : '0005', 'name' : 'dest_addr_subunit',            'technology' : 'GSM'},
    'dest_network_type'            : {'hex' : '0006', 'name' : 'dest_network_type',            'technology' : 'Generic'},
    'dest_bearer_type'             : {'hex' : '0007', 'name' : 'dest_bearer_type',             'technology' : 'Generic'},
    'dest_telematics_id'           : {'hex' : '0008', 'name' : 'dest_telematics_id',           'technology' : 'GSM'},

    'source_addr_subunit'          : {'hex' : '000d', 'name' : 'source_addr_subunit',          'technology' : 'GSM'},
    'source_network_type'          : {'hex' : '000e', 'name' : 'source_network_type',          'technology' : 'Generic'},
    'source_bearer_type'           : {'hex' : '000f', 'name' : 'source_bearer_type',           'technology' : 'Generic'},
    'source_telematics_id'         : {'hex' : '0010', 'name' : 'source_telematics_id',         'technology' : 'GSM'},

    'qos_time_to_live'             : {'hex' : '0017', 'name' : 'qos_time_to_live',             'technology' : 'Generic'},
    'payload_type'                 : {'hex' : '0019', 'name' : 'payload_type',                 'technology' : 'Generic'},
    'additional_status_info_text'  : {'hex' : '001d', 'name' : 'additional_status_info_text',  'technology' : 'Generic'},
    'receipted_message_id'         : {'hex' : '001e', 'name' : 'receipted_message_id',         'technology' : 'Generic'},
    'ms_msg_wait_facilities'       : {'hex' : '0030', 'name' : 'ms_msg_wait_facilities',       'technology' : 'GSM'},

    'PVCY_AuthenticationStr'       : {'hex' : '0101', 'name' : 'PVCY_AuthenticationStr',       'technology' : '? (J-Phone)'}, # v4 page 58-62

    'privacy_indicator'            : {'hex' : '0201', 'name' : 'privacy_indicator',            'technology' : 'CDMA,TDMA'},
    'source_subaddress'            : {'hex' : '0202', 'name' : 'source_subaddress',            'technology' : 'CDMA,TDMA'}, # v4 page 65-67
    'dest_subaddress'              : {'hex' : '0203', 'name' : 'dest_subaddress',              'technology' : 'CDMA,TDMA'}, # v4 page 65-67
    'user_message_reference'       : {'hex' : '0204', 'name' : 'user_message_reference',       'technology' : 'Generic'},
    'user_response_code'           : {'hex' : '0205', 'name' : 'user_response_code',           'technology' : 'CDMA,TDMA'},
    'source_port'                  : {'hex' : '020a', 'name' : 'source_port',                  'technology' : 'WAP'},
    'destination_port'             : {'hex' : '020b', 'name' : 'destination_port',             'technology' : 'WAP'},
    'sar_msg_ref_num'              : {'hex' : '020c', 'name' : 'sar_msg_ref_num',              'technology' : 'Generic'},
    'language_indicator'           : {'hex' : '020d', 'name' : 'language_indicator',           'technology' : 'CDMA,TDMA'},
    'sar_total_segments'           : {'hex' : '020e', 'name' : 'sar_total_segments',           'technology' : 'Generic'},
    'sar_segment_seqnum'           : {'hex' : '020f', 'name' : 'sar_segment_seqnum',           'technology' : 'Generic'},
    'sc_interface_version'         : {'hex' : '0210', 'name' : 'sc_interface_version',         'technology' : 'Generic'},

    'CC_CBN'                       : {'hex' : '0301', 'name' : 'CC_CBN',                       'technology' : 'V4'}, # v4 page 70
    'callback_num_pres_ind'        : {'hex' : '0302', 'name' : 'callback_num_pres_ind',        'technology' : 'TDMA'}, # v4 page 71
    'callback_num_atag'            : {'hex' : '0303', 'name' : 'callback_num_atag',            'technology' : 'TDMA'}, # v4 page 71
    'number_of_messages'           : {'hex' : '0304', 'name' : 'number_of_messages',           'technology' : 'CDMA'}, # v4 page 72
    'callback_num'                 : {'hex' : '0381', 'name' : 'callback_num',                 'technology' : 'CDMA,TDMA,GSM,iDEN'},

    'dpf_result'                   : {'hex' : '0420', 'name' : 'dpf_result',                   'technology' : 'Generic'},
    'set_dpf'                      : {'hex' : '0421', 'name' : 'set_dpf',                      'technology' : 'Generic'},
    'ms_availability_status'       : {'hex' : '0422', 'name' : 'ms_availability_status',       'technology' : 'Generic'},
    'network_error_code'           : {'hex' : '0423', 'name' : 'network_error_code',           'technology' : 'Generic'},
    'message_payload'              : {'hex' : '0424', 'name' : 'message_payload',              'technology' : 'Generic'},
    'delivery_failure_reason'      : {'hex' : '0425', 'name' : 'delivery_failure_reason',      'technology' : 'Generic'},
    'more_messages_to_send'        : {'hex' : '0426', 'name' : 'more_messages_to_send',        'technology' : 'GSM'},
    'message_state'                : {'hex' : '0427', 'name' : 'message_state',                'technology' : 'Generic'},
    'congestion_state'             : {'hex' : '0428', 'name' : 'congestion_state',             'technology' : 'Generic'},

    'ussd_service_op'              : {'hex' : '0501', 'name' : 'ussd_service_op',              'technology' : 'GSM (USSD)'},

    'broadcast_channel_indicator'  : {'hex' : '0600', 'name' : 'broadcast_channel_indicator',  'technology' : 'GSM'},
    'broadcast_content_type'       : {'hex' : '0601', 'name' : 'broadcast_content_type',       'technology' : 'CDMA, TDMA, GSM'},
    'broadcast_content_type_info'  : {'hex' : '0602', 'name' : 'broadcast_content_type_info',  'technology' : 'CDMA, TDMA'},
    'broadcast_message_class'      : {'hex' : '0603', 'name' : 'broadcast_message_class',      'technology' : 'GSM'},
    'broadcast_rep_num'            : {'hex' : '0604', 'name' : 'broadcast_rep_num',            'technology' : 'GSM'},
    'broadcast_frequency_interval' : {'hex' : '0605', 'name' : 'broadcast_frequency_interval', 'technology' : 'CDMA, TDMA, GSM'},
    'broadcast_area_identifier'    : {'hex' : '0606', 'name' : 'broadcast_area_identifier',    'technology' : 'CDMA, TDMA, GSM'},
    'broadcast_error_status'       : {'hex' : '0607', 'name' : 'broadcast_error_status',       'technology' : 'CDMA, TDMA, GSM'},
    'broadcast_area_success'       : {'hex' : '0608', 'name' : 'broadcast_area_success',       'technology' : 'GSM'},
    'broadcast_end_time'           : {'hex' : '0609', 'name' : 'broadcast_end_time',           'technology' : 'CDMA, TDMA, GSM'},
    'broadcast_service_group'      : {'hex' : '060a', 'name' : 'broadcast_service_group',      'technology' : 'CDMA, TDMA'},
    'billing_identification'       : {'hex' : '060b', 'name' : 'billing_identification',       'technology' : 'Generic'},
    'source_network_id'            : {'hex' : '060d', 'name' : 'source_network_id',            'technology' : 'Generic'},
    'dest_network_id'              : {'hex' : '060e', 'name' : 'dest_network_id',              'technology' : 'Generic'},
    'source_node_id'               : {'hex' : '060f', 'name' : 'source_node_id',               'technology' : 'Generic'},
    'dest_node_id'                 : {'hex' : '0610', 'name' : 'dest_node_id',                 'technology' : 'Generic'},
    'dest_addr_np_resolution'      : {'hex' : '0611', 'name' : 'dest_addr_np_resolution',      'technology' : 'CDMA, TDMA (US Only)'},
    'dest_addr_np_information'     : {'hex' : '0612', 'name' : 'dest_addr_np_information',     'technology' : 'CDMA, TDMA (US Only)'},
    'dest_addr_np_country'         : {'hex' : '0613', 'name' : 'dest_addr_np_country',         'technology' : 'CDMA, TDMA (US Only)'},

    'display_time'                 : {'hex' : '1201', 'name' : 'display_time',                 'technology' : 'CDMA,TDMA'},
    'sms_signal'                   : {'hex' : '1203', 'name' : 'sms_signal',                   'technology' : 'TDMA'},
    'ms_validity'                  : {'hex' : '1204', 'name' : 'ms_validity',                  'technology' : 'CDMA,TDMA'},

    'IS95A_AlertOnDelivery'        : {'hex' : '1304', 'name' : 'IS95A_AlertOnDelivery',        'technology' : 'CDMA'}, # v4 page 85
    'IS95A_LanguageIndicator'      : {'hex' : '1306', 'name' : 'IS95A_LanguageIndicator',      'technology' : 'CDMA'}, # v4 page 86
    'alert_on_message_delivery'    : {'hex' : '130c', 'name' : 'alert_on_message_delivery',    'technology' : 'CDMA'},
    'its_reply_type'               : {'hex' : '1380', 'name' : 'its_reply_type',               'technology' : 'CDMA'},
    'its_session_info'             : {'hex' : '1383', 'name' : 'its_session_info',             'technology' : 'CDMA Korean [KORITS]'},

    'operator_id'                  : {'hex' : '1402', 'name' : 'operator_id',                  'technology' : 'vendor extension'},
    'tariff'                       : {'hex' : '1403', 'name' : 'tariff',                       'technology' : 'Mobile Network Code vendor extension'},
    'mcc'                          : {'hex' : '1450', 'name' : 'mcc',                          'technology' : 'Mobile Country Code vendor extension'},
    'mnc'                          : {'hex' : '1451', 'name' : 'mnc',                          'technology' : 'Mobile Network Code vendor extension'},

    'PDC_MessageClass'             : {'hex' : '1101', 'name' : 'PDC_MessageClass',             'technology' : '? (J-Phone)'}, # v4 page 75
    'PDC_PresentationOption'       : {'hex' : '1102', 'name' : 'PDC_PresentationOption',       'technology' : '? (J-Phone)'}, # v4 page 76
    'PDC_AlertMechanism'           : {'hex' : '1103', 'name' : 'PDC_AlertMechanism',           'technology' : '? (J-Phone)'}, # v4 page 76
    'PDC_Teleservice'              : {'hex' : '1104', 'name' : 'PDC_Teleservice',              'technology' : '? (J-Phone)'}, # v4 page 77
    'PDC_MultiPartMessage'         : {'hex' : '1105', 'name' : 'PDC_MultiPartMessage',         'technology' : '? (J-Phone)'}, # v4 page 77
    'PDC_PredefinedMsg'            : {'hex' : '1106', 'name' : 'PDC_PredefinedMsg',            'technology' : '? (J-Phone)'} # v4 page 78
}

def optional_parameter_tag_hex_by_name(n):
    return optional_parameter_tag_by_name.get(n,{}).get('hex')


def decode_optional_parameters(optional_parameters_hex):
    optional_parameters = []
    data = optional_parameters_hex
    while len(data) > 0:
        (tag_hex, length_hex, rest) = (data[0:4], data[4:8], data[8: ])
        tag = optional_parameter_tag_name_by_hex(tag_hex)
        length = int(length_hex, 16)
        (value_hex, tail) = (rest[0:length*2], rest[length*2: ])
        if len(value_hex) == 0:
            value = 0 #TODO remove after testing
        else:
            value = int(value_hex, 16) #TODO need decoding mapping
        data = tail
        optional_parameters.append({'tag':tag, 'length':length, 'value':value})
    return optional_parameters


mandatory_parameter_lists = {
    'submit_sm' : [ # SMPP v3.4, section 4.4.1, table 4-10, page 59-61
        {'name':'service_type',            'min':1, 'max':6,  'var':True,  'type':'string',  'hex_map':None},
        {'name':'source_addr_ton',         'min':1, 'max':1,  'var':False, 'type':None,      'hex_map':addr_ton_by_hex},
        {'name':'source_addr_npi',         'min':1, 'max':1,  'var':False, 'type':None,      'hex_map':addr_npi_by_hex},
        {'name':'source_addr',             'min':1, 'max':21, 'var':True,  'type':'string',  'hex_map':None},
        {'name':'dest_addr_ton',           'min':1, 'max':1,  'var':False, 'type':None,      'hex_map':addr_ton_by_hex},
        {'name':'dest_addr_npi',           'min':1, 'max':1,  'var':False, 'type':None,      'hex_map':addr_npi_by_hex},
        {'name':'destination_addr',        'min':1, 'max':21, 'var':True,  'type':'string',  'hex_map':None},
        {'name':'esm_class',               'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'protocol_id',             'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'priority_flag',           'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'schedule_delivery_time',  'min':1, 'max':17, 'var':False, 'type':'string',  'hex_map':None},
        {'name':'validity_period',         'min':1, 'max':17, 'var':False, 'type':'string',  'hex_map':None},
        {'name':'registered_delivery',     'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'replace_if_present_flag', 'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'data_coding',             'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'sm_default_msg_id',       'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None},
        {'name':'sm_length',               'min':1, 'max':1,  'var':False, 'type':'integer', 'hex_map':None}
    ]
}


def decode_mandatory_parameters(fields, source):
    mandatory_parameters = {}
    for field in fields:
        data = ''
        octet = ''
        count = 0
        while (len(source[0]) > 1
                and (count < field['min']
                    or (count < field['max']
                        and (octet != '00')))):
            octet = octpop(source)
            data += octet
            count += 1
        if field['hex_map'] != None:
            mandatory_parameters[field['name']] = field.get('hex_map',{data:data})[data]
        else:
            mandatory_parameters[field['name']] = decode_hex_type(data, field['type'])
    if mandatory_parameters.get('sm_length', None) != None:
        short_message_hex = ''
        for i in range(mandatory_parameters['sm_length']):
            short_message_hex += octpop(source)
        mandatory_parameters['short_message'] = decode_hex_type(short_message_hex, 'string')
    return (mandatory_parameters, source[0])


# Command IDs - SMPP v3.4, section 5.1.2.1, table 5-1, page 110-111

def decode_empty(pdu, body_hex): print 'empty'; return (None, body_hex)
def decode_bind(pdu, body_hex): print 'bind'; return (None, body_hex)
def decode_bind_resp_v34(pdu, body_hex): print 'bind_resp_v34'; return (None, body_hex)
def decode_query_v34(pdu, body_hex): print 'query_v34'; return (None, body_hex)
def decode_query_resp_v34(pdu, body_hex): print 'query_resp_v34'; return (None, body_hex)

def decode_submit_v34(pdu, body_hex):
    print 'submit_v34'
    source = [body_hex]
    fields = mandatory_parameter_lists['submit_sm']
    return decode_mandatory_parameters(fields, source)

def decode_submit_resp_v34(pdu, body_hex): print 'submit_resp_v34'; return (None, body_hex)
def decode_replace_sm_v34(pdu, body_hex): print 'replace_sm_v34'; return (None, body_hex)
def decode_cancel(pdu, body_hex): print 'cancel'; return (None, body_hex)
def decode_outbind_v34(pdu, body_hex): print 'outbind_v34'; return (None, body_hex)
def decode_submit_multi(pdu, body_hex): print 'submit_multi'; return (None, body_hex)
def decode_submit_multi_resp(pdu, body_hex): print 'submit_multi_resp'; return (None, body_hex)
def decode_alert_notification(pdu, body_hex): print 'alert_notification'; return (None, body_hex)
def decode_data_sm(pdu, body_hex): print 'data_sm'; return (None, body_hex)
def decode_bind_resp_v4(pdu, body_hex): print 'bind_resp_v4'; return (None, body_hex)
def decode_query_v4(pdu, body_hex): print 'query_v4'; return (None, body_hex)
def decode_query_resp_v4(pdu, body_hex): print 'query_resp_v4'; return (None, body_hex)
def decode_submit_v4(pdu, body_hex): print 'submit_v4'; return (None, body_hex)
def decode_submit_sm_resp_v4(pdu, body_hex): print 'submit_sm_resp_v4'; return (None, body_hex)
def decode_deliver_sm_v4(pdu, body_hex): print 'deliver_sm_v4'; return (None, body_hex)
def decode_replace_sm_v4(pdu, body_hex): print 'replace_sm_v4'; return (None, body_hex)
def decode_delivery_receipt(pdu, body_hex): print 'delivery_receipt'; return (None, body_hex)
def decode_outbind_v4(pdu, body_hex): print 'outbind_v4'; return (None, body_hex)

command_id_by_hex = {
    '80000000' : {'hex' : '80000000', 'name' : 'generic_nack',             'action' : decode_empty},
    '00000001' : {'hex' : '00000001', 'name' : 'bind_receiver',            'action' : decode_bind},
    '80000001' : {'hex' : '80000001', 'name' : 'bind_receiver_resp',       'action' : decode_bind_resp_v34},
    '00000002' : {'hex' : '00000002', 'name' : 'bind_transmitter',         'action' : decode_bind},
    '80000002' : {'hex' : '80000002', 'name' : 'bind_transmitter_resp',    'action' : decode_bind_resp_v34},
    '00000003' : {'hex' : '00000003', 'name' : 'query_sm',                 'action' : decode_query_v34},
    '80000003' : {'hex' : '80000003', 'name' : 'query_sm_resp',            'action' : decode_query_resp_v34},
    '00000004' : {'hex' : '00000004', 'name' : 'submit_sm',                'action' : decode_submit_v34},
    '80000004' : {'hex' : '80000004', 'name' : 'submit_sm_resp',           'action' : decode_submit_resp_v34},
    '00000005' : {'hex' : '00000005', 'name' : 'deliver_sm',               'action' : decode_submit_v34},
    '80000005' : {'hex' : '80000005', 'name' : 'deliver_sm_resp',          'action' : decode_submit_resp_v34},
    '00000006' : {'hex' : '00000006', 'name' : 'unbind',                   'action' : decode_empty},
    '80000006' : {'hex' : '80000006', 'name' : 'unbind_resp',              'action' : decode_empty},
    '00000007' : {'hex' : '00000007', 'name' : 'replace_sm',               'action' : decode_replace_sm_v34},
    '80000007' : {'hex' : '80000007', 'name' : 'replace_sm_resp',          'action' : decode_empty},
    '00000008' : {'hex' : '00000008', 'name' : 'cancel_sm',                'action' : decode_cancel},
    '80000008' : {'hex' : '80000008', 'name' : 'cancel_sm_resp',           'action' : decode_empty},
    '00000009' : {'hex' : '00000009', 'name' : 'bind_transceiver',         'action' : decode_bind},
    '80000009' : {'hex' : '80000009', 'name' : 'bind_transceiver_resp',    'action' : decode_bind_resp_v34},
    '0000000b' : {'hex' : '0000000b', 'name' : 'outbind',                  'action' : decode_outbind_v34},
    '00000015' : {'hex' : '00000015', 'name' : 'enquire_link',             'action' : decode_empty},
    '80000015' : {'hex' : '80000015', 'name' : 'enquire_link_resp',        'action' : decode_empty},
    '00000021' : {'hex' : '00000021', 'name' : 'submit_multi',             'action' : decode_submit_multi},
    '80000021' : {'hex' : '80000021', 'name' : 'submit_multi_resp',        'action' : decode_submit_multi_resp},
    '00000102' : {'hex' : '00000102', 'name' : 'alert_notification',       'action' : decode_alert_notification},
    '00000103' : {'hex' : '00000103', 'name' : 'data_sm',                  'action' : decode_data_sm},
    '80000103' : {'hex' : '80000103', 'name' : 'data_sm_resp',             'action' : decode_submit_resp_v34},

               # v4 codes

    '80010000' : {'hex' : '80010000', 'name' : 'generic_nack_v4',          'action' : decode_empty},
    '00010001' : {'hex' : '00010001', 'name' : 'bind_receiver_v4',         'action' : decode_bind},
    '80010001' : {'hex' : '80010001', 'name' : 'bind_receiver_resp_v4',    'action' : decode_bind_resp_v4},
    '00010002' : {'hex' : '00010002', 'name' : 'bind_transmitter_v4',      'action' : decode_bind},
    '80010002' : {'hex' : '80010002', 'name' : 'bind_transmitter_resp_v4', 'action' : decode_bind_resp_v4},
    '00010003' : {'hex' : '00010003', 'name' : 'query_sm_v4',              'action' : decode_query_v4},
    '80010003' : {'hex' : '80010003', 'name' : 'query_sm_resp_v4',         'action' : decode_query_resp_v4},
    '00010004' : {'hex' : '00010004', 'name' : 'submit_sm_v4',             'action' : decode_submit_v4},
    '80010004' : {'hex' : '80010004', 'name' : 'submit_sm_resp_v4',        'action' : decode_submit_sm_resp_v4},
    '00010005' : {'hex' : '00010005', 'name' : 'deliver_sm_v4',            'action' : decode_deliver_sm_v4},
    '80010005' : {'hex' : '80010005', 'name' : 'deliver_sm_resp_v4',       'action' : decode_empty},
    '00010006' : {'hex' : '00010006', 'name' : 'unbind_v4',                'action' : decode_empty},
    '80010006' : {'hex' : '80010006', 'name' : 'unbind_resp_v4',           'action' : decode_empty},
    '00010007' : {'hex' : '00010007', 'name' : 'replace_sm_v4',            'action' : decode_replace_sm_v4},
    '80010007' : {'hex' : '80010007', 'name' : 'replace_sm_resp_v4',       'action' : decode_empty},
    '00010008' : {'hex' : '00010008', 'name' : 'cancel_sm_v4',             'action' : decode_cancel},
    '80010008' : {'hex' : '80010008', 'name' : 'cancel_sm_resp_v4',        'action' : decode_empty},
    '00010009' : {'hex' : '00010009', 'name' : 'delivery_receipt_v4',      'action' : decode_delivery_receipt},
    '80010009' : {'hex' : '80010009', 'name' : 'delivery_receipt_resp_v4', 'action' : decode_empty},
    '0001000a' : {'hex' : '0001000a', 'name' : 'enquire_link_v4',          'action' : decode_empty},
    '8001000a' : {'hex' : '8001000a', 'name' : 'enquire_link_resp_v4',     'action' : decode_empty},
    '0001000b' : {'hex' : '0001000b', 'name' : 'outbind_v4',               'action' : decode_outbind_v4}
}

def command_id_name_by_hex(x):
    return command_id_by_hex.get(x,{}).get('name')

def command_id_action_by_hex(x):
    return command_id_by_hex.get(x,{}).get('action')

command_id_by_name = {
    'generic_nack'             : {'hex' : '80000000', 'name' : 'generic_nack',             'action' : decode_empty},
    'bind_receiver'            : {'hex' : '00000001', 'name' : 'bind_receiver',            'action' : decode_bind},
    'bind_receiver_resp'       : {'hex' : '80000001', 'name' : 'bind_receiver_resp',       'action' : decode_bind_resp_v34},
    'bind_transmitter'         : {'hex' : '00000002', 'name' : 'bind_transmitter',         'action' : decode_bind},
    'bind_transmitter_resp'    : {'hex' : '80000002', 'name' : 'bind_transmitter_resp',    'action' : decode_bind_resp_v34},
    'query_sm'                 : {'hex' : '00000003', 'name' : 'query_sm',                 'action' : decode_query_v34},
    'query_sm_resp'            : {'hex' : '80000003', 'name' : 'query_sm_resp',            'action' : decode_query_resp_v34},
    'submit_sm'                : {'hex' : '00000004', 'name' : 'submit_sm',                'action' : decode_submit_v34},
    'submit_sm_resp'           : {'hex' : '80000004', 'name' : 'submit_sm_resp',           'action' : decode_submit_resp_v34},
    'deliver_sm'               : {'hex' : '00000005', 'name' : 'deliver_sm',               'action' : decode_submit_v34},
    'deliver_sm_resp'          : {'hex' : '80000005', 'name' : 'deliver_sm_resp',          'action' : decode_submit_resp_v34},
    'unbind'                   : {'hex' : '00000006', 'name' : 'unbind',                   'action' : decode_empty},
    'unbind_resp'              : {'hex' : '80000006', 'name' : 'unbind_resp',              'action' : decode_empty},
    'replace_sm'               : {'hex' : '00000007', 'name' : 'replace_sm',               'action' : decode_replace_sm_v34},
    'replace_sm_resp'          : {'hex' : '80000007', 'name' : 'replace_sm_resp',          'action' : decode_empty},
    'cancel_sm'                : {'hex' : '00000008', 'name' : 'cancel_sm',                'action' : decode_cancel},
    'cancel_sm_resp'           : {'hex' : '80000008', 'name' : 'cancel_sm_resp',           'action' : decode_empty},
    'bind_transceiver'         : {'hex' : '00000009', 'name' : 'bind_transceiver',         'action' : decode_bind},
    'bind_transceiver_resp'    : {'hex' : '80000009', 'name' : 'bind_transceiver_resp',    'action' : decode_bind_resp_v34},
    'outbind'                  : {'hex' : '0000000b', 'name' : 'outbind',                  'action' : decode_outbind_v34},
    'enquire_link'             : {'hex' : '00000015', 'name' : 'enquire_link',             'action' : decode_empty},
    'enquire_link_resp'        : {'hex' : '80000015', 'name' : 'enquire_link_resp',        'action' : decode_empty},
    'submit_multi'             : {'hex' : '00000021', 'name' : 'submit_multi',             'action' : decode_submit_multi},
    'submit_multi_resp'        : {'hex' : '80000021', 'name' : 'submit_multi_resp',        'action' : decode_submit_multi_resp},
    'alert_notification'       : {'hex' : '00000102', 'name' : 'alert_notification',       'action' : decode_alert_notification},
    'data_sm'                  : {'hex' : '00000103', 'name' : 'data_sm',                  'action' : decode_data_sm},
    'data_sm_resp'             : {'hex' : '80000103', 'name' : 'data_sm_resp',             'action' : decode_submit_resp_v34},

                               # v4 codes

    'generic_nack_v4'          : {'hex' : '80010000', 'name' : 'generic_nack_v4',          'action' : decode_empty},
    'bind_receiver_v4'         : {'hex' : '00010001', 'name' : 'bind_receiver_v4',         'action' : decode_bind},
    'bind_receiver_resp_v4'    : {'hex' : '80010001', 'name' : 'bind_receiver_resp_v4',    'action' : decode_bind_resp_v4},
    'bind_transmitter_v4'      : {'hex' : '00010002', 'name' : 'bind_transmitter_v4',      'action' : decode_bind},
    'bind_transmitter_resp_v4' : {'hex' : '80010002', 'name' : 'bind_transmitter_resp_v4', 'action' : decode_bind_resp_v4},
    'query_sm_v4'              : {'hex' : '00010003', 'name' : 'query_sm_v4',              'action' : decode_query_v4},
    'query_sm_resp_v4'         : {'hex' : '80010003', 'name' : 'query_sm_resp_v4',         'action' : decode_query_resp_v4},
    'submit_sm_v4'             : {'hex' : '00010004', 'name' : 'submit_sm_v4',             'action' : decode_submit_v4},
    'submit_sm_resp_v4'        : {'hex' : '80010004', 'name' : 'submit_sm_resp_v4',        'action' : decode_submit_sm_resp_v4},
    'deliver_sm_v4'            : {'hex' : '00010005', 'name' : 'deliver_sm_v4',            'action' : decode_deliver_sm_v4},
    'deliver_sm_resp_v4'       : {'hex' : '80010005', 'name' : 'deliver_sm_resp_v4',       'action' : decode_empty},
    'unbind_v4'                : {'hex' : '00010006', 'name' : 'unbind_v4',                'action' : decode_empty},
    'unbind_resp_v4'           : {'hex' : '80010006', 'name' : 'unbind_resp_v4',           'action' : decode_empty},
    'replace_sm_v4'            : {'hex' : '00010007', 'name' : 'replace_sm_v4',            'action' : decode_replace_sm_v4},
    'replace_sm_resp_v4'       : {'hex' : '80010007', 'name' : 'replace_sm_resp_v4',       'action' : decode_empty},
    'cancel_sm_v4'             : {'hex' : '00010008', 'name' : 'cancel_sm_v4',             'action' : decode_cancel},
    'cancel_sm_resp_v4'        : {'hex' : '80010008', 'name' : 'cancel_sm_resp_v4',        'action' : decode_empty},
    'delivery_receipt_v4'      : {'hex' : '00010009', 'name' : 'delivery_receipt_v4',      'action' : decode_delivery_receipt},
    'delivery_receipt_resp_v4' : {'hex' : '80010009', 'name' : 'delivery_receipt_resp_v4', 'action' : decode_empty},
    'enquire_link_v4'          : {'hex' : '0001000a', 'name' : 'enquire_link_v4',          'action' : decode_empty},
    'enquire_link_resp_v4'     : {'hex' : '8001000a', 'name' : 'enquire_link_resp_v4',     'action' : decode_empty},
    'outbind_v4'               : {'hex' : '0001000b', 'name' : 'outbind_v4',               'action' : decode_outbind_v4}
}

def command_id_hex_by_name(n):
    return command_id_by_name.get(n,{}).get('hex')

def command_id_action_by_name(n):
    return command_id_by_name.get(n,{}).get('action')


def decode_body(pdu, body_hex):
    body = {}
    body['mandatory_parameters'] = None
    if pdu['command'] != None:
        (body['mandatory_parameters'], optional_parameters_hex) = command_id_action_by_name(pdu['command'])(pdu, body_hex)
    body['optional_parameters'] = decode_optional_parameters(optional_parameters_hex)
    return body


def encode_optional_parameter(tag, value):
    optional = ''
    tag_hex = optional_parameter_tag_hex_by_name(tag)
    if tag_hex != None:
        value_hex = '%02x' % value #TODO need encoding mapping
        length_hex = '%04x' % (len(value_hex)/2)
        optional = tag_hex + length_hex + value_hex
    return optional


def unpack_pdu(pdu_bin):
    pdu_hex = binascii.b2a_hex(pdu_bin)
    (command_length, command_id,    command_status,  sequence_number, body_hex) = \
    (pdu_hex[0:8],   pdu_hex[8:16], pdu_hex[16:24],  pdu_hex[24:32],  pdu_hex[32: ])
    length = int(command_length, 16)
    command = command_id_name_by_hex(command_id)
    status = command_status_name_by_hex(command_status)
    sequence = int(sequence_number, 16)

    print '\n--------incoming--------'
    print command_length, length
    print command_id, command
    print command_status, status
    print sequence_number, sequence
    print body_hex
    print pdu_hex
    print '------------------------\n'

    pdu = {}
    pdu['length'] = length
    pdu['command'] = command
    pdu['status'] = status
    pdu['sequence'] = sequence
    pdu['body'] = decode_body(pdu, body_hex)
    print pdu
    return pdu


def pack_pdu(command='bind_transmitter', status='ESME_ROK', sequence=0, body_hex=''):
    length = 16 + len(body_hex)/2
    command_length = '%08x' % length
    command_id = command_id_hex_by_name(command)
    command_status = command_status_hex_by_name(status)
    sequence_number = '%08x' % sequence
    pdu_hex = command_length + command_id + command_status + sequence_number + body_hex

    print '\n--------outgoing--------'
    print command_length, length
    print command_id, command
    print command_status, status
    print sequence_number, sequence
    print body_hex
    print pdu_hex
    print '------------------------\n'

    return binascii.a2b_hex(pdu_hex)


def json_to_pdu(json):
    body_hex = ''
    body = json.get('body', {})
    for opt in body.get('optional_parameters',[]):
        body_hex += encode_optional_parameter(opt['tag'], opt['value'])
    return pack_pdu(json['command'], json['status'], json['sequence'], body_hex)


