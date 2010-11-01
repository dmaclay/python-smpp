
########################################
pdu_json_0000000001 = '''{
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
                "value": null
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
}'''

########################################
pdu_json_0000000002 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "dest_address": [
                {
                    "dest_addr_npi": "ISDN", 
                    "dest_addr_ton": "international", 
                    "dest_flag": 1, 
                    "destination_addr": "e"
                }, 
                {
                    "dest_flag": 2, 
                    "dl_name": "f"
                }
            ], 
            "esm_class": 0, 
            "number_of_dests": 2, 
            "priority_flag": 0, 
            "protocol_id": 0, 
            "registered_delivery": 0, 
            "replace_if_present_flag": 0, 
            "schedule_delivery_time": "", 
            "service_type": "", 
            "short_message": null, 
            "sm_default_msg_id": 0, 
            "sm_length": 0, 
            "source_addr": "", 
            "source_addr_npi": "unknown", 
            "source_addr_ton": "unknown", 
            "validity_period": ""
        }, 
        "optional_parameters": [
            {
                "length": 2, 
                "tag": "dest_addr_subunit", 
                "value": 0
            }, 
            {
                "length": 4, 
                "tag": "0000", 
                "value": "00000000"
            }
        ]
    }, 
    "header": {
        "command_id": "submit_multi", 
        "command_length": 0, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000003 = '''{
    "body": {
        "mandatory_parameters": {
            "message_id": "", 
            "no_unsuccess": 2, 
            "unsuccess_sme": [
                {
                    "dest_addr_npi": "ISDN", 
                    "dest_addr_ton": "international", 
                    "destination_addr": "eee", 
                    "error_status_code": 0
                }, 
                {
                    "dest_addr_npi": "ISDN", 
                    "dest_addr_ton": "international", 
                    "destination_addr": "fff", 
                    "error_status_code": 0
                }
            ]
        }
    }, 
    "header": {
        "command_id": "submit_multi_resp", 
        "command_length": 0, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''
