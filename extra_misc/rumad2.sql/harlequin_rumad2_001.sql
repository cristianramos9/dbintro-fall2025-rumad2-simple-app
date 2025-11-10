-- select cid from class
-- select cid, ccode, cdesc, classid, reqid, prereq
-- from class natural inner join requisite where cid = classid

-- select cid, classid from (class natural inner join requisite) where cid = classid

select cid, classid, reqid from (class natural inner join requisite)
where cid = classid order by cid