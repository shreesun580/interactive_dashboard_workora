# INTERACTIVE DATA ANALYTICS DASHBOARD

### Workora – Data Analytics Virtual Internship

**Developed by:** S. SHREE VATHY  
**Project:** Interactive Dashboard Development  
**Tools:** Python | Pandas | Streamlit | Plotly

---

## 1. Project Overview

The Interactive Data Analytics Dashboard is developed as part of the Workora Data Analytics Virtual Internship.

The primary objective of this project is to transform multiple structured datasets into an interactive business intelligence dashboard. The dashboard provides insights into website acquisition, customer retention, regional market demand, and A/B testing performance through KPI cards, interactive filters, and dynamic visualizations.

The application is developed using Python, Streamlit, Pandas, and Plotly and deployed publicly using Streamlit Community Cloud.

## 2. Dataset & Quality Validation

Four synthetic datasets were used for this project.

| Dataset | Records | Purpose |
|---|---:|---|
| Web Traffic | 900 | Website acquisition and engagement analysis |
| Customer Churn | 600 (after cleaning) | Customer retention analysis |
| Regional Market | 400 | Regional demand and market opportunity analysis |
| A/B Testing | 1,200 | Checkout conversion comparison |

### Data Preparation

The following preparation steps were performed:

- Inspected dataset structures, columns, and data types.
- Checked missing values and duplicate records.
- Removed 5 duplicate records from the customer churn dataset.
- Filled 13 missing Region values with `Unknown`.
- Converted TotalChargesINR into numeric format.
- Converted date and timestamp columns into datetime format.
- Standardized registration, churn-related, and experiment flags for analysis.
- Validated the cleaned datasets before dashboard development.

## 3. Methodology

The project followed a structured data analytics workflow:

1. **Data Collection:** Imported four CSV datasets.
2. **Data Inspection:** Examined dataset dimensions, columns, and data quality.
3. **Data Cleaning:** Handled duplicates, missing values, and data type inconsistencies.
4. **KPI Development:** Calculated relevant performance indicators.
5. **Data Analysis:** Performed acquisition, retention, regional, and experiment analysis.
6. **Visualization:** Created interactive charts using Plotly.
7. **Dashboard Development:** Integrated the analysis into a Streamlit application.
8. **Deployment:** Published the dashboard using Streamlit Community Cloud.

## 4. Dashboard KPI Summary

The dashboard includes the following key performance indicators:

| KPI | Result |
|---|---:|
| Total Website Sessions | 900 |
| Retained Customers | 353 |
| Customer Churn Rate | 41.17% |
| Average Ticket Size | ₹146.66 |
| Registered Users | 166 |
| Website Bounce Rate | 4.89% |
| Converted Order Value | ₹18,772 |

*Note: Each KPI is calculated from its respective dataset. Converted Order Value and Average Ticket Size refer only to converted orders in the A/B testing dataset.*

## 5. Interactive Filters

The dashboard provides interactive filtering capabilities:

- **Date Range:** Filter website traffic by selected dates.
- **Region:** Explore website traffic across available regions.
- **Category:** Filter traffic by device category.
- **Traffic Source:** Compare sessions across different acquisition sources.

The website traffic KPIs and acquisition chart respond to the selected filters. Other analytical sections use their respective datasets independently.

## 6. Key Visualizations & Analysis

### 6.1 Website Sessions by Traffic Source

A bar chart compares website sessions across different acquisition channels, helping identify the sources contributing to website traffic.

### 6.2 Customer Churn Rate by Contract Type

A comparative chart analyzes customer churn percentages across Month-to-Month, One Year, and Two Year contracts.

### 6.3 Regional Market Demand

A state-wise visualization compares monthly search demand across different Indian states to understand regional market interest.

### 6.4 A/B Testing Conversion Comparison

A bar chart compares conversion rates between experiment variants A and B.

| Variant | Visitors | Conversions | Conversion Rate |
|---|---:|---:|---:|
| A | 600 | 57 | 9.50% |
| B | 600 | 71 | 11.83% |

Variant B recorded a higher observed conversion rate, with a difference of approximately 2.33 percentage points compared with Variant A.

This is a descriptive comparison and does not independently establish statistical significance.

## 7. Key Findings

- The web traffic dataset contains 900 sessions and 166 completed registrations.
- The customer dataset contains 600 records after duplicate removal.
- Customer churn stands at approximately 41.17%.
- A total of 353 customers were retained in the customer dataset.
- The A/B testing dataset shows a higher observed conversion rate for Variant B.
- Regional demand varies across states, providing opportunities for further market analysis.
- Interactive filters make website traffic analysis more flexible and accessible.

## 8. Dataset Limitations

- All datasets are synthetic and intended for educational purposes.
- The results do not represent actual Workora business performance.
- The four datasets are analyzed independently and are not combined into a unified company-wide performance model.
- Retained customers should not be interpreted as active website users.
- Converted Order Value represents only the converted orders in the A/B testing sample.
- The A/B test comparison is descriptive; statistical significance has not been established.

## 9. Project Deliverables

The following deliverables were completed:

- Cleaned and validated datasets.
- Python-based dashboard application (`app.py`).
- Interactive KPI summary cards.
- Dynamic Plotly visualizations.
- Date Range, Region, Category, and Traffic Source filters.
- Dashboard dependency file (`requirements.txt`).
- Publicly deployed Streamlit dashboard.
- Project documentation (`README.md`).

### Live Dashboard

**Explore the Interactive Dashboard:**

https://interactive-dashboard-shree.streamlit.app/

### GitHub Repository

**View Source Code and Project Files:**

https://github.com/shreesun580/workora-interactive-dashboard

---

## Conclusion

This project demonstrates the practical application of data analytics and business intelligence concepts through data preparation, KPI development, exploratory analysis, interactive visualization, and cloud deployment.

The final dashboard provides an accessible platform to explore multiple business-related datasets and understand analytical findings through interactive visual representations.

---

**Developed by S. SHREE VATHY**  
*Workora – Data Analytics Virtual Internship*
