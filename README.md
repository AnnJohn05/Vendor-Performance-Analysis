# Vendor Performance Analysis

## 📌 Project Overview

This project analyzes vendor sales, purchasing, profitability, pricing, and inventory performance to identify key business opportunities and support data-driven vendor management decisions.

The analysis combines **SQL, Python, Pandas, statistical analysis, and Power BI** to transform raw vendor and transaction data into actionable business insights.

## 🎯 Business Objectives

- Evaluate vendor performance based on sales and profitability
- Identify top-performing vendors and brands
- Identify brands with low sales but high profit margins for promotional or pricing adjustments
- Analyze vendor contribution to total purchases
- Identify slow-moving inventory and capital locked in unsold stock
- Analyze the relationship between purchase quantity and unit purchase price
- Compare profit margins of top-performing and low-performing vendors using statistical analysis

## 🛠️ Tools & Technologies

- **Python** – Data cleaning, transformation, and analysis
- **Pandas & NumPy** – Data manipulation and numerical analysis
- **SQL / SQLite** – Data aggregation and vendor-level summary creation
- **Matplotlib & Seaborn** – Data visualization
- **SciPy** – Statistical analysis and hypothesis testing
- **Power BI** – Interactive dashboard and KPI reporting
- **Git & GitHub** – Version control

## 🔄 Project Workflow

Raw Transaction Data  
↓  
Data Ingestion into SQLite  
↓  
SQL-Based Vendor Summary  
↓  
Data Cleaning & Feature Engineering  
↓  
Exploratory Data Analysis  
↓  
Statistical & Business Analysis  
↓  
Power BI Dashboard  
↓  
Business Recommendations

## 📊 Key Analyses

### 1. Vendor & Brand Performance

Analyzed total sales and identified the top-performing vendors and brands based on sales contribution.

### 2. Promotional & Pricing Opportunities

Identified brands with lower sales performance but higher profit margins, highlighting potential opportunities for targeted promotions, improved visibility, or pricing adjustments.

### 3. Vendor Purchase Contribution

Performed a Pareto-style analysis to understand each vendor's contribution to total purchasing expenditure.

### 4. Inventory & Working Capital Analysis

Analyzed stock turnover and unsold inventory to identify slow-moving inventory and quantify capital tied up in unsold stock.

The analysis identified approximately **$2.71M in unsold inventory capital**.

### 5. Bulk Purchasing & Pricing

Segmented purchase quantities into Small, Medium, and Large order sizes to analyze the relationship between purchasing volume and unit purchase price.

### 6. Statistical Validation

Used a two-sample Welch's t-test to compare profit margins between top-performing and low-performing vendors.

**Result:**

- T-Statistic: **-17.6440**
- P-Value: **< 0.05**
- Decision: **Reject H₀**

This indicates a statistically significant difference in profit margins between the two vendor groups.

## 📈 Power BI Dashboard

The Power BI dashboard provides an interactive view of vendor performance using key KPIs and visualizations.

### Key KPIs

| KPI | Value |
|---|---:|
| Total Sales | $441.41M |
| Total Purchase | $307.34M |
| Gross Profit | $134.07M |
| Profit Margin | 38.7% |
| Unsold Capital | $2.71M |

### Dashboard Views

- Purchase Contribution by Vendor
- Top Vendors by Sales
- Top Brands by Sales
- Low Performing Vendors
- Low Sales & High Margin Brands
- Overall Vendor Performance KPIs

## 💡 Business Insights

- High-performing vendors have a significant impact on overall sales and purchasing.
- Certain brands generate relatively high margins despite lower sales, creating opportunities for targeted promotional strategies.
- Low stock turnover can indicate slow-moving inventory and potential working-capital inefficiencies.
- Unsold inventory represents significant capital that could potentially be released through better inventory planning and sales strategies.
- Statistical testing confirms that profit-margin behavior differs significantly between top and low-performing vendor groups.

## 📁 Repository Structure

```text
Vendor-Performance-Analysis/
│
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   └── vendor_invoice.csv
│
├── Exploratory Data Analysis.ipynb
├── Vendor Performance Analysis.ipynb
├── Vendor_Analysis.ipynb
├── get_vendor_summary.py
├── ingestion_db.py
├── vendor_sales_summary.csv
├── vendor_performance.pbix
├── Vendor Performance Report.pdf
└── .gitignore
