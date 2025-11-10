-- select sid, mid, semester, years, cdays
-- from section natural inner join meeting
-- where years like '2021' and semester like 'Fall'

select count(cdays)
from
(select sid, mid, semester, years, cdays
from section natural inner join meeting
where years like '2021' and semester like 'Fall')
where cdays like '%L%'