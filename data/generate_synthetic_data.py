import pandas as pd
import numpy as np

# seed for reproducibility
np.random.seed(123)

# list of countries
countries = [
    # East Asia
    "China",
    "Japan",  
    "South Korea",
    "Taiwan", 
    # Southeast Asia
    "Cambodia",
    "Laos",
    "Thailand",
    "Vietnam",
    "Indonesia",
    "Malaysia",  
    "Philippines",
    "Singapore",
]

# subjectively define general characteristics  
# for each country to guide synthetic data generation
country_profiles = {
    "China": {
        # general
        "id": 1,
        "iso_code": "CHN",
        "region": "East Asia",
        "population": 1439.7,
        # cost
        "avg_doctor_visit_cost": (10, 30),
        "avg_hospital_stay_day_cost": (50, 150),
        # health risk
        "dengue_risk": ["low", "medium"], 
        "malaria_risk": ["none", "low"], 
        "covid_risk": ["low", "medium"],
        # healthcare access
        "hospital_beds_per_1000": (4.0, 5.0), 
        "doctors_per_1000": (2.0, 2.4), 
        "emergency_quality_index": 70,
        # insurance options
        "avg_plan_monthly_cost": (100, 300), 
        "evacuation_prob": 0.4
    },
    "Japan": {
        # general
        "id": 2,
        "iso_code": "JPN",
        "region": "East Asia",
        "population": 124.2,
        # cost
        "avg_doctor_visit_cost": (50, 100), 
        "avg_hospital_stay_day_cost": (150, 400),
        # health risk
        "dengue_risk": ["low", "medium"], 
        "malaria_risk": ["none", "low"], 
        "covid_risk": ["low"],
        # healthcare access
        "hospital_beds_per_1000": (12.0, 14.0), 
        "doctors_per_1000": (2.4, 2.7), 
        "emergency_quality_index": 85,
        # insurance options
        "avg_plan_monthly_cost": (250, 500), 
        "evacuation_prob": 0.7
    },
    "South Korea": {
        # general
        "id": 3,
        "iso_code": "KOR",
        "region": "East Asia",
        "population": 51.8,
        # cost
        "avg_doctor_visit_cost": (20, 60), 
        "avg_hospital_stay_day_cost": (100, 300),
        # health risk
        "dengue_risk": ["low"], 
        "malaria_risk": ["none", "low"], 
        "covid_risk": ["low"],
        # healthcare access
        "hospital_beds_per_1000": (11.0, 13.0), 
        "doctors_per_1000": (2.3, 2.6), 
        "emergency_quality_index": 80,
        # insurance options
        "avg_plan_monthly_cost": (150, 350), 
        "evacuation_prob": 0.6
    },
    "Taiwan": {
        # general
        "id": 4,
        "iso_code": "TWN",
        "region": "East Asia",
        "population": 23.9,
        # cost
        "avg_doctor_visit_cost": (20, 50), 
        "avg_hospital_stay_day_cost": (80, 200),
        # health risk
        "dengue_risk": ["low", "medium"], 
        "malaria_risk": ["none"], 
        "covid_risk": ["low"],
        # healthcare access
        "hospital_beds_per_1000": (4.0, 7.0), 
        "doctors_per_1000": (1.9, 2.5), 
        "emergency_quality_index": 75,
        # insurance options
        "avg_plan_monthly_cost": (120, 320), 
        "evacuation_prob": 0.5
    },
    "Cambodia": {
        # general
        "id": 5,
        "iso_code": "KHM",
        "region": "Southeast Asia",
        "population": 17.4,
        # cost
        "avg_doctor_visit_cost": (10, 50), 
        "avg_hospital_stay_day_cost": (30, 70),
        # health risk
        "dengue_risk": ["high"], 
        "malaria_risk": ["medium", "high"], 
        "covid_risk": ["medium", "high"],
        # healthcare access
        "hospital_beds_per_1000": (0.7, 1.0), 
        "doctors_per_1000": (0.2, 0.5), 
        "emergency_quality_index": 25,
        # insurance options
        "avg_plan_monthly_cost": (20, 70), 
        "evacuation_prob": 0.05
    },
    "Laos": {
        # general
        "id": 6,
        "iso_code": "LAO",
        "region": "Southeast Asia",
        "population": 7.8,
        # cost
        "avg_doctor_visit_cost": (15, 30), 
        "avg_hospital_stay_day_cost": (30, 100),
        # health risk
        "dengue_risk": ["high"], 
        "malaria_risk": ["medium", "high"], 
        "covid_risk": ["medium", "high"],
        # healthcare access
        "hospital_beds_per_1000": (1.3, 1.7), 
        "doctors_per_1000": (0.3, 0.6), 
        "emergency_quality_index": 30,
        # insurance options
        "avg_plan_monthly_cost": (25, 80), 
        "evacuation_prob": 0.05
    },
    "Thailand": {
        # general
        "id": 7,
        "iso_code": "THA",
        "region": "Southeast Asia",
        "population": 70.3,
        # cost
        "avg_doctor_visit_cost": (20, 45), 
        "avg_hospital_stay_day_cost": (70, 150),
        # health risk
        "dengue_risk": ["medium", "high"], 
        "malaria_risk": ["low", "medium"], 
        "covid_risk": ["medium"],
        # healthcare access
        "hospital_beds_per_1000": (2.2, 2.8), 
        "doctors_per_1000": (0.7, 1.1), 
        "emergency_quality_index": 60,
        # insurance options
        "avg_plan_monthly_cost": (50, 125), 
        "evacuation_prob": 0.4
    },
    "Vietnam": {
        # general
        "id": 8,
        "iso_code": "VNM",
        "region": "Southeast Asia",
        "population": 102.2,
        # cost
        "avg_doctor_visit_cost": (15, 40), 
        "avg_hospital_stay_day_cost": (50, 150),
        # health risk
        "dengue_risk": ["high"], 
        "malaria_risk": ["low", "medium"], 
        "covid_risk": ["medium"],
        # healthcare access
        "hospital_beds_per_1000": (2.4, 3.0), 
        "doctors_per_1000": (0.8, 1.2), 
        "emergency_quality_index": 50,
        # insurance options
        "avg_plan_monthly_cost": (40, 120), 
        "evacuation_prob": 0.2
    },
    "Indonesia": {
        # general
        "id": 9,
        "iso_code": "IDN",
        "region": "Southeast Asia",
        "population": 279.5,
        # cost
        "avg_doctor_visit_cost": (30, 90), 
        "avg_hospital_stay_day_cost": (40, 120),
        # health risk
        "dengue_risk": ["high"], 
        "malaria_risk": ["medium", "high"], 
        "covid_risk": ["medium", "high"],
        # healthcare access
        "hospital_beds_per_1000": (0.9, 1.3), 
        "doctors_per_1000": (0.4, 0.7), 
        "emergency_quality_index": 35,
        # insurance options
        "avg_plan_monthly_cost": (30, 100), 
        "evacuation_prob": 0.1
    },
    "Malaysia": {
        # general
        "id": 10,
        "iso_code": "MYS",
        "region": "Southeast Asia",
        "population": 33.9,
        # cost
        "avg_doctor_visit_cost": (15, 50), 
        "avg_hospital_stay_day_cost": (70, 150),
        # health risk
        "dengue_risk": ["medium","high"], 
        "malaria_risk": ["low", "medium"], 
        "covid_risk": ["medium"],
        # healthcare access
        "hospital_beds_per_1000": (1.8, 2.2), 
        "doctors_per_1000": (1.8, 2.2), 
        "emergency_quality_index": 65,
        # insurance options
        "avg_plan_monthly_cost": (70, 200), 
        "evacuation_prob": 0.3
    },
    "Philippines": {
        # general
        "id": 11,
        "iso_code": "PHL",
        "region": "Southeast Asia",
        "population": 114.4,
        # cost
        "avg_doctor_visit_cost": (20, 60), 
        "avg_hospital_stay_day_cost": (50, 150),
        # health risk
        "dengue_risk": ["high"], 
        "malaria_risk": ["low", "medium"], 
        "covid_risk": ["medium", "high"],
        # healthcare access
        "hospital_beds_per_1000": (0.8, 1.2), 
        "doctors_per_1000": (0.6, 1.4), 
        "emergency_quality_index": 45,
        # insurance options
        "avg_plan_monthly_cost": (50, 150), 
        "evacuation_prob": 0.25
    },
    "Singapore": {
        # general
        "id": 12,
        "iso_code": "SGP",
        "region": "Southeast Asia",
        "population": 5.8,
        # cost
        "avg_doctor_visit_cost": (50, 150), 
        "avg_hospital_stay_day_cost": (200, 600),
        # health risk
        "dengue_risk": ["medium", "high"], 
        "malaria_risk": ["none"], 
        "covid_risk": ["low"],
        # healthcare access
        "hospital_beds_per_1000": (2.2, 2.8), 
        "doctors_per_1000": (2.3, 2.7), 
        "emergency_quality_index": 90,
        # insurance options
        "avg_plan_monthly_cost": (300, 600), 
        "evacuation_prob": 0.8
    },
}

# generate synthetic data
# dimRisk
dimRisk = []
dimRisk.append({
    "id": 1,
    "risk": "none"
})
dimRisk.append({
    "id": 2,
    "risk": "low"
})
dimRisk.append({
    "id": 3,
    "risk": "medium"
})
dimRisk.append({
    "id": 4,
    "risk": "high"
})
df_dimRisk = pd.DataFrame(dimRisk)
df_dimRisk.to_csv("dim_risk.csv", index=False)

# dimCoverage
dimCoverage = []
dimCoverage.append({
    "id": 1,
    "coverage_level": "basic"
})
dimCoverage.append({
    "id": 2,
    "coverage_level": "standard"
})
dimCoverage.append({
    "id": 3,
    "coverage_level": "comprehensive"
})
df_dimCoverage = pd.DataFrame(dimCoverage)
df_dimCoverage.to_csv("dim_coverage.csv", index=False)

# dimRegion
dimRegion = []
dimRegion.append({
    "id": 1,
    "region": "East Asia"
})
dimRegion.append({
    "id": 2,
    "region": "Southeast Asia"
})
df_dimRegion = pd.DataFrame(dimRegion)
df_dimRegion.to_csv("dim_region.csv", index=False)

# dimCountry
dimCountry = []
for country in countries:
    profile = country_profiles[country]

    # get region id
    if profile["region"]=="East Asia":
        region_id = [region["id"] for region in dimRegion if region["region"]=="East Asia"][0]
    elif profile["region"]=="Southeast Asia":
        region_id = [region["id"] for region in dimRegion if region["region"]=="Southeast Asia"][0] 
    else:
        region_id = 999999

    # populate dim table
    dimCountry.append({
        "id": profile["id"],
        "country": country,
        "iso_code": profile["iso_code"],
        "region_id": region_id,
    })
df_dimCountry = pd.DataFrame(dimCountry)
df_dimCountry.to_csv("dim_country.csv", index=False)

# fact
fact = []
for country in countries:
    profile = country_profiles[country]

    #########################################
    # cost
    doc_visit_lower, doc_visit_upper = profile["avg_doctor_visit_cost"]
    hosp_stay_lower, hosp_stay_upper = profile["avg_hospital_stay_day_cost"]

    avg_doctor_visit_cost = np.random.randint(doc_visit_lower, doc_visit_upper+1)
    avg_hospital_stay_day_cost = np.random.randint(hosp_stay_lower, hosp_stay_upper+1)

    # create a health cost index that loosely correlates with the above two costs
    # normalize cost to a 0-1 scale for rough calculation, then scale to 10-100
    # say, max possible doctor visit is 150, max hospital stay is 600
    norm_doc_visit = avg_doctor_visit_cost/150
    norm_hosp_stay = avg_hospital_stay_day_cost/600
    
    # weighted average, giving more weight to hospital stay as it's generally a larger expense
    # index will be between 0 and 1 initially with this weighting
    base_index = (0.4*norm_doc_visit + 0.6*norm_hosp_stay) 
    
    # scale to 10-100 range: min base_index could be around 0.05, max around 1.0
    health_cost_index = int(10 + base_index*90)
    
    # add some randomness to the index as well
    health_cost_index += np.random.randint(-5, 6)
    # ensure it stays within 10-100
    health_cost_index = max(10, min(100, health_cost_index)) 
    #########################################

    #########################################
    # health risk
    dengue_risk = np.random.choice(profile["dengue_risk"])
    malaria_risk = np.random.choice(profile["malaria_risk"])
    covid_risk = np.random.choice(profile["covid_risk"])

    dengue_risk_id = [risk["id"] for risk in dimRisk if risk["risk"]==dengue_risk][0] 
    malaria_risk_id = [risk["id"] for risk in dimRisk if risk["risk"]==malaria_risk][0] 
    covid_risk_id = [risk["id"] for risk in dimRisk if risk["risk"]==covid_risk][0] 
    #########################################

    #########################################
    # healthcare access
    hospital_beds_per_1000 = round(np.random.uniform(profile["hospital_beds_per_1000"][0], profile["hospital_beds_per_1000"][1]), 1)
    doctors_per_1000 = round(np.random.uniform(profile["doctors_per_1000"][0], profile["doctors_per_1000"][1]), 2)

    emergency_quality_index = np.random.randint(profile["emergency_quality_index"]-10, profile["emergency_quality_index"]+11)
    # ensure it stays within 10-100
    emergency_quality_index = max(10, min(100, emergency_quality_index)) 
    #########################################

    #########################################
    # insurance option
    plan_cost_lower, plan_cost_upper = profile["avg_plan_monthly_cost"]
    avg_plan_monthly_cost = np.random.randint(plan_cost_lower, plan_cost_upper+1)
    
    # determine coverage level based on avg_plan_monthly_cost
    # set arbitrary thresholds
    # upper third
    if avg_plan_monthly_cost > (plan_cost_lower + (plan_cost_upper-plan_cost_lower)*0.66):
        coverage_level = "comprehensive"
        coverage_level_id = [level["id"] for level in dimCoverage if level["coverage_level"]==coverage_level][0]
    # mid third
    elif avg_plan_monthly_cost > (plan_cost_lower + (plan_cost_upper-plan_cost_lower)*0.33): 
        coverage_level = "standard"
        coverage_level_id = [level["id"] for level in dimCoverage if level["coverage_level"]==coverage_level][0]
    # lower third
    else:
        coverage_level = "basic"   
        coverage_level_id = [level["id"] for level in dimCoverage if level["coverage_level"]==coverage_level][0]

    # determine include_evacuation based on probability and coverage level
    evacuation_prob_actual = profile["evacuation_prob"]
    # higher chance if comprehensive
    if coverage_level == "comprehensive":
        evacuation_prob_actual += 0.2 
    # lower chance if basic
    elif coverage_level == "basic":
        evacuation_prob_actual -= 0.15 
    include_evacuation = 1 if np.random.rand() < max(0.01, min(0.99, evacuation_prob_actual)) else 0
    #########################################

    #########################################
    # load fact table
    fact.append({
        "country_id": profile["id"],
        "population": profile["population"],
        "avg_doctor_visit_cost": avg_doctor_visit_cost,
        "avg_hospital_stay_day_cost": avg_hospital_stay_day_cost,
        "health_cost_index": health_cost_index,
        "dengue_risk_id": dengue_risk_id,
        "malaria_risk_id": malaria_risk_id,
        "covid_risk_id": covid_risk_id,
        "hospital_beds_per_1000": hospital_beds_per_1000,
        "doctors_per_1000": doctors_per_1000,
        "emergency_quality_index": emergency_quality_index,
        "avg_plan_monthly_cost": avg_plan_monthly_cost,
        "coverage_level_id": coverage_level_id,
        "include_evacuation": include_evacuation
    })

df_fact = pd.DataFrame(fact)
df_fact.to_csv("fact.csv", index=False)

# QC check
print("\nFirst 5 rows of the generated data:")
print(df_fact.head())
print("\nData Information:")
df_fact.info()
print("\nDescriptive Statistics (for numerical columns):")
print(df_fact.describe())
print("\nValue counts for categorical columns:")
for col in [
    "dengue_risk_id",
    "malaria_risk_id",
    "covid_risk_id",
    "coverage_level_id",
    "include_evacuation"
]:
    print(f"\n{col}:")
    print(df_fact[col].value_counts())