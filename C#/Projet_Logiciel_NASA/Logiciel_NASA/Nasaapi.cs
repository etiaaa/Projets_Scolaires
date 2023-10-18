//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

namespace NASAAPI
{ /** Nom du namespace NASAAPI **/


    public class Image_Du_Jour{ /** Classe Image du jour qui r�cup�re l'image du jour depuis l'API de la NASA, elle comporte:**/

        private static Image_Du_Jour? _instance; /** L'instance Image du jour **/
        private readonly string _url = "https://api.nasa.gov/planetary/apod"; /** L'url qui renvoie � l'API **/
        private HttpClient _httpClient; /** L' Http du Client **/

        private Image_Du_Jour(){ _httpClient = new HttpClient();} /** Le nouveau Http du client**/

        public static Image_Du_Jour Instance{ /** D�finition de l'instance Image du jour **/

            get{ if (_instance == null){ _instance = new Image_Du_Jour();}
                return _instance;
            }
        }

        public async void GetImage_Du_Jour(string apiKey, Action<Reponse_Image_Du_Jour> onSuccess, Action<Exception> onError){ 
            /**On d�finit une m�thode asynchromatique du Get Image du jour **/
            try{
                var Reponse = await _httpClient.GetAsync($"{_url}?api_key={apiKey}"); /** On d�finit une variable Reponse qui permettra au client de renseigner sa cl� d'API **/
                Reponse.EnsureSuccessStatusCode(); /** Qui permet de v�rifier que la cl� passer (donc le nouveau lien) est valide **/
                var jsonConvert = await Reponse.Content.ReadAsStringAsync(); /** La variable Attente qui attend la r�ponse de validit� de la variabe Reponse **/
                var Resultat = jsonConvert.DeserializeObject<Reponse_Image_Du_Jour>(jsonConvert); /** La variable r�sultat qui permet d'afficher le r�sultat, c'est � dire l'image du jour de la Nasa**/
                onSuccess?.Invoke(Resultat); /** Qui permet la mise � jour du r�sultat **/
            }

            catch (Exception ex){ onError?.Invoke(ex);}
        }
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Reponse_Image_Du_Jour{ /** La classe Reponse Image Du Jour qui en fonction de la r�ponse r�cup�re les donn�es de l'API Nasa elle comporte, **/ 

        public string? Copyright { get; set; } /** L'attribut set et get Copyright **/
        public string? Date { get; set; } /** L'attribut set et get Date **/
        public string? Explanation { get; set; } /** L'attribut set et get Explanation **/
        public string? HdUrl { get; set; } /** L'attribut set et get HdUrl **/
        public string? Titre { get; set; } /** L'attribut set et get Titre **/
        public string? Url { get; set; } /** L'attribut set et get Url **/
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Asteroide{ /** La classe Asteroide qui r�cup�te la liste des ast�roides les plus proches de la terre, elle contient **/

        private static Asteroide? _instance; /** L'instance asteroide  **/
        private readonly string _url = "https://api.nasa.gov/neo/rest/v1/feed"; /** L'attribut url qui r�cup�re l'url de l'image des asteroides **/
        private HttpClient _httpClient; /** L' http du client**/

        private Asteroide() { _httpClient = new HttpClient(); } /** Le nouvel http du client**/

        public static Asteroide Instance{ /** l'instance asteroide qui,**/

            get{
                if (_instance == null){_instance = new Asteroide();} /** si elle est nulle on cr�er une novuelle instance comportant les donn�es de l'assteroide **/
                return _instance;
            }
        }

        public async void GetListe_Asteroides(string Debut_Date, string Fin_Date, string apiKey, Action<Reponse_Asteroide> onSuccess, Action<Exception> onError){
            /**La m�thode asynchromatique de la liste des asteroide avec la date de d�but et de fin de vie de chaque asteroide  **/
            try
            {
                var Resultat = await _httpClient.GetAsync($"{_url}?start_date={Debut_Date}&end_date={Fin_Date}&api_key={apiKey}"); /** On d�finit une variable Reponse qui permettra au client de renseigner sa cl� d'API **/
                HttpResponseMessage resultat = Resultat;
                resultat.EnsureSuccessStatusCode(); /** Qui permet de v�rifier que la cl� passer (donc le nouveau lien) est valide **/
                var jsonConvert = await resultat.Content.ReadAsStringAsync();
                NewMethod(jsonConvert);/** La variable r�sultat qui permet d'afficher le r�sultat, c'est � dire l'image du jour de la Nasa**/
                onSuccess?.Invoke(resultat); /** Qui permet la mise � jour du r�sultat **/
            }
            catch (Exception ex) { onError?.Invoke(ex); }
        }

        private static void NewMethod(string jsonConvert)
        {
            /** La variable Attente qui attend la r�ponse de validit� de la variabe Reponse **/
            var Resultat = jsonConvert.DeserializeObject<Reponse_Asteroide>(jsonConvert);
        }
    }


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Reponse_Asteroide{ /** La classe de r�ponse de l'ast�roide qui r�cup�re les donn�es de la liste des asteroides les plus proches de la Terrre, elle comporte **/

        public string? NombreDelement { get; set; } /** Le nombre d'�l�ment **/
        public List<Asteroide>? NearEarthObjects { get; set; } /**La liste des ast�roides les plus proches de la terre **/
    }

   
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Donnees_Asteroides{ /** La classe Donn�es des ast�roides les plus proches elle contient,**/

        public string? Donnees { get; set; } /** L'attribut des donn�es **/
        public string? Vitesse { get; set; } /** L'attribut des vitesses **/
        public string? Distance { get; set; } /** L'attribut de la distance **/
    }


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

   

    public class Detail_Asteroide{ /** La classe Detail Asteroide qui contient les d�tails d'un asteroide, elle contient, **/

        private static Detail_Asteroide? _instance; /** Une instance Asteroide **/
        private readonly string _url = "https://api.nasa.gov/neo/rest/v1/neo"; /** Un url qui renvoie a l'image **/
        private HttpClient _httpClient; /** l'http Client  **/

        private Detail_Asteroide() { _httpClient = new HttpClient(); } 

        public static Detail_Asteroide Instance{ /** L'instant qui comporte, **/
                return Instance;

            get{ if (_instance == null) { _instance = new Detail_Asteroide();} /** si elle est nulle on cr�er une novuelle instance comportant les d�tails de l'assteroide **/
                return _instance;      
            }
        }

        public async void GetDetail_Asteroide(string Id_Asteroide, string Cle_API, Action<Reponse_Detail_Asteroide> onSuccess, Action<Exception> onError){
            /**La m�thode asynchromatique de les d�tails des ast�roides avec la date de d�but et de fin de vie de chaque asteroide  **/
            try{
                var Reponse = await _httpClient.GetAsync($"{_url}/{Id_Asteroide}?api_key={Cle_API}"); /** On d�finit une variable Reponse qui permettra au client de renseigner sa cl� d'API **/
                Reponse.EnsureSuccessStatusCode(); /** Qui permet de v�rifier que la cl� passer (donc le nouveau lien) est valide **/
                var jsonConvert = await Reponse.Content.ReadAsStringAsync(); /** La variable Attente qui attend la r�ponse de validit� de la variabe Reponse **/
                var Resultat = jsonConvert.DeserializeObject<Reponse_Detail_Asteroide>(jsonConvert); /** La variable r�sultat qui permet d'afficher le r�sultat, c'est � dire l'image du jour de la Nasa**/
                onSuccess?.Invoke(Resultat); /** Qui permet la mise � jour du r�sultat **/
            }
            catch (Exception ex){onError?.Invoke(ex);}
        }
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



    public class Reponse_Detail_Asteroide{ /** La classe de r�ponse au d�tail des ast�roides, elle comporte **/

        public string? Id { get; set; } /** **/ /** Id propre � chaque ast�roide **/
        public string? Nom { get; set; } /** Le nom de l'ast�roide **/
        public string? Diametre_Minimum { get; set; } /** Le diametre minimum de l'ast�roide **/
        public string? Diametre_Maximum { get; set; } /** Le diam�tre maximum de l'asteroide **/
        public List<Donnees_Asteroides>? Donnees_Asteroide { get; set; } /** La liste des donn�es correspondant � un asteroide **/
    }
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

namespace NASA { /** Nom du namespace NASA **/

using System;
using System.Collections.Generic;
using System.Threading.Tasks;

    public class Affichage{ /** Une classe Affichage qui permettra d'afficher l'image du jour les astéroides et leurs détails, elle comporte**/


        static void Main(string[] args, Dictionary<string, List<Asteroide>>? nearEarthObjects)
        { /** Une méthode principale**/

            /** Affiche l'image **/
            Console.WriteLine("Image du jour de la NASA"); 
            var apod = new APOD();
            apod.GetImage_Du_Jour("https://api.nasa.gov/planetary/apod?api_key=4Ic8iVU6C7fjrVl2YJpCy5XKyz5G5fdB9afPP0wd", Image => Console.WriteLine(Photo.Title), error => Console.WriteLine(error.Message));


            /** Affiche la liste des astéroides proches de la Terre **/
            Console.WriteLine("Liste des asteroides");
            var Asteroides = new Asteroides();
            Asteroides.GetAsteroides("https://api.nasa.gov/planetary/apod?api_key=4Ic8iVU6C7fjrVl2YJpCy5XKyz5G5fdB9afPP0wd", Resultat => {
                Console.WriteLine("Nombre d'éléments : " + Resultat.Nombre_D_Element);
                Console.WriteLine("Asteroides : ");

                foreach (var Asteroide in nearEarthObjects)
                {
                    Console.WriteLine("\t" + Asteroide.Nom + " - " + Asteroide.Diametre_Minimum + " - " + Asteroide.Diametre_Maximum);
                }
            }, error => Console.WriteLine(error.Message));


            /** Affiche les détails d'un astéroide **/
            Console.WriteLine("Détail d'un asteroide");
            var Detail_Asteroide = Detail_Asteroide.Instance;
            Detail_Asteroide.GetDetail_Asteroide("3542519", "https://api.nasa.gov/planetary/apod?api_key=4Ic8iVU6C7fjrVl2YJpCy5XKyz5G5fdB9afPP0wd", Resultat => {
                Console.WriteLine("Nom astéroide : " + Resultat.Name);
                Console.WriteLine("Diametre Minimum : " + Resultat.Diametre_Minimum);
                Console.WriteLine("Diametre Maximum : " + Resultat.Diametre_Maximum);
                Console.WriteLine("Données : ");

                foreach (var Donnees in Resultat.Donnees)
                {
                    Console.WriteLine("\t Donnees : " + Donnees_Asteroides.Donnees);
                    Console.WriteLine("\t Vitesse : " + Donnees_Asteroides.Vitesse);
                    Console.WriteLine("\t Distance : " + Donnees_Asteroides.Distance);
                }
            }, error => Console.WriteLine(error.Message));

            Console.WriteLine("Fin");
            Console.ReadLine();
        }
    }
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


namespace NASA { /** Nom du namespace NASA **/

using System;
using System.Net.Http;
using System.Threading.Tasks;

    public class APOD { /** La classe APOD qui récupère l'image du jour, elle contient **/


        private readonly HttpClient _httpClient; /** l' http du client**/
        private readonly string _url; /** url de l'API du client **/

        public APOD(){

            _httpClient = new HttpClient();
            _url = "https://api.nasa.gov/planetary/apod?api_key={0}";
        }

        public async void GetImage_Du_Jour(string apiKey, Action<APOD_Photo> success, Action<Exception> error){
            /** La méthode asynchromatique de l'image du jour **/
            try{
                var Reponse = await _httpClient.GetAsync(string.Format(_url, apiKey)); /**  **/ /** On définit une variable Reponse qui permettra au client de renseigner sa clé d'API **/
                Reponse.EnsureSuccessStatusCode(); /** Qui permet de vérifier que la clé passer (donc le nouveau lien) est valide **/
                var Content = await Reponse.Content.ReadAsStringAsync(); /** La variable qui vérifie le contenu de l'image **/
                var Photo = Newtonsoft.Attente.AttentenConvert.DeserializeObject<APOD_Photo>(Content); 

                success(Photo);
            }

            catch (Exception ex) { error(ex); }
        }
    }


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    public class APOD_Photo{ /** La class APOD Photo qui affiche la photo, elle comporte**/

        public string? Titre { get; set; } /** L'attribut Titre **/
        public string? Explanation { get; set; } /** L'attribut Explanation**/
        public string? Url { get; set; } /** L'url **/
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Asteroides{ /**La classe Asteroides qui récupere la liste des astéroides les plus proches de la Terre, contribue **/

        private readonly HttpClient _httpClient; /** L'http du client**/
        private readonly string _url; /** L'url **/

        public Asteroides(){ 

            _httpClient = new HttpClient();
            _url = "https://api.nasa.gov/neo/rest/v1/feed?start_date={0}&end_date={1}&api_key={2}";
        }

        public async void GetAsteroides(string apiKey, Action<Object_Asteroides> success, Action<Exception> error){
            try{
                var Debut_Date = DateTime.Now.ToString("yyyy-MM-dd");
                var Fin_Date = DateTime.Now.AddDays(7).ToString("yyyy-MM-dd");

                var Reponse = await _httpClient.GetAsync(string.Format(_url, Debut_Date, Fin_Date, apiKey));
                Reponse.EnsureSuccessStatusCode();

                var Content = await Reponse.Content.ReadAsStringAsync();
                var Object = Newtonsoft.Attente.AttenteConvert.DeserializeObject<Object_Asteroides>(Content);

                success(Object);
            }

            catch (Exception ex) { error(ex); }
        }
    }


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Object_Asteroides{ /** La classe Object aséroides qui comporte  **/

        public int Nombre_D_Element { get; set; } /** L'attribut Nombre_D_Element**/
        public Dictionary<string, List<Asteroide>>? NearEarthObjects { get; set; } /** Liste des asteroides**/
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Asteroide{ /** La classe Asteroide qui récupère les détails de chaque astéroide, elle contient**/

        public string? Nom { get; set; } /** L'attribut nom **/
        public double Diametre_Minimum { get; set; } /** L'attribut Diametre Minumum **/
        public double Diameter_Maximum { get; set; } /** L'attribut Diametre Maximum **/
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



namespace NASA { /** Nom du namespace NASA **/

using System;
    using System.Diagnostics.Tracing;
    using System.Net.Http;
    using System.Reflection.Metadata.Ecma335;
    using System.Threading.Tasks;

    public class AsteroideDetails{ /** La classe Asteroides qui détails un asteroides en particulier elle comporte**/

        private readonly HttpClient _httpClient; /** L'http du client **/
        private readonly string _url; /** L'url **/

        public Details_Asteroides(){ /** La méthode Asteroide **/

            _httpClient = new HttpClient();
            _url = "https://api.nasa.gov/neo/rest/v1/neo/{0}?api_key={1}";
        }

        public async void GetDetails_Asteroides(string IdAsteroide, string CleAPI, Action<Details_Objects_Asteroides> success, Action<Exception> error){
            
            try{
                var Reponse = await _httpClient.GetAsync(string.Format(_url, IdAsteroide, CleAPI));
                Reponse.EnsureSuccessStatusCode();
                var Content = await Reponse.Content.ReadAsStringAsync();
                var Objet = Newtonsoft.JsonConvert.JsonConvert.DeserializeObject<Details_Objects_Asteroides>(Content);

                success(Objet);
            }

            catch (Exception ex) { error(ex); }
        }
    }


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    public class Details_Objects_Asteroides{  /** La classe Details Asteroides qui donne des détails sur l'asteroide, elle comporte**/

        public string? Nom { get; set; }  /** Le nom **/
        public double Diametre_Minimum { get; set; }  /** Le diametre minimum**/
        public double Diametre_Maximum { get; set; }  /** Le diametre maximum **/
        public List<Donnees_Asteroides>? Donnees_Asteroides { get; set; }  /** La liste des données des astéroides **/
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  
    public class Donnees_Asteroides{ /** La classe Donnees_Asteroides qui représente les données d'un astéroide, elle comporte **/

        public Temps Asteroides { get; set; } /** L'attribut du temps de vie de l'asteroide**/
        public double Distance { get; set; }  /** L'atribut Distance qui donne les données de la distance entre l'asteroide choisi et la terre **/
    }
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


