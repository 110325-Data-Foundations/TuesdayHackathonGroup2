import pandas as pd
import matplotlib.pyplot as plt

def run(df):
    #2 Load Data

    CSV = df

    #print(CSV.head())

    #3 Clean Data

    clean_CSV = CSV.dropna() # Drops NaN values

    #print(clean_CSV)

    #4.1 Summary Stats

    mean_sales = CSV['EU_Sales'].mean()

    print(f"Mean Sales: {mean_sales}")

    avg_sales_per_publisher = CSV.groupby('Publisher')['EU_Sales'].mean()

    avg_sales_per_publisher = avg_sales_per_publisher.sort_values(ascending=False)

    print()
    print("Average Europe Sales per Publisher")
    print(avg_sales_per_publisher.head(10))

    #4.2 Correlation

    year_EU_Sales_correlation = CSV[['Year','EU_Sales']].corr() 
    
    print()
    print("Average Sales per Genre in Europe")
    print(year_EU_Sales_correlation) # Closer to 1, postive. Closer to -1, negative. Around 0, no relationship.

    #5 Filter and Extract

    filtered_CSV = CSV[CSV["Year"]>2005] # Remove all games made in or before 2005

    print()
    print("Removed all games made in or before 2005")
    print(filtered_CSV.head(10))

    #6 Visualization (Matplotlib)

    # Average Global Sales per Publisher (Top 10)
    top_publishers = avg_sales_per_publisher.sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    top_publishers.plot(kind='bar', color='green')
    plt.title('Top 10 Publishers by Average Global Sales')
    plt.xlabel('Publisher')
    plt.ylabel('Average Global Sales (millions)')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("vgsales.csv")
    run(df)