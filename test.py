#Lawson Lay
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#Are average video game sales going up over time?

#Lets drop all titles with NA for some fields
#Lets add together duplicate titles on multiple different consoles to create a df without Platforms

df = pd.read_csv("vgsales.csv", usecols=["Rank", "Name", "Platform", "Year", "Genre", "Publisher", "NA_Sales"])
cleanedDF = df.dropna()

salesDF = cleanedDF["NA_Sales"]

print(f"Mean:{salesDF.mean()}")
print(f"Median:{salesDF.median()}")
print(f"Min:{salesDF.min()}, Max:{salesDF.max()}")
print(f"StdDev:{salesDF.std()}")

uniqueYears = cleanedDF["Year"].sort_values().unique()

bestSellingPerYearDF = pd.DataFrame()

for x in uniqueYears:
    yearDF = cleanedDF.query(f"Year == {x}")
    maxNA_SalesForYear = yearDF["NA_Sales"].max()
    rowWithBestSellingGameForYear = yearDF.query(f"NA_Sales == {maxNA_SalesForYear}")
    bestSellingPerYearDF = pd.concat([bestSellingPerYearDF, rowWithBestSellingGameForYear], ignore_index=True)

bestSellingPerYearDF = bestSellingPerYearDF.reindex(columns=["Year", "Name", "Rank", "Platform", "Genre", "Publisher", "NA_Sales"])

#Lets remove the Platform and combine duplicates
noPlatformDuplicatesDF = pd.DataFrame()
allDuplicatesDF = cleanedDF[cleanedDF.duplicated("Name", keep=False)].sort_values("Name").reindex(columns=["Year", "Name", "Rank", "Genre", "Publisher", "NA_Sales"])
for name, group in allDuplicatesDF.groupby("Name"):
    newNonDuplicateRow = pd.DataFrame(
        {
        "Year" : [group["Year"].min()],
        "Name" : [name],
        "Rank" : [group["Rank"].min()],
        "Genre": [group["Genre"].min()],
        "Publisher": [group["Publisher"].min()],
        "NA_Sales": [group["NA_Sales"].sum()]
        },
        index=[1]
    )
    noPlatformDuplicatesDF = pd.concat([noPlatformDuplicatesDF, newNonDuplicateRow], ignore_index=True)

tempDF = cleanedDF.drop_duplicates(subset=["Name"], keep=False)
tempDF = tempDF.drop(columns=["Platform"])
noPlatformDF = pd.concat([noPlatformDuplicatesDF, tempDF], ignore_index=True)
noPlatformDF.to_csv("output.csv", index=False)


#print(bestSellingPerYearDF)

#Correlation Test
#x:Year y:NA_Sales

# a, b = np.polyfit(cleanedDF["Year"], cleanedDF["NA_Sales"], 1)
# y_fit = a * cleanedDF["Year"] + b

# cleanedDF.plot.scatter("Year", "NA_Sales")
# plt.plot(cleanedDF["Year"], y_fit, color="red", label="LOBF")



#plt.show()