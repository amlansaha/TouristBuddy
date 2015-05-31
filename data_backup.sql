--------------------------------------------------------
--  DDL for Sequence LOCATION_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "TOURISM"."LOCATION_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 12 CACHE 20 NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence USER_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "TOURISM"."USER_SEQ"  MINVALUE 1 MAXVALUE 999999999999999999 INCREMENT BY 1 START WITH 41 CACHE 20 NOORDER  NOCYCLE ;
   
  CREATE OR REPLACE TRIGGER "TOURISM"."LOCATION_ID_TRIG" 
BEFORE INSERT ON LOCATIONS 
FOR EACH ROW
 WHEN (new."LOCATION_ID" IS NULL) BEGIN
        SELECT "LOCATION_SEQ".nextval
        INTO :new."LOCATION_ID" FROM dual;
    END;
--BEGIN
--  SELECT LOCATION_SEQ.NEXTVAL
--  INTO :NEW.LOCATION_ID
--  FROM DUAL;
--END;
/
ALTER TRIGGER "TOURISM"."LOCATION_ID_TRIG" ENABLE;
--------------------------------------------------------
--  DDL for Trigger USER_ID_TRIG
--------------------------------------------------------
--drop trigger USER_DATE_JOIN_TRIG;
  CREATE OR REPLACE TRIGGER "TOURISM"."USER_INSERTION_TRIG" 
BEFORE INSERT ON USERS
FOR EACH ROW

BEGIN
  SELECT SYSDATE, 1
  INTO   :new.DATE_JOINED, :new.IS_ACTIVE
  FROM   dual;
  SELECT 1
  INTO	:new.IS_ACTIVE
  FROM	dual;
END;
/
ALTER TRIGGER "TOURISM"."USER_INSERTION_TRIG" ENABLE;

Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('DHK','Dhaka');
Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('RNG','Rangpur');
Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('BAR','Barisal');
Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('SYL','Sylhet');
Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('CTG','Chittagong');
Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('KHL','Khulna');
Insert into TOURISM.DISTRICTS (DIST_ID,DIST_NAME) values ('MYM','Mymensingh');

Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('SYL','Jaflong',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('CTG','Potenga',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('CTG','Kaptai',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('CTG','Foy''s Lake',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('CTG','Batali Hill',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('CTG','Ethnic museum',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('SYL','Tamabil',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('SYL','Bichnakandi',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('CTG','Second World War cemetery',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('SYL','The Shrine of Hazrat ShahJalal',null,null);
Insert into TOURISM.LOCATIONS (DIST_ID,LOCATION_NAME,DESCRIPTION,MAP) values ('SYL','Ratargul Swamp Forest',null,null);


