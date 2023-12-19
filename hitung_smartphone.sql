-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Des 2023 pada 15.46
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartphone`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `hitung_smartphone`
--

CREATE TABLE `hitung_smartphone` (
  `id` int(11) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `ram_gb` varchar(100) NOT NULL,
  `storage_gb` varchar(100) NOT NULL,
  `processor` varchar(100) NOT NULL,
  `battery` varchar(100) NOT NULL,
  `harga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `hitung_smartphone`
--

INSERT INTO `hitung_smartphone` (`id`, `brand`, `ram_gb`, `storage_gb`, `processor`, `battery`, `harga`) VALUES
(1, 'Samsung Galaxy A01', '2', '16', 'Qualcomm Snapdragon 439', '3000', '1499000'),
(2, 'Samsung Galaxy M01', '3', '32', 'Qualcomm Snapdragon 439', '4000', '1999000'),
(3, 'Xiaomi Redmi 9C', '3', '64', 'Mediatek Helio G35', '5000', '1899000'),
(4, 'Xiaomi Redmi 9', '3', '32', 'Mediatek Helio G80', '5020', '1799000'),
(5, 'Realme C11', '2', '32', 'Mediatek Helio G35', '5000', '1499000'),
(6, 'Realme C21', '3', '32', 'Mediatek Helio G35', '5000', '1699000'),
(7, 'Oppo A15', '3', '32', 'Mediatek Helio P35', '4230', '1699000'),
(8, 'Oppo A53', '4', '64', 'Qualcomm Snapdragon 460', '5000', '2299000'),
(9, 'Vivo Y12s', '3', '32', 'Mediatek Helio P35', '5000', '1699000'),
(10, 'Vivo Y20', '4', '64', 'Qualcomm Snapdragon 460', '5000', '2099000');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `hitung_smartphone`
--
ALTER TABLE `hitung_smartphone`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `hitung_smartphone`
--
ALTER TABLE `hitung_smartphone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
