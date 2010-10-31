

pdu_objects = [
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transmitter',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
                'system_type':'',
                'interface_version':'34',
                'addr_ton':1,
                'addr_npi':1,
                'address_range':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transmitter_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_receiver',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
                'system_type':'',
                'interface_version':'34',
                'addr_ton':1,
                'addr_npi':1,
                'address_range':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_receiver_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transceiver',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
                'system_type':'',
                'interface_version':'34',
                'addr_ton':1,
                'addr_npi':1,
                'address_range':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'bind_transceiver_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'outbind',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'system_id':'test_system',
                'password':'abc123',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'unbind',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'unbind_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'generic_nack',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'testing 123',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':0,
                'short_message':None,
                # 'short_message' can be of zero length
            },
            'optional_parameters': [
                {
                    'tag':'message_payload',
                    'length':0,
                    'value':'5666',
                },
            ],
        },
    },
#]
#breaker = [
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_sm_resp',
            'command_status': 'ESME_RSYSERR',
            'sequence_number': 0,
        },
        # submit_sm_resp can have no body for failures
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_multi',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'number_of_dests':0,
                'dest_address':[
                    {
                        'dest_flag':1,
                        'dest_addr_ton':1,
                        'dest_addr_npi':1,
                        'destination_addr':'the address'
                    },
                    {
                        'dest_flag':2,
                        'dl_name':'the list',
                    },
                    {
                        'dest_flag':2,
                        'dl_name':'the other list',
                    },
                    #{}
                    ],
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'testing 123',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'submit_multi_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'no_unsuccess':5,
                'unsuccess_sme':[
                    {
                        'dest_addr_ton':1,
                        'dest_addr_npi':1,
                        'destination_addr':'',
                        'error_status_code':0,
                    },
                    {
                        'dest_addr_ton':3,
                        'dest_addr_npi':1,
                        'destination_addr':'555',
                        'error_status_code':0,
                    },
                ],
            },
        },
    },
#]
#breaker = [
    {
        'header': {
            'command_length': 0,
            'command_id': 'deliver_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'protocol_id':0,
                'priority_flag':0,
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'deliver_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'data_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
                'esm_class':0,
                'registered_delivery':0,
                'data_coding':0,
            },
            'optional_parameters': [
                {
                    'tag':'message_payload',
                    'length':0,
                    'value':'',
                },
            ],
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'data_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'query_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'query_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'final_date':'',
                'message_state':0,
                'error_code':0,
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'cancel_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'service_type':'',
                'message_id':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'dest_addr_ton':1,
                'dest_addr_npi':1,
                'destination_addr':'',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'cancel_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'replace_sm',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'message_id':'',
                'source_addr_ton':1,
                'source_addr_npi':1,
                'source_addr':'',
                'schedule_delivery_time':'',
                'validity_period':'',
                'registered_delivery':0,
                'replace_if_present_flag':0,
                'data_coding':0,
                'sm_default_msg_id':0,
                'sm_length':1,
                'short_message':'is this an = sign?',
            },
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'replace_sm_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'enquire_link',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'enquire_link_resp',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
    },
    {
        'header': {
            'command_length': 0,
            'command_id': 'alert_notification',
            'command_status': 'ESME_ROK',
            'sequence_number': 0,
        },
        'body': {
            'mandatory_parameters': {
                'source_addr_ton':'international',
                'source_addr_npi':1,
                'source_addr':'',
                'esme_addr_ton':9,
                'esme_addr_npi':'',
                'esme_addr':'',
            },
        },
    },
]
