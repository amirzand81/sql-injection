-- Create table for users if not exists
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    age INT,
    phone BIGINT,
    user_type VARCHAR(50)
);

-- Create table for products if not exists
CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    owner VARCHAR(20),
    description TEXT,
    count INT,
    price INT,
    category VARCHAR(50),
    FOREIGN KEY (owner) REFERENCES users(user_id)
);

-- Insert meaningful data into users table
INSERT INTO users (user_id, name, password, address, age, phone, user_type) VALUES
('alice123', 'Alice Johnson', 'passAlice123', '123 Main St, Cityville', 30, 1234567890, 'Admin'),
('bob456', 'Bob Smith', 'passBob456', '456 Elm St, Townsville', 25, 9876543210, 'Regular'),
('charlie789', 'Charlie Brown', 'passCharlie789', '789 Oak St, Villageton', 35, 5551234567, 'Regular'),
('dianaabc', 'Diana Parker', 'passDianaABC', '456 Pine St, Hamletville', 28, 1112223333, 'Admin'),
('eva456', 'Eva Taylor', 'passEva456', '567 Maple St, Countryside', 40, 9998887777, 'Regular'),
('frank123', 'Frank White', 'passFrank123', '678 Cedar St, Suburbia', 22, 3334445555, 'Regular'),
('grace789', 'Grace Harris', 'passGrace789', '789 Birch St, Ruralville', 33, 6667778888, 'Admin'),
('henry123', 'Henry Martinez', 'passHenry123', '890 Walnut St, Seaside', 45, 2223334444, 'Regular'),
('isabella456', 'Isabella Lee', 'passIsabella456', '901 Cherry St, Mountainview', 29, 7778889999, 'Regular'),
('jack789', 'Jack Adams', 'passJack789', '234 Pineapple St, Beachtown', 38, 4445556666, 'Admin'),
('kelly123', 'Kelly Walker', 'passKelly123', '345 Orange St, Lakeside', 27, 8889990000, 'Regular'),
('liam456', 'Liam Carter', 'passLiam456', '456 Banana St, Riverside', 32, 1110002222, 'Regular'),
('mia789', 'Mia Scott', 'passMia789', '567 Grape St, Hillcrest', 26, 2221110000, 'Admin'),
('noah123', 'Noah Green', 'passNoah123', '678 Watermelon St, Valleyview', 39, 5556667777, 'Regular'),
('olivia456', 'Olivia Evans', 'passOlivia456', '789 Strawberry St, Parkside', 31, 6665554444, 'Regular'),
('peter789', 'Peter Allen', 'passPeter789', '890 Blueberry St, Meadowland', 24, 9990001111, 'Admin'),
('quinn123', 'Quinn Ward', 'passQuinn123', '901 Raspberry St, Woodland', 37, 3332221111, 'Regular'),
('rachel456', 'Rachel Hill', 'passRachel456', '234 Blackberry St, Oceanview', 28, 7778889999, 'Regular'),
('samuel789', 'Samuel Cole', 'passSamuel789', '345 Cranberry St, Farmland', 36, 4445556666, 'Admin'),
('taylor123', 'Taylor Powell', 'passTaylor123', '456 Lemon St, Hilltown', 23, 8889990000, 'Regular');

-- Insert meaningful data into products table
INSERT INTO products (product_id, name, owner, description, count, price, category) VALUES
('laptop123', 'Laptop', 'alice123', 'High-performance laptop with Intel Core i7 processor', 15, 1200, 'Electronics'),
('smartphone456', 'Smartphone', 'bob456', 'Latest smartphone model with dual cameras', 25, 800, 'Electronics'),
('chair789', 'Chair', 'charlie789', 'Comfortable office chair with adjustable armrests', 20, 150, 'Furniture'),
('headphonesabc', 'Headphones', 'dianaabc', 'Wireless noise-canceling headphones with Bluetooth', 30, 200, 'Electronics'),
('desk123', 'Desk', 'eva456', 'Sturdy wooden desk with multiple drawers', 18, 250, 'Furniture'),
('monitor456', 'Monitor', 'frank123', '27-inch LED monitor with Full HD resolution', 22, 300, 'Electronics'),
('bookshelf789', 'Bookshelf', 'grace789', 'Tall bookshelf with adjustable shelves', 17, 100, 'Furniture'),
('cameraabc', 'Camera', 'henry123', 'DSLR camera with 24MP sensor and 4K video recording', 12, 700, 'Electronics'),
('sofa123', 'Sofa', 'isabella456', 'Large sectional sofa with reclining seats', 14, 700, 'Furniture'),
('tablet456', 'Tablet', 'jack789', '10-inch tablet with touchscreen display and 128GB storage', 20, 400, 'Electronics'),
('diningtable789', 'Dining Table', 'kelly123', 'Wooden dining table with seating for six', 16, 350, 'Furniture'),
('smartwatchabc', 'Smartwatch', 'liam456', 'Waterproof smartwatch with fitness tracking features', 28, 150, 'Electronics'),
('bed123', 'Bed', 'mia789', 'Queen-size bed frame with upholstered headboard', 19, 600, 'Furniture'),
('printer456', 'Printer', 'noah123', 'Wireless all-in-one printer with scanning and copying', 24, 150, 'Electronics'),
('couch789', 'Couch', 'olivia456', 'Large leather couch with reclining seats', 10, 800, 'Furniture'),
('router123', 'Wireless Router', 'peter789', 'Dual-band wireless router for high-speed internet', 27, 80, 'Electronics'),
('coffeetable456', 'Coffee Table', 'quinn123', 'Modern glass coffee table with metal legs', 21, 120, 'Furniture');

