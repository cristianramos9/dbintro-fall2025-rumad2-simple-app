select count(cdays)
from section natural inner join meeting
where cdays like '%M%'
