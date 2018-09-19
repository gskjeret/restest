use djangobase;

create or replace view
v_ordrelinje as (
select o.ordrelinje_id, o.ordre_id, o.linjenr, o.antall, o.rabatt_pros, o.belop_linje_u_mva, o.kommentar
, v.produktnavn, v.produktkode, v.produkt_id
from ordrelinje o join vare v on v.produkt_id=o.produkt_id);
