-- select sid, mid, semester, years, cdays
-- from section natural inner join meeting
-- where years like '2020'
-- select count(years)
-- from section natural inner join meeting
-- where years like '2025'
select count(cdays) from
(select *
from section natural inner join meeting
where years like '2022')
where cdays like '%L%'