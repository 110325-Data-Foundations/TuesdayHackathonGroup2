import pandas
import matplotlib.pyplot as plt

#2 Load Data

CSV = pandas.read_csv('vgsales.csv')

print(CSV.head())

#3 Clean Data

clean_CSV = CSV.dropna() # Drops NaN values

print(clean_CSV)

#4.1 Summary Stats

mean_sales = CSV['JP_Sales'].mean()

print(f"Mean Sales: {mean_sales}")

avg_sales_per_publisher = CSV.groupby('Publisher')['Global_Sales'].mean()

print(avg_sales_per_publisher)

#4.2 Correlation

year_JP_Sales_correlation = CSV[['Year','JP_Sales']].corr() 

print(year_JP_Sales_correlation) # Closer to 1, postive. Closer to -1, negative. Around 0, no relationship.

#5 Filter and Extract

filtered_CSV = CSV[CSV["Year"]>2005] # Remove all games made in or before 2005

print(filtered_CSV)

#6 Visualization (Matplotlib)

# Average Global Sales per Publisher (Top 10)
top_publishers = avg_sales_per_publisher.sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_publishers.plot(kind='bar', color='green')
plt.title('Top 10 Publishers by Average Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Average Global Sales (millions)')
plt.show()
