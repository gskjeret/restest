/*
--------------------------------------------------------
-- CAPGEMINI FrontEnd gruppe
--
-- SCRIPT for testdatabase i mySQL.
-- 
-- Utfør først følgende:
-- I MySQL, opprett skjema djangobase
-- Fra shell, kjør:
-- py manage.py makemigrations
-- py manage.py migrate
-- py manage.py createsuperuser
------------------------------------------------------*/

USE djangobase;

DELIMITER //

DROP FUNCTION IF EXISTS Hent_Brukerid// 

CREATE FUNCTION Hent_Brukerid() RETURNS VARCHAR(30)
DETERMINISTIC SQL SECURITY INVOKER
BEGIN
  RETURN current_user();
END//


DROP TRIGGER IF EXISTS reg_leverandor_bir//

CREATE TRIGGER reg_leverandor_bir BEFORE INSERT ON leverandor FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_leverandor_bur//

CREATE TRIGGER reg_leverandor_bur BEFORE UPDATE ON leverandor FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DELIMITER ;


	   
/* Triggere som registrerer endringshistorikk */
DELIMITER //

DROP TRIGGER IF EXISTS reg_vare_bir//

CREATE TRIGGER reg_vare_bir BEFORE INSERT ON vare FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_vare_bur//

CREATE TRIGGER reg_vare_bur BEFORE UPDATE ON vare FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_varepris_bir//

CREATE TRIGGER reg_varepris_bir BEFORE INSERT ON varepris FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_varepris_bur//

CREATE TRIGGER reg_varepris_bur BEFORE UPDATE ON varepris FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//


/* Trigger som setter produktkode ut fra leverandorkode og lopenr */
DROP TRIGGER IF EXISTS chk_vare_bir//

CREATE TRIGGER chk_vare_bir BEFORE INSERT ON vare FOR EACH ROW  
BEGIN  
  DECLARE v_levkode VARCHAR(5);
  DECLARE v_lopenr  INT UNSIGNED;  
  IF NEW.leverandor_id IS NOT null THEN  
    SELECT leverandorkode INTO v_levkode
    FROM   leverandor
    WHERE  leverandor_id = NEW.leverandor_id;
  END IF;

  SELECT ifnull(max(convert(replace(produktkode,v_levkode,''),unsigned integer)),0) INTO v_lopenr
  FROM   vare
  WHERE  produktkode LIKE concat(v_levkode,'%');

  SET NEW.produktkode = concat(v_levkode, v_lopenr+1);
END//


/* Triggere som legger prishistorikk i VAREPRIS */
DROP TRIGGER IF EXISTS chk_vare_air//

CREATE TRIGGER chk_vare_air AFTER INSERT ON vare FOR EACH ROW  
BEGIN  
  INSERT INTO varepris (produkt_id, pris_fra_dato, pris_u_mva)
  VALUES (NEW.produkt_id, curdate(), NEW.pris_u_mva);
END//

DROP TRIGGER IF EXISTS chk_vare_aur//

CREATE TRIGGER chk_vare_aur AFTER UPDATE ON vare FOR EACH ROW  
BEGIN  
  DECLARE error   VARCHAR(30) DEFAULT '';
  DECLARE v_pris  DECIMAL;  
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET error='NO_DATA_FOUND';

  IF NEW.pris_u_mva <=> OLD.pris_u_mva THEN

    SELECT pris_u_mva INTO v_pris
    FROM   varepris 
    WHERE  produkt_id = NEW.produkt_id
    AND    pris_fra_dato = curdate();
	  
    IF v_pris IS NULL THEN
      INSERT INTO varepris (produkt_id, pris_fra_dato, pris_u_mva)
      VALUES (NEW.produkt_id, curdate(), NEW.pris_u_mva);
    END IF;

    IF v_pris IS NOT NULL AND NEW.pris_u_mva <> v_pris THEN
      UPDATE varepris SET pris_u_mva = NEW.pris_u_mva
      WHERE  produkt_id = NEW.produkt_id
      AND    pris_fra_dato = curdate();
	END IF;
  END IF;
END//

DELIMITER ;
		 



/* ----------------------------------------------
   Triggere som registrerer endringshistorikk  */
DELIMITER //

DROP TRIGGER IF EXISTS reg_kunde_bir//

CREATE TRIGGER reg_kunde_bir BEFORE INSERT ON kunde FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_kunde_bur//

CREATE TRIGGER reg_kunde_bur BEFORE UPDATE ON kunde FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DELIMITER ;
/* Slutt Triggere
   ----------------------------------------------- */

	   
   
	   
/* ----------------------------------------------
   Triggere som registrerer endringshistorikk  */
DELIMITER //

DROP TRIGGER IF EXISTS reg_ordre_bir//

CREATE TRIGGER reg_ordre_bir BEFORE INSERT ON ordre FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_ordre_bur//

CREATE TRIGGER reg_ordre_bur BEFORE UPDATE ON ordre FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

/* Trigger som hindrer oppdatering av ordre som faktureres eller er betalt */
DROP TRIGGER IF EXISTS chk_ordre_bur//

CREATE TRIGGER chk_ordre_bur BEFORE UPDATE ON ordre FOR EACH ROW  
BEGIN  
  DECLARE v_statusmelding VARCHAR(200);

  IF ( NEW.ordre_id    <=>  OLD.ordre_id
    OR NEW.ordre_dato  <=>  OLD.ordre_dato
    OR NEW.kunde_id    <=>  OLD.kunde_id
    OR NEW.belop_u_mva <=>  OLD.belop_u_mva
    OR NEW.mva_belop   <=>  OLD.mva_belop
    OR NEW.totalbelop  <=>  OLD.totalbelop )
  AND OLD.status IN ('FAKTURA','BETALT') THEN  
    SELECT os.beskrivelse INTO v_statusmelding 
    FROM   ordrestatus os 
    WHERE  os.statuskode = OLD.status;

    SIGNAL SQLSTATE '45000' SET message_text = v_statusmelding;
  END IF;  
END//


DELIMITER ;
/* Slutt Triggere
   ----------------------------------------------- */

	   
/* ----------------------------------------------
   Triggere som registrerer endringshistorikk  */
DELIMITER //

DROP TRIGGER IF EXISTS reg_ordrelinje_bir//

CREATE TRIGGER reg_ordrelinje_bir BEFORE INSERT ON ordrelinje FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_ordrelinje_bur//

CREATE TRIGGER reg_ordrelinje_bur BEFORE UPDATE ON ordrelinje FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

/* Trigger som setter linjenr på ordrelinjen */
DROP TRIGGER IF EXISTS chk_ordrelinje_bir//

CREATE TRIGGER chk_ordrelinje_bir BEFORE INSERT ON ordrelinje FOR EACH ROW  
BEGIN  
  DECLARE v_lopenr INT UNSIGNED;  

  SELECT  ifnull(max(linjenr),0) INTO v_lopenr
  FROM    ordrelinje
  WHERE   ordre_id = NEW.ordre_id;

  SET NEW.linjenr = v_lopenr+1;
END//

/* Trigger som hindrer oppdatering av ordre som faktureres eller er betalt */
DROP TRIGGER IF EXISTS chk_ordrelinje_bur//

CREATE TRIGGER chk_ordrelinje_bur BEFORE UPDATE ON ordrelinje FOR EACH ROW  
BEGIN  
  DECLARE v_ordrestatus   VARCHAR(10);  
  DECLARE v_statusmelding VARCHAR(200);

  SELECT o.status, os.beskrivelse INTO v_ordrestatus, v_statusmelding 
  FROM   ordre o, ordrestatus os 
  WHERE  o.ordre_id = NEW.ordre_id
  AND    o.status   = os.statuskode;

  IF v_ordrestatus IN ('FAKTURA','BETALT') THEN  
    SIGNAL SQLSTATE '45000' SET message_text = v_statusmelding;
  END IF;  
END//

DELIMITER ;
/* Slutt Triggere
   ----------------------------------------------- */

	   
/* ----------------------------------------------
   Triggere som registrerer endringshistorikk  */
DELIMITER //

DROP TRIGGER IF EXISTS reg_faktura_bir//

CREATE TRIGGER reg_faktura_bir BEFORE INSERT ON faktura FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  IF NEW.reg_bruker IS null THEN
    SET NEW.reg_bruker = v_user;
    SET NEW.reg_dato   = now();
  END IF;
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

DROP TRIGGER IF EXISTS reg_faktura_bur//

CREATE TRIGGER reg_faktura_bur BEFORE UPDATE ON faktura FOR EACH ROW  
BEGIN
  DECLARE v_user VARCHAR(30) DEFAULT Hent_Brukerid();
  SET NEW.endret_bruker = v_user;
  SET NEW.endret_dato   = now();
END//

/* Trigger som hindrer oppdatering av faktura som er sendt eller betalt */
DROP TRIGGER IF EXISTS chk_faktura_bur//

CREATE TRIGGER chk_faktura_bur BEFORE UPDATE ON faktura FOR EACH ROW  
BEGIN  
  DECLARE v_ordrestatus   VARCHAR(10);
  DECLARE v_statusmelding VARCHAR(200);

  IF ( NEW.ordre_id     <=>  OLD.ordre_id
    OR NEW.faktura_dato <=>  OLD.faktura_dato
    OR NEW.frist_dato   <=>  OLD.frist_dato
    OR NEW.belop_u_mva  <=>  OLD.belop_u_mva
    OR NEW.mva_belop    <=>  OLD.mva_belop
    OR NEW.totalbelop   <=>  OLD.totalbelop
    OR NEW.kidnr        <=>  OLD.kidnr ) THEN
	
    SELECT o.status, os.beskrivelse INTO v_ordrestatus, v_statusmelding 
    FROM   ordre o, ordrestatus os 
    WHERE  o.ordre_id = NEW.ordre_id
    AND    os.statuskode = o.status;

    IF v_ordrestatus IN ('FAKTURA','BETALT') THEN  
      SIGNAL SQLSTATE '45000' SET message_text = v_statusmelding;
    END IF;
  END IF;  
END//

DELIMITER ;
/* Slutt Triggere
   ----------------------------------------------- */

/* ---------------------------------------------*/
DELIMITER //

/* Trigger som hindrer oppdatering av faktura som er sendt eller betalt */
DROP TRIGGER IF EXISTS chk_fakturalinje_bur//

CREATE TRIGGER chk_fakturalinje_bur BEFORE UPDATE ON fakturalinje FOR EACH ROW  
BEGIN  
  DECLARE v_ordrestatus   VARCHAR(10);
  DECLARE v_statusmelding VARCHAR(200);

  SELECT o.status, os.beskrivelse INTO v_ordrestatus, v_statusmelding 
  FROM   faktura f, ordre o, ordrestatus os 
  WHERE  f.faktura_id = NEW.faktura_id
  AND    o.ordre_id   = f.ordre_id
  AND    o.status     = os.statuskode;

  IF v_ordrestatus IN ('FAKTURA','BETALT') THEN  
    SIGNAL SQLSTATE '45000' SET message_text = v_statusmelding;
  END IF;  
END//

DELIMITER ;
/* Slutt Triggere
   ----------------------------------------------- */
