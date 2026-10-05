# Customer Repeat Purchase Analysis

## 📌 Project Overview

This project analyzes customer purchasing behavior to measure repeat purchase rates and identify different customer segments.

The analysis was performed using Python and SQL on the Online Retail II dataset.

## 🎯 Objectives

- Measure the customer repeat purchase rate
- Identify first-time and repeat customers
- Compare spending behavior of first-time and repeat customers
- Segment customers based on purchase frequency
- Generate actionable business insights

## 🛠️ Tools & Technologies

- Python
- Pandas
- SQL
- SQLite
- Jupyter/VS Code
- GitHub

## 📊 Key Metrics

| Metric | Result |
|---|---:|
| Total Customers | 4,312 |
| First-Time Customers | 1,419 |
| Repeat Customers | 2,893 |
| Repeat Purchase Rate | 67.09% |

## 👥 Customer Segments

| Segment | Customers | Avg Purchases | Avg Spending |
|---|---:|---:|---:|
| One-Time | 1,419 | 1.00 | 351.69 |
| Repeat | 1,713 | 2.75 | 1,011.71 |
| Loyal | 1,180 | 11.09 | 5,593.14 |

## 💰 First-Time vs Repeat Customers

| Customer Type | Customers | Average Spending |
|---|---:|---:|
| First-Time Customer | 1,419 | 351.69 |
| Repeat Customer | 2,893 | 2,880.39 |

## 🔍 Key Insights

1. The repeat purchase rate is 67.09%, indicating strong customer retention.
2. Repeat customers represent a significant portion of the customer base.
3. Loyal customers have the highest average spending at 5,593.14.
4. One-time customers have the lowest average spending at 351.69.
5. Repeat customers have substantially higher average spending than first-time customers.
6. Customer loyalty programs and targeted retention campaigns can help increase repeat purchases.

📚 Dataset
Dataset used: Online Retail II
The dataset contains transaction-level retail purchase information including invoices, products, quantities, prices, customer IDs and countries.

👩‍💻 Author -- Diya Goel
VEDA Data Analytics Track – Day 28

## 📁 Project Structure

```text
VEDA-Day28-Customer-Repeat-Purchase-Analysis/
│
├── data/
├── python/
│   ├── repeat_purchase_analysis.py
│   ├── run_sql_analysis.py
│   └── README.md
│
├── sql/
│   └── repeat_purchase_analysis.sql
│
├── outputs/
│   ├── customer_summary.csv
│   ├── customer_segments.csv
│   ├── aov_comparison.csv
│   ├── repeat_purchase_metrics.csv
│   └── README.md
│
└── README.md
