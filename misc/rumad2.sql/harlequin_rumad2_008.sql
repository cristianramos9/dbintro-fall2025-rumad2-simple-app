-- select cdays, semester, years
-- from section natural inner join meeting
-- where semester like 'Spring'

select count(semester)
from
(select cdays, semester, years
from section natural inner join meeting
where semester like 'Fall')
where cdays like '%M%'