create table DHT22(
DHT22_id int primary key auto_increment,
luftfeuchtigkeit float,
zeitstempel varchar(255), 
temperatur float
);

alter table DHT22 auto_increment = 1;

create table SDS011(
SDS011_id int primary key auto_increment,
PM10 float,
PM25 float, 
zeitstempel varchar(255)
);

alter table SDS011 auto_increment = 1;