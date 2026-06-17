# Credit Risk & Customer Lifetime Value (CLV) Analysis
### Python · SQL · Power BI · RFM Segmentation · DAX

---

## 📌 Project Overview

An end-to-end analytics pipeline that evaluates **credit risk** and models **Customer Lifetime Value (CLV)** across 5,000+ customer records. The goal was to move beyond simple rule-based targeting and build a data-driven segmentation model that classifies customers by both their value and their risk — enabling smarter, more targeted outreach.

**Key result:** Engineered a composite risk score that enabled **30%+ more targeted outreach** than prior rule-based methods.

---

## 🎯 Business Problem

The business needed to answer two questions simultaneously:
1. Which customers are most valuable (high CLV)?
2. Which customers carry the highest risk of default or churn?

A customer who is high-value AND high-risk needs a different strategy than one who is low-value AND low-risk. Treating them the same wastes budget and increases exposure.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy) | Data cleaning, RFM calculation, risk scoring |
| Python (Matplotlib, Seaborn) | Visualisation and EDA |
| SQL | Data extraction and aggregation from customer database |
| Power BI + DAX | Interactive dashboard for stakeholder review |

---

## 📊 Methodology

### Step 1 — Data Extraction (SQL)
Extracted customer transaction history, payment behaviour, and account data using SQL joins and aggregations across multiple tables.

### Step 2 — RFM Segmentation (Python)
Calculated three scores per customer:
- **Recency** — how recently did they transact?
- **Frequency** — how often do they transact?
- **Monetary** — how much have they spent?

Each customer received an RFM score from 1–5 on each dimension, combined into a composite value score.

### Step 3 — Credit Risk Scoring (Python)
Built a composite risk score incorporating:
- Payment delay patterns
- Account delinquency flags
- Transaction volatility

### Step 4 — Value-Risk Tier Classification
Combined RFM value score + risk score to classify all 5,000+ customers into **4 tiers**:

| Tier | Description | Strategy |
|------|-------------|----------|
| High Value, Low Risk | Best customers | Retain and upsell |
| High Value, High Risk | Profitable but risky | Monitor and limit exposure |
| Low Value, Low Risk | Safe but small | Nurture with low-cost outreach |
| Low Value, High Risk | Drain on resources | Deprioritise or exit |

### Step 5 — Power BI Dashboard
Built interactive dashboards with DAX measures for stakeholders to explore:
- Segment distribution
- Risk distribution by geography and product
- CLV trends over time
- KPI summary cards

---

## 📁 Project Structure

```
Python-CreditRisk-CLV-Analysis/
│
├── data/
│   └── customer_data_sample.csv       # Anonymised sample dataset
│
├── notebooks/
│   └── credit_risk_clv_analysis.ipynb # Full Python analysis
│
├── sql/
│   └── customer_extraction.sql        # Data extraction queries
│
├── dashboard/
│   └── clv_risk_dashboard.pbix        # Power BI dashboard file
│
└── README.md
```

---

## 🔑 Key Findings

- Top 20% of customers by CLV score accounted for **68% of total revenue**
- High-risk customers represented **23% of the portfolio** but only **11% of revenue** — significant exposure for limited return
- RFM segmentation enabled **30%+ improvement in outreach targeting** vs. prior flat-list approach
- 4 distinct value-risk tiers identified, each requiring a different commercial strategy

---

## 📈 How to Run

1. Clone this repository
2. Open `notebooks/credit_risk_clv_analysis.ipynb` in Jupyter Notebook
3. Install requirements: `pip install pandas numpy matplotlib seaborn`
4. Run all cells sequentially
5. Open `dashboard/clv_risk_dashboard.pbix` in Power BI Desktop for the interactive view

---

## 📫 Questions?
**Logeshwaran A** · logesh17799@gmail.com · [LinkedIn](https://www.linkedin.com/in/logeshwaran-a-870078242)
