--
-- Team 13: Project Phase 2 Submission
-- Team Members: Shuheng Gan, Sonali Gupta, Kristine Lacek, 
-- Aparna Maddala, Danielle Temples
--

CREATE DATABASE IF NOT EXISTS `FOOD_TRUCKS`;
USE `FOOD_TRUCKS`;


DROP TABLE IF EXISTS BUILDING;
CREATE TABLE BUILDING (
	Name VARCHAR(64) NOT NULL,
	Description TEXT(64) NOT NULL,
	PRIMARY KEY (Name)
) Engine = InnoDB;

INSERT INTO BUILDING (Name, Description) VALUES
('Clough', 'Has starbucks, located near to transit hub'), 
('College of Computing', 'Famously called as CoC'), 
('CrossLand Tower', 'Library'), 
('KLAUS Adv Computing', 'Connected to CoC through binary bridge'), 
('Molecular Engineering', 'Hosts classes for molecular engineering'), 
('Skiles', 'Hosts classes for media and literature studies'), 
('Students_Center', 'Host for student activities'), 
('TechTower', 'Most Iconic building'), 
('Weber Building', 'Classes mostly related to space technology');


DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION (
	Name VARCHAR(64) NOT NULL,
	Capacity INT NOT NULL,
	Sponsor VARCHAR(64) NOT NULL,
	PRIMARY KEY (Name),
	FOREIGN KEY (Sponsor) REFERENCES Building (Name)
) Engine = InnoDB;

INSERT INTO STATION (Name, Capacity, Sponsor) VALUES
('Clough Commons', '20', 'Clough'), 
('CoC Court Yard', '15', 'College of Computing'), 
('Bio Quad', '20', 'Molecular Engineering'), 
('Skiles Walkway', '3', 'Skiles'), 
('Campanile', '7', 'Students_Center');


DROP TABLE IF EXISTS USER;
CREATE TABLE USER (
	Username VARCHAR(64) NOT NULL,
	Firstname VARCHAR(64) NOT NULL,
	Lastname VARCHAR(64) NOT NULL,
	User_Password VARCHAR(64) NOT NULL,
	PRIMARY KEY (Username)
) Engine = InnoDB;

INSERT INTO USER (Username, Firstname, Lastname, User_Password) VALUES
('2Cool_not_todoschool', 'Smarty', 'Pants', '4242424242'),
('4400_thebestclass', 'Seriously', 'Itis', '4400440044'),
('Aturning_Machine12', 'Alan', 'Turing', '3333333333'),
('beBatman!', 'Bruce', 'Wayne', '5555555555'),
('bestfriends4ever1', 'C3P0', 'Droid', '44444444433'),
('bestfriends4ever2', 'R2D2', 'Droid', '44444444443'),
('BuzzyAsAYellowJacket', 'Buzz', 'Buzz', '1010101010'),
('coxRaycox', 'Ray', 'Cox', '4242424242'),
('customer1', 'One', 'One', '1111111111'),
('customer2', 'Two', 'Two', '1011111111'),
('deer.john', 'John', 'Deer', '22222022222'),
('doe.jane', 'Jane', 'Doe', '22222222200'),
('doe.john', 'John', 'Doe', '20000000002'),
('EmmsBest', 'Emma', 'Williams', '1000000011'),
('employee1', 'Employee', 'Won', '1000111111'),
('Employeeofthemonth', 'Beast', 'Boy', '1000011111'),
('FatherofInfoTheory', 'Claude', 'Shannon', '2222222222'),
('ILikeFlowers', 'Lily', 'Rose', '1000000001'),
('JHallPride', 'James', 'Hall', '2222222222'),
('JNash28TheoryofGaming', 'John', 'Nash', '1111111111'),
('LadyVader1977', 'Leia', 'Organa', '54545454545'),
('LifeIsLikeABoxOfChoco.', 'Forrest', 'Gump', '4444444444'),
('LifeUniverseEverything', 'Forty', 'Two', '4242424242'),
('Manager1', 'First', 'Manager', '1000001111'),
('Manager2', 'Second', 'Manager', '1000000111'),
('Manager3', 'Third', 'Manager', '1000000011'),
('Manager4', 'Fourth', 'Manager', '1000000001'),
('mKJerrY', 'Mike', 'Jerry', '22222022222'),
('Nekonsh', 'Nelsh', 'Kong', '8888888888'),
('RPosince', 'Prince', 'Ross', '2222222222'),
('RRanskans', 'Ruby', 'Rans', '44444444433'),
('scoRa', 'Dhey', 'Scott', '7000000000'),
('sffrgerge', 'Blah', 'BlahBlah', '1000000000'),
('SShen', 'Soms', 'Shen', '4444444444'),
('Staff1', 'One', 'Staff', '3333333333'),
('Staff2', 'Two', 'Staff', '2222222222'),
('notmybusiness', 'Kermit', 'TheFrog', '7000000000'),
('theCustomersAlwaysRight', 'Always', 'Everytime', '1001111111'),
('thereal_GPBurdell', 'George', 'Burdell', '9999999999'),
('TingTong', 'Eva', 'Bell', '1000000000'),
('tkingTom', 'Tom', 'King', '2222222222'),
('TooCuteNottoMention', 'Baby', 'Yoda', '8888888888'),
('toongNonyLongy', 'Tony', 'Long', '20000000002'),
('Violax', 'Violet', 'Lax', '4400440044'),
('WomanWhoSmashedCode', 'Elizabeth', 'Friedman', '4444444444'),
('YayVish', 'Vishy', 'Yay', '6666666666'),
('YouBetterBeNiceToMe', 'Talking', 'Tina', '6666666666');


DROP TABLE IF EXISTS CUSTOMER;
CREATE TABLE CUSTOMER (
	Username VARCHAR(64) NOT NULL,
	Balance DECIMAL(10,2) NOT NULL DEFAULT 0,
	Locate_at VARCHAR(64),
	PRIMARY KEY (Username),
	FOREIGN KEY (Username) REFERENCES User (Username),
	FOREIGN KEY (Locate_at) REFERENCES Station (Name)
) Engine = InnoDB;

INSERT INTO CUSTOMER(Username, Balance, Locate_at) VALUES 	
('4400_thebestclass', '44', 'Clough Commons'),
('beBatman!', '89.99', 'Skiles Walkway'),
('BuzzyAsAYellowJacket', '0.5', 'Skiles Walkway'),
('coxRaycox', '4.5', 'CoC Court Yard'),
('customer1', '46.99', 'Clough Commons'),
('customer2', '47', 'CoC Court Yard'),
('JHallPride', '30.9', 'Clough Commons'),
('LifeUniverseEverything', '42.42', 'Campanile'),
('mKJerrY', '44.2', 'Bio Quad'),
('RPosince', '67.89', 'Campanile'),
('RRanskans', '7.78', 'Bio Quad'),
('sffrgerge', '4.09', 'Clough Commons'),
('notmybusiness', '19.55', 'Bio Quad'),
('theCustomersAlwaysRight', '2.99', 'CoC Court Yard'),
('TingTong', '50.25', 'Bio Quad'),
('tkingTom', '70.14', 'Skiles Walkway'),
('toongNonyLongy', '17.9', 'Clough Commons'),
('Violax', '15.2', 'Skiles Walkway'),
('YouBetterBeNiceToMe', '52.63', 'Bio Quad');


DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (
	Username VARCHAR(64) NOT NULL,
	Email VARCHAR(64) NOT NULL,
	PRIMARY KEY (Email),
	FOREIGN KEY (Username) REFERENCES User (Username)
) Engine = InnoDB;

INSERT INTO EMPLOYEE(Username, Email) VALUES
('2Cool_not_todoschool', 'school@gmail.com'),
('4400_thebestclass', '4400_thebestclass@gatech.edu'),
('Aturning_Machine12', 'machine12@outlook.com'),
('beBatman!', 'beBatman!@gatech.edu'),
('bestfriends4ever1', 'bff@hotmail.com'),
('bestfriends4ever2', 'bff2@gmail.com'),
('BuzzyAsAYellowJacket', 'BuzzyAsAYellowJacket@gatech.edu'),
('deer.john', 'dj3@outlook.com'),
('doe.jane', 'dj1@outlook.com'),
('doe.john', 'dj2@outlook.com'),
('EmmsBest', 'emmsbest@gatech.edu'),
('employee1', 'employee1@gatech.edu'),
('Employeeofthemonth', 'Employeeofthemonth@gatech.edu'),
('FatherofInfoTheory', 'fot@gmail.com'),
('ILikeFlowers', 'flora@gatech.edu'),
('JNash28TheoryofGaming', 'jg@hotmail.com'),
('LadyVader1977', 'lv1977@gatech.edu'),
('LifeIsLikeABoxOfChoco.', 'chocolate@gmail.com'),
('Manager1', 'manager1@gatech.edu'),
('Manager2', 'manager2@gatech.edu'),
('Manager3', 'manager3@gatech.edu'),
('Manager4', 'manager4@gatech.edu'),
('Nekonsh', 'nekonsh@gatech.edu'),
('RRanskans', 'rranskans@gatech.edu'),
('scoRa', 'scoRa@gatech.edu'),
('sffrgerge', 'sff@outlook.com'),
('SShen', 'sshen@gatech.edu'),
('Staff1', 'staff1@gatech.edu'),
('Staff2', 'staff2@gatech.edu'),
('thereal_GPBurdell', 'gpb@gatech.edu'),
('TingTong', 'tingtong@gatech.edu'),
('TooCuteNottoMention', 'mention@gmail.com'),
('Violax', 'violax@gatech.edu'),
('WomanWhoSmashedCode', 'smashedcode@gmail.com'),
('YayVish', 'yayvish@gatech.edu');


DROP TABLE IF EXISTS MANAGER;
CREATE TABLE MANAGER (
	Username VARCHAR(64) NOT NULL,
	PRIMARY KEY (Username),
FOREIGN KEY (Username) REFERENCES Employee (Username)
) Engine = InnoDB;

INSERT INTO MANAGER (Username) VALUES 
('doe.jane'), ('FatherofInfoTheory'), ('LadyVader1977'), 
('LifeIsLikeABoxOfChoco.'), ('Manager1'), ('Manager2'), 
('Manager3'), ('Manager4'), ('SShen'), ('thereal_GPBurdell'), 
('YayVish');


DROP TABLE IF EXISTS ADMIN;
CREATE TABLE ADMIN (
	Username VARCHAR(64) NOT NULL,
	PRIMARY KEY (Username),
	FOREIGN KEY (Username) REFERENCES Employee (Username)
) Engine = InnoDB;

INSERT INTO ADMIN (Username) VALUES 
('4400_thebestclass'), ('Nekonsh'), ('scoRa');


DROP TABLE IF EXISTS FOOD_TRUCK;
CREATE TABLE FOOD_TRUCK (
	Name VARCHAR(64) NOT NULL,
	Manage VARCHAR(64) NOT NULL,
	Host VARCHAR(64) NOT NULL,
	PRIMARY KEY (Name),
	FOREIGN KEY (Manage) REFERENCES Manager (Username),
	FOREIGN KEY (Host) REFERENCES Station (Name)
) Engine = InnoDB;

INSERT INTO FOOD_TRUCK (Name, Host, Manage) VALUES
('BurgerBird', 'Clough Commons', 'LadyVader1977'), 
('FourAnalystInATacoTruck', 'Clough Commons', 'FatherofInfoTheory'), 
('GoodFoodTruck', 'CoC Court Yard', 'FatherofInfoTheory') , 
('WaffleTruffle', 'CoC Court Yard', 'SShen'), 
('GoodOnAStudentBudget', 'Bio Quad', 'thereal_GPBurdell'), 
('ShawarmaExpress', 'Bio Quad', 'Manager3'), 
('FoodTrolley', 'Skiles Walkway', 'LadyVader1977'), 
('BubbaGumps', 'Campanile', 'LifeIsLikeABoxOfChoco.'), 
('CrazyPies', 'Campanile', 'Manager1'), 
('FoodTruckYoureLookingFor', 'Campanile', 'LadyVader1977'), 
('FusionFoodTruck', 'Campanile', 'YayVish'), 
('JohnJaneAndVenison', 'Campanile', 'doe.jane'), 
('NachoBizness', 'Campanile', 'Manager2'), 
('TruckOfFood', 'Campanile', 'Manager2');


DROP TABLE IF EXISTS STAFF;
CREATE TABLE STAFF (
	Username VARCHAR(64) NOT NULL,
	Work_in VARCHAR(64),
	PRIMARY KEY (Username),
	FOREIGN KEY (Username) REFERENCES Employee (Username),
	FOREIGN KEY (Work_in) REFERENCES Food_Truck (Name)
) Engine = InnoDB;

INSERT INTO STAFF (Username, Work_in) VALUES 
('2Cool_not_todoschool', 'WaffleTruffle'), 
('Aturning_Machine12', 'FourAnalystInATacoTruck'), 
('beBatman!', 'WaffleTruffle'), 
('bestfriends4ever1', 'FoodTruckYoureLookingFor'), 
('bestfriends4ever2', 'BurgerBird'), 
('BuzzyAsAYellowJacket', 'ShawarmaExpress'), 
('deer.john', 'JohnJaneAndVenison'), 
('doe.john', 'TruckOfFood'), 
('EmmsBest', 'CrazyPies'), 
('employee1', 'BurgerBird'), 
('Employeeofthemonth', 'ShawarmaExpress'), 
('ILikeFlowers', 'CrazyPies'), 
('JNash28TheoryofGaming', 'GoodFoodTruck'), 
('RRanskans', 'FoodTrolley'), 
('sffrgerge', 'GoodOnAStudentBudget'), 
('Staff1', 'BubbaGumps'), 
('Staff2', 'BubbaGumps'), 
('TingTong', 'FusionFoodTruck'), 
('TooCuteNottoMention', 'NachoBizness'), 
('Violax', 'FoodTrolley'), 
('WomanWhoSmashedCode', 'FourAnalystInATacoTruck');


DROP TABLE IF EXISTS CUSTOMER_ORDER;
CREATE TABLE CUSTOMER_ORDER (
	OrderID VARCHAR(64),
	Order_Date DATE NOT NULL,
	Ordered_by VARCHAR(64) NOT NULL,
	PRIMARY KEY (OrderID),
Constraint fk11 FOREIGN KEY (Ordered_by) REFERENCES USER (Username)
) Engine = InnoDB;

INSERT INTO CUSTOMER_ORDER VALUES ('0000000038', '2020-03-01', 'beBatman!'),
('0000000039', '2020-03-01', 'beBatman!'),
('0000000022', '2020-02-10', 'BuzzyAsAYellowJacket'),
('0000000023', '2020-02-10', 'BuzzyAsAYellowJacket'),
('0000000026', '2020-02-11', 'BuzzyAsAYellowJacket'),
('0000000001', '2020-01-01', 'customer1'),
('0000000002', '2020-01-01', 'customer1'),
('0000000005', '2020-02-02', 'customer1'),
('0000000010', '2020-02-04', 'customer1'),
('0000000018', '2020-02-10', 'customer1'),
('0000000024', '2020-02-10', 'customer1'),
('0000000030', '2020-02-29', 'customer1'),
('0000000031', '2020-03-01', 'customer1'),
('0000000036', '2020-03-01', 'customer1'),
('0000000003', '2020-01-01', 'customer2'),
('0000000004', '2020-02-01', 'customer2'),
('0000000006', '2020-02-03', 'customer2'),
('0000000011', '2020-02-05', 'customer2'),
('0000000019', '2020-02-10', 'customer2'),
('0000000020', '2020-02-10', 'customer2'),
('0000000021', '2020-02-10', 'customer2'),
('0000000025', '2020-02-10', 'customer2'),
('0000000027', '2020-02-11', 'customer2'),
('0000000028', '2020-02-22', 'customer2'),
('0000000029', '2020-02-29', 'customer2'),
('0000000032', '2020-03-01', 'customer2'),
('0000000033', '2020-03-01', 'customer2'),
('0000000037', '2020-03-01', 'LifeUniverseEverything'),
('0000000034', '2020-03-01', 'sffrgerge'),
('0000000035', '2020-03-01', 'sffrgerge'),
('0000000009', '2020-02-04', 'notmybusiness'),
('0000000013', '2020-02-05', 'notmybusiness'),
('0000000014', '2020-02-05', 'notmybusiness'),
('0000000015', '2020-02-06', 'notmybusiness'),
('0000000017', '2020-02-06', 'notmybusiness'),
('0000000007', '2020-02-04', 'theCustomersAlwaysRight'),
('0000000008', '2020-02-04', 'theCustomersAlwaysRight'),
('0000000012', '2020-02-05', 'theCustomersAlwaysRight'),
('0000000016', '2020-02-06', 'theCustomersAlwaysRight'),
('0000000040', '2020-03-01', 'YouBetterBeNiceToMe'),
('0000000041', '2020-03-01', 'YouBetterBeNiceToMe');


DROP TABLE IF EXISTS FOOD;
CREATE TABLE FOOD (
	Name VARCHAR(64),
	PRIMARY KEY(Name)
) Engine = InnoDB;

INSERT INTO FOOD VALUES ('Bagels'), ('CeasarSalad'), ('CheeseBurger'), 
('ChickenSandwich'), ('ChickenTacos'), ('ChickenWings'), ('ChocolateShake'), 
('ElkBurger'), ('HamBurger'), ('HotDog'), ('MargheritaPizza'), ('Nachos'), 
('Noodles'), ('Pie'), ('SalmonTacos'), ('Shawarma'), ('ShrimpGumbo'), 
('SouthWestChickenSalad'), ('TrailMix'), ('VegetarianGumbo'), ('VegetarianTacos'), 
('VegPizza'), ('VegSpringRolls'), ('Waffles');


DROP TABLE IF EXISTS MENU_ITEM;
CREATE TABLE MENU_ITEM (
	Food_item VARCHAR(64) NOT NULL,
	Sold_by VARCHAR(64) NOT NULL,
	Price DECIMAL(10,2) NOT NULL,
	Primary key (Food_item, Sold_by),
Constraint fk12 foreign key (Food_item) references FOOD (Name),
Constraint fk13 FOREIGN KEY (Sold_by) REFERENCES FOOD_TRUCK (Name)
) Engine = InnoDB;

INSERT INTO MENU_ITEM VALUES ('CeasarSalad', 'GoodOnAStudentBudget', 3.46), 
('CheeseBurger', 'BurgerBird', 4.76), 
('CheeseBurger', 'GoodOnAStudentBudget', 4.51), 
('ChickenTacos', 'BubbaGumps', 5.21), 
('ChickenTacos', 'FourAnalystInATacoTruck', 6.22), 
('ChickenTacos', 'NachoBizness', 6.58), 
('ChickenWings', 'FoodTrolley', 6.01), 
('ChickenWings', 'FourAnalystInATacoTruck', 5.28), 
('ChocolateShake', 'FoodTrolley', 7.54), 
('ChocolateShake', 'GoodOnAStudentBudget', 5.48), 
('ChocolateShake', 'ShawarmaExpress', 4.85), 
('ElkBurger', 'BurgerBird', 6.68), 
('ElkBurger', 'JohnJaneAndVenison', 10.17), 
('HamBurger', 'BurgerBird', 7.05), 
('HamBurger', 'GoodOnAStudentBudget', 3.82), 
('HotDog', 'GoodOnAStudentBudget', 2.23), 
('MargheritaPizza', 'CrazyPies', 4.28), 
('MargheritaPizza', 'FoodTruckYoureLookingFor', 7.58), 
('Nachos', 'FoodTruckYoureLookingFor', 3.21), 
('Nachos', 'NachoBizness', 5.13), 
('Noodles', 'GoodFoodTruck', 4.40), 
('Noodles', 'TruckOfFood', 4.77), 
('Pie', 'BurgerBird', 4.53), 
('Pie', 'CrazyPies', 4.19), 
('Pie', 'FoodTrolley', 4.51), 
('SalmonTacos', 'FourAnalystInATacoTruck', 8.03), 
('SalmonTacos', 'FusionFoodTruck', 7.16), 
('SalmonTacos', 'NachoBizness', 7.59), 
('Shawarma', 'ShawarmaExpress', 6.30), 
('ShrimpGumbo', 'BubbaGumps', 6.22), 
('SouthWestChickenSalad', 'FoodTruckYoureLookingFor', 9.57), 
('SouthWestChickenSalad', 'GoodFoodTruck', 9.06), 
('TrailMix', 'JohnJaneAndVenison', 4.36), 
('VegetarianGumbo', 'BubbaGumps', 3.82), 
('VegetarianTacos', 'FourAnalystInATacoTruck', 5.84), 
('VegetarianTacos', 'FusionFoodTruck', 5.95), 
('VegetarianTacos', 'NachoBizness', 4.70), 
('VegPizza', 'CrazyPies', 3.48), 
('VegPizza', 'FoodTruckYoureLookingFor', 7.88), 
('VegSpringRolls', 'GoodFoodTruck', 3.11), 
('VegSpringRolls', 'TruckOfFood', 3.53), 
('Waffles', 'FoodTrolley', 5.82), 
('Waffles', 'GoodOnAStudentBudget', 3.44), 
('Waffles', 'WaffleTruffle', 6.65);


DROP TABLE IF EXISTS TAG;
CREATE TABLE TAG (
	Building_name VARCHAR(64),
	Tag_name VARCHAR(64),
	PRIMARY KEY (Building_name, Tag_name),
	Constraint fk14 FOREIGN KEY (Building_name) REFERENCES Building (Name)
) Engine = InnoDB;

INSERT INTO TAG VALUES ('Clough', 'ADA'), ('Clough', 'Labs'), 
('Clough', 'LEED'), ('College of Computing', 'Computing'), 
('CrossLand Tower', 'LEED'), ('CrossLand Tower', 'Library'), 
('KLAUS Adv Computing', 'Computing'), ('Molecular Engineering', 'Engineering'), 
('Skiles', 'Liberal Arts'), ('Students_Center', 'LEED'), 
('TechTower', 'ADA'), ('TechTower', 'Registrar'), ('Weber Building', 'ADA'), 
('Weber Building', 'Sciences');


DROP TABLE IF EXISTS ORDER_CONTAINS;
CREATE TABLE ORDER_CONTAINS (
	OrderID VARCHAR(64) NOT NULL,
Sold_by VARCHAR(64) NOT NULL,
	Food_item VARCHAR(64) NOT NULL,
	Purchase_qty INT NOT NULL,
	PRIMARY KEY (OrderID, Food_item, Sold_by),
	FOREIGN KEY (OrderID) REFERENCES Customer_Order (OrderID),
FOREIGN KEY (Sold_by) REFERENCES Menu_item (Sold_by),
FOREIGN KEY (Food_item) REFERENCES Menu_item (Food_item)
) Engine = InnoDB;

INSERT INTO ORDER_CONTAINS VALUES ('0000000001','CrazyPies', 'MargheritaPizza', 1), 
('0000000001','CrazyPies', 'Pie', 2), 
('0000000001','CrazyPies', 'VegPizza', 1), 
('0000000002','GoodOnAStudentBudget', 'CeasarSalad', 1), 
('0000000002','GoodOnAStudentBudget', 'HotDog', 1), 
('0000000003','GoodOnAStudentBudget', 'CheeseBurger', 1), 
('0000000003','GoodOnAStudentBudget', 'HamBurger', 1), 
('0000000003','GoodOnAStudentBudget', 'Waffles', 2), 
('0000000004','FoodTrolley', 'ChickenWings', 4), 
('0000000005','NachoBizness', 'SalmonTacos', 3), 
('0000000006','FourAnalystInATacoTruck', 'ChickenTacos', 3), 
('0000000006','FourAnalystInATacoTruck', 'ChickenWings', 4), 
('0000000006','FourAnalystInATacoTruck', 'SalmonTacos', 1), 
('0000000007','BurgerBird', 'ElkBurger', 2), 
('0000000007','BurgerBird', 'HamBurger', 2), 
('0000000008','ShawarmaExpress', 'Shawarma', 2), 
('0000000009','JohnJaneAndVenison', 'TrailMix', 2), 
('0000000010','TruckOfFood', 'Noodles', 1), 
('0000000010','TruckOfFood', 'VegSpringRolls', 3), 
('0000000011', 'NachoBizness', 'ChickenTacos', 1), 
('0000000011', 'NachoBizness', 'Nachos', 4), 
('0000000011', 'NachoBizness', 'SalmonTacos', 3), 
('0000000011' ,'NachoBizness', 'VegetarianTacos', 3), 
('0000000012', 'FoodTruckYoureLookingFor', 'MargheritaPizza', 2), 
('0000000012', 'FoodTruckYoureLookingFor', 'VegPizza', 2), 
('0000000013', 'FoodTrolley', 'ChocolateShake', 1), 
('0000000013', 'FoodTrolley', 'ChickenWings', 1), 
('0000000014','GoodOnAStudentBudget', 'HamBurger', 4), 
('0000000015', 'FoodTrolley', 'ChickenWings', 1), 
('0000000016', 'FoodTrolley', 'ChickenWings', 2), 
('0000000017','ShawarmaExpress', 'Shawarma', 6), 
('0000000018','WaffleTruffle', 'Waffles', 4), 
('0000000019','FourAnalystInATacoTruck', 'VegetarianTacos', 3), 
('0000000020','FourAnalystInATacoTruck', 'ChickenWings', 1), 
('0000000020','FourAnalystInATacoTruck', 'VegetarianTacos', 2), 
('0000000021','GoodOnAStudentBudget', 'CheeseBurger', 1), 
('0000000021','GoodOnAStudentBudget', 'ChocolateShake', 1), 
('0000000021','GoodOnAStudentBudget', 'HamBurger', 3), 
('0000000022','GoodOnAStudentBudget', 'CeasarSalad', 5), 
('0000000022','GoodOnAStudentBudget', 'CheeseBurger', 1), 
('0000000022','GoodOnAStudentBudget', 'HotDog', 1), 
('0000000022','GoodOnAStudentBudget', 'Waffles', 3), 
('0000000023','GoodOnAStudentBudget', 'ChocolateShake', 2), 
('0000000023','GoodOnAStudentBudget', 'HamBurger', 1), 
('0000000024','TruckofFood', 'Noodles', 1), 
('0000000024','TruckofFood', 'VegSpringRolls', 5), 
('0000000025','BurgerBird', 'Pie', 1), 
('0000000026','FoodTrolley', 'ChickenWings', 6), 
('0000000026','FoodTrolley', 'ChocolateShake', 2), 
('0000000026','FoodTrolley', 'Pie', 1), 
('0000000026','FoodTrolley', 'Waffles', 2), 
('0000000027', 'FoodTruckYoureLookingFor', 'VegPizza', 1), 
('0000000028','BurgerBird', 'CheeseBurger', 1), 
('0000000029','FourAnalystInATacoTruck', 'ChickenWings', 6), 
('0000000030','BubbaGumps', 'VegetarianGumbo', 1), 
('0000000031','FourAnalystInATacoTruck', 'ChickenTacos', 3), 
('0000000031','FourAnalystInATacoTruck', 'ChickenWings', 5), 
('0000000031','FourAnalystInATacoTruck', 'SalmonTacos', 3), 
('0000000031','FourAnalystInATacoTruck', 'VegetarianTacos', 1), 
('0000000032','BurgerBird', 'CheeseBurger', 3), 
('0000000032','BurgerBird', 'Pie', 1), 
('0000000033', 'FoodTrolley', 'ChickenTacos', 5), 
('0000000033', 'FoodTrolley', 'Pie', 1), 
('0000000033', 'FoodTrolley', 'Waffles', 2), 
('0000000034', 'FourAnalystInATacoTruck', 'ChickenTacos', 3), 
('0000000034', 'FourAnalystInATacoTruck', 'ChickenWings', 5), 
('0000000034', 'FourAnalystInATacoTruck', 'SalmonTacos', 3), 
('0000000035', 'GoodOnAStudentBudget', 'CeasarSalad', 2), 
('0000000035', 'GoodOnAStudentBudget', 'Waffles', 1), 
('0000000036', 'GoodOnAStudentBudget', 'ChocolateShake', 1), 
('0000000036', 'GoodOnAStudentBudget', 'HamBurger', 1), 
('0000000037', 'BurgerBird', 'CheeseBurger', 1), 
('0000000038', 'BubbaGumps', 'ChickenTacos', 7), 
('0000000039', 'NachoBizness', 'Nachos', 2), 
('0000000040', 'CrazyPies', 'MargheritaPizza', 1), 
('0000000040', 'CrazyPies', 'VegPizza', 1), 
('0000000041', 'BubbaGumps', 'ChickenTacos', 1), 
('0000000041', 'BubbaGumps', 'ShrimpGumbo', 1), 
('0000000041', 'BubbaGumps', 'VegetarianGumbo', 1);
