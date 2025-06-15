# 🌍 Travel Insurance Dashboard

This dashboard helps travelers compare health risks, medical costs, and insurance cost estimates across countries using synthetic data. Originally built in Power BI, it was later recreated in Tableau.

## ✨ Key Features  
- Side-by-side comparison of two countries
- Insurance cost estimator based on selected risk tolerance
- Interactive slicers and what-if parameters
- Star schema data model built with synthetic data

## 📁 Main Files
- `travel_insurance_dashboard.pbix` – Power BI report file
- `travel_insurance_dashboard_tableau.twb` – Tableau version of the same dashboard
- `data/generate_synthetic_data.py` – Python script for generating synthetic data
- `data/dim_region.csv` – Region dimension table 
- `data/dim_country.csv` – Country dimension table
- `data/dim_risk.csv` – Risk level dimension table
- `data/dim_coverage.csv` – Coverage level dimension table
- `data/facts.csv` – Fact table with healthcare and insurance data

## 📊 Sneak Peek  
Explore the interactive version here 👉 [View on Tableau](https://public.tableau.com/views/TravelInsuranceDashboard_17499991074090/Story?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### 🧭 Landing Page   
<img src="img/snapshot landing page.png" width="80%">

### 🆚 Side-by-Side Country Comparison   
<img src="img/side-by-side comparison page.png" width="80%"> 

### 💰 Cost Estimator (Risk Tolerance Selector)  
<img src="img/cost estimator page.png" width="80%"> 

Cost rises as users lower their risk tolerance (i.e., become more risk averse).  
<img src="img/cost estimator page example 1.png" width="40%"> <img src="img/cost estimator page example 2.png" width="40%"> 