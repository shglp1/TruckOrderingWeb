CREATE TABLE truck_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
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
);