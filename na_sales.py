#Lawson Lay 11/11/25

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def printBasicStats_NA(cleanedDF):
    salesDF = cleanedDF["NA_Sales"]
    print()
    print("Video Game Sales in North America Basic Stats")
    print(f"Mean:{salesDF.mean():.3f}")
    print(f"Median:{salesDF.median():.3f}")
    print(f"Min:{salesDF.min()}, Max:{salesDF.max():.3f}")
    print(f"StdDev:{salesDF.std():.3f}")

def removePlatformDuplicates_NA(cleanedDF):
    #No Duplicate Games
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

    return noPlatformDF
    #noPlatformDF.to_csv("output.csv", index=False)

def bestSellingGamePerYear_NA(cleanedDF):
    #Best Selling Game per Year
    uniqueYears = cleanedDF["Year"].sort_values().unique()
    bestSellingPerYearDF = pd.DataFrame()
    for x in uniqueYears:
        yearDF = cleanedDF.query(f"Year == {x}")
        maxNA_SalesForYear = yearDF["NA_Sales"].max()
        rowWithBestSellingGameForYear = yearDF.query(f"NA_Sales == {maxNA_SalesForYear}")
        bestSellingPerYearDF = pd.concat([bestSellingPerYearDF, rowWithBestSellingGameForYear], ignore_index=True)

    bestSellingPerYearDF = bestSellingPerYearDF.reindex(columns=["Year", "Name", "Rank", "Platform", "Genre", "Publisher", "NA_Sales"])
    print()
    print("Best Selling Video Game per Year in North America with Platforms")
    print(bestSellingPerYearDF)

def bestSellingGamePerYear_NoPlatform_NA(noPlatformDF):
    #Best Selling Game per Year without Platforms
    uniqueYears = noPlatformDF["Year"].sort_values().unique()
    bestSellingPerYearNoPlatformDF = pd.DataFrame()
    for x in uniqueYears:
        yearDF = noPlatformDF.query(f"Year == {x}")
        maxNA_SalesForYear = yearDF["NA_Sales"].max()
        rowWithBestSellingGameForYear = yearDF.query(f"NA_Sales == {maxNA_SalesForYear}")
        bestSellingPerYearNoPlatformDF = pd.concat([bestSellingPerYearNoPlatformDF, rowWithBestSellingGameForYear], ignore_index=True)

    bestSellingPerYearNoPlatformDF = bestSellingPerYearNoPlatformDF.reindex(columns=["Year", "Name", "Rank", "Genre", "Publisher", "NA_Sales"])
    print()
    print("Best Selling Video Game per Year in North America")
    print(bestSellingPerYearNoPlatformDF)


def plotBarYearVSales_NoPlatform_NA(noPlatformDF):
    #Are average video game sales going up over time in NA?
    #x: Year y: NA_Sales
    #For each unique year, add together all NA_Sales
    yearVsNASalesDF = pd.DataFrame()

    tempDF = noPlatformDF.reindex(columns=["Year", "NA_Sales"])
    for name, group in tempDF.groupby("Year"):
        newNonDuplicateRow = pd.DataFrame(
            {
            "Year" : [group["Year"].min()],
            "NA_Sales": [group["NA_Sales"].sum()]
            },
            index=[1]
        )
        yearVsNASalesDF = pd.concat([yearVsNASalesDF, newNonDuplicateRow], ignore_index=True)

    yearVsNASalesDF.plot.bar(x="Year",y="NA_Sales",title="Total Game Sales per Year")


def corrAllSales(cleanedDF):
    #Correlation Matrix between Sales in different regions
    df2 = cleanedDF.reindex(columns=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
    print()
    print("Correlation Coefficients between Region Sales")
    print(df2.corr())

def avgSalesPerGenre_NoPlatform_NA(noPlatformDF):
    #Average Mean Sales per Genre in NA
    avgNASalesPerGenreDF = pd.DataFrame()

    tempDF = noPlatformDF.reindex(columns=["Genre", "NA_Sales"])
    for name, group in tempDF.groupby("Genre"):
        newNonDuplicateRow = pd.DataFrame(
            {
            "Genre" : [group["Genre"].min()],
            "NA_Sales": [group["NA_Sales"].mean()]
            },
            index=[1]
        )
        avgNASalesPerGenreDF = pd.concat([avgNASalesPerGenreDF, newNonDuplicateRow], ignore_index=True)
    print()
    print("Average Sales per Genre in North America")
    print(avgNASalesPerGenreDF)

def bestSellingGame_NA(cleanedDF):
    #Best Selling game in NA with Platform
    maxNA_Sales = cleanedDF["NA_Sales"].max()
    rowWithMaxNA_Sales = cleanedDF.query(f"NA_Sales == {maxNA_Sales}")
    print()
    print("Best Selling Game in North America")
    print(rowWithMaxNA_Sales)

def cleanSales(df):
    cleanedDF = df.dropna()
    cleanedDF["Year"] = cleanedDF["Year"].astype(int)
    return cleanedDF

def run(df):
    pd.options.mode.chained_assignment = None
    cleanedDF = cleanSales(df)
    
    printBasicStats_NA(cleanedDF)
    noPlatformDF = removePlatformDuplicates_NA(cleanedDF)
    bestSellingGamePerYear_NoPlatform_NA(noPlatformDF)
    bestSellingGame_NA(cleanedDF)
    plotBarYearVSales_NoPlatform_NA(noPlatformDF)
    corrAllSales(cleanedDF)
    avgSalesPerGenre_NoPlatform_NA(noPlatformDF)

    #plt.show()

if __name__ == "__main__":
    df = pd.read_csv("vgsales.csv")
    run(df)