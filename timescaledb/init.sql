CREATE EXTENSION IF NOT EXISTS timescaledb;


ALTER SYSTEM SET shared_preload_libraries = 'timescaledb';
ALTER SYSTEM SET timescaledb.telemetry_level = 'off';


-- CREATE TABLE IF NOT EXISTS metrics (
--     time        TIMESTAMPTZ       NOT NULL,
--     measurement TEXT              NOT NULL,
--     field_key   TEXT              NOT NULL,
--     field_value DOUBLE PRECISION NOT NULL,
--     tags        JSONB
-- );

-- SELECT create_hypertable('metrics', 'time', if_not_exists => TRUE);

-- CREATE OR REPLACE FUNCTION verificar_metricas()
-- RETURNS TABLE (
--     numero_metrica INT,
--     nome_metrica VARCHAR(100),
--     existe BOOLEAN,
--     quantidade_registros BIGINT
-- ) AS $$
-- BEGIN
--     RETURN QUERY
--     WITH metricas AS (
--         SELECT 1 AS n, 'fivegs_amffunction_rm_registeredsubnbr' AS metrica UNION ALL
--         SELECT 2, 'fivegs_amffunction_rm_regmobreq' UNION ALL
--         SELECT 3, 'fivegs_amffunction_rm_regmobsucc' UNION ALL
--         SELECT 4, 'fivegs_amffunction_rm_regmobfail' UNION ALL
--         SELECT 5, 'fivegs_smffunction_sm_sessionnbr' UNION ALL
--         SELECT 6, 'fivegs_smffunction_sm_pdusessioncreationreq' UNION ALL
--         SELECT 7, 'fivegs_smffunction_sm_pdusessioncreationsucc' UNION ALL
--         SELECT 8, 'fivegs_smffunction_sm_pdusessioncreationfail' UNION ALL
--         SELECT 9, 'fivegs_ep_n3_gtp_indatapktn3upf' UNION ALL
--         SELECT 10, 'fivegs_ep_n3_gtp_outdatapktn3upf' UNION ALL
--         SELECT 11, 'fivegs_upffunction_upf_sessionnbr' UNION ALL
--         SELECT 12, 'fivegs_upffunction_upf_qosflows12' UNION ALL
--         SELECT 13, 'fivegs_upffunction_sm_n4sessionreport' UNION ALL
--         SELECT 14, 'fivegs_upffunction_sm_n4sessionreportsucc' UNION ALL
--         SELECT 15, 'fivegs_upffunction_sm_n4sessionestabfail' UNION ALL
--         SELECT 16, 'fivegs_upffunction_sm_n4sessionestabreq'
--     )
--     SELECT 
--         m.n AS numero_metrica,
--         m.metrica AS nome_metrica,
--         EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = m.metrica) AS existe,
--         CASE 
--             WHEN EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = m.metrica) 
--             THEN (SELECT COUNT(*) FROM (SELECT 1 FROM ONLY public." || m.metrica || ") t)
--             ELSE 0
--         END AS quantidade_registros
--     FROM metricas m
--     ORDER BY m.n;
-- END;
-- $$ LANGUAGE plpgsql;


-- select count(*) from "fivegs_amffunction_rm_registeredsubnbr";
-- select count(*) from "fivegs_amffunction_rm_regmobreq";
-- select count(*) from "fivegs_amffunction_rm_regmobsucc";
-- select count(*) from "fivegs_amffunction_rm_regmobfail";
-- select count(*) from "fivegs_smffunction_sm_sessionnbr";
-- select count(*) from "fivegs_smffunction_sm_pdusessioncreationreq";
-- select count(*) from "fivegs_smffunction_sm_pdusessioncreationsucc";
-- select count(*) from "fivegs_smffunction_sm_pdusessioncreationfail";
-- select count(*) from "fivegs_ep_n3_gtp_indatapktn3upf";
-- select count(*) from "fivegs_ep_n3_gtp_outdatapktn3upf";
-- select count(*) from "fivegs_upffunction_upf_sessionnbr";
-- select count(*) from "fivegs_upffunction_upf_qosflows12";
-- select count(*) from "fivegs_upffunction_sm_n4sessionreport";
-- select count(*) from "fivegs_upffunction_sm_n4sessionreportsucc";
-- select count(*) from "fivegs_upffunction_sm_n4sessionestabfail";
-- select count(*) from "fivegs_upffunction_sm_n4sessionestabreq";