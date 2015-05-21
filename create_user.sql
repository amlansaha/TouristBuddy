CREATE user TouristBuddy identified by TouristBuddy;


GRANT CONNECT TO TouristBuddy;


GRANT EXECUTE on schema.procedure TO TouristBuddy;


GRANT CONNECT,RESOURCE,DBA TO TouristBuddy;

GRANT CREATE SESSION GRANT ANY PRIVILEGE TO TouristBuddy;

GRANT UNLIMITED TABLESPACE TO TouristBuddy;
