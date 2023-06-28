CREATE TABLE "emploi" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "cours" varchar(50) NOT NULL DEFAULT 'maths',
    "professeur" varchar(50) NOT NULL DEFAULT 'prof1',
    "quota_total" integer NOT NULL DEFAULT 30,
    "quota_restante" integer NOT NULL DEFAULT 30
);

CREATE TABLE "nouveauemploi_l1" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "texte" varchar(1000),
    "semaine" varchar(50) NOT NULL DEFAULT 'Semaine du __ au __',
    "emploi_id" integer NOT NULL REFERENCES "emploi" ("id") DEFERRABLE INITIALLY DEFERRED,
    "jour" varchar(10) NOT NULL,
    "heure_debut" time NOT NULL,
    "heure_fin" time NOT NULL,
    "duree_cours" integer NOT NULL DEFAULT 0,
    "actif" bool NOT NULL DEFAULT False,
    "salle" varchar(50) NOT NULL DEFAULT 'IRAN1',
    "groupe" varchar(50) NOT NULL DEFAULT 'Groupe 1'
);

CREATE TABLE "nouveauemploi_l2" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "texte" varchar(1000),
    "semaine" varchar(50) NOT NULL DEFAULT 'Semaine du __ au __',
    "emploi_id" integer NOT NULL REFERENCES "emploi" ("id") DEFERRABLE INITIALLY DEFERRED,
    "jour" varchar(10) NOT NULL,
    "heure_debut" time NOT NULL,
    "heure_fin" time NOT NULL,
    "duree_cours" integer NOT NULL DEFAULT 0,
    "actif" bool NOT NULL DEFAULT False,
    "salle" varchar(50) NOT NULL DEFAULT 'IRAN1',
    "groupe" varchar(50) NOT NULL DEFAULT 'Groupe 1'
);

CREATE TABLE "nouveauemploi_l3" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "texte" varchar(1000),
    "semaine" varchar(50) NOT NULL DEFAULT 'Semaine du __ au __',
    "emploi_id" integer NOT NULL REFERENCES "emploi" ("id") DEFERRABLE INITIALLY DEFERRED,
    "jour" varchar(10) NOT NULL,
    "heure_debut" time NOT NULL,
    "heure_fin" time NOT NULL,
    "duree_cours" integer NOT NULL DEFAULT 0,
    "actif" bool NOT NULL DEFAULT False,
    "salle" varchar(50) NOT NULL DEFAULT 'IRAN1',
    "groupe" varchar(50) NOT NULL DEFAULT 'Groupe 1'
);

CREATE TABLE "nouveauemploi_m1" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "texte" varchar(1000),
    "semaine" varchar(50) NOT NULL DEFAULT 'Semaine du __ au __',
    "emploi_id" integer NOT NULL REFERENCES "emploi" ("id") DEFERRABLE INITIALLY DEFERRED,
    "jour" varchar(10) NOT NULL,
    "heure_debut" time NOT NULL,
    "heure_fin" time NOT NULL,
    "duree_cours" integer NOT NULL DEFAULT 0,
    "actif" bool NOT NULL DEFAULT False,
    "salle" varchar(50) NOT NULL DEFAULT 'IRAN1',
    "groupe" varchar(50) NOT NULL DEFAULT 'Groupe 1'
);

CREATE TABLE "nouveauemploi_m2" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "texte" varchar(1000),
    "semaine" varchar(50) NOT NULL DEFAULT 'Semaine du __ au __',
    "emploi_id" integer NOT NULL REFERENCES "emploi" ("id") DEFERRABLE INITIALLY DEFERRED,
    "jour" varchar(10) NOT NULL,
    "heure_debut" time NOT NULL,
    "heure_fin" time NOT NULL,
    "duree_cours" integer NOT NULL DEFAULT 0,
    "actif" bool NOT NULL DEFAULT False,
    "salle" varchar(50) NOT NULL DEFAULT 'IRAN1',
    "groupe" varchar(50) NOT NULL DEFAULT 'Groupe 1'
);

CREATE TABLE "nouveauemploi_m3" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "texte" varchar(1000),
    "semaine" varchar(50) NOT NULL DEFAULT 'Semaine du __ au __',
    "emploi_id" integer NOT NULL REFERENCES "emploi" ("id") DEFERRABLE INITIALLY DEFERRED,
    "jour" varchar(10) NOT NULL,
    "heure_debut" time NOT NULL,
    "heure_fin" time NOT NULL,
    "duree_cours" integer NOT NULL DEFAULT 0,
    "actif" bool NOT NULL DEFAULT False,
    "salle" varchar(50) NOT NULL DEFAULT 'IRAN1',
    "groupe" varchar(50) NOT NULL DEFAULT 'Groupe 1'
);
