CREATE TABLE Utilisateurs (
  IDUtilisateur INT PRIMARY KEY AUTO_INCREMENT,
  Nom VARCHAR(255),
  Prenom VARCHAR(255),
  Email VARCHAR(255),
  MotDePasse VARCHAR(255)
);

CREATE TABLE Filieres (
  IDFiliere INT PRIMARY KEY AUTO_INCREMENT,
  NomFiliere VARCHAR(255)
);

CREATE TABLE Groupes (
  IDGroupe INT PRIMARY KEY AUTO_INCREMENT,
  IDFiliere INT,
  NomGroupe VARCHAR(255),
  FOREIGN KEY (IDFiliere) REFERENCES Filieres(IDFiliere)
);

CREATE TABLE Enseignements (
  IDEnseignement INT PRIMARY KEY AUTO_INCREMENT,
  NomEnseignement VARCHAR(255)
);

CREATE TABLE EmploisDuTemps (
  IDEmploiDuTemps INT PRIMARY KEY AUTO_INCREMENT,
  IDGroupe INT,
  IDEnseignement INT,
  Jour VARCHAR(255),
  HeureDebut TIME,
  HeureFin TIME,
  Salle VARCHAR(255),
  FOREIGN KEY (IDGroupe) REFERENCES Groupes(IDGroupe),
  FOREIGN KEY (IDEnseignement) REFERENCES Enseignements(IDEnseignement)
);
