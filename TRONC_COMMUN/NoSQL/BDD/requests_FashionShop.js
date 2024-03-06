// 1.Récupérer tous les produits avec un certain pourcentage de réduction (par exemple, 20%)
db.products.find({ discountPercentage: 20 });

// 2. Récupérer les détails d'une commande spécifique (par exemple, orderId = 1)
db.processOrderStatus.find({ orderId: 1 });

// 3. Récupérer les produits inclus dans une commande spécifique (par exemple, orderId = 1) avec les détails de chaque produit
db.processOrderLinesDetails.aggregate([
  { $match: { orderId: 1 } },
  {
    $lookup: {
      from: 'products',
      localField: 'productsLines.productId',
      foreignField: 'productId',
      as: 'productDetails'
    }
  }
]);


// 4. Récupérer tous les clients ayant utilisé une promotion spécifique (par exemple, promoCode = 'ETE10')
db.customers.find({ 'purchaseHistory.promoCode': 'ETE10' });

// 5. Récupérer tous les clients ayant effectué au moins une commande
db.customers.find({ purchaseHistory: { $exists: true, $ne: [] } });

// 6. Récupérer les promotions actives à la date actuelle
const currentDate = new Date();
db.promotions.find({
  promotionStart: { $lte: currentDate },
  promotionEnd: { $gte: currentDate }
});

// 7. Récupérer les catégories distinctes disponibles
db.categories.distinct('categoryName');

// 8. Récupérer les produits qui sont en stock (disponibles)
db.products.find({ availableStock: { $gt: 0 } });

// 9. Récupérer les produits avec une évaluation moyenne supérieure à 4
db.products.find({ averageRating: { $gt: 4 } });


// 10. Récupérer les promotions qui sont actuellement actives (à la date actuelle) :
const currentDate = new Date();
db.promotions.find({
  promotionStart: { $lte: currentDate },
  promotionEnd: { $gte: currentDate }
});
