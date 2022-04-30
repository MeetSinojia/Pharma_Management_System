-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2021 at 11:51 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_disease`
--

CREATE TABLE `add_disease` (
  `id` int(11) NOT NULL,
  `disease` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `add_disease`
--

INSERT INTO `add_disease` (`id`, `disease`) VALUES
(1, 'Fever'),
(2, 'Cuf'),
(3, 'Flue'),
(4, 'Vomite'),
(5, 'Acidity');

-- --------------------------------------------------------

--
-- Table structure for table `departure`
--

CREATE TABLE `departure` (
  `id` int(11) NOT NULL,
  `ref_no` int(11) NOT NULL,
  `city` varchar(70) NOT NULL,
  `medname` varchar(70) NOT NULL,
  `depid` int(11) NOT NULL,
  `vehicleno` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `departure`
--

INSERT INTO `departure` (`id`, `ref_no`, `city`, `medname`, `depid`, `vehicleno`) VALUES
(2, 1, 'Botad', 'FabiFlu', 426, 'GJ-12-XY-1245'),
(3, 2, 'Viramgam', 'Peracetamol', 326, 'GJ-1-AB-2013'),
(4, 1, 'Rajkot', 'FabiFlu', 475, 'GJ-12-XY-6666'),
(5, 3, 'Botad', 'Peracetamol', 426, 'GJ-12-XY-7777');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `ref_no` int(11) NOT NULL,
  `medname` varchar(80) NOT NULL,
  `efficiency` int(11) NOT NULL,
  `sideeffect` varchar(80) NOT NULL,
  `typemed` varchar(80) NOT NULL,
  `cmpname` varchar(80) NOT NULL,
  `disease` varchar(80) NOT NULL,
  `expdate` datetime NOT NULL,
  `mfgdate` datetime NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`ref_no`, `medname`, `efficiency`, `sideeffect`, `typemed`, `cmpname`, `disease`, `expdate`, `mfgdate`, `user_id`) VALUES
(1, 'FabiFlu  upadted', 90, 'Vomiting', 'Liquid', 'Sun Pharma', 'Cuf', '2023-04-01 00:00:00', '2021-02-01 00:00:00', 1),
(4, 'Naxdom', 85, 'Fever', 'Tablet', 'Zydus', 'Flue', '2025-11-01 00:00:00', '2020-11-01 00:00:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `price` float NOT NULL,
  `does_available` int(11) NOT NULL,
  `dose_sale` int(11) NOT NULL,
  `medname` varchar(70) NOT NULL,
  `profit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `price`, `does_available`, `dose_sale`, `medname`, `profit`) VALUES
(1, 24.99, 100, 400, 'Peracetamol', 90),
(2, 52.99, 100, 300, 'Naxdom', 56),
(3, 68.89, 400, 1000, 'Peracetamol', 78);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`) VALUES
(1, 'shubham@gmail.com', '$2b$12$hegF3avA./S.gRFULsGKqeZofxgbAg4s6jMDspn0zgNNWrwT0/JXW'),
(2, 'vasu@gmail.com', '$2b$12$Uy1v6.J7BHF19l/0Bo1xGOsYAfHXRY3RyeOJS8VYkfc/KQBR2Oafi'),
(3, 'mihir@gmail.com', '$2b$12$q1i2235ppFNefM/j1emiGOCWsPkmjuo3vByWoGZAPRX3i4movam72');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_disease`
--
ALTER TABLE `add_disease`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `departure`
--
ALTER TABLE `departure`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`ref_no`),
  ADD UNIQUE KEY `medname` (`medname`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_disease`
--
ALTER TABLE `add_disease`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `departure`
--
ALTER TABLE `departure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `ref_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `medicine`
--
ALTER TABLE `medicine`
  ADD CONSTRAINT `medicine_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
