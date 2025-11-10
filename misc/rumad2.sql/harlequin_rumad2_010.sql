-- select class.cid, rid, cname, ccode, rid
-- from section inner join room on section.roomid = room.rid 
-- inner join class on section.cid = class.cid
-- order by class.cid


select cid, count(distinct rid)
-- select cid, count(rid)
-- select cid, rid, cname, ccode
from
(select class.cid, cname, ccode, rid
from section inner join room on section.roomid = room.rid 
inner join class on section.cid = class.cid)
group by cid
order by cid