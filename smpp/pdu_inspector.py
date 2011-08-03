
from pdu import *


def detect_multipart(pdu):
    to_msisdn = pdu['body']['mandatory_parameters']['destination_addr']
    from_msisdn = pdu['body']['mandatory_parameters']['source_addr']
    short_message = pdu['body']['mandatory_parameters']['short_message']
    optional_parameters = {}
    for d in pdu['body'].get('optional_parameters',[]):
        optional_parameters[d['tag']] = d['value']

    #print repr(pdu)

    try:
        mdict = {'multipart_type':'TLV'}
        mdict['to_msisdn'] = to_msisdn
        mdict['from_msisdn'] = from_msisdn
        mdict['reference_number'] = optional_parameters['sar_msg_ref_num']
        mdict['total_number'] = optional_parameters['sar_total_segments']
        mdict['part_number'] = optional_parameters['sar_segment_seqnum']
        mdict['part_message'] = short_message
        return mdict
    except:
        pass

    # all other multipart types will fail on short_message == None
    if short_message == None:
        return None

    if (short_message[0:1] == '\x00'
    and short_message[1:2] == '\x03'
    and len(short_message) >= 5):
        mdict = {'multipart_type':'SAR'}
        mdict['to_msisdn'] = to_msisdn
        mdict['from_msisdn'] = from_msisdn
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
        mdict['to_msisdn'] = to_msisdn
        mdict['from_msisdn'] = from_msisdn
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
        mdict['to_msisdn'] = to_msisdn
        mdict['from_msisdn'] = from_msisdn
        mdict['reference_number'] = int(binascii.b2a_hex(short_message[3:5]), 16)
        mdict['total_number'] = int(binascii.b2a_hex(short_message[5:6]), 16)
        mdict['part_number'] = int(binascii.b2a_hex(short_message[6:7]), 16)
        mdict['part_message'] = short_message[7:]
        return mdict

    return None


def multipart_key(multipart, delimiter='_'):
        key_list = []
        key_list.append(str(multipart.get('from_msisdn')))
        key_list.append(str(multipart.get('to_msisdn')))
        key_list.append(str(multipart.get('reference_number')))
        key_list.append(str(multipart.get('total_number')))
        return delimiter.join(key_list)


class MultipartMessage:

    def __init__(self, array=None):
        self.array = {}
        for k,v in (array or {}).items():
            self.array.update({int(k):v})

    def add_pdu(self, pdu):
        part = detect_multipart(pdu)
        if part:
            self.array[part['part_number']] = part
            return True
        else:
            return False

    def get_partial(self):
        items = self.array.items()
        message = ''.join([i[1]['part_message'] for i in items])
        to_msisdn = from_msisdn = ''
        if len(items):
            to_msisdn = items[0][1].get('to_msisdn')
            from_msisdn = items[0][1].get('from_msisdn')
        return {'to_msisdn':to_msisdn,
                'from_msisdn':from_msisdn,
                'message':message}

    def get_completed(self):
        items = self.array.items()
        if len(items) and len(items) == items[0][1].get('total_number'):
            return self.get_partial()
        return None

    def get_key(self, delimiter = '_'):
        items = self.array.items()
        if len(items):
            return multipart_key(items[0][1], delimiter)
        return None

    def get_array(self):
        return self.array





