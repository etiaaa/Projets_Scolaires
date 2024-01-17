/**********************************************************************************************/

// Classe Position
public class Position { /** On définit la classe Position **/
    private double x; /** Elle comporte une valeur x ... **/
    private double y; /** Et y qui représente les points d'abcisses de la position **/

    public Position(double x, double y){ /** On définit la méthode Position que l'on réutilisera dans les autres classes **/
        this.x = x;
        this.y = y;
    }

    public double getX(){ /**Le getteur qui renvoie la valeur du x **/
        return x; 
    }

    public double getY(){ /**Le getteur qui renvoie la valeur du y **/
        return y; 
    }

    public void setX(int x){ /**Le setteur qui recupere la valeur du x **/
        this.x = x; 
    }

    public void setY(int y){ /**Le setteur qui recupere la valeur du y **/
        this.y = y;         
    }

    public string affichePosition(){ /**Et la fonction affichePosition qui nous retourne plus lisiblement les données de la position**/
        return "position: x: " + x + "km" + "\n" + "y:" + y + "km";
    }
}

/**********************************************************************************************/
