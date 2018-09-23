use djangobase;

create or replace view
v_ordrelinje as (
select o.ordrelinje_id, o.ordre_id, o.linjenr, o.antall, o.rabatt_pros, o.belop_linje_u_mva, o.kommentar
, v.produktnavn, v.produktkode, v.produkt_id
from ordrelinje o join vare v on v.produkt_id=o.produkt_id);

update vare set produktkategori = substring(beskrivelse, 1, locate(' - ', beskrivelse));
update vare set beskrivelse = substring(beskrivelse, char_length(produktkategori)+3);

update vare set produkttype = substring(beskrivelse, 1, locate(' - ', beskrivelse));
update vare set beskrivelse = substring(beskrivelse, char_length(produkttype)+3);

update vare set produktopprinnelse = substring(beskrivelse, 1, locate(' - ', beskrivelse)) where beskrivelse like '% - %';
update vare set produktopprinnelse = substring(beskrivelse, 1) where beskrivelse not like '% - %';

update vare set produktaar = substr(beskrivelse, char_length(beskrivelse)-4) where beskrivelse like '% - %';

update vare set beskrivelse = concat(produktkategori , ' - ' , produkttype , ' - ' , beskrivelse);
