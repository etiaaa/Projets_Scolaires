CREATE TABLE Envoie_Facture (
idDate_Envoie DATE NOT NULL,
idCode INT NOT NULL,
idNumero INT NOT NULL,

PRIMARY KEY (`idDate_Envoie`),
FOREIGN KEY (`idCode`) REFERENCES `projet_1mode`.`client` (`idCode`),
FOREIGN KEY (`idNumero`) REFERENCES `projet_1mode`.`compteur` (`idNumero`)
);

