-- Schéma de la base de données
CREATE TABLE IF NOT EXISTS machines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(15) NOT NULL,
    machine_name VARCHAR(255),
    scan_results TEXT
);
