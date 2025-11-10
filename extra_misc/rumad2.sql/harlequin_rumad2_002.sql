-- select cid from class

select classid,reqid from requisite 
where classid in (select cid from class)
and reqid in (select cid from class)
and classid = 9 and reqid = 6