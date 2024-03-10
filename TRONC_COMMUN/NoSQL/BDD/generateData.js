const { MongoClient, ObjectId } = require('mongodb');
const faker = require('faker/locale/fr'); 
const moment = require('moment');

const url = 'mongodb://localhost:27017';
const dbName = 'FashionShop';

///// PROMOTION ////////////////////////////////////////////////////////////////////////////////

const promotionsList = [
  { promoName: 'Solde d\'été', promoCode: 'ETE10', promotionDescription: 'Profitez des nouvelles collections pour refaire votre garde-robe festive.', discountPercentage: 40 },
  { promoName: 'Solde d\'hiver', promoCode: 'HIVER15', promotionDescription: 'Économisez sur les articles chauds et confortables pour l\'hiver.', discountPercentage: 35 },
  { promoName: 'Black Friday', promoCode: 'BF20', promotionDescription: 'Les meilleures offres de l\'année sont là. Ne les manquez pas !', discountPercentage: 30 },
  { promoName: 'Solde de noël', promoCode: 'NOEL12', promotionDescription: 'Célébrez les fêtes avec des remises spéciales sur une sélection festive.', discountPercentage: 40 },
  { promoName: 'Rentrée Scolaire', promoCode: 'RENTREE8', promotionDescription: 'Préparez-vous pour une nouvelle année scolaire avec des réductions sur les essentiels.', discountPercentage: 50 },
  { promoName: 'Printemps Fleuri', promoCode: 'PRINTEMPS18', promotionDescription: 'Égayez votre printemps avec des offres spéciales sur nos articles les plus fleuris.', discountPercentage: 20 },
  { promoName: 'Cyber Monday', promoCode: 'CYBER25', promotionDescription: 'Les meilleures affaires en ligne vous attendent. Profitez du Cyber Monday !', discountPercentage: 25 },
  { promoName: 'Fête des Mères', promoCode: 'FDM14', promotionDescription: 'Célébrez les mamans avec des cadeaux spéciaux à des prix réduits.', discountPercentage: 15 },
  { promoName: 'Saint-Valentin', promoCode: 'LOVE15', promotionDescription: 'Trouvez le cadeau parfait pour votre être cher avec nos offres de la Saint-Valentin.', discountPercentage: 15 },
  { promoName: 'Spécial Anniversaire', promoCode: 'ANNIV10', promotionDescription: 'Joyeux anniversaire ! Célébrez avec des réductions spéciales sur nos produits.', discountPercentage: 10 },
  { promoName: 'Vacances d\'été', promoCode: 'VACANCES22', promotionDescription: 'Partez en vacances avec des économies. Découvrez nos offres estivales !', discountPercentage: 25 },
  { promoName: 'Promo Flash', promoCode: 'FLASH30', promotionDescription: 'Économies éclair ! Saisissez nos offres flash avant qu\'elles ne disparaissent.', discountPercentage: 30 },
  { promoName: 'Back to School', promoCode: 'BTS16', promotionDescription: 'Préparez-vous pour une nouvelle année scolaire avec des réductions exceptionnelles.', discountPercentage: 15 },
  { promoName: 'Halloween', promoCode: 'HALLOWEEN18', promotionDescription: 'Frémissez de plaisir avec nos offres spéciales d\'Halloween.', discountPercentage: 20 },
  { promoName: 'Promo d\'Automne', promoCode: 'AUTOMNE14', promotionDescription: 'Accueillez l\'automne avec des remises chaleureuses sur nos produits.', discountPercentage: 15 },
  { promoName: 'Cadeau Gratuit', promoCode: 'CADEAU0', promotionDescription: 'Avec tout achat, recevez un cadeau gratuit !', discountPercentage: 5 },
  { promoName: 'Soldes de Fin d\'Année', promoCode: 'FINANNEE25', promotionDescription: 'Terminez l\'année en beauté avec nos soldes de fin d\'année.', discountPercentage: 25 },
  { promoName: 'Nouvel An', promoCode: 'NOUVELAN18', promotionDescription: 'Célébrez le Nouvel An avec des réductions spéciales sur une sélection festive.', discountPercentage: 18 },
  { promoName: 'Fête du Travail', promoCode: 'TRAVAIL10', promotionDescription: 'Détendez-vous et économisez lors de la Fête du Travail.', discountPercentage: 10 },
  { promoName: 'Saint-Patrick', promoCode: 'STPATRICK17', promotionDescription: 'Portez du vert et économisez pour la Saint-Patrick !', discountPercentage: 20 },
  { promoName: 'Journée Internationale de la Femme', promoCode: 'FEMME15', promotionDescription: 'Célébrez la Journée Internationale de la Femme avec des offres exclusives.', discountPercentage: 15 },
  { promoName: 'Semaine du Client', promoCode: 'CLIENT20', promotionDescription: 'Merci à nos clients ! Profitez de réductions spéciales cette semaine.', discountPercentage: 20 },
  { promoName: 'Spécial Étudiants', promoCode: 'ETUDIANT10', promotionDescription: 'Économisez sur vos achats étudiants avec notre promotion spéciale.', discountPercentage: 10 },
];

let promotionIdCounter = 1;
function generateRandomPromotion() {
  const promotionId = promotionIdCounter++;
  const randomPromo = faker.random.arrayElement(promotionsList);
  const startDate = faker.date.past();
  const endDate = faker.date.between(startDate, moment(startDate).add(Math.floor(Math.random() * 30) + 1, 'days').toDate());

  const minDiscountPercentage = 5;
  const maxDiscountPercentage = randomPromo.discountPercentage;
  const discountPercentage = Math.floor(Math.random() * (maxDiscountPercentage - minDiscountPercentage + 1) + minDiscountPercentage);

  return {
    promotionId,
    promotionName: randomPromo.promoName,
    promoCode: randomPromo.promoCode,
    promotionDescription: randomPromo.promotionDescription,
    promotionStart: startDate,
    promotionEnd: endDate,
    discountPercentage,
  };
}

///// PRODUIT //////////////////////////////////////////////////////////////////////////////////

const productsList = [
  { category: 'T-shirt', style: 'Décontracté', type: 'T-shirt basique', colors: ['Bleu', 'Blanc', 'Gris', 'Vert', 'Jaune'], sizes: ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'], fabrics: 'Coton', description: 'T-shirt décontracté en coton pour un look confortable.' },
  { category: 'Robe', style: 'Élégant', type: 'Robe de soirée', colors: ['Noir', 'Rouge', 'Bleu marine', 'Argent', 'Or'], sizes: ['XS', 'S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Soie', description: 'Robe de soirée élégante en soie pour une allure sophistiquée.' },
  { category: 'Blazer', style: 'Chic', type: 'Blazer ajusté', colors: ['Gris anthracite', 'Noir', 'Blanc', 'Bleu marine', 'Bordeaux'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Polyester', description: 'Blazer ajusté chic pour un look professionnel.' },
  { category: 'Pull', style: 'Oversize', type: 'Pull en tricot oversize', colors: ['Gris clair', 'Beige', 'Rose poudré', 'Bleu ciel', 'Mauve'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Acrylique', description: 'Pull en tricot oversize pour un confort maximal.' },
  { category: 'Sportswear', style: 'Sportif', type: 'Pantalon de survêtement', colors: ['Noir', 'Bleu roi', 'Vert kaki', 'Gris', 'Rouge'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Polyester', description: 'Pantalon de survêtement sportif pour un look décontracté.' },
  { category: 'Chemise', style: 'Classe', type: 'Chemise élégante', colors: ['Blanc', 'Bleu clair', 'Rose pâle', 'Rayures fines', 'Noir'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Coton', description: 'Chemise élégante en coton pour un style raffiné.' },
  { category: 'Denim', style: 'Vintage', type: 'Veste en jean', colors: ['Bleu délavé', 'Noir', 'Marron', 'Rose', 'Vert'], sizes: ['M', 'L', 'XL', 'XXL'], fabrics: 'Denim', description: 'Veste en jean vintage pour un look rétro.' },
  { category: 'Robe', style: 'Bohème', type: 'Robe longue fluide', colors: ['Jaune moutarde', 'Vert olive', 'Bleu ciel', 'Rose saumon', 'Violet'], sizes: ['S', 'M', 'L'], fabrics: 'Viscose', description: 'Robe longue fluide pour un style bohème décontracté.' },
  { category: 'Manteau', style: 'Chaud', type: 'Parka imperméable', colors: ['Noir', 'Vert foncé', 'Bleu marine', 'Gris', 'Rouge'], sizes: ['M', 'L', 'XL', 'XXL'], fabrics: 'Nylon', description: 'Parka imperméable pour rester au chaud par temps humide.' },
  { category: 'Pyjama', style: 'Confortable', type: 'Pyjama en flanelle', colors: ['Gris à carreaux', 'Rose pâle', 'Bleu ciel', 'Vert pastel', 'Violet clair'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Flanelle', description: 'Pyjama en flanelle pour une nuit de sommeil confortable.' },
  { category: 'Short', style: 'Décontracté', type: 'Short en lin', colors: ['Beige', 'Bleu clair', 'Blanc', 'Kaki', 'Rose pâle'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Lin', description: 'Short décontracté en lin pour les journées ensoleillées.' },
  { category: 'Robe', style: 'Élégant', type: 'Robe cocktail', colors: ['Noir', 'Rouge vif', 'Bleu nuit', 'Doré', 'Argenté'], sizes: ['XS', 'S', 'M', 'L', 'XL'], fabrics: 'Polyester', description: 'Robe cocktail élégante pour les occasions spéciales.' },
  { category: 'Jupe', style: 'Chic', type: 'Jupe crayon', colors: ['Noir', 'Blanc', 'Gris', 'Bleu marine', 'Bordeaux'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Coton mélangé', description: 'Jupe crayon chic pour un look féminin et sophistiqué.' },
  { category: 'Pull', style: 'Oversize', type: 'Sweat à capuche oversize', colors: ['Gris chiné', 'Bleu marine', 'Rose pâle', 'Vert kaki', 'Noir'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Coton', description: 'Sweat à capuche oversize pour un confort maximal.' },
  { category: 'Sportswear', style: 'Sportif', type: 'Ensemble de jogging', colors: ['Bleu marine', 'Gris', 'Noir', 'Rouge', 'Blanc'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Polyester', description: 'Ensemble de jogging sportif pour un style décontracté.' },
  { category: 'Chemisier', style: 'Classe', type: 'Chemisier à col lavallière', colors: ['Blanc', 'Bleu ciel', 'Rose poudré', 'Noir', 'Imprimé floral'], sizes: ['S', 'M', 'L'], fabrics: 'Soie', description: 'Chemisier à col lavallière classe pour un look féminin.' },
  { category: 'Pantalon', style: 'Vintage', type: 'Pantalon taille haute', colors: ['Marron', 'Vert forêt', 'Bleu marine', 'Carreaux rétro', 'Jaune moutarde'], sizes: ['M', 'L', 'XL', 'XXL'], fabrics: 'Velours côtelé', description: 'Pantalon taille haute vintage pour une touche rétro.' },
  { category: 'Short', style: 'Décontracté', type: 'Short en jean', colors: ['Bleu délavé', 'Blanc', 'Rose', 'Vert', 'Jaune'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Denim', description: 'Short en jean décontracté pour un look estival.' },
  { category: 'Costume', style: 'Élégant', type: 'Costume deux pièces', colors: ['Noir', 'Gris anthracite', 'Bleu marine', 'Bordeaux', 'Marron'], sizes: ['M', 'L', 'XL', 'XXL'], fabrics: 'Laine mélangée', description: 'Costume deux pièces élégant pour une allure sophistiquée.' },
  { category: 'Jupe', style: 'Chic', type: 'Jupe plissée', colors: ['Rose poudré', 'Vert émeraude', 'Bleu marine', 'Noir', 'Blanc'], sizes: ['S', 'M', 'L'], fabrics: 'Polyester', description: 'Jupe plissée chic pour un look féminin.' },
  { category: 'Chemise', style: 'Oversize', type: 'Chemise oversize', colors: ['Gris chiné', 'Blanc', 'Bleu clair', 'Rose pâle', 'Kaki'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Coton', description: 'Chemise oversize pour un style décontracté.' },
  { category: 'Sportswear', style: 'Sportif', type: 'Short de sport', colors: ['Noir', 'Bleu roi', 'Gris', 'Rouge', 'Blanc'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Polyester', description: 'Short de sport pour un look dynamique.' },
  { category: 'Chemisier', style: 'Classe', type: 'Blouse en soie', colors: ['Blanc', 'Noir', 'Rouge', 'Bleu marine', 'Imprimé floral'], sizes: ['S', 'M', 'L'], fabrics: 'Soie', description: 'Blouse en soie pour un look classe et féminin.' },
  { category: 'Veste', style: 'Vintage', type: 'Veste en velours', colors: ['Bleu nuit', 'Bordeaux', 'Vert forêt', 'Marron', 'Rose antique'], sizes: ['M', 'L', 'XL', 'XXL'], fabrics: 'Velours', description: 'Veste en velours vintage pour une touche rétro.' },
  { category: 'Tunique', style: 'Bohème', type: 'Tunique brodée', colors: ['Ivoire', 'Bleu ciel', 'Rose poudré', 'Moutarde', 'Vert sauge'], sizes: ['S', 'M', 'L'], fabrics: 'Coton', description: 'Tunique brodée bohème pour un style décontracté.' },
  { category: 'Manteau', style: 'Chaud', type: 'Manteau en laine', colors: ['Noir', 'Gris', 'Camel', 'Rouge', 'Bleu marine'], sizes: ['M', 'L', 'XL', 'XXL'], fabrics: 'Laine', description: 'Manteau en laine pour rester au chaud avec style.' },
  { category: 'Pyjama', style: 'Confortable', type: 'Pyjama en jersey', colors: ['Gris chiné', 'Bleu clair', 'Rose pâle', 'Vert menthe', 'Rayures fines'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Jersey', description: 'Pyjama en jersey pour une nuit confortable.' },
  { category: 'T-shirt', style: 'Décontracté', type: 'T-shirt à manches longues', colors: ['Noir', 'Blanc', 'Gris', 'Bleu marine', 'Rouge'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Coton', description: 'T-shirt à manches longues décontracté pour un style polyvalent.' },
  { category: 'Robe', style: 'Élégant', type: 'Robe midi', colors: ['Noir', 'Rouge', 'Bleu marine', 'Blanc', 'Imprimé géométrique'], sizes: ['XS', 'S', 'M', 'L', 'XL'], fabrics: 'Polyester', description: 'Robe midi élégante pour un look tendance.' },
  { category: 'Chemisier', style: 'Chic', type: 'Chemisier à volants', colors: ['Blanc', 'Bleu ciel', 'Rose pâle', 'Noir', 'Imprimé floral'], sizes: ['S', 'M', 'L'], fabrics: 'Coton', description: 'Chemisier à volants chic pour une allure féminine.' },
  { category: 'Pull', style: 'Oversize', type: 'Pull en tricot oversize', colors: ['Gris clair', 'Beige', 'Rose poudré', 'Bleu ciel', 'Mauve'], sizes: ['S', 'M', 'L', 'XL', 'XXL'], fabrics: 'Acrylique', description: 'Pull en tricot oversize pour un confort maximal.' },
  { category: 'Sportswear', style: 'Sportif', type: 'Legging de sport', colors: ['Noir', 'Bleu marine', 'Gris', 'Rouge', 'Rose', 'Imprimé camouflage'], sizes: ['S', 'M', 'L', 'XL'], fabrics: 'Spandex', description: 'Legging de sport pour un look dynamique.' },
];

function getPromotionForType(type) {
  const product = productsList.find((product) => product.type === type);
  const randomPromo = faker.random.arrayElement(promotionsList);
  return {
    promoName: randomPromo.promoName,
    discountPercentage: randomPromo.discountPercentage,
  };
}

let productIdCounter = 1;
function generateRandomProduct(productsList) {
  const product = faker.random.arrayElement(productsList);
  const promotion = getPromotionForType(product.type);

  return {
    productId: productIdCounter++,
    productName: `${product.type} - ${product.style}`,
    price: Number((Math.random() * 100).toFixed(2)),
    size: faker.random.arrayElement(product.sizes),
    color: faker.random.arrayElement(product.colors),
    fabric: product.fabrics,
    productDescription: product.description,
    availableStock: faker.datatype.number({ min: 0, max: 100 }),
    averageRating: Math.round((Math.random() * 4 + 0.5) * 100) / 100,
    categoryName: product.category,
    promoName: promotion.promoName,
    discountPercentage: promotion.discountPercentage,
  };
}

///// CATEGORY /////////////////////////////////////////////////////////////////////////////////

let categoryIdCounter = 1;
function generateRandomCategory() {
  const categoryId = categoryIdCounter++;
  const categoryName = faker.random.arrayElement(productsList.map(product => product.category));
  const categoryDescription = `Explorez notre collection de vêtements ${categoryName.toLowerCase()} offrant un mélange exquis de styles pour tous les goûts.`;

  return {
    categoryId,
    categoryName,
    categoryDescription,
  };
}

///// CUSTOMER /////////////////////////////////////////////////////////////////////////////////

let customerIdCounter = 1;
function generateRandomCustomer() {
  const customerId = customerIdCounter++;
  const firstName = faker.name.firstName();
  const lastName = faker.name.lastName();
  const emailDomain = faker.random.arrayElement(['gmail.com', 'yahoo.com', 'hotmail.com']);
  const emailAddress = `${firstName}${lastName}@${emailDomain}`;
  const mailingAddress = faker.address.streetAddress(true).replace(/\b\d{3,}/, (match) => match.slice(0, 2)).replace(/(?:Suite|Apt\.) \d+/i, '').trim() + ' ' + faker.address.city() + ' ' + faker.address.zipCode();
  const phoneNumber = faker.phone.phoneNumber(`0${faker.random.arrayElement(['6', '7'])}########`);
  const creditCard = faker.finance.creditCardNumber().replace(/(\d{4})(\d{4})(\d{4})(\d{4})/, '$1 $2 $3 $4');

  return {
    customerId,
    firstName,
    lastName,
    emailAddress,
    password: faker.internet.password(),
    mailingAddress,
    phoneNumber,
    creditCard,
    purchaseHistory: [],
  };
}

///// PROCESS ORDER LINES DETAILS //////////////////////////////////////////////////////////////

let orderLineIdCounter = 1; 
function processOrderLinesDetails(orderId, products) {
  const orderLineId = orderLineIdCounter++;
  const numProducts = Math.floor(Math.random() * 5) + 1;
  const productsLines = [];

  if (products && products.length > 0) {
    for (let i = 0; i < numProducts; i++) {
      const productId = faker.random.arrayElement(products.map(product => product.productId));
      const selectedProduct = products.find(product => product.productId === productId);

      if (selectedProduct) {
        const quantity = Math.floor(Math.random() * 5) + 1;

        const discountedPrice = selectedProduct.price - (selectedProduct.price * selectedProduct.discountPercentage / 100);
        const discountAmount = selectedProduct.discountPercentage; 
        const discountedAmount = selectedProduct.price * (selectedProduct.discountPercentage / 100);
        const totalProductPrice = discountedPrice * quantity;

        productsLines.push({
          orderLineId,
          productId: productId,
          quantity: quantity,
          originalPrice: selectedProduct.price,
          discountedPrice: Number(discountedPrice.toFixed(2)),
          discountAmount: Number(discountAmount.toFixed(2)),
          totalProductPrice: Number(totalProductPrice.toFixed(2)),
        });
      }
    }
  }

  return {
    orderLineId, 
    orderId,
    productsLines,
  };
}

///// PROCESS ORDER STATUS /////////////////////////////////////////////////////////////////////

let orderIdCounter = 1;
function processOrderStatus(customerId, productsList) {
  const orderId = orderIdCounter++;
  const orderStatusOptions = ['In preparation', 'In shipment', 'Shipped', 'In delivery', 'Delivered', 'In refund', 'Refunded'];
  const paymentMethodOptions = ['Credit card', 'PayPal', 'Bank transfer', 'Cheque'];

  const orderLines = processOrderLinesDetails(orderId, productsList);

  let orderTotalCost = 0;
  let totalProducts = 0;

  if (Array.isArray(orderLines.productsLines)) {
    orderTotalCost = orderLines.productsLines.reduce((total, orderLine) => total + orderLine.totalProductPrice, 0);
    totalProducts = orderLines.productsLines.reduce((total, orderLine) => total + orderLine.quantity, 0);
  }

  const orderDate = faker.date.past();
  const deliveryDate = new Date(orderDate.getTime() + Math.floor(Math.random() * (7 * 24 * 60 * 60 * 1000))); // Livraison dans les 7 jours
  const deliveryTime = `${Math.floor(Math.random() * 24)}:${Math.floor(Math.random() * 60)}`;

  const datesByStatus = {};
  const chosenStatus = faker.random.arrayElement(orderStatusOptions.slice(0, orderStatusOptions.indexOf('Delivered') + 1));

  orderStatusOptions.slice(0, orderStatusOptions.indexOf(chosenStatus) + 1).forEach((status, index) => {
    datesByStatus[status] = new Date(orderDate.getTime() + (index * 24 * 60 * 60 * 1000)); // Ajouter un jour pour chaque étape
  });

  if (['In refund', 'Refunded'].includes(chosenStatus)) {
    datesByStatus['In refund'] = new Date(orderDate.getTime() + ((orderStatusOptions.indexOf('In refund') + 1) * 24 * 60 * 60 * 1000));
    datesByStatus['Refunded'] = new Date(orderDate.getTime() + ((orderStatusOptions.indexOf('Refunded') + 1) * 24 * 60 * 60 * 1000));
  }

  const orderStatus = chosenStatus;

  return {
    orderId,
    orderDate: orderDate.toISOString().split('T')[0],
    orderStatus,
    orderTotalCost: Number(orderTotalCost.toFixed(2)),
    paymentMethod: faker.random.arrayElement(paymentMethodOptions),
    customerOrder: customerId,
    totalProducts,
    deliveryDate: deliveryDate.toISOString().split('T')[0],
    deliveryTime,
    datesByStatus: Object.fromEntries(
      Object.entries(datesByStatus).map(([key, value]) => [key, value.toISOString().split('T')[0]])
    ),
    orderLines,
  };
}
  
///// INSERT DATA //////////////////////////////////////////////////////////////////////////////

async function insertRandomData() {
  const client = new MongoClient(url, { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();
    const db = client.db(dbName);

    await Promise.all([
      db.collection('promotions').deleteMany({}),
      db.collection('products').deleteMany({}),
      db.collection('categories').deleteMany({}),
      db.collection('customers').deleteMany({}),
      db.collection('processOrderStatus').deleteMany({}),
      db.collection('processOrderLinesDetails').deleteMany({}),
    ]);
    
    const promotionsCollection = db.collection('promotions');
    const numPromotions = 30;
    const promotions = Array.from({ length: numPromotions }, generateRandomPromotion);
    await promotionsCollection.insertMany(promotions);

    const productsCollection = db.collection('products');
    const numProducts = 500;
    const products = Array.from({ length: numProducts }, () => generateRandomProduct(productsList));
    const insertProductsResult = await productsCollection.insertMany(products);
    const productIds = insertProductsResult.insertedIds;

    const categoriesCollection = db.collection('categories');
    const categories = Array.from({ length: productsList.length }, generateRandomCategory);
    const uniqueCategories = Array.from(new Set(categories.map(category => category.categoryName)))
      .map(categoryName => categories.find(category => category.categoryName === categoryName));
    await categoriesCollection.insertMany(uniqueCategories);

    const customersCollection = db.collection('customers');
    const numCustomers = 500;
    const customers = Array.from({ length: numCustomers }, generateRandomCustomer);
    await customersCollection.insertMany(customers);

    const processOrderStatusCollection = db.collection('processOrderStatus');
    const numOrders = 500;
    const orders = Array.from({ length: numOrders }, () => {
      const randomCustomer = faker.random.arrayElement(customers);
      return processOrderStatus(randomCustomer.customerId, products);
    });
    await processOrderStatusCollection.insertMany(orders);

    const processOrderLinesDetailsCollection = db.collection('processOrderLinesDetails');
    const orderLines = orders.flatMap(order => processOrderLinesDetails(order.orderId, products));
    await processOrderLinesDetailsCollection.insertMany(orderLines);

    console.log('Données générées et insérées avec succès dans la base de données.');
  } catch (error) {
    console.error('Erreur lors de l\'insertion des données :', error);
  } finally {
    await client.close();
  }
}

(async () => {
  await insertRandomData();
})();
