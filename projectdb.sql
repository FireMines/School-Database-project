-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 31. Mar, 2022 22:14 PM
-- Tjener-versjon: 10.4.22-MariaDB
-- PHP Version: 8.1.1

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
  `token` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `role` varchar(50) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `authenticator`
--

INSERT INTO `authenticator` (`token`, `role`) VALUES
('thisisaproductionplannertoken', 'ProductionPlanner'),
('thisisacustomerreptoken', 'CustomerRep'),
('thisisatransportertoken', 'Transporter'),
('thisisacustomertoken', 'customer'),
('thisisastorekeepertoken', 'Storekeeper');

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
(2, '2022-03-26'),
(3, '2017-09-17');

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

--
-- Dataark for tabell `franchise`
--

INSERT INTO `franchise` (`customerID`, `name`, `buying_price`, `shipping_address`, `Franchise`) VALUES
(1, 'Habbo ', '9000.00', 'Habbo Club Street 17', 'Habbo Gjøvik'),
(2, 'XXL', '12000.00', 'XXL Street 5', 'XXL Oslo');

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
('Habbo Gjøvik', '37'),
('Habbo Hamar', '72'),
('XXL Oslo', '42');

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
(10, 1, 20, '6000.00', 'new', '2022-03-31 20:01:37', 2),
(11, 1, 60, '20000.00', 'available', '2022-03-31 20:02:04', 2),
(22, 2, 12, '3000.00', 'ready', '2022-03-31 20:02:35', 3);

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
(1, 1, '2022-03-30', '2022-07-30');

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
(1, 3, 5, 3);

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
(3, 1, '202', '60-70', NULL);

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
(2, 'classic', 'racePro', 'it looks cool and goes fast but green', 0, 'https://i1.adis.ws/s/madshus/madshus_2122_redline-3-skate-green-ltd?w=340&qlt=100&fmt=webp&fmt.interlaced=true&bg=white&dpi=96', '3600.00');

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

--
-- Dataark for tabell `store`
--

INSERT INTO `store` (`name`, `customerID`, `price`, `address`) VALUES
('Gjøviks Local Gymstore', 1, '6000.00', 'Exercise Street 2');

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
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  MODIFY `productID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `skitype`
--
ALTER TABLE `skitype`
  MODIFY `typeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
