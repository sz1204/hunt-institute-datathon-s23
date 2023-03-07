import pandas as pd
link = "https://raw.githubusercontent.com/sz1204/hunt-institute-datathon-s23/main/cleaned-data/data_20"

s = "% Uninsured"

dfs = []

for i in range(15,23):
    df = pd.read_csv(link+str(i)+".csv")
    dfs.append(df)


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
    plt.plot(line)

# Set the axis labels and title
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Line Chart')

# Display the chart
plt.show()