###################################################################
#1 Liste des avions de la compagnie :

SELECT NUMERO_ENREGISTREMENT 
FROM AVION;

###################################################################
#2 Liste des pilotes de Sup Air Line :

SELECT * 
FROM SALARIE 
WHERE FONCTION = "Pilote";

###################################################################
#3 Liste du personnel par catégorie :

SELECT * 
FROM SALARIE 
ORDER BY FONCTION;

###################################################################
#4 Liste des passagers par vol :	
	
SELECT NUMERO_DU_VOL,NUMERO_DU_PASSAGER 
FROM DEPART 
GROUP BY DATE_DE_DEPART;

###################################################################
#5 Liste des vols vers une ville donnée :

SELECT NUMERO_DE_VOL,VILLE_DE_DESTINATION 
FROM ROUTE 
ORDER BY VILLE_DE_DESTINATION; 

###################################################################
#6 Liste des départs de la journée :

SELECT * 
FROM DEPART 
GROUP BY DAY(DATE_DE_DEPART);

###################################################################
#7 Liste des villes desservies par Sup Air Line :

SELECT DISTINCT VILLE_DE_DESTINATION 
FROM ROUTE;

###################################################################
#8 Liste des destinations desservies par un commandant de bord :

SELECT VILLE_DE_DESTINATION, NUMERO_SECURITE_SOCIALE 
FROM ROUTE 
JOIN DEPART 
ON ROUTE.NUMERO_DE_VOL= DEPART.NUMERO_DU_VOL 
GROUP BY NUMERO_SECURITE_SOCIALE;

###################################################################
#9 Liste des pilotes dont la licence doit être renouvelée :

SELECT * 
FROM SALARIE 
WHERE YEAR(DATE_DE_VALIDITE_DE_LA_LICENCE) = "2022";

###################################################################
#10 Listes des passagers réguliers qui effectuent plus de 2 vols/mois :

SELECT NUMERO_DU_PASSAGER, COUNT(NUMERO_DU_PASSAGER) 
FROM DEPART 
GROUP BY NUMERO_DU_PASSAGER,MONTH(DATE_DE_DEPART) 
HAVING COUNT(NUMERO_DU_PASSAGER)= 2;

###################################################################
#11 Professions avec les passagers les plus réguliers:

SELECT NUMERO_DU_PASSAGER, PROFESSION 
FROM PASSAGER 
NATURAL JOIN DEPART 
GROUP BY NUMERO_DU_PASSAGER,MONTH(DATE_DE_DEPART) 
HAVING COUNT(NUMERO_DU_PASSAGER)= 2 ;

###################################################################
#12 Nombres d'heure de travail par un commandant de bord:
# PAS FAITE

###################################################################
#13 Nombres d'heure de vol de chaque avion
SELECT TIMEDIFF(HEURE_ARRIVEE,HEURE_DEPART) 
FROM VOL;

###################################################################
#14 Nombre de passagers transportés par avion sur une période donnée:

SELECT NUMERO_ENREGISTREMENT,COUNT(NUMERO_DU_PASSAGER) 
FROM DEPART 
GROUP BY NUMERO_ENREGISTREMENT,DATE_DE_DEPART 
BETWEEN "2022-01-01" AND "2022-07-19"; 

###################################################################
#15 Nombre de passagers transportés sur une période donnée:

SELECT COUNT(NUMERO_DU_PASSAGER) 
FROM DEPART 
GROUP BY DATE_DE_DEPART 
BETWEEN "2022-01-01" AND "2022-03-19"; 

###################################################################
#16 Nombres de billets vendus par jour/semaine/mois: 
#Par jour:
SELECT COUNT(NUMERO_DU_BILLET)
FROM BILLET
GROUP BY DAY(DATE_D_EMISSION);

##############################
#Par mois
SELECT COUNT(NUMERO_DU_BILLET)
FROM BILLET
GROUP BY WEEK(DATE_D_EMISSION); 

##############################
#Par année:
SELECT COUNT(NUMERO_DU_BILLET)
FROM BILLET
GROUP BY MONTH(DATE_D_EMISSION);

###################################################################
#17 Ventes totales:
SELECT COUNT(NUMERO_DU_BILLET)
FROM BILLET;

################################################################### 
#18 Nombres moyens de vol par pilotes:

SELECT NUMERO_SECURITE_SOCIALE, AVG(NUMERO_DU_VOL)
FROM DEPART
NATURAL JOIN SALARIE
GROUP BY FONCTION="Pilote";

###################################################################
#19 Destination les plus rentables (taux d'occupations élevé):

SELECT VILLE_DE_DESTINATION,COUNT(VILLE_DE_DESTINATION) 
FROM ROUTE
GROUP BY VILLE_DE_DESTINATION
HAVING COUNT(VILLE_DE_DESTINATION) >=3;

###################################################################
#20 Taux d'occupations par avion/vol/destination:
#Par avion
SELECT NUMERO_ENREGISTREMENT,PLACES_OCCUPEES 
FROM DEPART
GROUP BY NUMERO_ENREGISTREMENT;

##############################
#Par vol:
SELECT NUMERO_DU_VOL,PLACES_OCCUPEES 
FROM DEPART
GROUP BY NUMERO_DU_VOL;

##############################
#Par destination
SELECT DISTINCT VILLE_DE_DESTINATION,PLACES_OCCUPEES 
FROM DEPART
NATURAL JOIN ROUTE
GROUP BY VILLE_DE_DESTINATION;

###################################################################
#21 Quels pilotent volent vers leur ville:
# PAS FAITE

###################################################################
							#FIN
###################################################################