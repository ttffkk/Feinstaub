create table DHT22(
DHT22_id int primary key auto_increment,
luftfeuchtigkeit float,
zeitstempel Datetime,
temperatur float
);

create table SDS011(
SDS011_id int primary key auto_increment,
PM10 float,
PM25 float, 
zeitstempel datetime
);

