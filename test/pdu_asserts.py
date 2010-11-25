
########################################
pdu_json_0000000001 = '''{
    "body": {
        "mandatory_parameters": {
            "addr_npi": "ISDN", 
            "addr_ton": "international", 
            "address_range": "", 
            "interface_version": "34", 
            "password": "abc123", 
            "system_id": "test_system", 
            "system_type": ""
        }
    }, 
    "header": {
        "command_id": "bind_transmitter", 
        "command_length": 40, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000002 = '''{
    "body": {
        "mandatory_parameters": {
            "system_id": "test_system"
        }
    }, 
    "header": {
        "command_id": "bind_transmitter_resp", 
        "command_length": 28, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000003 = '''{
    "body": {
        "mandatory_parameters": {
            "addr_npi": "ISDN", 
            "addr_ton": "international", 
            "address_range": "", 
            "interface_version": "34", 
            "password": "abc123", 
            "system_id": "test_system", 
            "system_type": ""
        }
    }, 
    "header": {
        "command_id": "bind_receiver", 
        "command_length": 40, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000004 = '''{
    "body": {
        "mandatory_parameters": {
            "system_id": "test_system"
        }
    }, 
    "header": {
        "command_id": "bind_receiver_resp", 
        "command_length": 28, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000005 = '''{
    "body": {
        "mandatory_parameters": {
            "addr_npi": "ISDN", 
            "addr_ton": "international", 
            "address_range": "", 
            "interface_version": "34", 
            "password": "abc123", 
            "system_id": "test_system", 
            "system_type": ""
        }
    }, 
    "header": {
        "command_id": "bind_transceiver", 
        "command_length": 40, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000006 = '''{
    "body": {
        "mandatory_parameters": {
            "system_id": "test_system"
        }
    }, 
    "header": {
        "command_id": "bind_transceiver_resp", 
        "command_length": 28, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000007 = '''{
    "body": {
        "mandatory_parameters": {
            "password": "abc123", 
            "system_id": "test_system"
        }
    }, 
    "header": {
        "command_id": "outbind", 
        "command_length": 35, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000008 = '''{
    "header": {
        "command_id": "unbind", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000009 = '''{
    "header": {
        "command_id": "unbind_resp", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000010 = '''{
    "header": {
        "command_id": "generic_nack", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000011 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "dest_addr_npi": "ISDN", 
            "dest_addr_ton": "international", 
            "destination_addr": "", 
            "esm_class": 0, 
            "priority_flag": 0, 
            "protocol_id": 0, 
            "registered_delivery": 0, 
            "replace_if_present_flag": 0, 
            "schedule_delivery_time": "", 
            "service_type": "", 
            "short_message": "testing 123", 
            "sm_default_msg_id": 0, 
            "sm_length": 11, 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international", 
            "validity_period": ""
        }
    }, 
    "header": {
        "command_id": "submit_sm", 
        "command_length": 44, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000012 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "dest_addr_npi": "ISDN", 
            "dest_addr_ton": "international", 
            "destination_addr": "", 
            "esm_class": 0, 
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
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international", 
            "validity_period": ""
        }, 
        "optional_parameters": [
            {
                "length": 2, 
                "tag": "message_payload", 
                "value": "5666"
            }
        ]
    }, 
    "header": {
        "command_id": "submit_sm", 
        "command_length": 39, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000013 = '''{
    "body": {
        "mandatory_parameters": {
            "message_id": ""
        }
    }, 
    "header": {
        "command_id": "submit_sm_resp", 
        "command_length": 17, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000014 = '''{
    "header": {
        "command_id": "submit_sm_resp", 
        "command_length": 16, 
        "command_status": "ESME_RSYSERR", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000015 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "dest_address": [
                {
                    "dest_addr_npi": "ISDN", 
                    "dest_addr_ton": "international", 
                    "dest_flag": 1, 
                    "destination_addr": "the address"
                }, 
                {
                    "dest_flag": 2, 
                    "dl_name": "the list"
                }, 
                {
                    "dest_flag": 2, 
                    "dl_name": "the other list"
                }
            ], 
            "esm_class": 0, 
            "number_of_dests": 3, 
            "priority_flag": 0, 
            "protocol_id": 0, 
            "registered_delivery": 0, 
            "replace_if_present_flag": 0, 
            "schedule_delivery_time": "", 
            "service_type": "", 
            "short_message": "testing 123", 
            "sm_default_msg_id": 0, 
            "sm_length": 11, 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international", 
            "validity_period": ""
        }
    }, 
    "header": {
        "command_id": "submit_multi", 
        "command_length": 83, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000016 = '''{
    "body": {
        "mandatory_parameters": {
            "message_id": "", 
            "no_unsuccess": 2, 
            "unsuccess_sme": [
                {
                    "dest_addr_npi": "ISDN", 
                    "dest_addr_ton": "international", 
                    "destination_addr": "", 
                    "error_status_code": 0
                }, 
                {
                    "dest_addr_npi": "ISDN", 
                    "dest_addr_ton": "network_specific", 
                    "destination_addr": "555", 
                    "error_status_code": 0
                }
            ]
        }
    }, 
    "header": {
        "command_id": "submit_multi_resp", 
        "command_length": 35, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000017 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "dest_addr_npi": "ISDN", 
            "dest_addr_ton": "international", 
            "destination_addr": "", 
            "esm_class": 0, 
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
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international", 
            "validity_period": ""
        }
    }, 
    "header": {
        "command_id": "deliver_sm", 
        "command_length": 33, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000018 = '''{
    "body": {
        "mandatory_parameters": {
            "message_id": ""
        }
    }, 
    "header": {
        "command_id": "deliver_sm_resp", 
        "command_length": 17, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000019 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "dest_addr_npi": "ISDN", 
            "dest_addr_ton": "international", 
            "destination_addr": "", 
            "esm_class": 0, 
            "registered_delivery": 0, 
            "service_type": "", 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international"
        }, 
        "optional_parameters": [
            {
                "length": 0, 
                "tag": "message_payload", 
                "value": null
            }
        ]
    }, 
    "header": {
        "command_id": "data_sm", 
        "command_length": 30, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000020 = '''{
    "body": {
        "mandatory_parameters": {
            "message_id": ""
        }
    }, 
    "header": {
        "command_id": "data_sm_resp", 
        "command_length": 17, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000021 = '''{
    "body": {
        "mandatory_parameters": {
            "message_id": "", 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international"
        }
    }, 
    "header": {
        "command_id": "query_sm", 
        "command_length": 20, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000022 = '''{
    "body": {
        "mandatory_parameters": {
            "error_code": 0, 
            "final_date": "", 
            "message_id": "", 
            "message_state": 0
        }
    }, 
    "header": {
        "command_id": "query_sm_resp", 
        "command_length": 20, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000023 = '''{
    "body": {
        "mandatory_parameters": {
            "dest_addr_npi": "ISDN", 
            "dest_addr_ton": "international", 
            "destination_addr": "", 
            "message_id": "", 
            "service_type": "", 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international"
        }
    }, 
    "header": {
        "command_id": "cancel_sm", 
        "command_length": 24, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000024 = '''{
    "header": {
        "command_id": "cancel_sm_resp", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000025 = '''{
    "body": {
        "mandatory_parameters": {
            "data_coding": 0, 
            "message_id": "", 
            "registered_delivery": 0, 
            "replace_if_present_flag": 0, 
            "schedule_delivery_time": "", 
            "short_message": "is this an = sign?", 
            "sm_default_msg_id": 0, 
            "sm_length": 18, 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international", 
            "validity_period": ""
        }
    }, 
    "header": {
        "command_id": "replace_sm", 
        "command_length": 45, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000026 = '''{
    "header": {
        "command_id": "replace_sm_resp", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000027 = '''{
    "header": {
        "command_id": "enquire_link", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000028 = '''{
    "header": {
        "command_id": "enquire_link_resp", 
        "command_length": 16, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''

########################################
pdu_json_0000000029 = '''{
    "body": {
        "mandatory_parameters": {
            "esme_addr": "", 
            "esme_addr_npi": "unknown", 
            "esme_addr_ton": 9, 
            "source_addr": "", 
            "source_addr_npi": "ISDN", 
            "source_addr_ton": "international"
        }
    }, 
    "header": {
        "command_id": "alert_notification", 
        "command_length": 22, 
        "command_status": "ESME_ROK", 
        "sequence_number": 0
    }
}'''
