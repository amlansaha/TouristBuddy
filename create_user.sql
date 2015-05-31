--drop user tourism cascade;
CREATE user tourism identified by tourism;

GRANT CONNECT TO tourism;

GRANT EXECUTE on schema.procedure TO tourism;

GRANT CONNECT,RESOURCE,DBA TO tourism;
GRANT CREATE SESSION GRANT ANY PRIVILEGE TO tourism;
GRANT UNLIMITED TABLESPACE TO tourism;
