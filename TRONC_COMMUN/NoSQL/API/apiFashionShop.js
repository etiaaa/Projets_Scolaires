const express = require('express');
const mongoose = require('mongoose');
const { Product, Category, Promotion, Customer, Order, OrderLine } = require('./modelsFashionShop');

const app = express();
const port = 27018;

mongoose.connect('mongodb://localhost:27017/FashionShop', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'Erreur de connexion à MongoDB :'));
db.once('open', () => {
  console.log('Connecté à MongoDB');
});

app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    console.error('Erreur lors de la récupération des produits :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.get('/api/categories', async (req, res) => {
  try {
    const categories = await Category.find();
    res.json(categories);
  } catch (error) {
    console.error('Erreur lors de la récupération des catégories :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.get('/api/promotions', async (req, res) => {
  try {
    const promotions = await Promotion.find();
    res.json(promotions);
  } catch (error) {
    console.error('Erreur lors de la récupération des promotions :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.get('/api/customers', async (req, res) => {
  try {
    const customers = await Customer.find();
    res.json(customers);
  } catch (error) {
    console.error('Erreur lors de la récupération des clients :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.get('/api/processOrderLinesDetails', async (req, res) => {
  try {
    const processOrderLinesDetails = await processOrderLinesDetailsModel.find(); 
    res.json(processOrderLinesDetails);
  } catch (error) {
    console.error('Erreur lors de la récupération des lignes de commande :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.get('/api/processOrderStatus', async (req, res) => {
  try {
    const processOrderStatus = await processOrderStatusModel.find(); 
    res.json(processOrderStatus);
  } catch (error) {
    console.error('Erreur lors de la récupération des statuts de commande :', error);
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.listen(port, () => {
  console.log(`Serveur en cours d'exécution sur le port ${port}`);
});

