select cdays from (select mid, cid, sid, semester, years, mid, cid, ccode, cdays
from section natural inner join meeting
order by ccode) 