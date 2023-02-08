-- SQLite

CREATE TABLE User (
id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
gender VARCHAR(100),
lastname VARCHAR(100),
firstname VARCHAR(100),
email VARCHAR(100),
date_of_birth DATE,
phone_number INT
);



CREATE TABLE Address (
id_address INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
country VARCHAR(100),
city VARCHAR(100),
mail_address VARCHAR(100),
postal_code VARCHAR(100),
house_num INT,
floor_num INT,
id_user INT, 
FOREIGN KEY (id_user) REFERENCES User(id_user)
); 


CREATE TABLE Payment(
id_payment INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
iban VARCHAR(100),
card_number VARCHAR(100),
cryptogram INT,
expiration_date DATE,
name varchar(100),
id_user INT,
id_command INT,
FOREIGN KEY (id_user) REFERENCES User(id_user),
FOREIGN KEY (id_command) REFERENCES Command(id_command)
);


CREATE TABLE Product(
id_product INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100),
price INT,
size VARCHAR(100),
color VARCHAR(100),
stock INT,
id_category INT,
FOREIGN KEY (id_category) REFERENCES Category(id_category)
);



CREATE TABLE Rate(
id_rate INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
grade INT,
id_product INT,
id_user INT,

FOREIGN KEY (id_product) REFERENCES Product(id_product),
FOREIGN KEY (id_user) REFERENCES User(id_user)
);



CREATE TABLE Photo(
id_photo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_product INT,
id_user INT,

FOREIGN KEY (id_product) REFERENCES Product(id_product),
FOREIGN KEY (id_user) REFERENCES User(id_user)
);


CREATE TABLE Cart(
id_cart INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
quantity_product INT,
nb_products INT,
amount INT,
id_product INT,
id_user INT,

FOREIGN KEY (id_product) REFERENCES Product(id_product),
FOREIGN KEY (id_user)    REFERENCES User(id_user)
);


CREATE TABLE Command(
id_command INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
command_date DATE,
estimated_delivery_date DATE,
amount INT,
shipping_cost INT,
nb_products INT,
position_product VARCHAR(100),
id_product INT,
id_user INT,
id_address INT,

FOREIGN KEY (id_product) REFERENCES Product(id_product),
FOREIGN KEY (id_user)    REFERENCES User(id_user),
FOREIGN KEY (id_address) REFERENCES Address(id_address)
);


CREATE TABLE Command_line(
id_command_line INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_product INT,
id_user INT,
id_address INT,
id_command INT,

FOREIGN KEY (id_product) REFERENCES Product(id_product),
FOREIGN KEY (id_user)    REFERENCES User(id_user),
FOREIGN KEY (id_address) REFERENCES Address(id_address),
FOREIGN KEY (id_command) REFERENCES Command(id_command)

);


CREATE TABLE Invoices(
id_invoices INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_product INT,
id_user INT,
id_address INT,
id_command_line INT,

FOREIGN KEY (id_product)      REFERENCES Product(id_product),
FOREIGN KEY (id_user)         REFERENCES User(id_user),
FOREIGN KEY (id_address)      REFERENCES Address(id_address),
FOREIGN KEY (id_command_line) REFERENCES Command_line(id_command_line)

);


CREATE TABLE Category(
id_category INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name_category VARCHAR(100)
); 