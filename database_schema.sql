-- MySQL Compatible Database Schema for TruckingPro
-- This file is for reference and MySQL setup.
-- The main Django application uses SQLite by default.

CREATE DATABASE IF NOT EXISTS truckingpro_db;
USE truckingpro_db;

-- Table for contact messages (PHP Module)
CREATE TABLE IF NOT EXISTS contact_messages (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for truck orders (MySQL version of Django model)
CREATE TABLE IF NOT EXISTS truck_order (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    pickup_location VARCHAR(255) NOT NULL,
    delivery_location VARCHAR(255) NOT NULL,
    shipment_size VARCHAR(100) NOT NULL,
    shipment_weight DECIMAL(10,2) NOT NULL,
    shipment_type VARCHAR(100) NOT NULL,
    pickup_time DATETIME NOT NULL,
    delivery_time DATETIME NULL,
    status VARCHAR(20) DEFAULT 'pending',
    admin_comment TEXT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
