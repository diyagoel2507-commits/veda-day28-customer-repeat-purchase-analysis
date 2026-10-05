-- VEDA Day 28
-- Customer Repeat Purchase Analysis

SELECT COUNT(*) AS total_customers
FROM customer_summary;

SELECT COUNT(*) AS first_time_customers
FROM customer_summary
WHERE PurchaseCount = 1;

SELECT COUNT(*) AS repeat_customers
FROM customer_summary
WHERE PurchaseCount > 1;

SELECT
    ROUND(
        SUM(CASE WHEN PurchaseCount > 1 THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS repeat_purchase_rate
FROM customer_summary;

SELECT
    Segment,
    COUNT(*) AS customers,
    ROUND(AVG(PurchaseCount), 2) AS avg_purchases,
    ROUND(AVG(TotalSpending), 2) AS avg_spending
FROM customer_summary
GROUP BY Segment
ORDER BY customers DESC;

SELECT
    CustomerType,
    COUNT(*) AS customers,
    ROUND(AVG(TotalSpending), 2) AS average_spending
FROM customer_summary
GROUP BY CustomerType;
