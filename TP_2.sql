create database if not exists Bibliotheque;
use Bibliotheque;
create table Livres(
	IdLivres int primary key,
    Titre varchar(20),
    AuteurId int ,	
	AnneePublication year,
	Quantite int default 1,
constraint Auteur_Id 
foreign key (AuteurId) references Auteurs(IdAuteur),
constraint AnneePublication check(AnneePublication>1800)
    );
create table Auteurs(
	IdAuteur int primary key,
    Nom varchar(20),
    Pays  varchar(20)
); 
create table Emprunts(
	IdEmprunts int primary key,
    UtilisateurId int,
    LivreId int,
    DateEmprunt date,
    DateRetour date,
constraint Utilisateur_Id
foreign key (UtilisateurId) references Emprunts(UtilisateurId),
constraint Livre_Id
foreign key (IdLivres) references Livres(IdLivres)
);