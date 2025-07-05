CREATE EXTENSION IF NOT EXISTS timescaledb;


ALTER SYSTEM SET shared_preload_libraries = 'timescaledb';
ALTER SYSTEM SET timescaledb.telemetry_level = 'off';
CREATE TABLE IF NOT EXISTS metric (
    time TIMESTAMPTZ NOT NULL PRIMARY KEY, -- Metric timestamp
    fivegs_amffunction_rm_registeredsubnbr INT, -- Number of registered subscribers
    fivegs_amffunction_rm_regmobreq INT, -- Mobility registration update requests
    fivegs_amffunction_rm_regmobsucc INT, -- Successful mobility registration updates
    fivegs_amffunction_rm_regmobfail INT, -- Failed mobility registration updates
    fivegs_smffunction_sm_sessionnbr INT, -- Number of active sessions
    fivegs_smffunction_sm_pdusessioncreationreq INT, -- PDU session creation requests
    fivegs_smffunction_sm_pdusessioncreationsucc INT, -- Successful PDU session creations
    fivegs_ep_n3_gtp_indatapktn3upf INT, -- Uplink throughput on N3 interface
    fivegs_ep_n3_gtp_outdatapktn3upf INT, -- Downlink throughput on N3 interface
    fivegs_upffunction_upf_sessionnbr INT, -- Average number of PDU sessions
    fivegs_smffunction_upf_qos_flow_nbr INT, -- Number of active QoS flows
    fivegs_upffunction_sm_n4sessionreport INT, -- N4 session reports
    fivegs_upffunction_sm_n4sessionreportsucc INT, -- Successful N4 session reports
    fivegs_upffunction_sm_n4sessionestabreq INT, -- N4 session establishment requests
    fivegs_upffunction_sm_n4sessionestabfail INT, -- Failed N4 session establishments
    softmodern_bler_dl INT, -- Block error rate - downlink
    softmodern_bler_ul INT, -- Block error rate - uplink
    softmodern_rsrp INT, -- Received signal power
    pfcp_sessions_active INT -- Used for testing value changes
);

COMMENT ON COLUMN metric.time IS 'Timestamp da métrica';
COMMENT ON COLUMN metric.fivegs_amffunction_rm_registeredsubnbr IS 'Número de assinantes registrados';
COMMENT ON COLUMN metric.fivegs_amffunction_rm_regmobreq IS 'Solicitações de atualização de mobilidade';
COMMENT ON COLUMN metric.fivegs_amffunction_rm_regmobsucc IS 'Sucessos de atualização de mobilidade';
COMMENT ON COLUMN metric.fivegs_amffunction_rm_regmobfail IS 'Falhas na atualização de mobilidade';
COMMENT ON COLUMN metric.fivegs_smffunction_sm_sessionnbr IS 'Número de sessões ativas';
COMMENT ON COLUMN metric.fivegs_smffunction_sm_pdusessioncreationreq IS 'Requisições de criação de PDU session';
COMMENT ON COLUMN metric.fivegs_smffunction_sm_pdusessioncreationsucc IS 'Sucessos na criação de PDU session';
COMMENT ON COLUMN metric.fivegs_ep_n3_gtp_indatapktn3upf IS 'Throughput UL na interface N3';
COMMENT ON COLUMN metric.fivegs_ep_n3_gtp_outdatapktn3upf IS 'Throughput DL na interface N3';
COMMENT ON COLUMN metric.fivegs_upffunction_upf_sessionnbr IS 'Número médio de sessões PDU';
COMMENT ON COLUMN metric.fivegs_smffunction_upf_qos_flow_nbr IS 'Número de fluxos de QoS ativos';
COMMENT ON COLUMN metric.fivegs_upffunction_sm_n4sessionreport IS 'Relatórios de sessão N4';
COMMENT ON COLUMN metric.fivegs_upffunction_sm_n4sessionreportsucc IS 'Sucesso nos relatórios de N4';
COMMENT ON COLUMN metric.fivegs_upffunction_sm_n4sessionestabreq IS 'Requisições de estabelecimento de sessões N4';
COMMENT ON COLUMN metric.fivegs_upffunction_sm_n4sessionestabfail IS 'Falhas no estabelecimento de sessões N4';
COMMENT ON COLUMN metric.softmodern_bler_dl IS 'Taxa de erro de bloco - downlink';
COMMENT ON COLUMN metric.softmodern_bler_ul IS 'Taxa de erro de bloco - uplink';
COMMENT ON COLUMN metric.softmodern_rsrp IS 'Potência do sinal recebido';
COMMENT ON COLUMN metric.pfcp_sessions_active IS 'Sessões PFCP ativas';

SELECT create_hypertable('metric', 'time', if_not_exists => TRUE);