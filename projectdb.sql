-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2022 at 05:08 PM
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
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerID` int(20) NOT NULL,
  `customerName` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `address` varchar(40) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employeeNumber` int(20) NOT NULL,
  `name` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `department` varchar(40) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `franchise`
--

CREATE TABLE `franchise` (
  `customerID` int(20) NOT NULL,
  `negotiatedPrice` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `information` date DEFAULT NULL,
  `address` varchar(30) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `orderNumber` int(20) NOT NULL,
  `quantity` int(2) NOT NULL,
  `totalPrice` float NOT NULL,
  `state` enum('new','open','available','cancelled','ready','shipped') COLLATE utf8_danish_ci NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `productionplan`
--

CREATE TABLE `productionplan` (
  `employeeNumber` int(20) NOT NULL,
  `typeID` int(11) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shipment`
--

CREATE TABLE `shipment` (
  `shipmentNumber` int(20) NOT NULL,
  `orderNumber` int(20) NOT NULL,
  `transporterID` int(20) NOT NULL,
  `customerID` int(20) NOT NULL,
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
  `msrp` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `customerID` int(20) NOT NULL,
  `price` float NOT NULL,
  `address` varchar(30) COLLATE utf8_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teamskier`
--

CREATE TABLE `teamskier` (
  `customerID` int(20) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `club` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `numSkis` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transporter`
--

CREATE TABLE `transporter` (
  `transporterID` int(20) NOT NULL,
  `name` varchar(100) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

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
  ADD PRIMARY KEY (`customerID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderNumber`);

--
-- Indexes for table `productionplan`
--
ALTER TABLE `productionplan`
  ADD PRIMARY KEY (`startDate`),
  ADD KEY `employeeNumber` (`employeeNumber`),
  ADD KEY `typeID` (`typeID`);

--
-- Indexes for table `shipment`
--
ALTER TABLE `shipment`
  ADD PRIMARY KEY (`shipmentNumber`),
  ADD KEY `transporterID` (`transporterID`),
  ADD KEY `customerID` (`customerID`),
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
  ADD PRIMARY KEY (`customerID`);

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
-- Constraints for dumped tables
--

--
-- Constraints for table `franchise`
--
ALTER TABLE `franchise`
  ADD CONSTRAINT `franchise_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Constraints for table `productionplan`
--
ALTER TABLE `productionplan`
  ADD CONSTRAINT `productionplan_ibfk_1` FOREIGN KEY (`employeeNumber`) REFERENCES `employee` (`employeeNumber`),
  ADD CONSTRAINT `productionplan_ibfk_2` FOREIGN KEY (`typeID`) REFERENCES `skitype` (`typeID`);

--
-- Constraints for table `shipment`
--
ALTER TABLE `shipment`
  ADD CONSTRAINT `shipment_ibfk_1` FOREIGN KEY (`transporterID`) REFERENCES `transporter` (`transporterID`),
  ADD CONSTRAINT `shipment_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`),
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
