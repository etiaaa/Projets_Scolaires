/**********************************************************************************************/

public class Simulation { /** On définit la class Simulation**/
    private int frequence; /** Elle comporte une frequence qui calcule la vitesse de rafraichissement en metre par seconde (ms)**/
    private Planete planete; /** Une planete et toutes les informations concernant la planete**/
    private Objet objet; /** Un objet et toutes les informations concernantl'objet**/
    private int angleLancement; /** Un angle de  **/
    private int vitesse; /** Une vitesse **/
    public Simulation(Planete planete, Objet objet, int angleLancement, int vitesse, int frequence){ /** Une méthode que l'on utilisera au besoin par la suite **/
        this.planete = planete;
        this.objet = objet;
        this.angleLancement = angleLancement;
        this.vitesse = vitesse;
        this.frequence = frequence;
    }

    public Planete getPlanete(){  /** Un getteur Planete qui retourne la planete **/
        return planete; 
    }
    public Objet getObjet(){  /** Un getteur Objet qui retourne la planete **/
        return objet; 
    }
    public int getAngleLancement(){ /** Un getteur AngleLancement qui retourne la planete **/
        return angleLancement; 
    }
    public int getVitesse(){ /** Un getteur Vitesse qui retourne la planete **/
        return vitesse;
    }

    public void setPlanete(Planete planete){ /** Un setteur Planete qui recupere la planete **/
        this.planete = planete; 
    }
    public void setObjet(Objet objet){ /** Un setteur Objet qui recupere la planete **/
        this.objet = objet; 
    }

    public void setAngleLancement(int angleLancement){  /** Un setteur AngleLancement qui recupere la planete **/
        this.angleLancement = angleLancement; 
    }
    public void setVitesse(int vitesse){ /** Un setteur Vitesse qui recupere la planete **/
        this.vitesse = vitesse; 
    }

    public void startSimulation(string hauteur){ /** Une méthode startSimulation qui permet de lancer la simulation **/
        while (true){ 

            /** Premierement on calcul la force gravitationnelle entre l'objet et la planète **/
            double forceGravitationnelle = Constante.ForceGravitationnelle(objet.getPoids(), planete.getPoids(), Constante.Distance(objet.getPosition(), planete.getPosition()));

            /** Deuxièmement on modifie la direction de l'objet en fonction de la force gravitationnelle **/
            double[] vecteurDirection = Constante.Direction(angleLancement, vitesse + forceGravitationnelle);

            
            Position position = objet.getPosition();
            Console.WriteLine("position:   x:" + position.getX() + "km\n" + "            y:" + position.getY() + "km");
            Console.WriteLine("vitesse:    " + vitesse + "ms");
            Console.WriteLine("hauteur:    " + hauteur + "km");

            Thread.Sleep(frequence);
        

            /** Troisiemement on calcule la distance entre l'objet et la planète **/
            double distance = Constante.Distance(objet.getPosition(), planete.getPosition());

            /** Et enfin on arrête la simulation si l'objet touche la planète **/
            if (distance <= 0){
                Console.WriteLine("Simulation terminée : l'objet a touché la planète.");
                break;
            }
        }
    }
}

/**********************************************************************************************/