
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Workora Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load datasets
web_df = pd.read_csv("dashboard_data/web_traffic.csv")
churn_df = pd.read_csv("dashboard_data/customer_churn.csv")
regional_df = pd.read_csv("dashboard_data/regional_market.csv")
ab_df = pd.read_csv("dashboard_data/checkout_ab_test.csv")

# Clean data
web_df["Date"] = pd.to_datetime(web_df["Date"])
churn_df = churn_df.drop_duplicates().copy()
churn_df["Region"] = churn_df["Region"].fillna("Unknown")
churn_df["TotalChargesINR"] = pd.to_numeric(
    churn_df["TotalChargesINR"], errors="coerce"
)

for col in ["StartedRegistration", "Registered", "Bounced"]:
    web_df[col] = web_df[col].astype(str).str.strip().str.lower().map(
        {"yes": True, "no": False, "true": True, "false": False}
    )

for col in ["CheckoutStarted", "Converted"]:
    ab_df[col] = ab_df[col].astype(str).str.strip().str.lower().map(
        {"yes": True, "no": False, "true": True, "false": False}
    )

ab_df["Timestamp"] = pd.to_datetime(ab_df["Timestamp"])

# Title
st.title("📊 Workora Data Analytics Dashboard")
st.caption("Acquisition | Engagement | Regional Demand | Customer Retention | A/B Testing")
st.info("All datasets are synthetic and intended only for educational purposes.")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

date_range = st.sidebar.date_input(
    "Web Traffic Date Range",
    value=(web_df["Date"].min().date(), web_df["Date"].max().date()),
    min_value=web_df["Date"].min().date(),
    max_value=web_df["Date"].max().date()
)

regions = sorted(web_df["Region"].unique())
selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)

sources = sorted(web_df["Source"].unique())
selected_sources = st.sidebar.multiselect(
    "Traffic Source",
    sources,
    default=sources
)
categories = sorted(web_df["DeviceCategory"].unique())

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

# Apply filters
filtered_web = web_df[
    web_df["Region"].isin(selected_regions) &
    web_df["Source"].isin(selected_sources) &
    web_df["DeviceCategory"].isin(selected_categories) 
].copy()

if len(date_range) == 2:
    filtered_web = filtered_web[
        filtered_web["Date"].dt.date.between(date_range[0], date_range[1])
    ]

# KPI calculations
total_sessions = len(filtered_web)
registered_users = filtered_web["Registered"].sum()
bounce_rate = filtered_web["Bounced"].mean() * 100 if total_sessions else 0

total_customers = len(churn_df)
churned = churn_df["Churn"].str.strip().str.lower().eq("yes").sum()
active_customers = total_customers - churned
churn_rate = churned / total_customers * 100

converted_orders = ab_df.loc[ab_df["Converted"], "OrderValueINR"]
avg_ticket = converted_orders.mean() if len(converted_orders) else 0
ab_revenue = converted_orders.sum()

# KPI cards
st.subheader("Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sessions", f"{total_sessions:,}")
c2.metric("Retained Customers", f"{active_customers:,}")
c3.metric("Churn Rate", f"{churn_rate:.2f}%")
c4.metric("Avg Ticket Size", f"₹{avg_ticket:.2f}")

c5, c6, c7 = st.columns(3)
c5.metric("Registered Users", f"{registered_users:,}")
c6.metric("Bounce Rate", f"{bounce_rate:.2f}%")
c7.metric("Converted Order Value", f"₹{ab_revenue:,.0f}")

# Traffic chart
st.subheader("1. Acquisition & Engagement")

source_data = filtered_web.groupby("Source").agg(
    Sessions=("SessionID", "count")
).reset_index()

fig1 = px.bar(
    source_data,
    x="Source",
    y="Sessions",
    color="Source",
    title="Website Sessions by Traffic Source"
)
st.plotly_chart(fig1, use_container_width=True)

# Churn chart
st.subheader("2. Customer Retention")

churn_df["ChurnFlag"] = churn_df["Churn"].str.strip().str.lower().eq("yes")

contract_data = churn_df.groupby("ContractType").agg(
    Customers=("CustomerID", "count"),
    Churned=("ChurnFlag", "sum")
).reset_index()

contract_data["ChurnRate"] = (
    contract_data["Churned"] / contract_data["Customers"] * 100
)

fig2 = px.bar(
    contract_data,
    x="ContractType",
    y="ChurnRate",
    color="ContractType",
    title="Churn Rate by Contract Type",
    labels={"ChurnRate": "Churn Rate (%)"}
)
st.plotly_chart(fig2, use_container_width=True)

# Regional chart
st.subheader("3. Regional Market Demand")

state_data = regional_df.groupby("State").agg(
    SearchDemand=("MonthlySearchDemand", "sum")
).reset_index().sort_values("SearchDemand", ascending=False)

fig3 = px.bar(
    state_data,
    x="State",
    y="SearchDemand",
    color="SearchDemand",
    title="Monthly Search Demand by State"
)
st.plotly_chart(fig3, use_container_width=True)

# A/B testing
st.subheader("4. A/B Testing")

ab_df["ConvertedFlag"] = ab_df["Converted"].astype(bool)

ab_data = ab_df.groupby("Variant").agg(
    Visitors=("VisitorID", "count"),
    Conversions=("ConvertedFlag", "sum")
).reset_index()

ab_data["ConversionRate"] = (
    ab_data["Conversions"] / ab_data["Visitors"] * 100
)

fig4 = px.bar(
    ab_data,
    x="Variant",
    y="ConversionRate",
    color="Variant",
    title="A/B Test Conversion Rate",
    labels={"ConversionRate": "Conversion Rate (%)"}
)
st.plotly_chart(fig4, use_container_width=True)

st.subheader("A/B Test Summary")
st.text(ab_data.to_string(index=False))

st.caption("Developed by S. SHREE VATHY | Workora Data Analytics Internship")