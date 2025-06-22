CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password_hash VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE accounts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  account_type ENUM('savings', 'checking', 'loan'),
  balance DECIMAL(12,2) DEFAULT 0.00,
  currency VARCHAR(10) DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  account_id INT,
  type ENUM('deposit', 'withdrawal', 'transfer'),
  amount DECIMAL(12,2),
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  description TEXT,
  FOREIGN KEY (account_id) REFERENCES accounts(id)
);

CREATE TABLE transfers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  from_account_id INT,
  to_account_id INT,
  amount DECIMAL(12,2),
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (from_account_id) REFERENCES accounts(id),
  FOREIGN KEY (to_account_id) REFERENCES accounts(id)
);