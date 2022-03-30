-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 30, 2022 at 07:03 PM
-- Server version: 10.4.22-MariaDB
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
-- Table structure for table `authenticator`
--

CREATE TABLE `authenticator` (
  `token` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `role` varchar(50) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerID` int(20) NOT NULL,
  `startDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customerID`, `startDate`) VALUES
(1, '2022-03-26'),
(2, '2022-03-26');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employeeNumber` int(20) NOT NULL,
  `name` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `department` enum('Production planner','Storekeeper','Customer rep') COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employeeNumber`, `name`, `department`) VALUES
(1, 'Karl Petter', 'Production planner');

-- --------------------------------------------------------

--
-- Table structure for table `franchise`
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
-- Table structure for table `franchise_store`
--

CREATE TABLE `franchise_store` (
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `shipping` varchar(50) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dumping data for table `franchise_store`
--

INSERT INTO `franchise_store` (`name`, `shipping`) VALUES
('Habbos nye brusmaskin', '37');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
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

-- --------------------------------------------------------

--
-- Table structure for table `productionplan`
--

CREATE TABLE `productionplan` (
  `employeeNumber` int(20) NOT NULL,
  `planID` int(11) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `productionplanreference`
--

CREATE TABLE `productionplanreference` (
  `planID` int(11) NOT NULL,
  `productID` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shipment`
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
-- Table structure for table `ski`
--

CREATE TABLE `ski` (
  `productID` int(20) NOT NULL,
  `typeID` int(11) NOT NULL,
  `length` enum('142','147','152','157','162','167','172','177','182','187','192','197','202','207') COLLATE utf8_danish_ci NOT NULL,
  `weight` enum('20-30','30-40','40-50','50-60','60-70','70-80','80-90','90+') COLLATE utf8_danish_ci NOT NULL,
  `reserved` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `skitype`
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

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `customerID` int(20) NOT NULL,
  `price` decimal(15,2) NOT NULL,
  `address` varchar(30) COLLATE utf8_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teamskier`
--

CREATE TABLE `teamskier` (
  `name` varchar(50) COLLATE utf8_danish_ci NOT NULL,
  `customerID` int(20) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `club` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `annual_skies` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dumping data for table `teamskier`
--

INSERT INTO `teamskier` (`name`, `customerID`, `dateOfBirth`, `club`, `annual_skies`) VALUES
('Jens Habbosen', 1, '2012-03-06', 'FC habbo', 2),
('test', 2, '2022-03-14', 'yaya', 22);

-- --------------------------------------------------------

--
-- Table structure for table `transporter`
--

CREATE TABLE `transporter` (
  `transporterID` int(20) NOT NULL,
  `name` varchar(100) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dumping data for table `transporter`
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
  ADD KEY `PlanReference_planID_FK` (`planID`),
  ADD KEY `PlanReference_Ski_FK` (`productID`);

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
  MODIFY `productID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `skitype`
--
ALTER TABLE `skitype`
  MODIFY `typeID` int(11) NOT NULL AUTO_INCREMENT;

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
-- Constraints for dumped tables
--

--
-- Constraints for table `franchise`
--
ALTER TABLE `franchise`
  ADD CONSTRAINT `Franchise_ibfk_2` FOREIGN KEY (`Franchise`) REFERENCES `franchise_store` (`name`),
  ADD CONSTRAINT `franchise_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `Orders_Customer_FK` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customerID`),
  ADD CONSTRAINT `Orders_Ski_FK` FOREIGN KEY (`productID`) REFERENCES `ski` (`productID`);

--
-- Constraints for table `productionplan`
--
ALTER TABLE `productionplan`
  ADD CONSTRAINT `productionplan_ibfk_1` FOREIGN KEY (`employeeNumber`) REFERENCES `employee` (`employeeNumber`);

--
-- Constraints for table `productionplanreference`
--
ALTER TABLE `productionplanreference`
  ADD CONSTRAINT `PlanReference_Plan_FK` FOREIGN KEY (`planID`) REFERENCES `productionplan` (`planID`),
  ADD CONSTRAINT `PlanReference_Ski_FK` FOREIGN KEY (`productID`) REFERENCES `ski` (`productID`);

--
-- Constraints for table `shipment`
--
ALTER TABLE `shipment`
  ADD CONSTRAINT `shipment_ibfk_1` FOREIGN KEY (`transporterID`) REFERENCES `transporter` (`transporterID`),
  ADD CONSTRAINT `shipment_ibfk_3` FOREIGN KEY (`orderNumber`) REFERENCES `orders` (`orderNumber`);

--
-- Constraints for table `ski`
--
ALTER TABLE `ski`
  ADD CONSTRAINT `ski_ibfk_1` FOREIGN KEY (`typeID`) REFERENCES `skitype` (`typeID`);

--
-- Constraints for table `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `store_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Constraints for table `teamskier`
--
ALTER TABLE `teamskier`
  ADD CONSTRAINT `teamskier_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
