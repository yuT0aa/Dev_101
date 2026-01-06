create database if not exists GestionEmployes;
use GestionEmployes;
create table Employes(
	IdEmploye INT primary key,
    nom VARCHAR(10),
    prenom VARCHAR(10),
    poste VARCHAR(10),
    salaire INT,
    IdDepartement INT,
	DateEmbauche DATE,
    constraint dep_emp
    foreign key(IdDepartement)
    references Departements(IdDepartement),
	constraint salaire check (salaire>3000)
     );
create table Departements(
	IdDepartement INT,
    NomDepartement VARCHAR(15),
    Budget BIGINT,
    constraint Budget_check check (Budget>10000)
    );
alter table Departements
add primary key (IdDepartement);
show create table Departements;
alter table Employes
modify salaire DECIMAL(12,2),
drop column poste ;
alter table Departements
rename to services;
drop table Employes;