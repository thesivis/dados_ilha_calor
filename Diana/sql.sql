select i1.LONG,i1.LAT, 
     (select concat(i2.LONG,';',i2.LAT) FROM INVERNO_2011 i2 order by sqrt((i1.LONG - i2.LONG)*(i1.LONG - i2.LONG) + (i1.LAT - i2.LAT)*(i1.LAT - i2.LAT)) LIMIT 1)

from INVERNO_2016 i1
LIMIT 10




select row_number() over (ORDER BY distance),i1.index as index_solo, i1.long as long_solo, i1.lat as lat_solo, i1.alt as alt_solo, i1.pontos as pontos_solo, i1.cob_pais as cob_pais_solo, i1.cob_arb as cob_arb_solo, i1.solo_exp as solo_exp_solo, i1.a_pav as a_pav_solo, i1.a_edf as a_edf_solo, i1.agua as agua_solo, i2.index as index, i2.dia as dia, i2.long as long, i2.lat as lat, i2.hora as hora, i2.temp as temp, i2.ur as ur, i2.alt as alt, i2.v as v, sqrt((i1.LONG - i2.LONG)*(i1.LONG - i2.LONG) + (i1.LAT - i2.LAT)*(i1.LAT - i2.LAT)) as distance from "cob._transecto_2011-2012" i1, inverno_2011 i2 limit 10



select *, (
	SELECT i2.index 
	  from inverno_2011_solo_tudo i2
	where i2.index = i1.index
	order by i2.distance
	limit 1
	) from inverno_2011 i1

limit 10



select * from inverno_2011_solo_tudo i3
where i3.row_number in (
select  (
	SELECT i2.row_number 
	  from inverno_2011_solo_tudo i2
	where i2.index = i1.index
	order by i2.distance
	limit 1
	) from inverno_2011 i1
)
limit 10
