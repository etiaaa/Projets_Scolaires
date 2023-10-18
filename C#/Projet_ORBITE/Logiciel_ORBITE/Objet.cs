/**********************************************************************************************/
// Classe Objet
public class Objet { /** On définit la classe Objet **/
    private Position position_objet; /**Elle comporte une positon **/
    private double poids; /** Et un poid **/

    public Objet(Position position_objet, double poids){ /** On définit une méthode public objet que l'on réutilisera dans les autres classes**/
        this.position_objet = position_objet; /** Elle comporte donc la position de l'objet **/
        this.poids = poids; /** Et son poid **/
    }

    public Position getPosition(){  /** Le getteur Position qui retourne la position de l'object **/
        return position_objet; 
    }

    public double getPoids(){  /** Le getteur Poid qui retourne le poid de l'objet **/
        return poids; 
    }

    public void setPosition(Position position_objet){ /** Logiquement le setteur Positon qui récupère les données de la position dans la variable position_objet **/
        this.position_objet = position_objet; 
    }

    public void setPoids(double poids){  /** Logiquement le setteur qui Poid qui récupère les données du poid dans la variable poid **/
        this.poids = poids; 
    }
}

/**********************************************************************************************/
