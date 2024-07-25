create database voluntify;
use voluntify;
create table events(name1 varchar(100), date1 date, activity1 varchar(500), duration1 bigint);
desc events;
insert into events(name1,date1,activity1,duration1)values
("Sudheera","2024-07-01", "Women in coding class", 4),
("Sudheera","2024-07-21", "Hiking in the mountains",5),
("Rohit","2024-07-02","IT Support at a zoo", 6),
("Rahul","2024-07-20","Gym body building",3);
select * from events;
select * from events where name1="Sudheera";
select sum(duration1) from events where name1="Sudheera";
select * from events where name1="Sudheera" and date1="2024-07-21";
select sum(duration1) from events where name1="Sudheera" and date1="2024-07-21";
select * from events order by duration1 desc;
select * from events order by duration1;
alter table events add column category1 varchar(20) default "sports";

















