"""
Credit Risk & Customer Lifetime Value (CLV) Analysis
=====================================================
Dataset : 5,000 customer records (synthetic, based on real-world distributions)
Tools   : Python (Pandas, NumPy, Matplotlib, Seaborn)
Author  : Logeshwaran A
GitHub  : https://github.com/Log-ware
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────────
# STEP 1 — Load & Inspect Data
# ─────────────────────────────────────────────────────────────
df = pd.read_csv('credit_risk_data.csv')


print("STEP 1 — Data Overview")

print(f"Shape          : {df.shape}")
print(f"Null values    : {df.isnull().sum().sum()}")
print(f"Default rate   : {df['default'].mean()*100:.1f}%")
print(f"Avg credit score: {df['credit_score'].mean():.0f}")
print(f"Avg income     : ₹{df['annual_income'].mean():,.0f}")
print()

# ─────────────────────────────────────────────────────────────
# STEP 2 — RFM Segmentation
# ─────────────────────────────────────────────────────────────

print("STEP 2 — RFM Segmentation")


rfm = df[['customer_id', 'recency_days', 'frequency', 'monetary']].copy()

# Score each dimension 1–4
rfm['R'] = pd.qcut(rfm['recency_days'], 4, labels=[4, 3, 2, 1]).astype(int)
rfm['F'] = pd.qcut(rfm['frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4]).astype(int)
rfm['M'] = pd.qcut(rfm['monetary'], 4, labels=[1, 2, 3, 4]).astype(int)
rfm['RFM_Score'] = rfm['R'] + rfm['F'] + rfm['M']

def assign_segment(score):
    if score >= 10:  return 'Champions'
    elif score >= 8: return 'Loyal'
    elif score >= 6: return 'At Risk'
    else:            return 'Lost'

rfm['segment'] = rfm['RFM_Score'].apply(assign_segment)
df = df.merge(rfm[['customer_id', 'R', 'F', 'M', 'RFM_Score', 'segment']], on='customer_id')

print(df['segment'].value_counts())
print()

# ─────────────────────────────────────────────────────────────
# STEP 3 — Composite Risk Score
# ─────────────────────────────────────────────────────────────

print("STEP 3 — Composite Risk Score Engineering")


# Weighted formula:
#   40% → credit score (inverted — lower score = higher risk)
#   20% → debt-to-income (loan / income)
#   10% × existing loans
#   30% → recency (longer since last transaction = higher risk)

df['risk_score'] = (
    (850 - df['credit_score']) / 550 * 40
    + (df['loan_amount'] / df['annual_income']) * 20
    + df['existing_loans'] * 10
    + df['recency_days'] / 365 * 30
).round(1).clip(0, 100)

def assign_risk_tier(score):
    if score < 25:   return 'Low Risk'
    elif score < 50: return 'Medium Risk'
    elif score < 75: return 'High Risk'
    else:            return 'Critical Risk'

df['risk_tier'] = df['risk_score'].apply(assign_risk_tier)

print("Risk tier distribution:")
print(df['risk_tier'].value_counts())
print()

default_by_tier = df.groupby('risk_tier')['default'].mean() * 100
tier_order = ['Low Risk', 'Medium Risk', 'High Risk', 'Critical Risk']
print("Default rate by risk tier:")
for t in tier_order:
    if t in default_by_tier.index:
        print(f"  {t:<15}: {default_by_tier[t]:.1f}%")
print()

# ─────────────────────────────────────────────────────────────
# STEP 4 — CLV Estimation
# ─────────────────────────────────────────────────────────────

print("STEP 4 — Customer Lifetime Value Estimation")


# CLV proxy: monetary × frequency / recency weight
df['estimated_clv'] = (
    df['monetary'] * df['frequency'] * (1 / (df['recency_days'] / 365 + 0.1))
).round(0)

clv_by_segment = df.groupby('segment')['estimated_clv'].agg(['mean', 'sum'])
print("CLV by segment:")
print(clv_by_segment.round(0))

champions = df[df['segment'] == 'Champions']
total_monetary = df['monetary'].sum()
champ_monetary = champions['monetary'].sum()
print(f"\n→ Champions ({len(champions)} customers) account for "
      f"{champ_monetary/total_monetary*100:.1f}% of total monetary value")
print(f"→ Targeting Champions vs. mass outreach = "
      f"{df['segment'].value_counts()['Champions'] / len(df) * 100:.1f}% of customer base")
print()

# ─────────────────────────────────────────────────────────────
# STEP 5 — Key Business Insights
# ─────────────────────────────────────────────────────────────

print("STEP 5 — Key Business Insights")


high_value_low_risk = df[
    (df['segment'].isin(['Champions', 'Loyal'])) &
    (df['risk_tier'].isin(['Low Risk', 'Medium Risk']))
]
print(f"High-value + Low-risk customers: {len(high_value_low_risk)} "
      f"({len(high_value_low_risk)/len(df)*100:.1f}% of base)")
print(f"→ Priority segment for credit line expansion")
print()

at_risk_high_clv = df[
    (df['segment'] == 'At Risk') &
    (df['estimated_clv'] > df['estimated_clv'].quantile(0.6))
]
print(f"At-Risk customers with high CLV: {len(at_risk_high_clv)}")
print(f"→ Priority retention targets — high value, slipping away")
print()

df.to_csv('credit_risk_segmented.csv', index=False)
print("✅ Segmented dataset saved to credit_risk_segmented.csv")
