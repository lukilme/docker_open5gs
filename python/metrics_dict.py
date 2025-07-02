
metrics_dict = {
    "gnb": {
        "help": "gNodeBs",
        "type": "gauge"
    },
    "fivegs_amffunction_mm_confupdate": {
        "help": "Number of UE Configuration Update commands requested by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_reginitreq": {
        "help": "Number of initial registration requests received by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regemergreq": {
        "help": "Number of emergency registration requests received by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_mm_paging5greq": {
        "help": "Number of 5G paging procedures initiated at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regperiodreq": {
        "help": "Number of periodic registration update requests received by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_mm_confupdatesucc": {
        "help": "Number of UE Configuration Update complete messages received by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_reginitsucc": {
        "help": "Number of successful initial registrations at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_amf_authreject": {
        "help": "Number of authentication rejections sent by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regmobreq": {
        "help": "Number of mobility registration update requests received by the AMF",
        "type": "counter"
    },
    "amf_session": {
        "help": "AMF Sessions",
        "type": "gauge"
    },
    "fivegs_amffunction_rm_regmobsucc": {
        "help": "Number of successful mobility registration updates at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_amf_authreq": {
        "help": "Number of authentication requests sent by the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regemergsucc": {
        "help": "Number of successful emergency registrations at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_mm_paging5gsucc": {
        "help": "Number of successful 5G paging procedures initiated at the AMF",
        "type": "counter"
    },
    "ran_ue": {
        "help": "RAN UEs",
        "type": "gauge"
    },
    "fivegs_amffunction_rm_regperiodsucc": {
        "help": "Number of successful periodic registration update requests at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regtime": {
        "help": "Time of registration procedure",
        "type": "histogram"
    },
    "fivegs_amffunction_rm_registeredsubnbr": {
        "help": "Number of registered state subscribers per AMF",
        "type": "gauge"
    },
    "fivegs_amffunction_rm_reginitfail": {
        "help": "Number of failed initial registrations at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regmobfail": {
        "help": "Number of failed mobility registration updates at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regperiodfail": {
        "help": "Number of failed periodic registration update requests at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_rm_regemergfail": {
        "help": "Number of failed emergency registrations at the AMF",
        "type": "counter"
    },
    "fivegs_amffunction_amf_authfail": {
        "help": "Number of authentication failure messages received by the AMF",
        "type": "counter"
    },
    "process_max_fds": {
        "help": "Maximum number of open file descriptors.",
        "type": "gauge"
    },
    "process_virtual_memory_max_bytes": {
        "help": "Maximum amount of virtual memory available in bytes.",
        "type": "gauge"
    },
    "process_cpu_seconds_total": {
        "help": "Total user and system CPU time spent in seconds.",
        "type": "gauge"
    },
    "process_virtual_memory_bytes": {
        "help": "Virtual memory size in bytes.",
        "type": "gauge"
    },
    "process_resident_memory_bytes": {
        "help": "Resident memory size in bytes.",
        "type": "gauge"
    },
    "process_start_time_seconds": {
        "help": "Start time of the process since unix epoch in seconds.",
        "type": "gauge"
    },
    "process_open_fds": {
        "help": "Number of open file descriptors.",
        "type": "gauge"
    },
    "fivegs_ep_n3_gtp_indatapktn3upf": {
        "help": "Number of incoming GTP data packets on the N3 interface",
        "type": "counter"
    },
    "fivegs_ep_n3_gtp_outdatapktn3upf": {
        "help": "Number of outgoing GTP data packets on the N3 interface",
        "type": "counter"
    },
    "fivegs_upffunction_sm_n4sessionestabreq": {
        "help": "Number of requested N4 session establishments",
        "type": "counter"
    },
    "fivegs_upffunction_sm_n4sessionreport": {
        "help": "Number of requested N4 session reports",
        "type": "counter"
    },
    "fivegs_upffunction_sm_n4sessionreportsucc": {
        "help": "Number of successful N4 session reports",
        "type": "counter"
    },
    "fivegs_upffunction_upf_sessionnbr": {
        "help": "Active Sessions",
        "type": "gauge"
    },
    "pfcp_peers_active": {
        "help": "Active PFCP peers",
        "type": "gauge"
    },
    "fivegs_ep_n3_gtp_indatavolumeqosleveln3upf": {
        "help": "Data volume of incoming GTP data packets per QoS level on the N3 interface",
        "type": "counter"
    },
    "fivegs_ep_n3_gtp_outdatavolumeqosleveln3upf": {
        "help": "Data volume of outgoing GTP data packets per QoS level on the N3 interface",
        "type": "counter"
    },
    "fivegs_upffunction_sm_n4sessionestabfail": {
        "help": "Number of failed N4 session establishments",
        "type": "counter"
    },
    "fivegs_upffunction_upf_qosflows": {
        "help": "Number of QoS flows of UPF",
        "type": "gauge"
    },
    "gn_rx_createpdpcontextreq": {
        "help": "Received GTPv1C CreatePDPContextRequest messages",
        "type": "counter"
    },
    "gn_rx_deletepdpcontextreq": {
        "help": "Received GTPv1C DeletePDPContextRequest messages",
        "type": "counter"
    },
    "gtp1_pdpctxs_active": {
        "help": "Active GTPv1 PDP Contexts (GGSN)",
        "type": "gauge"
    },
    "fivegs_smffunction_sm_n4sessionreport": {
        "help": "Number of requested N4 session reports evidented by SMF",
        "type": "counter"
    },
    "ues_active": {
        "help": "Active User Equipments",
        "type": "gauge"
    },
    "gtp2_sessions_active": {
        "help": "Active GTPv2 Sessions (PGW)",
        "type": "gauge"
    },
    "pfcp_sessions_active": {
        "help": "Active PFCP Sessions",
        "type": "gauge"
    },
    "s5c_rx_createsession": {
        "help": "Received GTPv2C CreateSessionRequest messages",
        "type": "counter"
    },
    "s5c_rx_deletesession": {
        "help": "Received GTPv2C DeleteSessionRequest messages",
        "type": "counter"
    },
    "gtp_new_node_failed": {
        "help": "Unable to allocate new GTP (peer) Node",
        "type": "counter"
    },
    "s5c_rx_parse_failed": {
        "help": "Received GTPv2C messages discarded due to parsing failure",
        "type": "counter"
    },
    "fivegs_smffunction_sm_n4sessionreportsucc": {
        "help": "Number of successful N4 session reports evidented by SMF",
        "type": "counter"
    },
    "fivegs_smffunction_sm_n4sessionestabreq": {
        "help": "Number of requested N4 session establishments evidented by SMF",
        "type": "counter"
    },
    "bearers_active": {
        "help": "Active Bearers",
        "type": "gauge"
    },
    "gn_rx_parse_failed": {
        "help": "Received GTPv1C messages discarded due to parsing failure",
        "type": "counter"
    },
    "gtp_peers_active": {
        "help": "Active GTP peers",
        "type": "gauge"
    },
    "gtp_node_gn_rx_parse_failed": {
        "help": "Received GTPv1C messages discarded due to parsing failure",
        "type": "counter"
    },
    "gtp_node_gn_rx_createpdpcontextreq": {
        "help": "Received GTPv1C CreatePDPContextRequest messages",
        "type": "counter"
    },
    "gtp_node_gn_rx_deletepdpcontextreq": {
        "help": "Received GTPv1C DeletePDPContextRequest messages",
        "type": "counter"
    },
    "gtp_node_s5c_rx_parse_failed": {
        "help": "Received GTPv2C messages discarded due to parsing failure",
        "type": "counter"
    },
    "gtp_node_s5c_rx_createsession": {
        "help": "Received GTPv2C CreateSessionRequest messages",
        "type": "counter"
    },
    "gtp_node_s5c_rx_deletesession": {
        "help": "Received GTPv2C DeleteSessionRequest messages",
        "type": "counter"
    },
    "fivegs_smffunction_sm_sessionnbr": {
        "help": "Active Sessions",
        "type": "gauge"
    },
    "fivegs_smffunction_sm_pdusessioncreationreq": {
        "help": "Number of PDU sessions requested to be created by the SMF",
        "type": "counter"
    },
    "fivegs_smffunction_sm_pdusessioncreationsucc": {
        "help": "Number of PDU sessions successfully created by the SMF",
        "type": "counter"
    },
    "fivegs_smffunction_sm_qos_flow_nbr": {
        "help": "Number of QoS flows at the SMF",
        "type": "gauge"
    },
    "fivegs_smffunction_sm_n4sessionestabfail": {
        "help": "Number of failed N4 session establishments evidented by SMF",
        "type": "counter"
    },
    "fivegs_smffunction_sm_pdusessioncreationfail": {
        "help": "Number of PDU sessions failed to be created by the SMF",
        "type": "counter"
    }
}