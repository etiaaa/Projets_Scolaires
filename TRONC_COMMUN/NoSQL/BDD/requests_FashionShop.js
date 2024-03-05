const { MongoClient, ObjectId } = require('mongodb');
const moment = require('moment');

// URL de connexion à la base de données MongoDB
const url = 'mongodb://localhost:27017';
const dbName = 'FashionShop';

// Fonction pour exécuter les requêtes
async function runQueries() {
  const client = new MongoClient(url, { useUnifiedTopology: true });

  try {
    await client.connect();
    console.log('Connexion à la base de données établie.');

    const db = client.db(dbName);

    // Requêtes de recherche de produits :
    // 1. Récupérer tous les produits d'une catégorie spécifique (par exemple, "T-shirt")
    const query1 = await db.collection('products').find({ category: 'T-shirt' }).toArray();
    console.log('1. Tous les produits de la catégorie "T-shirt":', query1);

    // 2. Récupérer tous les produits avec une certaine couleur (par exemple, "Bleu")
    const query2 = await db.collection('products').find({ colors: 'Bleu' }).toArray();
    console.log('2. Tous les produits de couleur "Bleu":', query2);

    // 3. Récupérer tous les produits avec un certain pourcentage de réduction (par exemple, 20%)
    const query3 = await db.collection('products').find({ discountPercentage: 20 }).toArray();
    console.log('3. Tous les produits avec 20% de réduction:', query3);

    // 4. Effectuer une recherche textuelle dans les descriptions des produits (par exemple, "élégant")
    const query4 = await db.collection('products').find({ $text: { $search: 'élégant' } }).toArray();
    console.log('4. Produits avec une description "élégant":', query4);

    // Requêtes de gestion des commandes :
    // 5. Récupérer les détails d'une commande spécifique (par exemple, orderId = 1)
    const query5 = await db.collection('processOrderStatus').find({ orderId: 1 }).toArray();
    console.log('5. Détails de la commande avec orderId = 1:', query5);

    // 6. Récupérer toutes les commandes en cours de livraison
    const query6 = await db.collection('processOrderStatus').find({ orderStatus: 'En cours de livraison' }).toArray();
    console.log('6. Toutes les commandes en cours de livraison:', query6);

    // 7. Récupérer les produits inclus dans une commande spécifique (par exemple, orderId = 1) avec les détails de chaque produit
    const query7 = await db.collection('processOrderLinesDetails').aggregate([
      { $match: { orderId: 1 } },
      {
        $lookup: {
          from: 'products',
          localField: 'productsLines.productId',
          foreignField: 'productId',
          as: 'productDetails'
        }
      }
    ]).toArray();
    console.log('7. Produits inclus dans la commande avec orderId = 1:', query7);

    // Requêtes liées aux clients :
    // 8. Récupérer les clients ayant effectué des achats pendant une période spécifique (par exemple, entre le 01/01/2023 et le 31/01/2023)
    const query8 = await db.collection('customers').find({
      'purchaseHistory.orderDate': {
        $gte: ISODate('2023-01-01'),
        $lt: ISODate('2023-01-31')
      }
    }).toArray();
    console.log('8. Clients ayant effectué des achats entre le 01/01/2023 et le 31/01/2023:', query8);

    // 9. Récupérer tous les clients ayant utilisé une promotion spécifique (par exemple, promoCode = 'ETE10')
    const query9 = await db.collection('customers').find({ 'purchaseHistory.promoCode': 'ETE10' }).toArray();
    console.log('9. Tous les clients ayant utilisé la promotion "ETE10":', query9);

    // 10. Récupérer tous les clients ayant effectué au moins une commande
    const query10 = await db.collection('customers').find({ 'purchaseHistory': { $exists: true, $ne: [] } }).toArray();
    console.log('10. Tous les clients ayant effectué au moins une commande:', query10);

    // Requêtes sur les promotions :
    // 11. Récupérer les promotions actives à la date actuelle
    const currentDate = new Date();
    const query11 = await db.collection('promotions').find({
      promotionStart: { $lte: currentDate },
      promotionEnd: { $gte: currentDate }
    }).toArray();
    console.log('11. Promotions actives à la date actuelle:', query11);

    // 12. Récupérer les produits avec une certaine taille (par exemple, 'L')
    const query12 = await db.collection('products').find({ sizes: 'L' }).toArray();
    console.log('12. Produits avec une taille "L":', query12);

    // Autres requêtes :
    // 13. Récupérer les catégories distinctes disponibles
    const query13 = await db.collection('categories').distinct('categoryName');
    console.log('13. Catégories distinctes disponibles:', query13);

    // 14. Récupérer les produits qui sont en stock (disponibles)
    const query14 = await db.collection('products').find({ availableStock: { $gt: 0 } }).toArray();
    console.log('14. Produits qui sont en stock:', query14);

    // 15. Récupérer les produits avec une évaluation moyenne supérieure à 4
    const query15 = await db.collection('products').find({ averageRating: { $gt: 4 } }).toArray();
    console.log('15. Produits avec une évaluation moyenne supérieure à 4:', query15);

  } finally {
    await client.close();
    console.log('Connexion à la base de données fermée.');
  }
}

// Exécute les requêtes
runQueries();
