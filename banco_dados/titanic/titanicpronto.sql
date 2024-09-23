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

select count(*) from titanic_base;
select count(*) from titanic_base where survived=1;
SELECT COUNT(*) from titanic_base where survived=1 and age < 12;
select count(*) from titanic_base where survived=1 and sex = 'female';
select count(*) from titanic_base where survived=1 and sex = 'male';



