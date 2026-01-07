create database if not exists GestionArticle;
use GestionArticle;
create table Articles(
	Code_article varchar(5) primary key,
    Designation varchar(20),
    Prix_unitaire decimal(6,2),
    Quantite_stock int
    );
create table Livraisons(
	Num_livraison varchar(5) primary key,
    Date_livraison date,
    Code_article varchar(5),
    Qte_livree int,
	constraint CodArticle
    foreign key (Code_article) references Articles(Code_article)
    );
insert into Articles
values('P0001','Ordinateur', 950.50, 10),
	('P0002','Ecran', 120.00, 30),
	('P0003','Clavier', 15.80, 120),
	('P0004','Imprimante', 250.00, NULL);
insert into Livraisons
values('L0010','2020-06-01','P0001', 2),
	('L0020','2020-06-15','P0003', 26),
	('L0030','2020-06-30','P0004', 10);
select * from Articles;
select Designation,Quantite_stock from Articles;
select * from Articles
where Prix_unitaire>=100;
select * from Articles
where Quantite_stock<=30 and Quantite_stock>=10;
select * from Articles
where Designation like 'C%';
select * from Articles
where Designation like '%r%';
update Articles
set Quantite_stock=Quantite_stock-2
where Code_article='P0001';
delete from Articles
where Code_article='P0002';
select sum(Quantite_stock) as Som_quantite from Articles;
select avg(Prix_unitaire) as Moyen from Articles;
select * from Livraisons
where Date_livraison between '2020-06-01'and'2020-06-30'