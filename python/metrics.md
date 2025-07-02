# HELP gnb gNodeBs
# TYPE gnb gauge
gnb 0

# HELP fivegs_amffunction_mm_confupdate Number of UE Configuration Update commands requested by the AMF
# TYPE fivegs_amffunction_mm_confupdate counter
fivegs_amffunction_mm_confupdate 0

# HELP fivegs_amffunction_rm_reginitreq Number of initial registration requests received by the AMF
# TYPE fivegs_amffunction_rm_reginitreq counter
fivegs_amffunction_rm_reginitreq 0

# HELP fivegs_amffunction_rm_regemergreq Number of emergency registration requests received by the AMF
# TYPE fivegs_amffunction_rm_regemergreq counter
fivegs_amffunction_rm_regemergreq 0

# HELP fivegs_amffunction_mm_paging5greq Number of 5G paging procedures initiated at the AMF
# TYPE fivegs_amffunction_mm_paging5greq counter
fivegs_amffunction_mm_paging5greq 0

# HELP fivegs_amffunction_rm_regperiodreq Number of periodic registration update requests received by the AMF
# TYPE fivegs_amffunction_rm_regperiodreq counter
fivegs_amffunction_rm_regperiodreq 0

# HELP fivegs_amffunction_mm_confupdatesucc Number of UE Configuration Update complete messages received by the AMF
# TYPE fivegs_amffunction_mm_confupdatesucc counter
fivegs_amffunction_mm_confupdatesucc 0

# HELP fivegs_amffunction_rm_reginitsucc Number of successful initial registrations at the AMF
# TYPE fivegs_amffunction_rm_reginitsucc counter
fivegs_amffunction_rm_reginitsucc 0

# HELP fivegs_amffunction_amf_authreject Number of authentication rejections sent by the AMF
# TYPE fivegs_amffunction_amf_authreject counter
fivegs_amffunction_amf_authreject 0

# HELP fivegs_amffunction_rm_regmobreq Number of mobility registration update requests received by the AMF
# TYPE fivegs_amffunction_rm_regmobreq counter
fivegs_amffunction_rm_regmobreq 0

# HELP amf_session AMF Sessions
# TYPE amf_session gauge
amf_session 0

# HELP fivegs_amffunction_rm_regmobsucc Number of successful mobility registration updates at the AMF
# TYPE fivegs_amffunction_rm_regmobsucc counter
fivegs_amffunction_rm_regmobsucc 0

# HELP fivegs_amffunction_amf_authreq Number of authentication requests sent by the AMF
# TYPE fivegs_amffunction_amf_authreq counter
fivegs_amffunction_amf_authreq 0

# HELP fivegs_amffunction_rm_regemergsucc Number of successful emergency registrations at the AMF
# TYPE fivegs_amffunction_rm_regemergsucc counter
fivegs_amffunction_rm_regemergsucc 0

# HELP fivegs_amffunction_mm_paging5gsucc Number of successful 5G paging procedures initiated at the AMF
# TYPE fivegs_amffunction_mm_paging5gsucc counter
fivegs_amffunction_mm_paging5gsucc 0

# HELP ran_ue RAN UEs
# TYPE ran_ue gauge
ran_ue 0

# HELP fivegs_amffunction_rm_regperiodsucc Number of successful periodic registration update requests at the AMF
# TYPE fivegs_amffunction_rm_regperiodsucc counter
fivegs_amffunction_rm_regperiodsucc 0

# HELP fivegs_amffunction_rm_regtime Time of registration procedure
# TYPE fivegs_amffunction_rm_regtime histogram

# HELP fivegs_amffunction_rm_registeredsubnbr Number of registered state subscribers per AMF
# TYPE fivegs_amffunction_rm_registeredsubnbr gauge

# HELP fivegs_amffunction_rm_reginitfail Number of failed initial registrations at the AMF
# TYPE fivegs_amffunction_rm_reginitfail counter

# HELP fivegs_amffunction_rm_regmobfail Number of failed mobility registration updates at the AMF
# TYPE fivegs_amffunction_rm_regmobfail counter

# HELP fivegs_amffunction_rm_regperiodfail Number of failed periodic registration update requests at the AMF
# TYPE fivegs_amffunction_rm_regperiodfail counter

# HELP fivegs_amffunction_rm_regemergfail Number of failed emergency registrations at the AMF
# TYPE fivegs_amffunction_rm_regemergfail counter

# HELP fivegs_amffunction_amf_authfail Number of authentication failure messages received by the AMF
# TYPE fivegs_amffunction_amf_authfail counter

# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1048576

# HELP process_virtual_memory_max_bytes Maximum amount of virtual memory available in bytes.
# TYPE process_virtual_memory_max_bytes gauge
process_virtual_memory_max_bytes -1

# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total gauge
process_cpu_seconds_total 0

# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1774628864

# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 20934656

# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 688781

# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 39

# HELP fivegs_ep_n3_gtp_indatapktn3upf Number of incoming GTP data packets on the N3 interface
# TYPE fivegs_ep_n3_gtp_indatapktn3upf counter
fivegs_ep_n3_gtp_indatapktn3upf 0

# HELP fivegs_ep_n3_gtp_outdatapktn3upf Number of outgoing GTP data packets on the N3 interface
# TYPE fivegs_ep_n3_gtp_outdatapktn3upf counter
fivegs_ep_n3_gtp_outdatapktn3upf 0

# HELP fivegs_upffunction_sm_n4sessionestabreq Number of requested N4 session establishments
# TYPE fivegs_upffunction_sm_n4sessionestabreq counter
fivegs_upffunction_sm_n4sessionestabreq 0

# HELP fivegs_upffunction_sm_n4sessionreport Number of requested N4 session reports
# TYPE fivegs_upffunction_sm_n4sessionreport counter
fivegs_upffunction_sm_n4sessionreport 0

# HELP fivegs_upffunction_sm_n4sessionreportsucc Number of successful N4 session reports
# TYPE fivegs_upffunction_sm_n4sessionreportsucc counter
fivegs_upffunction_sm_n4sessionreportsucc 0

# HELP fivegs_upffunction_upf_sessionnbr Active Sessions
# TYPE fivegs_upffunction_upf_sessionnbr gauge
fivegs_upffunction_upf_sessionnbr 0

# HELP pfcp_peers_active Active PFCP peers
# TYPE pfcp_peers_active gauge
pfcp_peers_active 1

# HELP fivegs_ep_n3_gtp_indatavolumeqosleveln3upf Data volume of incoming GTP data packets per QoS level on the N3 interface
# TYPE fivegs_ep_n3_gtp_indatavolumeqosleveln3upf counter

# HELP fivegs_ep_n3_gtp_outdatavolumeqosleveln3upf Data volume of outgoing GTP data packets per QoS level on the N3 interface
# TYPE fivegs_ep_n3_gtp_outdatavolumeqosleveln3upf counter

# HELP fivegs_upffunction_sm_n4sessionestabfail Number of failed N4 session establishments
# TYPE fivegs_upffunction_sm_n4sessionestabfail counter

# HELP fivegs_upffunction_upf_qosflows Number of QoS flows of UPF
# TYPE fivegs_upffunction_upf_qosflows gauge

# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1048576

# HELP process_virtual_memory_max_bytes Maximum amount of virtual memory available in bytes.
# TYPE process_virtual_memory_max_bytes gauge
process_virtual_memory_max_bytes -1

# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total gauge
process_cpu_seconds_total 0

# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 368320512

# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 33603584

# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 815098

# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 15

# HELP gn_rx_createpdpcontextreq Received GTPv1C CreatePDPContextRequest messages
# TYPE gn_rx_createpdpcontextreq counter
gn_rx_createpdpcontextreq 0

# HELP gn_rx_deletepdpcontextreq Received GTPv1C DeletePDPContextRequest messages
# TYPE gn_rx_deletepdpcontextreq counter
gn_rx_deletepdpcontextreq 0

# HELP gtp1_pdpctxs_active Active GTPv1 PDP Contexts (GGSN)
# TYPE gtp1_pdpctxs_active gauge
gtp1_pdpctxs_active 0

# HELP pfcp_peers_active Active PFCP peers
# TYPE pfcp_peers_active gauge
pfcp_peers_active 1

# HELP fivegs_smffunction_sm_n4sessionreport Number of requested N4 session reports evidented by SMF
# TYPE fivegs_smffunction_sm_n4sessionreport counter
fivegs_smffunction_sm_n4sessionreport 0

# HELP ues_active Active User Equipments
# TYPE ues_active gauge
ues_active 0

# HELP gtp2_sessions_active Active GTPv2 Sessions (PGW)
# TYPE gtp2_sessions_active gauge
gtp2_sessions_active 0

# HELP pfcp_sessions_active Active PFCP Sessions
# TYPE pfcp_sessions_active gauge
pfcp_sessions_active 0

# HELP s5c_rx_createsession Received GTPv2C CreateSessionRequest messages
# TYPE s5c_rx_createsession counter
s5c_rx_createsession 0

# HELP s5c_rx_deletesession Received GTPv2C DeleteSessionRequest messages
# TYPE s5c_rx_deletesession counter
s5c_rx_deletesession 0

# HELP gtp_new_node_failed Unable to allocate new GTP (peer) Node
# TYPE gtp_new_node_failed counter
gtp_new_node_failed 0

# HELP s5c_rx_parse_failed Received GTPv2C messages discarded due to parsing failure
# TYPE s5c_rx_parse_failed counter
s5c_rx_parse_failed 0

# HELP fivegs_smffunction_sm_n4sessionreportsucc Number of successful N4 session reports evidented by SMF
# TYPE fivegs_smffunction_sm_n4sessionreportsucc counter
fivegs_smffunction_sm_n4sessionreportsucc 0

# HELP fivegs_smffunction_sm_n4sessionestabreq Number of requested N4 session establishments evidented by SMF
# TYPE fivegs_smffunction_sm_n4sessionestabreq counter
fivegs_smffunction_sm_n4sessionestabreq 0

# HELP bearers_active Active Bearers
# TYPE bearers_active gauge
bearers_active 0

# HELP gn_rx_parse_failed Received GTPv1C messages discarded due to parsing failure
# TYPE gn_rx_parse_failed counter
gn_rx_parse_failed 0

# HELP gtp_peers_active Active GTP peers
# TYPE gtp_peers_active gauge
gtp_peers_active 0

# HELP gtp_node_gn_rx_parse_failed Received GTPv1C messages discarded due to parsing failure
# TYPE gtp_node_gn_rx_parse_failed counter

# HELP gtp_node_gn_rx_createpdpcontextreq Received GTPv1C CreatePDPContextRequest messages
# TYPE gtp_node_gn_rx_createpdpcontextreq counter

# HELP gtp_node_gn_rx_deletepdpcontextreq Received GTPv1C DeletePDPContextRequest messages
# TYPE gtp_node_gn_rx_deletepdpcontextreq counter

# HELP gtp_node_s5c_rx_parse_failed Received GTPv2C messages discarded due to parsing failure
# TYPE gtp_node_s5c_rx_parse_failed counter

# HELP gtp_node_s5c_rx_createsession Received GTPv2C CreateSessionRequest messages
# TYPE gtp_node_s5c_rx_createsession counter

# HELP gtp_node_s5c_rx_deletesession Received GTPv2C DeleteSessionRequest messages
# TYPE gtp_node_s5c_rx_deletesession counter

# HELP fivegs_smffunction_sm_sessionnbr Active Sessions
# TYPE fivegs_smffunction_sm_sessionnbr gauge

# HELP fivegs_smffunction_sm_pdusessioncreationreq Number of PDU sessions requested to be created by the SMF
# TYPE fivegs_smffunction_sm_pdusessioncreationreq counter

# HELP fivegs_smffunction_sm_pdusessioncreationsucc Number of PDU sessions successfully created by the SMF
# TYPE fivegs_smffunction_sm_pdusessioncreationsucc counter

# HELP fivegs_smffunction_sm_qos_flow_nbr Number of QoS flows at the SMF
# TYPE fivegs_smffunction_sm_qos_flow_nbr gauge

# HELP fivegs_smffunction_sm_n4sessionestabfail Number of failed N4 session establishments evidented by SMF
# TYPE fivegs_smffunction_sm_n4sessionestabfail counter

# HELP fivegs_smffunction_sm_pdusessioncreationfail Number of PDU sessions failed to be created by the SMF
# TYPE fivegs_smffunction_sm_pdusessioncreationfail counter

# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1048576

# HELP process_virtual_memory_max_bytes Maximum amount of virtual memory available in bytes.
# TYPE process_virtual_memory_max_bytes gauge
process_virtual_memory_max_bytes -1

# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total gauge
process_cpu_seconds_total 0

# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 3205099520

# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 56295424

# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 815082

# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 37





