import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sb

df = pd.read_csv("vgsales.csv")
#print(df)
#print(df.info())


#clean data
df = df.dropna()
#print(df.info())

#basic info
print(f"Global Sales Mean: {df["Global_Sales"].mean()}\n")
print(f"Global Sales Median: {df["Global_Sales"].median()}\n")
print(f"Global Sales Mode: {df["Global_Sales"].mode()}\n")

#All general correlations
#print(df.corr(numeric_only=True))

#Get rid of other sales columns -> focus on global sales
df.drop(columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], axis=1, inplace=True)

#Setting up genre compares to global sales
df_genre_compare = df.drop(columns=['Rank', 'Name', 'Platform', 'Year', 'Publisher'], axis=1, inplace=False)
df_genre_compare = pd.get_dummies(df_genre_compare, columns=['Genre'], drop_first=True)

#Print comparisons of global sales to genres platform and misc
print(f"Platform Genre Corr: \n{df_genre_compare['Global_Sales'].corr(df_genre_compare['Genre_Platform'])}\n")
print(f"Misc Genre Corr: \n{df_genre_compare['Global_Sales'].corr(df_genre_compare['Genre_Misc'])}\n")


#Show boxplot - groupby separates the data in specified columns, performs a function (mean in this case) and merges the data back together
df.groupby("Genre")["Global_Sales"].mean().sort_values()
plot = sb.boxplot(data=df, x="Genre", y="Global_Sales")
mpl.show()