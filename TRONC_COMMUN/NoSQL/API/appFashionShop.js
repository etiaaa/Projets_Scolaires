const express = require('express');
const mongoose = require('mongoose');
const { Product, Category, Promotion, Customer, Order, OrderLine } = require('./models'); // Assurez-vous d'ajuster le chemin correctement

const app = express();
const port = 3000;

mongoose.connect('mongodb://localhost:27017/FashionShop', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'Erreur de connexion à MongoDB :'));
db.once('open', () => {
  console.log('Connecté à MongoDB');
});

// Route pour obtenir toutes les promotions
app.get('/api/promotions', async (req, res) => {
  try {
    const promotions = await Promotion.find();
    res.json(promotions);
  } catch (error) {
    console.error('Erreur lors de la récupération des promotions :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

// Route pour obtenir tous les produits
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    console.error('Erreur lors de la récupération des produits :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

// Route pour obtenir toutes les catégories
app.get('/api/categories', async (req, res) => {
  try {
    const categories = await Category.find();
    res.json(categories);
  } catch (error) {
    console.error('Erreur lors de la récupération des catégories :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

// Route pour obtenir toutes les commandes
app.get('/api/orders', async (req, res) => {
  try {
    const orders = await Order.find();
    res.json(orders);
  } catch (error) {
    console.error('Erreur lors de la récupération des commandes :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

// Route pour obtenir toutes les lignes de commandes
app.get('/api/orderlines', async (req, res) => {
  try {
    const orderLines = await OrderLine.find();
    res.json(orderLines);
  } catch (error) {
    console.error('Erreur lors de la récupération des lignes de commandes :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.listen(port, () => {
  console.log(`Serveur en cours d'exécution sur le port ${port}`);
});
