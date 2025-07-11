
CREATE DATABASE grocerydb;
USE grocerydb;

CREATE TABLE inventory (
    itemid VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50),
    itemcateg VARCHAR(30),
    stock INT,
    lastupd DATE,
    expdate DATE,
    cp DECIMAL(10,2),
    sp DECIMAL(10,2)
);

CREATE TABLE supplier (
    ID VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE orders (
    itemid VARCHAR(20),
    ordcnt INT,
    orddate DATE

);



CREATE TABLE itemsup (
    itemid VARCHAR(20),
    supid VARCHAR(20)
    
);
INSERT INTO inventory VALUES
('I001', 'Milk', 'Dairy', 100, '2025-07-01', '2025-08-01', 25.50, 30.00),
('I002', 'Bread', 'Bakery', 50, '2025-07-05', '2025-07-15', 15.00, 20.00),
('I003', 'Eggs', 'Poultry', 200, '2025-07-02', '2025-07-22', 5.00, 6.00);

INSERT INTO supplier VALUES
('S001', 'DairyFresh Co.'),
('S002', 'Bakers Ltd.'),
('S003', 'PoultryFarm Inc.');
INSERT INTO orders VALUES
('I001', 20, '2025-07-10'),
('I002', 10, '2025-07-10'),
('I003', 30, '2025-07-11');
INSERT INTO itemsup (itemid, supid) VALUES
('I001', 'S001'),
('I002', 'S002'),
('I003', 'S001');

