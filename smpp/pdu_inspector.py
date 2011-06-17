
from pdu import *


def detect_multipart(pdu):
    short_message = pdu['body']['mandatory_parameters']['short_message']
    optional_parameters = {}
    for d in pdu['body'].get('optional_parameters',[]):
        optional_parameters[d['tag']] = d['value']

    #print repr(pdu)

    try:
        mdict = {'multipart_type':'TLV'}
        mdict['reference_number'] = optional_parameters['sar_msg_ref_num']
        mdict['total_number'] = optional_parameters['sar_total_segments']
        mdict['part_number'] = optional_parameters['sar_segment_seqnum']
        mdict['part_message'] = short_message
        return mdict
    except:
        pass

    if (short_message[0:1] == '\x00'
    and short_message[1:2] == '\x03'
    and len(short_message) >= 5):
        mdict = {'multipart_type':'SAR'}
        mdict['reference_number'] = int(binascii.b2a_hex(short_message[2:3]), 16)
        mdict['total_number'] = int(binascii.b2a_hex(short_message[3:4]), 16)
        mdict['part_number'] = int(binascii.b2a_hex(short_message[4:5]), 16)
        mdict['part_message'] = short_message[5:]
        return mdict

    if (short_message[0:1] == '\x05'
    and short_message[1:2] == '\x00'
    and short_message[2:3] == '\x03'
    and len(short_message) >= 6):
        mdict = {'multipart_type':'CSM'}
        mdict['reference_number'] = int(binascii.b2a_hex(short_message[3:4]), 16)
        mdict['total_number'] = int(binascii.b2a_hex(short_message[4:5]), 16)
        mdict['part_number'] = int(binascii.b2a_hex(short_message[5:6]), 16)
        mdict['part_message'] = short_message[6:]
        return mdict

    if (short_message[0:1] == '\x06'
    and short_message[1:2] == '\x00'
    and short_message[2:3] == '\x04'
    and len(short_message) >= 7):
        mdict = {'multipart_type':'CSM16'}
        mdict['reference_number'] = int(binascii.b2a_hex(short_message[3:5]), 16)
        mdict['total_number'] = int(binascii.b2a_hex(short_message[5:6]), 16)
        mdict['part_number'] = int(binascii.b2a_hex(short_message[6:7]), 16)
        mdict['part_message'] = short_message[7:]
        return mdict

    return None

