/**********************************************************************************************/

// Classe Planète
public class Planete : Objet{ /** On définit la classe Planète qui hérite de la class Objet d'ou le ": Objet" **/
    private double diametre; /** Elle comporte uniquement un diametre **/

    public Planete(Position position_objet, double poids, double diametre) : base(position_objet, poids){ /** On définit une méthode Planete que nous réutiliserons dans les classes la nécéssitant **/
        this.diametre = diametre; 
    }

    public double getDiametre(){  /** Le getteur diametre qui renvoie le diametre **/
        return diametre; 
    }

    public void setDiametre(double diametre){  /** Le setteur qui recupere les données du diametre**/
        this.diametre = diametre; 
    }
}

/**********************************************************************************************/

