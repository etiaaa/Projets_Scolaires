const mongoose = require('mongoose');

// Schéma pour Product
const productSchema = new mongoose.Schema({
  productId: Number,
  name: String,
  price: Number,
  size: String,
  color: String,
  fabric: String,
  description: String,
  availableStock: Number,
  averageRating: Number,
  category: { type: mongoose.Schema.Types.ObjectId, ref: 'Category' },
  promoName: String,
  discountPercentage: Number,
});

// Schéma pour Category
const categorySchema = new mongoose.Schema({
  categoryId: Number,
  name: String,
  description: String,
});

// Schéma pour Promotion
const promotionSchema = new mongoose.Schema({
  promotionId: Number,
  name: String,
  promoCode: String,
  description: String,
  start: Date,
  end: Date,
  discountPercentage: Number,
});

// Schéma pour Customer
const customerSchema = new mongoose.Schema({
  customerId: Number,
  firstName: String,
  lastName: String,
  emailAddress: String,
  password: String,
  mailingAddress: String,
  phoneNumber: String,
  creditCard: String,
  purchaseHistory: Array,
});

// Schéma pour ProcessOrderLinesDetails
const processOrderLinesDetailsSchema = new mongoose.Schema({
  orderLineId: Number,
  orderId: Number,
  productsLines: [{
    productId: Number,
    quantity: Number,
    originalPrice: Number,
    discountedPrice: Number,
    discountAmount: Number,
    totalProductPrice: Number,
  }],
}, { collection: 'processOrderLinesDetails' }); 

// Schéma pour ProcessOrderStatus
const processOrderStatusSchema = new mongoose.Schema({
  orderId: Number,
  orderDate: Date,
  orderStatus: String,
  orderTotalCost: Number,
  paymentMethod: String,
  customerOrder: Number,
  TotalProducts: Number,
  deliveryDate: Date,
  deliveryTime: String,
  datesByStatus: Object,
}, { collection: 'processOrderStatus' });

// Modèles MongoDB basés sur les schémas
const Product = mongoose.model('Product', productSchema);
const Category = mongoose.model('Category', categorySchema);
const Promotion = mongoose.model('Promotion', promotionSchema);
const Customer = mongoose.model('Customer', customerSchema);
const ProcessOrderLinesDetails = mongoose.model('ProcessOrderLinesDetails', processOrderLinesDetailsSchema);
const ProcessOrderStatus = mongoose.model('ProcessOrderStatus', processOrderStatusSchema);

module.exports = {
  Product,
  Category,
  Promotion,
  Customer,
  ProcessOrderLinesDetails,
  ProcessOrderStatus,
};
