-- Create table
CREATE TABLE sales (
    month VARCHAR(20),
    product VARCHAR(20),
    revenue INT
);

-- Insert data
INSERT INTO sales VALUES
('January', 'Product A', 1200),
('January', 'Product B', 900),
('February', 'Product A', 1500),
('February', 'Product B', 1100),
('March', 'Product A', 1800),
('March', 'Product B', 1300);

-- Analysis
SELECT product, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product;

SELECT [month], SUM(revenue) AS total_revenue
FROM sales
GROUP BY [month];

SELECT TOP 1 *
FROM sales
ORDER BY revenue DESC;
