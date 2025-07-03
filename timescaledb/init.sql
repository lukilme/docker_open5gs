CREATE EXTENSION IF NOT EXISTS timescaledb;


ALTER SYSTEM SET shared_preload_libraries = 'timescaledb';
ALTER SYSTEM SET timescaledb.telemetry_level = 'off';
CREATE TABLE IF NOT EXISTS metric (
    time TIMESTAMPTZ NOT NULL PRIMARY KEY,
    fivegs_amffunction_rm_registeredsubnbr INT,
    fivegs_amffunction_rm_regmobreq INT,
    fivegs_amffunction_rm_regmobsucc INT,
    fivegs_amffunction_rm_regmobfail INT,
    fivegs_smffunction_sm_sessionnbr INT,
    fivegs_smffunction_sm_pdusessioncreationreq INT,
    fivegs_smffunction_sm_pdusessioncreationsucc INT,
    fivegs_ep_n3_gtp_indatapktn3upf INT,
    fivegs_ep_n3_gtp_outdatapktn3upf INT,
    fivegs_upffunction_upf_sessionnbr INT,
    fivegs_smffunction_upf_qos_flow_nbr INT,
    fivegs_upffunction_sm_n4sessionreport INT,
    fivegs_upffunction_sm_n4sessionreportsucc INT,
    fivegs_upffunction_sm_n4sessionestabreq INT,
    fivegs_upffunction_sm_n4sessionestabfail INT,
    softmodern_bler_dl INT,
    softmodern_bler_ul INT,
    softmodern_rsrp INT
);
SELECT create_hypertable('metric', 'time', if_not_exists => TRUE);