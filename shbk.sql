#create database shbk;
#create table shbk(
#id int(3),
#name varchar(8),
#sex varchar(2),
#age int(3),
#area varchar(10)
#)

create database shbk default character set utf8 collate UTF8_general_ci;

use shbk;

create table `article` (
  `id` int unsigned not null primary key,
  `content` varchar(200)
);

use shbk;

create table `commenttable` (
  `uesr` int unsigned not null primary key,
  `opinion` varchar(255)
);

use shbk;

create table `class`(
  `id` int unsigned not null primary key,
  `name` varchar(4),
  `tel` varchar(11)
);


