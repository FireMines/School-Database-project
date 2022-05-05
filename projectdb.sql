-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 05. Mai, 2022 17:31 PM
-- Tjener-versjon: 10.4.22-MariaDB
-- PHP Version: 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectdb`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `authenticator`
--

CREATE TABLE `authenticator` (
  `Username` varchar(200) COLLATE utf8_danish_ci NOT NULL,
  `Hashedpassword` varchar(200) COLLATE utf8_danish_ci NOT NULL,
  `salt` varchar(200) COLLATE utf8_danish_ci NOT NULL,
  `role` enum('Transporter','Customer','Customer_rep','Storekeeper','Production_planner') COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `authenticator`
--

INSERT INTO `authenticator` (`Username`, `Hashedpassword`, `salt`, `role`) VALUES
('User1', 'f38cf1c69ed9b263868210a723962e9105f741fa07ed9bf707aa54e754cbed17', 'Ttm3CzoHhJ9CU77Y', 'Customer'),
('User2', '82a40cc7b69f88a8f322b39072a48daa3edab81d84e88e9b0f17923008c1a283', 'uH7lo6vzThJ6WdMb', 'Transporter'),
('User3', '342c2254259acd1994f927df8306fa3f8ce428cd2627b4ee6262f14bcd73f828', 'CTHEHvj7JmUtHkSc', 'Customer_rep'),
('User4', '80aedceb173770e0401be6ce4cafb3bae60942c471a62348d8a97e36e624ab41', 'lfRCYM81sH0J7PyA', 'Storekeeper'),
('User5', '238651697ab1b01c13180751c7839676e37a2883f045222603958f68f6b24394', 'a45GzfkRNagGv7KF', 'Production_planner');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `customer`
--

CREATE TABLE `customer` (
  `customerID` int(20) NOT NULL,
  `startDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `customer`
--

INSERT INTO `customer` (`customerID`, `startDate`) VALUES
(1, '2022-03-26'),
(2, '2022-03-26');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `employee`
--

CREATE TABLE `employee` (
  `employeeNumber` int(20) NOT NULL,
  `name` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `department` enum('Production planner','Storekeeper','Customer rep') COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `employee`
--

INSERT INTO `employee` (`employeeNumber`, `name`, `department`) VALUES
(1, 'Karl Petter', 'Production planner');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `franchise`
--

CREATE TABLE `franchise` (
  `customerID` int(20) NOT NULL,
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `buying_price` decimal(15,2) NOT NULL,
  `shipping_address` varchar(30) COLLATE utf8_danish_ci NOT NULL,
  `Franchise` varchar(50) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `franchise_store`
--

CREATE TABLE `franchise_store` (
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `shipping` varchar(50) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `franchise_store`
--

INSERT INTO `franchise_store` (`name`, `shipping`) VALUES
('Habbos nye brusmaskin', '37');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `orders`
--

CREATE TABLE `orders` (
  `orderNumber` int(20) NOT NULL,
  `customer_id` int(20) NOT NULL,
  `quantity` int(2) NOT NULL,
  `totalPrice` decimal(15,2) NOT NULL,
  `state` enum('new','open','available','cancelled','ready','shipped') COLLATE utf8_danish_ci NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `productID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `orders`
--

INSERT INTO `orders` (`orderNumber`, `customer_id`, `quantity`, `totalPrice`, `state`, `date`, `productID`) VALUES
(100100, 1, 10, '1010.10', 'available', '2022-05-03 17:14:17', 2),
(200200, 2, 2, '200.20', 'new', '2018-05-02 22:00:00', 2);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `productionplan`
--

CREATE TABLE `productionplan` (
  `employeeNumber` int(20) NOT NULL,
  `planID` int(11) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `productionplan`
--

INSERT INTO `productionplan` (`employeeNumber`, `planID`, `startDate`, `endDate`) VALUES
(1, 1, '2022-03-30', '2022-07-30'),
(1, 2, '2022-02-01', '2022-02-28');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `productionplanreference`
--

CREATE TABLE `productionplanreference` (
  `planID` int(11) NOT NULL,
  `productID` int(20) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `ReferenceID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `productionplanreference`
--

INSERT INTO `productionplanreference` (`planID`, `productID`, `Quantity`, `ReferenceID`) VALUES
(1, 1, 13, 1),
(1, 2, 33, 2),
(1, 3, 5, 3),
(2, 2, 10, 4),
(2, 1, 5, 5);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `shipment`
--

CREATE TABLE `shipment` (
  `shipmentNumber` int(20) NOT NULL,
  `orderNumber` int(20) NOT NULL,
  `transporterID` int(20) NOT NULL,
  `shippingAddress` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `pickUpDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `state` enum('ready','shipped') COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `shipment`
--

INSERT INTO `shipment` (`shipmentNumber`, `orderNumber`, `transporterID`, `shippingAddress`, `pickUpDate`, `state`) VALUES
(1, 100100, 1, 'Address', '2022-03-31 14:25:43', 'shipped');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `ski`
--

CREATE TABLE `ski` (
  `productID` int(20) NOT NULL,
  `typeID` int(11) NOT NULL,
  `length` enum('142','147','152','157','162','167','172','177','182','187','192','197','202','207') COLLATE utf8_danish_ci NOT NULL,
  `weight` enum('20-30','30-40','40-50','50-60','60-70','70-80','80-90','90+') COLLATE utf8_danish_ci NOT NULL,
  `reserved` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `ski`
--

INSERT INTO `ski` (`productID`, `typeID`, `length`, `weight`, `reserved`) VALUES
(1, 1, '147', '50-60', NULL),
(2, 2, '182', '50-60', NULL),
(3, 1, '202', '60-70', NULL),
(10, 4, '147', '20-30', NULL);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `skitype`
--

CREATE TABLE `skitype` (
  `typeID` int(11) NOT NULL,
  `type` enum('classic','skate','doublePole') COLLATE utf8_danish_ci NOT NULL,
  `model` enum('active','activePro','endurance','intrasonic','racePro','raceSpeed','redline') COLLATE utf8_danish_ci NOT NULL,
  `description` varchar(200) COLLATE utf8_danish_ci NOT NULL,
  `historical` tinyint(1) DEFAULT NULL,
  `url` varchar(255) COLLATE utf8_danish_ci NOT NULL,
  `msrp` decimal(15,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `skitype`
--

INSERT INTO `skitype` (`typeID`, `type`, `model`, `description`, `historical`, `url`, `msrp`) VALUES
(1, 'classic', 'activePro', 'it looks cool and goes fast', 0, 'https://i1.adis.ws/s/madshus/madshus_2021_redline-3-skate-f2?w=340&qlt=100&fmt=webp&fmt.interlaced=true&bg=white&dpi=96', '7700.00'),
(2, 'classic', 'racePro', 'it looks cool and goes fast but green', 0, 'https://i1.adis.ws/s/madshus/madshus_2122_redline-3-skate-green-ltd?w=340&qlt=100&fmt=webp&fmt.interlaced=true&bg=white&dpi=96', '3600.00'),
(4, 'classic', 'active', 'These are skies', NULL, 'None', '200.00');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `store`
--

CREATE TABLE `store` (
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `customerID` int(20) NOT NULL,
  `price` decimal(15,2) NOT NULL,
  `address` varchar(30) COLLATE utf8_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `teamskier`
--

CREATE TABLE `teamskier` (
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `customerID` int(20) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `club` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `annual_skies` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `teamskier`
--

INSERT INTO `teamskier` (`name`, `customerID`, `dateOfBirth`, `club`, `annual_skies`) VALUES
('Jens Habbosen', 1, '2012-03-06', 'FC habbo', 2),
('test', 2, '2022-03-14', 'yaya', 22);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `transporter`
--

CREATE TABLE `transporter` (
  `transporterID` int(20) NOT NULL,
  `name` varchar(100) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `transporter`
--

INSERT INTO `transporter` (`transporterID`, `name`) VALUES
(1, 'HeavyTrucker');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employeeNumber`);

--
-- Indexes for table `franchise`
--
ALTER TABLE `franchise`
  ADD PRIMARY KEY (`customerID`),
  ADD KEY `Franchise_ibfk_2` (`Franchise`);

--
-- Indexes for table `franchise_store`
--
ALTER TABLE `franchise_store`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderNumber`),
  ADD KEY `Orders_Customer_FK` (`customer_id`),
  ADD KEY `Orders_Ski_FK` (`productID`);

--
-- Indexes for table `productionplan`
--
ALTER TABLE `productionplan`
  ADD PRIMARY KEY (`planID`),
  ADD KEY `employeeNumber` (`employeeNumber`);

--
-- Indexes for table `productionplanreference`
--
ALTER TABLE `productionplanreference`
  ADD PRIMARY KEY (`ReferenceID`),
  ADD KEY `productionplanreference_ibfk_1` (`planID`) USING BTREE,
  ADD KEY `productionplanreference_ibfk_2` (`productID`) USING BTREE;

--
-- Indexes for table `shipment`
--
ALTER TABLE `shipment`
  ADD PRIMARY KEY (`shipmentNumber`),
  ADD KEY `transporterID` (`transporterID`),
  ADD KEY `orderNumber` (`orderNumber`);

--
-- Indexes for table `ski`
--
ALTER TABLE `ski`
  ADD PRIMARY KEY (`productID`),
  ADD KEY `typeID` (`typeID`);

--
-- Indexes for table `skitype`
--
ALTER TABLE `skitype`
  ADD PRIMARY KEY (`typeID`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`name`),
  ADD KEY `customerID` (`customerID`);

--
-- Indexes for table `teamskier`
--
ALTER TABLE `teamskier`
  ADD KEY `customerID` (`customerID`);

--
-- Indexes for table `transporter`
--
ALTER TABLE `transporter`
  ADD PRIMARY KEY (`transporterID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employeeNumber` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `orderNumber` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6969670;

--
-- AUTO_INCREMENT for table `shipment`
--
ALTER TABLE `shipment`
  MODIFY `shipmentNumber` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ski`
--
ALTER TABLE `ski`
  MODIFY `productID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `skitype`
--
ALTER TABLE `skitype`
  MODIFY `typeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teamskier`
--
ALTER TABLE `teamskier`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transporter`
--
ALTER TABLE `transporter`
  MODIFY `transporterID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Begrensninger for dumpede tabeller
--

--
-- Begrensninger for tabell `franchise`
--
ALTER TABLE `franchise`
  ADD CONSTRAINT `Franchise_ibfk_2` FOREIGN KEY (`Franchise`) REFERENCES `franchise_store` (`name`),
  ADD CONSTRAINT `franchise_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Begrensninger for tabell `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `Orders_Customer_FK` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customerID`),
  ADD CONSTRAINT `Orders_Ski_FK` FOREIGN KEY (`productID`) REFERENCES `ski` (`productID`);

--
-- Begrensninger for tabell `productionplan`
--
ALTER TABLE `productionplan`
  ADD CONSTRAINT `productionplan_ibfk_1` FOREIGN KEY (`employeeNumber`) REFERENCES `employee` (`employeeNumber`);

--
-- Begrensninger for tabell `productionplanreference`
--
ALTER TABLE `productionplanreference`
  ADD CONSTRAINT `PlanReference_Plan_FK` FOREIGN KEY (`planID`) REFERENCES `productionplan` (`planID`),
  ADD CONSTRAINT `PlanReference_Ski_FK` FOREIGN KEY (`productID`) REFERENCES `ski` (`productID`);

--
-- Begrensninger for tabell `shipment`
--
ALTER TABLE `shipment`
  ADD CONSTRAINT `shipment_ibfk_1` FOREIGN KEY (`transporterID`) REFERENCES `transporter` (`transporterID`),
  ADD CONSTRAINT `shipment_ibfk_3` FOREIGN KEY (`orderNumber`) REFERENCES `orders` (`orderNumber`);

--
-- Begrensninger for tabell `ski`
--
ALTER TABLE `ski`
  ADD CONSTRAINT `ski_ibfk_1` FOREIGN KEY (`typeID`) REFERENCES `skitype` (`typeID`);

--
-- Begrensninger for tabell `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `store_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Begrensninger for tabell `teamskier`
--
ALTER TABLE `teamskier`
  ADD CONSTRAINT `teamskier_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
