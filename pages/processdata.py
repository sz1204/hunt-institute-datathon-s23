import pandas as pd

import os
# assign directory
directory = 'data'
filenames = []
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        filenames.append(f)


dfs = []
dfs2 = []
for file in filenames:
    df = pd.read_excel(file, sheet_name = 3, skiprows=[0])
    dfs.append(df)
    df = pd.read_excel(file, sheet_name = 4, skiprows=[0])
    dfs2.append(df)
    


merged_data = []
for i in range(len(dfs)):
    #mergedf = pd.merge(dfs[i],dfs2[i],on="FIPS")
    #mergedf = dfs[i].join(dfs2[i],lsuffix="_x",rsuffix="_y")
    mergedf = pd.concat([dfs[i],dfs2[i]],axis=1,join='outer')
    merged_data.append(mergedf)



final_merged = []
cols_to_keep = ["% Fair/Poor", "Mentally Unhealthy Days", "Physically Unhealthy Days", "MHP Rate", "PCP Rate", "Graduation Rate", "% Some College", "% Unemployed", "Income Ratio", "% Severe Housing Problems"]
cols_to_keep = cols_to_keep+["% African American","% American Indian/ Alaskan Native","% Asian","% Native Hawaiian/ Other Pacific Islander","% Hispanic","% Non-Hispanic white","% Insufficient Sleep"]
# Drop all columns except the ones in the list

#keep_cols = [9,19,80,14,72,102,106,112,121,
for i in merged_data[:5]:
    i = i.drop(columns=[col for col in i.columns if col not in cols_to_keep])
    final_merged.append(i)

cols_to_keep = ["% Fair or Poor Health","Average Number of Mentally Unhealthy Days","Average Number of Physically Unhealthy Days","Mental Health Provider Rate","Primary Care Physicians Rate","High School Graduation Rate","% Some College","% Unemployed","Income Ratio","% Severe Housing Problems"]
cols_to_keep = cols_to_keep+["Population","% less than 18 years of age","% Rural"]+["% Black", "% American Indian & Alaska Native", "% Asian", "% Native Hawaiian/Other Pacific Islander", "% Hispanic", "% Non-Hispanic White","% Insufficient Sleep"]

i = merged_data[5].drop(columns=[col for col in merged_data[5].columns if col not in cols_to_keep])
final_merged.append(i)

for i in merged_data[6:]:
    i = i.drop(columns=[col for col in i.columns if col not in cols_to_keep])
    final_merged.append(i)

year = 2015

for i in merged_data:
    i.to_csv("data_"+str(year)+".csv")
    year+=1


    
