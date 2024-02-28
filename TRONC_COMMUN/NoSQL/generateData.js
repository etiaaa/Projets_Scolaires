// Importation des modules MongoDB nécessaires
const { MongoClient, ObjectId } = require('mongodb');
const faker = require('faker/locale/fr'); // Importez Faker.js avec la localisation française
const moment = require('moment');

// URL de connexion à la base de données MongoDB
const url = 'mongodb://localhost:27017';
const dbName = 'FashionShop';

///// ID ENTITES  //////////////////////////////////////////////////////////////////////////////////

let productIdCounter = 1; // Variable globale pour les IDs de produit
let categoryIdCounter = 1; // Variable globale pour les IDs de catégorie
let promotionIdCounter = 1; // Variable globale pour les IDs de promotion
let customerIdCounter = 1; // Variable globale pour les IDs de client
let orderIdCounter = 1; // Variable globale pour les IDs de commande
let orderLineIdCounter = 1; // Variable globale pour les IDs de ligne de commande

let customers; // Déclaration de la variable customers
let productIds; // Déclaration de la variable productIds
let products; // Déclaration de la variable products

const numOrders = 500; // Déclaration de la variable numOrders avec une valeur appropriée

///// CATEGORY /////////////////////////////////////////////////////////////////////////////////

// Fonction pour générer une catégorie aléatoire avec un nom, une description et un pourcentage de réduction associés
function generateRandomCategory() {
  const categoryId = categoryIdCounter++; // Incrémentation de l'ID
  const categoryName = faker.commerce.product(); // Utilisation de Faker.js pour générer un nom de catégorie (corrigé)
  const categoryDescription = faker.lorem.sentence(); // Utilisation de Faker.js pour générer une description de catégorie
  const discountPercentage = Math.floor(Math.random() * 20); // Pourcentage de réduction aléatoire entre 0 et 20
  // Retourne un objet de catégorie avec un ID généré, le nom de catégorie, la description associée et le pourcentage de réduction
  return {
    categoryId, // ID unique généré automatiquement pour la catégorie
    categoryName, // Nom d'une catégorie généré aléatoirement par Faker.js
    categoryDescription, // Description associée à une catégorie, générée aléatoirement par Faker.js
    discountPercentage, // Pourcentage de réduction associé à la catégorie
  };
}

///// PROMOTION ////////////////////////////////////////////////////////////////////////////////

// Liste de promotions
const promotionsList = [
  { promoName: 'Solde Été', promoCode: 'ETE10', discountPercentage: 10 },
  { promoName: 'Promotion Hiver', promoCode: 'HIVER15', discountPercentage: 15 },
  { promoName: 'Black Friday', promoCode: 'BF20', discountPercentage: 20 },
  { promoName: 'Noël', promoCode: 'NOEL12', discountPercentage: 12 },
  { promoName: 'Rentrée Scolaire', promoCode: 'RENTREE8', discountPercentage: 8 },
  { promoName: 'Printemps Fleuri', promoCode: 'PRINTEMPS18', discountPercentage: 18 },
  { promoName: 'Cyber Monday', promoCode: 'CYBER25', discountPercentage: 25 },
  { promoName: 'Fête des Mères', promoCode: 'FDM14', discountPercentage: 14 },
  { promoName: 'Saint-Valentin', promoCode: 'LOVE15', discountPercentage: 15 },
  { promoName: 'Spécial Anniversaire', promoCode: 'ANNIV10', discountPercentage: 10 },
  { promoName: 'Vacances d\'été', promoCode: 'VACANCES22', discountPercentage: 22 },
  { promoName: 'Promo Flash', promoCode: 'FLASH30', discountPercentage: 30 },
  { promoName: 'Back to School', promoCode: 'BTS16', discountPercentage: 16 },
  { promoName: 'Oktoberfest', promoCode: 'OKTOBER12', discountPercentage: 12 },
  { promoName: 'Journée de la Terre', promoCode: 'TERRE20', discountPercentage: 20 },
  { promoName: 'Halloween', promoCode: 'HALLOWEEN18', discountPercentage: 18 },
  { promoName: 'Jour de l\'Indépendance', promoCode: '4JUILLET15', discountPercentage: 15 },
  { promoName: 'Promo d\'Automne', promoCode: 'AUTOMNE14', discountPercentage: 14 },
  { promoName: 'Cadeau Gratuit', promoCode: 'CADEAU0', discountPercentage: 0 },
  { promoName: 'Soldes de Fin d\'Année', promoCode: 'FINANNEE25', discountPercentage: 25 },
  { promoName: 'Nouvel An', promoCode: 'NOUVELAN18', discountPercentage: 18 },
  { promoName: 'Fête du Travail', promoCode: 'TRAVAIL10', discountPercentage: 10 },
  { promoName: 'Saint-Patrick', promoCode: 'STPATRICK17', discountPercentage: 17 },
  { promoName: 'Journée Internationale de la Femme', promoCode: 'FEMME15', discountPercentage: 15 },
  { promoName: 'Semaine du Client', promoCode: 'CLIENT20', discountPercentage: 20 },
  { promoName: 'Fête du Canada', promoCode: 'CANADA12', discountPercentage: 12 },
  { promoName: 'Spécial Étudiants', promoCode: 'ETUDIANT10', discountPercentage: 10 },
];

// Fonction pour générer des données aléatoires pour une promotion
function generateRandomPromotion() {
  const promotionId = promotionIdCounter++; // Utilisation de l'incrémentation pour générer l'ID

  // Sélectionner une promotion aléatoire à partir de la liste prédéfinie
  const randomPromo = faker.random.arrayElement(promotionsList);

  // Générer des dates aléatoires pour le début et la fin de la promotion
  const startDate = faker.date.past(); // Promotion peut commencer à une date passée
  const endDate = faker.date.between(startDate, moment(startDate).add(Math.floor(Math.random() * 30) + 1, 'days').toDate());

  return {
    promotionId, // Génère un ID unique et automatique pour la promotion
    promotionName: randomPromo.promoName, // Nom de la promotion aléatoire
    promotionDescription: faker.lorem.sentence(), // Ajoutez une description de la promotion appropriée ici
    promotionStart: startDate, // Date de début de la promotion
    promotionEnd: endDate, // Date de fin de la promotion
    profitAmount: parseFloat((Math.random() * 50).toFixed(2)), // Montant de profit aléatoire entre 0 et 50
    discountPercentage: randomPromo.discountPercentage, // Pourcentage de réduction de la promotion prédéfinie
  };
}

///// PRODUIT //////////////////////////////////////////////////////////////////////////////////

const existingCategories = new Set(); // Pour stocker les catégories existantes
// Fonction pour obtenir une catégorie en fonction du type de produit
function getCategoryForType(productType) {
  const firstWord = productType.split(' ')[0].toLowerCase(); // Prend le premier mot en minuscules

  if (!existingCategories.has(firstWord)) {
    existingCategories.add(firstWord);

    return {
      categoryId: firstWord,
      categoryName: firstWord.charAt(0).toUpperCase() + firstWord.slice(1), // Met en majuscule la première lettre
      categoryDescription: faker.lorem.sentence(),
      discountPercentage: Math.floor(Math.random() * 20),
    };
  }

  return null; // Retourne null si la catégorie existe déjà
}

function getPromotionForType(type) {
  // Choisissez aléatoirement une promotion parmi les éléments de la liste prédéfinie
  const randomPromo = faker.random.arrayElement(promotionsList);
  return {
    promotionName: randomPromo.promoName,
    discountPercentage: randomPromo.discountPercentage,
  };
}

// Fonction pour générer des données aléatoires pour un produit
function generateRandomProduct() {
  const productId = productIdCounter++; // Utilisation de la variable globale pour les IDs de produit    

  // Fonction pour obtenir un élément aléatoire d'un tableau
  function getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
  }

  // Sélectionne aléatoirement un type de produit et une couleur
  const type = getRandomElement(types);
  const color = getRandomElement(colors);

  // Obtenir la catégorie et la promotion en fonction du type de produit
  const category = getCategoryForType(type);
  const promotion = getPromotionForType(type);

  return {
    productId, // ID unique généré automatiquement pour le produit
    productName: faker.commerce.productName(), // Utilisation de Faker.js pour générer un nom de produit
    price: Number((Math.random() * 100).toFixed(2)), // Prix généré aléatoirement entre 0 et 100€
    size: faker.random.arrayElement(sizes), // Utilisation de Faker.js pour générer une taille
    color: faker.random.arrayElement(colors), // Utilisation de Faker.js pour générer une couleur
    fabric: getRandomElement(fabrics), // Utilisation de Faker.js pour générer un tissu
    productDescription: faker.lorem.sentence(), // Utilisation de Faker.js pour générer une description
    availableStock: faker.random.number({ min: 0, max: 100 }), // Utilisation de Faker.js pour générer le stock
    averageRating: Number((Math.random() * 5).toFixed(2)), // Évaluation générée aléatoirement entre 0 et 5
    productCategory: {
      categoryName: category ? category.categoryName : null,
    },
    promotion: {
      promotionName: promotion.promotionName,
      discountPercentage: promotion.discountPercentage,
    },
  };
}

///// CUSTOMER /////////////////////////////////////////////////////////////////////////////////

// Fonction pour générer des données aléatoires pour un client
function generateRandomCustomer() {
  const customerId = customerIdCounter++; // Incrémentation de l'ID
  return {
    customerId,
    firstName: faker.name.firstName(),
    lastName: faker.name.lastName(),
    emailAddress: faker.internet.email(),
    password: faker.internet.password(),
    mailingAddress: faker.address.streetAddress(),
    phoneNumber: faker.phone.phoneNumberFormat(),
    creditCard: faker.finance.creditCardNumber(),
    purchaseHistory: [],
  };
}

///// ORDER ////////////////////////////////////////////////////////////////////////////////////

// Fonction pour générer un tableau de produits commandés
// Fonction pour générer un tableau de produits commandés
function generateRandomProductsOrdered(products) {
  const numProducts = Math.floor(Math.random() * 5) + 1;
  const productsOrdered = [];

  if (products && products.length > 0) { // Vérifiez que products est défini et non vide
    for (let i = 0; i < numProducts; i++) {
      const productId = faker.random.arrayElement(products.map(product => product.productId));
      const selectedProduct = products.find(product => product.productId === productId);

      if (selectedProduct) {
        const quantity = Math.floor(Math.random() * 5) + 1;
        productsOrdered.push({
          productId,
          quantity,
          price: selectedProduct.price,
        });
      }
    }
  }

  return productsOrdered;
}

// Fonction pour générer des données aléatoires pour une commande
function generateRandomOrder(customerId, productIds, orderLines) {
  const orderId = orderIdCounter++; // Incrémentation de l'ID
  // Liste des statuts de commande disponibles
  const orderStatusOptions = ['En cours', 'En préparation', 'En cours d\'expédition', 'Expédiée', 'En cours de livraison', 'Livrée', 'En cours d\'annulation', 'Annulée', 'Remboursée'];
  const paymentMethodOptions = ['Carte de crédit', 'PayPal', 'Virement bancaire', 'Chèque']; // Liste des moyens de paiement disponibles
  const productsOrdered = generateRandomProductsOrdered(productIds);
  const orderTotalCost = productsOrdered.reduce((total, product) => total + product.price * product.quantity, 0);
  return {
    orderId, // Utilisation de l'ID incrémental
    orderDate: faker.date.past(), // Utilisation de faker pour générer une date passée
    orderStatus: faker.random.arrayElement(orderStatusOptions), // Utilisation de faker pour un statut de commande aléatoire
    orderTotalCost, // Utilisation du prix total calculé
    paymentMethod: faker.random.arrayElement(paymentMethodOptions), // Utilisation de faker pour un moyen de paiement aléatoire
    productsOrdered,
    customerOrder: customerId,
    orderLines,
  };
}
const orders = Array.from({ length: numOrders }, () => {
  const randomCustomer = faker.random.arrayElement(customers);
  return generateRandomOrder(randomCustomer.customerId, productIds);
});

///// ORDERLINE ////////////////////////////////////////////////////////////////////////////////
  
// Fonction pour générer des données aléatoires pour une ligne de commande
function generateRandomOrderLine(orderId, productId) {
  const orderLineId = orderLineIdCounter++; // Incrémentation de l'ID
  const selectedProduct = products.find(product => product.productId === productId);

  return {
    orderLineId, // Génère un ID unique et automatique pour la ligne de commande
    orderDate: faker.date.past(), // Utilise faker pour générer une date passée
    productOrdered: productId, // Utilise l'ID du produit comme clé étrangère
    orderedQuantity: faker.random.number({ min: 1, max: 10 }), // Utilise faker pour une quantité aléatoire entre 1 et 10
    costSubtotalLine: selectedProduct.price * faker.random.number({ min: 1, max: 10 }), // Utilise le prix réel du produit multiplié par une quantité aléatoire
    orderId: orderId, // L'ID de la commande à laquelle cette ligne appartient
  };
}

///////////////////////////////////////////////////////////////////////////////////////////////

// Fonction principale pour insérer des données aléatoires dans la base de données
async function insertRandomData() {
  // Connexion à la base de données
  const client = new MongoClient(url, { useUnifiedTopology: true });

  try {
    await client.connect();
    const db = client.db(dbName);

    // Insérer des catégories aléatoires
    const categoriesCollection = db.collection('categories');
    const numCategories = 10;
    const categories = Array.from({ length: numCategories }, generateRandomCategory);
    await categoriesCollection.insertMany(categories);

    // Insérer des promotions aléatoires à partir de la liste prédéfinie
    const promotionsCollection = db.collection('promotions');
    const numPromotions = 30; // ou le nombre que vous souhaitez
    const promotions = Array.from({ length: numPromotions }, () => {
      const randomPromo = faker.random.arrayElement(promotionsList);
      return {
        promotionId: faker.random.uuid(),
        promotionName: randomPromo.promoName,
        promotionDescription: faker.lorem.sentence(),
        promotionStart: faker.date.future(0.1, new Date()),
        promotionEnd: faker.date.future(0.3, new Date()),
        profitAmount: parseFloat((Math.random() * 50).toFixed(2)),
        discountPercentage: randomPromo.discountPercentage,
      };
    });
    await promotionsCollection.insertMany(promotions);
    
    // Insérer des produits aléatoires
    const productsCollection = db.collection('products');
    const numProducts = 100;
    products = Array.from({ length: numProducts }, generateRandomProduct);
    const insertProductsResult = await productsCollection.insertMany(products);

    // Récupérer les IDs des produits insérés
    productIds = insertProductsResult.insertedIds;

    // Insérer des clients aléatoires
    const customersCollection = db.collection('customers');
    const numCustomers = 500;
    customers = Array.from({ length: numCustomers }, generateRandomCustomer);
    await customersCollection.insertMany(customers);

    // Insérer des commandes aléatoires
    const ordersCollection = db.collection('orders');
    const numOrders = 500;
    const orders = Array.from({ length: numOrders }, () => {
      const randomCustomer = faker.random.arrayElement(customers);
      const numOrderLines = Math.floor(Math.random() * 5) + 1; // Nombre aléatoire de lignes de commande par commande

      const orderLines = Array.from({ length: numOrderLines }, () => {
        const randomProduct = faker.random.arrayElement(products);
        return generateRandomOrderLine(randomCustomer.customerId, randomProduct.productId);
      });

      return generateRandomOrder(randomCustomer.customerId, productIds, orderLines);
    });
    await ordersCollection.insertMany(orders);
    
    // Afficher un message de confirmation
    console.log('Données générées et insérées avec succès dans la base de données.');
  } finally {
    // Fermer la connexion à la base de données
    await client.close();
  }
}

// Appelez la fonction pour insérer les données
(async () => {
  await insertRandomData();
})();