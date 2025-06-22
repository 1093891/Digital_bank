
INSERT INTO users (full_name, email, password_hash) VALUES
('Alice Johnson', 'alice.johnson@example.com', '$2b$10$abc123...'), 
('Bob Smith', 'bob.smith@example.com', '$2b$10$def456...'),
('Cathy Nguyen', 'cathy.nguyen@example.com', '$2b$10$ghi789...'),
('David Lee', 'david.lee@example.com', '$2b$10$jkl012...'),
('Ella Davis', 'ella.davis@example.com', '$2b$10$mno345...');

INSERT INTO accounts (user_id, account_type, balance, currency) VALUES
(1, 'checking', 2500.00, 'USD'),
(2, 'savings', 15000.50, 'USD'),
(3, 'loan', -5000.00, 'USD'),
(4, 'checking', 3200.75, 'USD'),
(5, 'savings', 7800.00, 'USD');


INSERT INTO transactions (account_id, type, amount, description) VALUES
(1, 'deposit', 1000.00, 'Initial deposit'),
(2, 'withdrawal', 500.00, 'ATM withdrawal'),
(3, 'deposit', 200.00, 'Loan repayment'),
(4, 'withdrawal', 120.75, 'Online purchase'),
(5, 'deposit', 500.00, 'Paycheck');



INSERT INTO transfers (from_account_id, to_account_id, amount) VALUES
(1, 2, 300.00),
(2, 4, 1000.00),
(5, 1, 500.00),
(4, 3, 450.00),
(3, 5, 200.00);