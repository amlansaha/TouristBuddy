--CREATE SEQUENCE LOCATION_SEQ;

CREATE OR REPLACE TRIGGER LOCATION_ID_TRIG 
BEFORE INSERT ON LOCATIONS
FOR EACH ROW

BEGIN
  SELECT LOCATION_SEQ.NEXTVAL
  INTO   :new.LOCATION_id
  FROM   dual;
END;
