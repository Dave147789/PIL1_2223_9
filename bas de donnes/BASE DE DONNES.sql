-- Création de la base de données
CREATE DATABASE IF NOT EXISTS gestion_emplois_du_temps;
USE gestion_emplois_du_temps;

-- Table pour les utilisateurs
CREATE TABLE utilisateurs (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255) NOT NULL,
  prenom VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  mot_de_passe VARCHAR(255) NOT NULL,
  role ENUM('etudiant', 'administration') NOT NULL
);

-- Table pour les promotions
CREATE TABLE promotions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255) NOT NULL
);

-- Table pour les filières
CREATE TABLE filieres (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255) NOT NULL
);

-- Table pour les groupes
CREATE TABLE groupes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255) NOT NULL,
  id_promotion INT,
  id_filiere INT,
  FOREIGN KEY (id_promotion) REFERENCES promotions(id),
  FOREIGN KEY (id_filiere) REFERENCES filieres(id)
);

-- Table pour les enseignements
CREATE TABLE enseignements (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255) NOT NULL,
  id_filiere INT,
  FOREIGN KEY (id_filiere) REFERENCES filieres(id)
);

-- Table pour les salles
CREATE TABLE salles (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255) NOT NULL
);

-- Table pour les cours
CREATE TABLE cours (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_enseignement INT,
  id_groupe INT,
  id_enseignant INT,
  id_salle INT,
  jour_semaine ENUM('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi') NOT NULL,
  heure_debut TIME NOT NULL,
  heure_fin TIME NOT NULL,
  FOREIGN KEY (id_enseignement) REFERENCES enseignements(id),
  FOREIGN KEY (id_groupe) REFERENCES groupes(id),
  FOREIGN KEY (id_enseignant) REFERENCES utilisateurs(id),
  FOREIGN KEY (id_salle) REFERENCES salles(id)
);

-- Table pour les emploi du temps
CREATE TABLE emploi_du_temps (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_promotion INT,
  id_groupe INT,
  id_cours INT,
  date DATE NOT NULL,
  FOREIGN KEY (id_promotion) REFERENCES promotions(id),
  FOREIGN KEY (id_groupe) REFERENCES groupes(id),
  FOREIGN KEY (id_cours) REFERENCES cours(id)
);
