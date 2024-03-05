async function fetchAndDisplayProducts() {
    try {
        const response = await fetch('http://localhost:27018/api/products');
        const products = await response.json();

        const productsContainer = document.getElementById('productsContainer');
        productsContainer.innerHTML = '';

        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.classList.add('product');
            productElement.innerHTML = `
                <h3>${product.name}</h3>
                <p>Prix: ${product.price} $</p>
                <p>Catégorie: ${product.category.name}</p>
            `;
            productsContainer.appendChild(productElement);
        });
    } catch (error) {
        console.error('Erreur lors de la récupération des produits :', error);
    }
}

fetchAndDisplayProducts();
