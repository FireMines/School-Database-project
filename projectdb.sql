-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2022 at 11:12 PM
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
    `customerID` Int (20) NOT NULL PRIMARY KEY,
    `customerName` varchar (60)NOT NULL,
    `startDate` date NOT NULL,
    `endDate` date NOT NULL,
    `address` varchar (40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
    `employeeNumber` Int (20) NOT NULL PRIMARY KEY,
    `name` varchar (60)NOT NULL,
    `department` varchar (40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `franchise_store`
--

CREATE TABLE `franchise_store` (
    `customerID` Int (20) PRIMARY KEY NOT NULL ,
    `negotiatedPrice` varchar (60)NOT NULL,
    `information` date DEFAULT NULL,
    `address` varchar (30)NOT NULL,
    
    FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `productID` int(20) NOT NULL PRIMARY KEY,
    `typeID` int(11) NOT NULL,
    `length` enum('142','147','152','157','162','167','172','177','182','187','192','197','202','207') NOT NULL,
    `weight` enum('20-30','30-40','40-50','50-60','60-70','70-80','80-90','90+') NOT NULL,
    `reserved` int(11) DEFAULT NULL,
    
     FOREIGN KEY (`typeID`) REFERENCES `skiType` (`typeID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `production_plan`
--

CREATE TABLE `production_plan` (
   `employeeNumber` int (20) NOT NULL,
    `typeID` int(11) NOT NULL,
    `startDate` date NOT NULL PRIMARY KEY,
    `endDate` date DEFAULT NULL,
    
    FOREIGN KEY (`employeeNumber`) REFERENCES `employee` (`employeeNumber`) ,
    FOREIGN KEY (`typeID`) REFERENCES `skiType` (`typeID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shipment`
--

CREATE TABLE `shipment` (
  `shipmentNumber` int(20) NOT NULL PRIMARY KEY,
    `orderNumber` int(20) NOT NULL,
    `transporterID` int(20) NOT NULL,
    `customerID` int(20) NOT NULL,
    `shippingAddress` varchar(100) NOT NULL,
    `pickUpDate` timestamp NOT NULL DEFAULT current_timestamp(),
    `state` enum('ready', 'shipped') NOT NULL,
    
    FOREIGN KEY (`transporterID`) REFERENCES `transporter` (`transporterID`) ,
    FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`) ,
    FOREIGN KEY (`orderNumber`) REFERENCES `orders` (`orderNumber`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ski_order`
--

CREATE TABLE `ski_order` (
  `orderNumber` Int (20) NOT NULL PRIMARY KEY,
  `quantity` int(2) NOT NULL,
  `totalPrice` float NOT NULL ,
  `state` ENUM('new','open','available','cancelled','ready','shipped') NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ski_type`
--

CREATE TABLE `ski_type` (
  `typeID` int(11) NOT NULL PRIMARY KEY,
  `type` enum('classic','skate','doublePole') NOT NULL,
  `model` enum('active','activePro','endurance','intrasonic','racePro','raceSpeed','redline') NOT NULL,
  `description` varchar(200) NOT NULL,
  `historical` tinyint(1) DEFAULT NULL,
  `url` varchar(255) NOT NULL,
  `msrpp` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `store` (
    `customerID` Int (20) NOT NULL PRIMARY KEY,
 	`price` float NOT NULL,
    `address` varchar (30),
    FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`) 
);

-- --------------------------------------------------------

--
-- Table structure for table `team_skier`
--

CREATE TABLE `team_skier` (
  `customerID` int(20) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `club` varchar(100) NOT NULL,
  `numSkis` int(3) DEFAULT NULL,

  FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transporter`
--

CREATE TABLE `transporter` (
  `transporterID` int(20) PRIMARY KEY NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employee_number`);

--
-- Indexes for table `franchise_store`
--
ALTER TABLE `franchise_store`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_number`);

--
-- Indexes for table `production_plan`
--
ALTER TABLE `production_plan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shipment`
--
ALTER TABLE `shipment`
  ADD PRIMARY KEY (`shipment_number`);

--
-- Indexes for table `ski_order`
--
ALTER TABLE `ski_order`
  ADD PRIMARY KEY (`order_number`);

--
-- Indexes for table `ski_type`
--
ALTER TABLE `ski_type`
  ADD PRIMARY KEY (`model`);

--
-- Indexes for table `transporter`
--
ALTER TABLE `transporter`
  ADD PRIMARY KEY (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;




