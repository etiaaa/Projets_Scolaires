/**********************************************************************************************/

static class Constante{ /** On définit la class Constante**/
    /** Elle ne comporte rien mise à part des méthodes**/
    public static double[] Direction(double angle, double vitesse){ /** La métode Direction qui calcule la direction à l'aide de vecteur**/
        double[] vecteurDirection = new double[2]; /** Elle comporte un vecteur de direction**/
        vecteurDirection[0] = Math.Cos(angle) * vitesse; /** Le premier element de cette liste de vecteur est le calcul du cosinus**/
        vecteurDirection[1] = Math.Sin(angle) * vitesse; /** Le premier element de cette liste de vecteur est le calcul du sinus**/
        return vecteurDirection;
    }

    public static readonly double GRAVITE = 9.81; /** Attribut qui indique la gravite en minute par seconde (mss)**/

    public static double Distance(double x1, double y1, double x2, double y2){ /** La métode Distance qui calcule la distance **/
        return Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));
    }

    public static double ForceGravitationnelle(double masse1, double masse2, double distance){ /** La métode ForceGravitationnelle qui calcule la force gravitationnelle**/
        return GRAVITE * (masse1 * masse2 / Math.Pow(distance, 2));
    }

    internal static double Distance(Position position1, Position position2){ 
        throw new NotImplementedException();
    }

    internal static double CalculerForceGravitationnelle(double v1, double v2, object value)
    {
        throw new NotImplementedException();
    }
}