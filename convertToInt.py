import pandas as pd

data = pd.read_csv("WFH_WFO_dataset.csv")
gender = {'Male': 1, 'Female': 0}
calm = {'CALMER': 1, 'STRESSED': 0}
digital = {'Yes': 1, 'No': 0, 'yes':1, 'no':0}
occupation = {'Tutor':1, 'HR':2, 'Engineer':3, 'Recruiter':4, 'Business':5, 'Marketing ':6,'Manager':7}
# money = {'Yes':1, 'No':0}
# sleep = {'Yes':1, 'No':0}
# time = {'Yes': 1, 'No': 0}

data.Gender = [gender[item] for item in data.Gender]
data.calmer_stressed = [calm[item] for item in data.calmer_stressed]
data.digital_connect_sufficient = [digital[item] for item in data.digital_connect_sufficient]
data.RM_save_money = [digital[item] for item in data.RM_save_money]
data.RM_better_sleep = [digital[item] for item in data.RM_better_sleep]
data.RM_quality_time = [digital[item] for item in data.RM_quality_time]
data.kids = [digital[item] for item in data.kids]
df['Occupation'] = [occupation[item] for item in df['Occupation']]
df['Same_ofiice_home_location'] = [digital[item] for item in df['Same_ofiice_home_location']]

data.to_csv("WFH_WFO_dataset_pre.csv", index=False)
