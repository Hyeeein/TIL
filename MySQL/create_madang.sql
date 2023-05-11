drop database if exists madangdb;
drop user if exists madang@localhost;

create database madangdb;

create user madang@localhost
identified with mysql_native_password by 'madang';

grant all privileges on madangdb.* to madang@localhost with grant option;

commit;