--drop user tourism cascade;
CREATE user tourism identified by tourism;

GRANT CONNECT TO Tourism;

GRANT EXECUTE on schema.procedure TO Tourism;

GRANT CONNECT,RESOURCE,DBA TO Tourism;
GRANT CREATE SESSION GRANT ANY PRIVILEGE TO Tourism;
GRANT UNLIMITED TABLESPACE TO Tourism;
