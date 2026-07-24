import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="AI Job Market Dashboard",
    page_icon="🤖",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\91801\Downloads\ai_job_dataset.csv")

df = load_data()
# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

h1{
    color:#1F4E79;
    text-align:center;
    font-weight:bold;
}

h2,h3{
    color:#004080;
}

div[data-testid="metric-container"]{
    background:linear-gradient(135deg,#4F8BF9,#6A5ACD);
    padding:20px;
    border-radius:15px;
    color:white;
    box-shadow:0px 5px 15px rgba(0,0,0,0.2);
}

div[data-testid="metric-container"] label{
    color:white;
}

div[data-testid="metric-container"] div{
    color:white;
}

.stAlert{
    border-radius:12px;
}

.css-1r6slb0{
    border-radius:15px;
}

</style>
""",unsafe_allow_html=True)
# =========================
# SIDEBAR
# =========================

st.sidebar.image(
    "https://img.icons8.com/color/480/artificial-intelligence.png",
    width=130
)

st.sidebar.title("AI Job Dashboard")

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
### 📖 Dashboard Sections

Explore

✔ Overview

✔ Job Market

✔ Salary Analysis

✔ Geographic Insights

✔ Advanced Analytics

✔ Final Insights
"""
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Job Market Analysis",
        "Salary Analysis",
        "Geographic Analysis",
        "Advanced Analytics",
        "Insights & Conclusion"
    ]
)


# =========================
# OVERVIEW PAGE
# =========================
# =========================
# OVERVIEW PAGE
# =========================

if page == "Overview":

    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#D6EAF8,#EBF5FB);
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:2px 2px 12px rgba(0,0,0,0.1);">

    <h1 style="color:#154360;">
    🤖 AI Job Market & Salary Trends Dashboard
    </h1>

    <p style="font-size:18px;color:#2E4053;">
    An interactive dashboard that explores global AI hiring trends,
    salary analysis, company characteristics and workforce insights.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ======================
    # KPI CARDS
    # ======================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("💼 Total Jobs", len(df))

    with c2:
        st.metric(
            "💰 Avg Salary",
            f"${df['salary_usd'].mean():,.0f}"
        )

    with c3:
        st.metric(
            "🌍 Countries",
            df["company_location"].nunique()
        )

    with c4:
        st.metric(
            "🏭 Industries",
            df["industry"].nunique()
        )

    st.write("")
    st.divider()

    # ======================
    # DATASET OVERVIEW
    # ======================

    left, right = st.columns([1,1])

    with left:

        st.markdown("### 📏 Dataset Shape")

        rows, cols = df.shape

        st.info(f"""
**Rows :** {rows:,}

**Columns :** {cols}

The dataset contains comprehensive information about AI jobs,
salary trends, company characteristics and employment details.
""")

    with right:

        st.markdown("### 📊 Dataset Statistics")

        st.success(f"""
**Average Salary**

${df['salary_usd'].mean():,.0f}

**Maximum Salary**

${df['salary_usd'].max():,.0f}

**Minimum Salary**

${df['salary_usd'].min():,.0f}
""")

    st.divider()

    # ======================
    # DATA PREVIEW
    # ======================

    st.subheader("🔍 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.caption("First five records of the AI Job Market dataset.")

    st.divider()

    # ======================
    # DATA INFORMATION
    # ======================

    st.subheader("📋 Dataset Information")

    info = pd.DataFrame({

        "Column Name": df.columns,

        "Data Type": df.dtypes.astype(str)

    })

    st.dataframe(
        info,
        use_container_width=True
    )

    st.divider()

    # ======================
    # MISSING VALUES
    # ======================

    st.subheader("🧹 Missing Values")

    miss = pd.DataFrame({

        "Column": df.columns,

        "Missing Values": df.isnull().sum()

    })

    st.dataframe(
        miss,
        use_container_width=True
    )

    if df.isnull().sum().sum() == 0:

        st.success("✅ Excellent! No missing values found in the dataset.")

    st.divider()

    # ======================
    # QUICK INSIGHTS
    # ======================

    st.subheader("📌 Dashboard Highlights")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### 💼 Job Market

• Machine Learning Researcher is the most demanded role.

• AI hiring is spread across multiple countries.

• Full-Time employment dominates the market.
""")

    with col2:

        st.info("""
### 💰 Salary Insights

• Executive professionals earn the highest salaries.

• Large companies offer better salary packages.

• Consulting is the highest-paying industry.
""")

    st.divider()

    # ======================
    # PROJECT OBJECTIVE
    # ======================

    st.subheader("🎯 Project Objective")

    st.markdown("""

This dashboard aims to:

- Analyze the global AI job market.

- Compare salaries across countries and industries.

- Understand hiring patterns.

- Explore company characteristics.

- Generate meaningful business insights through Exploratory Data Analysis (EDA).

""")

    st.divider()

    # ======================
    # FOOTER
    # ======================

    st.markdown("""

<div style="
background:#EBF5FB;
padding:18px;
border-radius:12px;
text-align:center;
">

### 🤖 AI Job Market Dashboard

Developed using **Python • Pandas • Plotly • Streamlit**

</div>

""", unsafe_allow_html=True)


# =========================
# JOB MARKET ANALYSIS
# =========================

elif page == "Job Market Analysis":

    st.title("💼 Job Market Analysis")

    st.markdown("Analyze hiring trends, job roles, industries, employment types, and company sizes across the global AI job market.")

    # Sidebar Filters
    st.sidebar.subheader("🔍 Filter Data")

    selected_country = st.sidebar.multiselect(
        "Select Country",
        sorted(df["company_location"].unique()),
        default=sorted(df["company_location"].unique())
    )

    selected_industry = st.sidebar.multiselect(
        "Select Industry",
        sorted(df["industry"].unique()),
        default=sorted(df["industry"].unique())
    )

    filtered_df = df[
        (df["company_location"].isin(selected_country)) &
        (df["industry"].isin(selected_industry))
    ]

    # =====================
    # KPI Cards
    # =====================

    st.subheader("📊 Job Market Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Jobs", len(filtered_df))
    c2.metric("Job Roles", filtered_df["job_title"].nunique())
    c3.metric("Countries", filtered_df["company_location"].nunique())
    c4.metric("Industries", filtered_df["industry"].nunique())

    st.divider()

    # =====================
    # Top Job Roles
    # =====================

    st.subheader("🏆 Top 10 AI Job Roles")

    top_jobs = (
        filtered_df["job_title"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_jobs.columns = ["Job Title", "Count"]

    fig = px.bar(
        top_jobs,
        x="Job Title",
        y="Count",
        color="Count",
        text="Count",
        title="Top 10 Most Demanded AI Job Roles"
    )

    fig.update_layout(xaxis_tickangle=-25)

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Insight**

    • Machine Learning Researcher is one of the most demanded AI roles.

    • AI Software Engineer, Machine Learning Engineer and AI Architect also have strong hiring demand.

    • Organizations are investing heavily in research, automation and intelligent systems.
    """)

    st.divider()

    # =====================
    # Employment Type
    # =====================

    st.subheader("👨‍💼 Employment Type Distribution")

    emp = (
        filtered_df["employment_type"]
        .value_counts()
        .reset_index()
    )

    emp.columns = ["Employment Type", "Count"]

    fig = px.pie(
        emp,
        values="Count",
        names="Employment Type",
        hole=0.45,
        title="Employment Type Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Insight**

    • Full-time jobs dominate the AI market.

    • Contract, Part-Time and Freelance opportunities are comparatively fewer.

    • Companies prefer long-term skilled AI professionals.
    """)

    st.divider()

    # =====================
    # Industry Distribution
    # =====================

    st.subheader("🏭 Industry-wise Job Distribution")

    industry = (
        filtered_df["industry"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    industry.columns = ["Industry", "Jobs"]

    fig = px.bar(
        industry,
        x="Industry",
        y="Jobs",
        color="Jobs",
        text="Jobs",
        title="Top Industries Hiring AI Professionals"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Business Insight**

    • Technology, Finance, Manufacturing and Healthcare industries contribute significantly to AI hiring.

    • AI adoption is no longer limited to technology companies.

    • Multiple industries are integrating AI into business operations.
    """)

    st.divider()

    # =====================
    # Company Size
    # =====================

    st.subheader("🏢 Company Size Distribution")

    company = (
        filtered_df["company_size"]
        .value_counts()
        .reset_index()
    )

    company.columns = ["Company Size", "Count"]

    fig = px.bar(
        company,
        x="Company Size",
        y="Count",
        color="Count",
        text="Count",
        title="Distribution of Company Sizes"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Business Insight**

    • Medium-sized companies represent the largest share of AI hiring.

    • Large companies also recruit extensively for AI positions.

    • Small companies are increasingly adopting AI talent.
    """)

    st.divider()

    # =====================
    # Hiring Countries
    # =====================

    st.subheader("🌍 Top Hiring Countries")

    country = (
        filtered_df["company_location"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    country.columns = ["Country", "Jobs"]

    fig = px.bar(
        country,
        x="Country",
        y="Jobs",
        color="Jobs",
        text="Jobs",
        title="Top Countries Hiring AI Professionals"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Business Insight**

    • Germany, Denmark, France and Canada are among the leading hiring countries.

    • AI employment opportunities are distributed across multiple global regions.

    • The worldwide demand highlights the growing importance of AI across industries.
    """)
    # =========================
# SALARY ANALYSIS
# =========================

elif page == "Salary Analysis":

    st.title("💰 Salary Analysis")
    st.markdown("""
    Analyze salary trends across different experience levels, company sizes,
    job roles, industries, and countries.
    """)

    st.divider()

    # =====================
    # KPI CARDS
    # =====================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Average Salary", f"${df['salary_usd'].mean():,.0f}")
    c2.metric("Maximum Salary", f"${df['salary_usd'].max():,.0f}")
    c3.metric("Minimum Salary", f"${df['salary_usd'].min():,.0f}")
    c4.metric("Median Salary", f"${df['salary_usd'].median():,.0f}")

    st.divider()

    # =====================
    # Salary by Experience
    # =====================

    st.subheader("📈 Average Salary by Experience Level")

    exp_salary = (
        df.groupby("experience_level")["salary_usd"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        exp_salary,
        x="experience_level",
        y="salary_usd",
        color="salary_usd",
        text_auto=".2s",
        labels={
            "experience_level":"Experience Level",
            "salary_usd":"Average Salary (USD)"
        },
        title="Average Salary by Experience Level"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• Executive-level professionals receive the highest salaries.

• Entry-level professionals earn the lowest salaries.

• Salary increases significantly with experience, highlighting the value of expertise in AI careers.
""")

    st.divider()

    # =====================
    # Salary by Company Size
    # =====================

    st.subheader("🏢 Average Salary by Company Size")

    company_salary = (
        df.groupby("company_size")["salary_usd"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        company_salary,
        x="company_size",
        y="salary_usd",
        color="salary_usd",
        text_auto=".2s",
        labels={
            "company_size":"Company Size",
            "salary_usd":"Average Salary (USD)"
        },
        title="Average Salary by Company Size"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• Large organizations offer the highest average salaries.

• Medium-sized companies remain competitive.

• Small companies generally provide comparatively lower salaries.
""")

    st.divider()

    # =====================
    # Highest Paying Roles
    # =====================

    st.subheader("💼 Top 10 Highest Paying AI Job Roles")

    role_salary = (
        df.groupby("job_title")["salary_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        role_salary,
        x="salary_usd",
        y="job_title",
        orientation="h",
        color="salary_usd",
        text_auto=".2s",
        labels={
            "salary_usd":"Average Salary (USD)",
            "job_title":"Job Role"
        },
        title="Top 10 Highest Paying AI Roles"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• AI Specialist, Machine Learning Engineer and Head of AI are among the highest-paying roles.

• Specialized AI skills command premium salaries.

• Leadership and advanced technical positions receive higher compensation.
""")

    st.divider()

    # =====================
    # Highest Paying Industries
    # =====================

    st.subheader("🏭 Top 10 Highest Paying Industries")

    industry_salary = (
        df.groupby("industry")["salary_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        industry_salary,
        x="industry",
        y="salary_usd",
        color="salary_usd",
        text_auto=".2s",
        title="Highest Paying Industries"
    )

    fig.update_layout(xaxis_tickangle=-30)

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• Consulting provides the highest average salaries.

• Manufacturing, Media and Education also offer attractive AI compensation.

• AI talent is highly valued across diverse industries.
""")

    st.divider()

    # =====================
    # Highest Paying Countries
    # =====================

    st.subheader("🌍 Top 10 Highest Paying Countries")

    country_salary = (
        df.groupby("company_location")["salary_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        country_salary,
        x="company_location",
        y="salary_usd",
        color="salary_usd",
        text_auto=".2s",
        labels={
            "company_location":"Country",
            "salary_usd":"Average Salary"
        },
        title="Top 10 Highest Paying Countries"
    )

    fig.update_layout(xaxis_tickangle=-30)

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• Switzerland offers the highest average AI salary.

• Denmark, Norway and the United States are also among the highest-paying countries.

• Developed AI markets provide better salary opportunities.
""")

    st.divider()

    # =====================
    # Salary Distribution
    # =====================

    st.subheader("📊 Salary Distribution")

    fig = px.histogram(
        df,
        x="salary_usd",
        nbins=30,
        color_discrete_sequence=["royalblue"],
        title="Distribution of AI Salaries"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• Most salaries are concentrated around the middle salary range.

• A few high-paying executive positions create a right-skewed distribution.

• Salary variation reflects differences in experience, industry and geography.
""")

    st.divider()

    # =====================
    # Salary Box Plot
    # =====================

    st.subheader("📦 Salary Spread by Experience Level")

    fig = px.box(
        df,
        x="experience_level",
        y="salary_usd",
        color="experience_level",
        title="Salary Distribution Across Experience Levels"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
**Business Insight**

• Salary variability increases with experience level.

• Executive positions show both the highest salaries and the widest salary range.

• Entry-level salaries remain relatively consistent compared to senior positions.
""")

    st.success("""
### 📌 Salary Analysis Summary

✔ Executive professionals receive the highest salaries.

✔ Large companies generally pay more than medium and small organizations.

✔ AI Specialist and Machine Learning Engineer are among the highest-paying roles.

✔ Consulting is the highest-paying industry.

✔ Switzerland leads in average AI salaries globally.

✔ Salary increases steadily with experience and specialization.
""")
# =========================
# GEOGRAPHIC ANALYSIS
# =========================

elif page == "Geographic Analysis":

    st.title("🌍 Geographic Analysis")
    st.markdown("""
    Explore AI hiring trends, salary patterns and workforce distribution
    across different countries.
    """)

    st.divider()

    # =====================
    # KPI CARDS
    # =====================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Countries", df["company_location"].nunique())
    c2.metric("Highest Salary", f"${df['salary_usd'].max():,.0f}")
    c3.metric("Average Salary", f"${df['salary_usd'].mean():,.0f}")
    c4.metric("Remote Categories", df["remote_ratio"].nunique())

    st.divider()

    # =====================
    # Top Hiring Countries
    # =====================

    st.subheader("🌎 Top 10 Hiring Countries")

    hiring = (
        df["company_location"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    hiring.columns = ["Country", "Jobs"]

    fig = px.bar(
        hiring,
        x="Country",
        y="Jobs",
        color="Jobs",
        text="Jobs",
        title="Top Countries by Number of AI Jobs"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
### Business Insight

• Germany has the highest number of AI job opportunities.

• Denmark, France and Canada are also major AI hiring hubs.

• AI recruitment is expanding across multiple developed economies.
""")

    st.divider()

    # =====================
    # Highest Paying Countries
    # =====================

    st.subheader("💰 Highest Paying Countries")

    salary_country = (
        df.groupby("company_location")["salary_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        salary_country,
        x="company_location",
        y="salary_usd",
        color="salary_usd",
        text_auto=".2s",
        title="Top 10 Countries by Average Salary"
    )

    fig.update_layout(xaxis_tickangle=-25)

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
### Business Insight

• Switzerland provides the highest average salary.

• Denmark and Norway also provide excellent salary packages.

• Developed countries continue to lead in AI compensation.
""")

    st.divider()

    # =====================
    # Salary by Country
    # =====================

    st.subheader("📈 Salary Comparison by Country")

    fig = px.box(
        df,
        x="company_location",
        y="salary_usd",
        color="company_location",
        points=False
    )

    fig.update_layout(
        xaxis_tickangle=-60,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
### Business Insight

• Salary distributions differ significantly across countries.

• Some countries have wider salary ranges due to varying experience levels and industries.

• AI professionals can identify countries offering better earning potential.
""")

    st.divider()

    # =====================
    # Remote Work Distribution
    # =====================

    st.subheader("🏠 Remote Work Distribution")

    remote = (
        df["remote_ratio"]
        .value_counts()
        .reset_index()
    )

    remote.columns = ["Remote Ratio", "Count"]

    fig = px.pie(
        remote,
        names="Remote Ratio",
        values="Count",
        hole=0.45,
        title="Remote Work Availability"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
### Business Insight

• The dataset includes fully remote, hybrid and on-site jobs.

• Organizations are increasingly adopting flexible work arrangements.

• Remote work has become an important factor in AI recruitment.
""")

    st.divider()

    # =====================
    # Education Requirement
    # =====================

    st.subheader("🎓 Education Requirement Distribution")

    edu = (
        df["education_required"]
        .value_counts()
        .reset_index()
    )

    edu.columns = ["Education", "Count"]

    fig = px.bar(
        edu,
        x="Education",
        y="Count",
        color="Count",
        text="Count",
        title="Education Requirements"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
### Business Insight

• Most AI roles require Bachelor's or Master's degrees.

• Advanced education is preferred for research and leadership positions.

• Educational qualifications remain an important hiring criterion.
""")

    st.divider()

    # =====================
    # Country Hiring Pie
    # =====================

    st.subheader("🌍 Top Hiring Countries Share")

    fig = px.pie(
        hiring,
        values="Jobs",
        names="Country",
        hole=0.55,
        title="Share of Top Hiring Countries"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("""
### 📌 Geographic Analysis Summary

✔ Germany leads in AI hiring.

✔ Switzerland offers the highest salaries.

✔ Developed countries dominate AI employment.

✔ Remote work opportunities are widely available.

✔ Higher education plays a significant role in AI recruitment.
""")
# =========================
# ADVANCED ANALYTICS
# =========================

elif page == "Advanced Analytics":

    st.title("📊 Advanced Analytics")

    st.markdown("""
    Explore advanced analytical insights including salary distribution,
    correlation analysis, experience trends and interactive pivot tables.
    """)

    st.divider()

    # ======================================
    # KPI CARDS
    # ======================================

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Average Salary",f"${df['salary_usd'].mean():,.0f}")
    c2.metric("Median Salary",f"${df['salary_usd'].median():,.0f}")
    c3.metric("Salary Std",f"${df['salary_usd'].std():,.0f}")
    c4.metric("Remote Categories",df['remote_ratio'].nunique())

    st.divider()

    # ======================================
    # Salary Distribution
    # ======================================

    st.subheader("📈 Salary Distribution")

    fig = px.histogram(
        df,
        x="salary_usd",
        nbins=30,
        color_discrete_sequence=["royalblue"]
    )

    fig.update_layout(
        title="Distribution of AI Salaries"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
**Insight**

• Salary distribution is right-skewed.

• Most AI professionals earn within the middle salary range.

• Few executive positions receive significantly higher salaries.
""")

    st.divider()

    # ======================================
    # Box Plot
    # ======================================

    st.subheader("📦 Salary Spread")

    fig = px.box(
        df,
        y="salary_usd",
        color="experience_level"
    )

    fig.update_layout(
        title="Salary Spread Across Experience Levels"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
**Insight**

• Executive positions have the widest salary variation.

• Entry-level salaries are comparatively consistent.

• Higher experience generally leads to higher salaries.
""")

    st.divider()

    # ======================================
    # Correlation Heatmap
    # ======================================

    st.subheader("🔥 Correlation Heatmap")

    numeric = df.select_dtypes(include=np.number)

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Viridis"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
**Insight**

• Numerical features show weak-to-moderate correlations.

• Salary is influenced by multiple factors rather than one single variable.
""")

    st.divider()

    # ======================================
    # Salary vs Experience
    # ======================================

    st.subheader("📊 Experience vs Salary")

    fig = px.box(
        df,
        x="experience_level",
        y="salary_usd",
        color="experience_level"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
**Business Insight**

Executive professionals earn the highest salaries.

Salary steadily increases with experience level.
""")

    st.divider()

    # ======================================
    # Salary vs Company Size
    # ======================================

    st.subheader("🏢 Company Size vs Salary")

    fig = px.box(
        df,
        x="company_size",
        y="salary_usd",
        color="company_size"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
**Business Insight**

Large companies generally offer better salaries.

Medium companies remain highly competitive.
""")

    st.divider()

    # ======================================
    # Pivot Table
    # ======================================

    st.subheader("📋 Interactive Pivot Table")

    pivot = pd.pivot_table(
        df,
        values="salary_usd",
        index="experience_level",
        columns="company_size",
        aggfunc="mean"
    )

    st.dataframe(
        pivot.style.format("{:,.0f}"),
        use_container_width=True
    )

    st.info("""
Average salary is calculated for every combination of
experience level and company size.
""")

    st.divider()

    # ======================================
    # Salary Currency
    # ======================================

    st.subheader("💵 Salary Currency Distribution")

    currency = (
        df["salary_currency"]
        .value_counts()
        .reset_index()
    )

    currency.columns=["Currency","Count"]

    fig = px.pie(
        currency,
        values="Count",
        names="Currency",
        hole=.45
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
Most salaries are reported in USD.

EUR and GBP are also commonly used.
""")

    st.divider()

    # ======================================
    # Remote Work
    # ======================================

    st.subheader("🏠 Remote Work Analysis")

    remote = (
        df["remote_ratio"]
        .value_counts()
        .reset_index()
    )

    remote.columns=["Remote Ratio","Count"]

    fig = px.bar(
        remote,
        x="Remote Ratio",
        y="Count",
        color="Count",
        text="Count"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
AI companies increasingly support remote and hybrid work models.
""")

    st.success("""
### 📌 Advanced Analytics Summary

✔ Salary increases with experience.

✔ Large companies generally pay higher salaries.

✔ Executive professionals receive premium compensation.

✔ USD dominates salary reporting.

✔ Salary depends on multiple business factors rather than a single feature.
""")
# =========================
# INSIGHTS & CONCLUSION
# =========================

elif page == "Insights & Conclusion":

    st.title("📌 Insights & Conclusion")

    st.markdown("""
    This section summarizes the most important findings obtained from the
    AI Job Market analysis and provides recommendations for professionals,
    organizations and future AI job seekers.
    """)

    st.divider()

    # ====================================
    # Dashboard Summary
    # ====================================

    st.subheader("📊 Dashboard Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Jobs", len(df))
    col2.metric("Countries", df["company_location"].nunique())
    col3.metric("Industries", df["industry"].nunique())

    st.divider()

    # ====================================
    # Top Business Insights
    # ====================================

    st.subheader("💡 Top Business Insights")

    st.success("""
### 1️⃣ AI Job Demand

• Machine Learning Researcher is the most demanded AI role.

• AI Software Engineer and Machine Learning Engineer are also among the fastest growing roles.
""")

    st.success("""
### 2️⃣ Salary Insights

• Executive-level professionals receive the highest salaries.

• Salary consistently increases with experience level.
""")

    st.success("""
### 3️⃣ Company Insights

• Large companies generally provide higher salaries.

• Medium-sized companies contribute the highest hiring volume.
""")

    st.success("""
### 4️⃣ Industry Insights

• Consulting is the highest paying industry.

• Technology, Manufacturing and Finance also provide attractive compensation.
""")

    st.success("""
### 5️⃣ Geographic Insights

• Germany records the highest AI hiring.

• Switzerland provides the highest average salaries.

• Denmark and Norway are also among the highest paying countries.
""")

    st.success("""
### 6️⃣ Employment Trends

• Full-Time employment dominates the AI job market.

• Remote and Hybrid jobs continue to increase globally.
""")

    st.divider()

    # ====================================
    # Recommendations
    # ====================================

    st.subheader("🎯 Recommendations for Students")

    st.info("""
✔ Learn Python, SQL and Machine Learning.

✔ Build strong Data Science and AI projects.

✔ Develop communication and problem-solving skills.

✔ Earn AI certifications.

✔ Build an impressive GitHub portfolio.

✔ Practice interview questions regularly.
""")

    st.divider()

    st.subheader("🏢 Recommendations for Companies")

    st.info("""
✔ Continue investing in AI talent.

✔ Encourage flexible remote work.

✔ Provide employee upskilling programs.

✔ Offer competitive salary packages.

✔ Expand AI adoption across business operations.
""")

    st.divider()

    # ====================================
    # Future Scope
    # ====================================

    st.subheader("🚀 Future Scope")

    st.markdown("""
Future work may include:

- Predicting AI salaries using Machine Learning.
- Forecasting future AI job demand.
- Developing AI salary recommendation systems.
- Integrating real-time job portals.
- Creating interactive global AI maps.
- Building AI career recommendation applications.
""")

    st.divider()

    # ====================================
    # Final Conclusion
    # ====================================

    st.subheader("📖 Final Conclusion")

    st.write("""
The AI job market is experiencing rapid global growth with increasing
demand across multiple industries. Professionals possessing advanced
AI and Machine Learning skills receive significantly higher salaries,
particularly in developed countries.

Organizations continue to invest heavily in AI technologies, creating
excellent career opportunities for skilled professionals worldwide.

Overall, the analysis demonstrates that Artificial Intelligence remains
one of the most promising and rewarding career domains for the future.
""")

    st.balloons()

    st.success("""
## 🎉 Thank You!

### AI Job Market Dashboard

Prepared using:

✔ Python

✔ Pandas

✔ Plotly

✔ Streamlit

✔ Exploratory Data Analysis (EDA)

Thank you for exploring the AI Job Market Dashboard!
""")                              