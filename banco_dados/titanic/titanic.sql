CREATE database titanic;
use titanic;

create table titanic_base(
passengerld int primary key,
survived int,
pclass int,
nome varchar(100),
sex varchar(20),
age varchar(10),
sibsp int,
parch int,
ticket varchar(70),
fare float,
cabin VARCHAR(20),
embarked varchar(10)
);

drop table titanic_base;
select count(*) from titanic_base limit 10000;