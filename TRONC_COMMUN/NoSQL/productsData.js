// Liste d'adjectifs, de types de produits, de couleurs, de tailles, de tissus et de descriptions
const adjectives = [
    'Décontracté', 'Élégant', 'Moderne', 'Sophistiqué', 'Chic',
    'Sportif', 'Décontracté', 'Classique', 'Tendance', 'Vintage'
    ]; 

const types = [ 
    'Manteau sans manche', 'Pull oversize', 'Sweat à capuche', 'Chemise élégante', 'Robe de soirée', 'Jupe plissée', 'Pantalon ample', 'Blouson en cuir',
    'T-shirt graphique', 'Short décontracté', 'Veste en jean', 'Blazer ajusté', 'Combinaison', 'Pantalon de survêtement', 'Blouse fluide', 'Veste en velours',
    'Parka imperméable', 'Costume élégant', 'Legging confortable', 'Chemisier en soie', 'Blouson aviateur', 'Cardigan en tricot', 'Jean slim', 'Trench-coat classique',
    'Salopette décontractée', 'Short en lin', 'Chemise à carreaux', 'Poncho ethnique', 'Tunique bohème', 'Cape en laine', 'Chemise en jean', 'Salopette en jean',
    'Veste en cuir suédé', 'Combishort estival', 'Jogging décontracté', 'Kimono en satin', 'Chemisier à volants', 'Pantalon cargo', 'Pantalon chino', 'Gilet en maille',
    'Sarouel confortable', 'Tunique imprimée', 'Pantalon de plage', 'Combinaison en lin', 'Veste en tweed', 'Pantalon à pinces', 'Pantalon large', 'Robe chemise',
    'Veste en soie', 'Pantalon à sequins', 'Gilet en dentelle', 'Veste en mesh', 'Pantalon en jersey', 'Pantalon à imprimé', 'Veste en organza', 'Pantalon cargo',
    'Pantalon en dentelle', 'Veste à franges', 'Pantalon en néoprène', 'Pantalon ample', 'Veste en tulle', 'Pantalon à carreaux', 'Veste en tricot', 'Pantalon à lacets',
    'Veste en tweed', 'Pantalon à plis', 'Veste en velours', 'Pantalon asymétrique', 'Pantalon en flanelle', 'Veste en cachemire', 'Pantalon à taille haute', 'Veste en jersey',
    'Pantalon à volants', 'Veste en maille', 'Pantalon à imprimé', 'Veste en satin', 'Pantalon à lacets', 'Veste en néoprène', 'Pantalon à sequins', 'Pantalon à pois',
    'Veste en tulle', 'Pantalon à rayures', 'Veste en dentelle', 'Pantalon à sequins', 'Veste en flanelle', 'Pantalon à taille haute', 'Veste en organza', 'Pantalon à dentelle',
    'Veste en tweed', 'Pantalon à franges', 'Veste en tricot', 'Pantalon à imprimé', 'Veste en velours', 'Pantalon à lacets', 'Veste en maille', 'Pantalon à sequins',
    'Pantalon à pois', 'Pantalon à rayures', 'Pantalon à sequins', 'Pantalon à taille haute', 'Pantalon à volants', 'Pantalon ample', 'Pantalon cargo', 'Pantalon chino',
    'Pantalon cigarette', 'Pantalon de plage', 'Pantalon de pyjama', 'Pantalon de survêtement', 'Pantalon évasé', 'Pantalon en cachemire', 'Pantalon en cuir', 'Pantalon en dentelle',
    'Pantalon en flanelle', 'Pantalon en jersey', 'Pantalon en laine', 'Pantalon en lin', 'Pantalon en maille', 'Pantalon en néoprène', 'Pantalon en organza', 'Pantalon en satin',
    'Pantalon en sequins', 'Pantalon en soie', 'Pantalon en tulle', 'Pantalon en tweed', 'Pantalon en velours', 'Pantalon en viscose', 'Pantalon flare', 'Pantalon large', 'Pantalon palazzo',
    'Pantalon paperbag', 'Pantalon skinny', 'Pantalon slim', 'Pantalon straight', 'Pantalon à pont', 'Pantalon à lacets', 'Pantalon à pinces', 'Pantalon à plis', 'Pantalon à taille haute',
    'Pantalon à volants', 'Pantalon à imprimé', 'Pantalon à pois', 'Pantalon à rayures', 'Pantalon à sequins', 'Pantalon à taille haute', 'Pantalon à volants', 'Pantalon ample', 'Pantalon cargo',
    'Pantalon chino', 'Pantalon cigarette', 'Pantalon de plage', 'Pantalon de pyjama', 'Pantalon de survêtement', 'Pantalon évasé', 'Pantalon en cachemire', 'Pantalon en cuir', 'Pantalon en dentelle',
    'Pantalon en flanelle', 'Pantalon en jersey', 'Pantalon en laine', 'Pantalon en lin', 'Pantalon en maille', 'Pantalon en néoprène', 'Pantalon en organza', 'Pantalon en satin', 'Pantalon en sequins',
    'Pantalon en soie', 'Pantalon en tulle', 'Pantalon en tweed', 'Pantalon en velours', 'Pantalon en viscose', 'Pantalon flare', 'Pantalon large', 'Pantalon palazzo', 'Pantalon paperbag', 'Pantalon skinny',
    'Pantalon slim', 'Pantalon straight', 'Pantalon à pont', 'Pantalon à lacets', 'Pantalon à pinces', 'Pantalon à plis', 'Pantalon à taille haute', 'Pantalon à volants', 'Pantalon à imprimé', 'Pantalon à pois',
    'Pantalon à rayures', 'Pantalon à sequins', 'Pantalon à taille haute', 'Pantalon à volants', 'Pantalon ample', 'Pantalon cargo', 'Pantalon chino', 'Pantalon cigarette', 'Pantalon de plage', 'Pantalon de pyjama',
    'Pantalon de survêtement', 'Pantalon évasé', 'Pantalon en cachemire', 'Pantalon en cuir', 'Pantalon en dentelle', 'Pantalon en flanelle', 'Pantalon en jersey', 'Pantalon en laine', 'Pantalon en lin', 'Pantalon en maille',
    'Pantalon en néoprène', 'Pantalon en organza', 'Pantalon en satin', 'Pantalon en sequins', 'Pantalon en soie', 'Pantalon en tulle', 'Pantalon en tweed', 'Pantalon en velours', 'Pantalon en viscose', 'Pantalon flare',
    'Pantalon large', 'Pantalon palazzo', 'Pantalon paperbag', 'Pantalon skinny', 'Pantalon slim', 'Pantalon straight', 'Pantalon à pont', 'Pantalon à lacets', 'Pantalon à pinces', 'Pantalon à plis', 'Pantalon à taille haute',
    'Pantalon à volants', 'Pantalon à imprimé', 'Pantalon à pois', 'Pantalon à rayures', 'Pantalon à sequins', 'Pantalon à taille haute', 'Pantalon à volants', 'Pantalon ample', 'Pantalon cargo', 'Pantalon chino',
    'Pantalon cigarette', 'Pantalon de plage', 'Pantalon de pyjama', 'Pantalon de survêtement', 'Pantalon évasé', 'Pantalon en cachemire', 'Pantalon en cuir', 'Pantalon en dentelle', 'Pantalon en flanelle', 'Pantalon en jersey',
    'Pantalon en laine', 'Pantalon en lin', 'Pantalon en maille', 'Pantalon en néoprène', 'Pantalon en organza', 'Pantalon en satin', 'Pantalon en sequins', 'Pantalon en soie', 'Pantalon en tulle', 'Pantalon en tweed',
    'Pantalon en velours', 'Pantalon en viscose', 'Pantalon flare', 'Pantalon large', 'Pantalon palazzo', 'Pantalon paperbag', 'Pantalon skinny', 'Pantalon slim', 'Pantalon straight', 'Pantalon à pont', 'Pantalon à lacets',
    'Pantalon à pinces', 'Pantalon à plis', 'Pantalon à taille haute', 'Pantalon à volants', 'Pantalon à imprimé', 'Pantalon à pois', 'Pantalon à rayures', 'Pantalon à sequins', 'Pantalon à taille haute', 'Pantalon à volants'
    ];

const colors = [
    'Bleu', 'Rouge', 'Vert', 'Noir', 'Blanc', 'Jaune', 'Orange', 'Rose',
    'Violet', 'Gris', 'Marron', 'Beige', 'Turquoise', 'Indigo', 'Cyan', 'Magenta'
    ];

const sizes = [
    'XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL',
    '34', '36', '38', '40', '42', '44', '46', '48', '50', '52', '54', '56', '58', '60'
    ];

const fabrics = [
    'Coton', 'Lin', 'Polyester', 'Soie', 'Laine', 'Denim', 'Cuir', 'Velours',
    'Nylon', 'Spandex', 'Acrylique', 'Viscose', 'Modal', 'Fibres mélangées', 'Chanvre',
    'Bambou', 'Polyamide', 'Acétate', 'Angora', 'Alpaga', 'Mérinos', 'Mohair', 'Tencel',
    'Elasthanne', 'Fourrure synthétique'
    ];

const descriptions = [
    'Belle pièce de vêtement avec un design unique.',
    'Style élégant pour une allure moderne.',
    'Confortable à porter toute la journée.',
    'Matériaux durables et de haute qualité.',
    'Adapté à toutes les occasions, que ce soit décontracté ou formel.',
    'Design tendance pour rester à la pointe de la mode.',
    'Élégance et praticité réunies dans cette pièce.',
    'Une addition parfaite à votre garde-robe.',
    'Choix idéal pour exprimer votre style personnel.',
    'Incontournable pour les amateurs de mode.'
    ];

module.exports = {
    adjectives,
    types,
    colors,
    sizes,
    fabrics,
    descriptions,
    categoryNames,
};