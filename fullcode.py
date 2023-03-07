import pandas as pd
import numpy as np

""" READING IN THE DATA """


s = "% Severe Housing Problems"
t = "% Insufficient Sleep"
u = "Graduation Rate"
dfs = []
link = "data_20"
#link = "https://github.com/sz1204/hunt-institute-datathon-s23/blob/main/data_20"
for i in range(16,23):
    df = pd.read_csv(link+str(i)+".csv")
    dfs.append(df.fillna(df.mean()))
    
    #county_list = ["Cherokee", "Graham", "Clay", "Polk", "Yancey", "Alleghany", "Caswell", "Warren", "Greene", "Bladen", "Hyde", "Tyrrell"]
    #county_list = ["Buncombe", "Gaston", "Cabarrus", "Catawba", "Guilford", "Alamance", "Orange", "Cumberland"]
    #county_list = ["Mecklenburg", "Forsyth", "Durham", "Wake", "New Hanover"]
    #county_list = ['Alexander', 'Anson', 'Ashe', 'Avery', 'Beaufort', 'Bertie', 'Brunswick', 'Burke', 'Caldwell', 'Camden', 'Carteret', 'Chatham', 'Chowan', 'Cleveland', 'Columbus', 'Craven', 'Currituck', 'Dare', 'Davidson', 'Davie', 'Duplin', 'Edgecombe', 'Franklin', 'Gates', 'Granville', 'Halifax', 'Harnett', 'Haywood', 'Henderson', 'Hertford', 'Hoke', 'Iredell', 'Jackson', 'Johnston', 'Jones', 'Lee', 'Lenoir', 'Lincoln', 'Macon', 'Madison', 'Martin', 'McDowell', 'Mitchell', 'Montgomery', 'Moore', 'Nash', 'Northampton', 'Onslow', 'Pamlico', 'Pasquotank', 'Pender', 'Perquimans', 'Person', 'Pitt', 'Randolph', 'Richmond', 'Robeson', 'Rockingham', 'Rowan', 'Rutherford', 'Sampson', 'Scotland', 'Stanly', 'Stokes', 'Surry', 'Swain', 'Transylvania', 'Union', 'Vance', 'Washington', 'Watauga', 'Wayne', 'Wilkes', 'Wilson', 'Yadkin']
    # create a boolean mask to filter the rows in the dataframe
    #mask = df["County"].isin(county_list)

    # apply the mask to the dataframe
    #filtered_df = df[mask]
    
    #dfs.append(filtered_df.fillna(filtered_df.mean()))


""" MAKE LINE CHART """

s = "% Severe Housing Problems"
x = [2016,2017,2018,2019,2020,2021,2022]

counties = []

for i in dfs:
    counties.append(i[s].tolist())


import matplotlib.pyplot as plt

original_list = counties
transposed_list = list(zip(*original_list))

print(original_list)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposed_list)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# Loop through each sub-list in the main list and plot it as a line
for line in transposed_list:
    plt.plot(x,line)


# Set the axis labels and title
plt.xlabel('Year')
plt.ylabel(s)
plt.title("Housing Issues Through the Years")

# Display the chart
plt.show()

s = "% Severe Housing Problems"
t = "% Insufficient Sleep"
u = "Graduation Rate"

plt.scatter(dfs[1][s],dfs[1][u])

plt.xlabel(s)
plt.ylabel(u)
plt.title(s+" vs. "+u)



#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(dfs[1][s].tolist(), dfs[1][u].tolist(), 1)

#add linear regression line to scatterplot 
plt.plot(dfs[1][s], m*dfs[1][s]+b)
plt.show()

plt.scatter(dfs[1][t],dfs[1][u])

plt.xlabel(t)
plt.ylabel(u)
plt.title(t+" vs. "+u)



#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(dfs[1][t].tolist(), dfs[1][u].tolist(), 1)

#add linear regression line to scatterplot 
plt.plot(dfs[1][t], m*dfs[1][t]+b)
plt.show()

df = dfs[1]

corr_matrix = df.corr()

# sort the matrix and extract the top 10 correlations
top_correlations = corr_matrix.unstack().sort_values(ascending=False)[:1000]

# print the top correlations and associated variable names if variables are different
for i in range(0, len(top_correlations), 2):
    #print("here")
    var1 = top_correlations.index[i][0]
    var2 = top_correlations.index[i][1]
    correlation = top_correlations[i]
    if var1 != var2:
        continue
        #print(f"{var1} and {var2}: {correlation}")



# calculate the correlation matrix
corr_matrix = df.corr()

oof = "% Insufficient Sleep"

# get the correlations associated with "Graduation Rate"
grad_rate_correlations = corr_matrix[oof].sort_values(ascending=False)

# print the correlations associated with "Graduation Rate"
for variable, correlation in grad_rate_correlations.iteritems():
    if variable != oof:
        print(f"{oof} and {variable}: {correlation}")

co = []
w = 1
for i in dfs[1:]:
    list1 = i[oof].tolist()
    if(w<4):
        list2 = i["Graduation Rate"]
    else:
        list2 = i["High School Graduation Rate"]
    correlation_matrix = np.corrcoef(list1, list2)
    correlation = correlation_matrix[0,1]
    co.append(correlation)
    w+=1

counties = []

for i in dfs:
    counties.append(i[s].tolist())


import matplotlib.pyplot as plt

original_list = counties
transposed_list = list(zip(*original_list))

print(original_list)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposed_list)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

""" PLOTTING CORRELATION THROUGHOUT THE YEARS  """


cos = [co[0],co[2],+co[5]]

# Loop through each sub-list in the main list and plot it as a line
#for line in transposed_list:
#    plt.plot(line)

plt.plot([2016,2018,2021],cos)
# Set the axis labels and title
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Line Chart')

# Display the chart
plt.show()
