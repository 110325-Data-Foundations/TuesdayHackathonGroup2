import pandas as pd
import matplotlib.pyplot as plt

def run(df):
    clean_df = df.dropna()
    jp_sales_groupby_genre(clean_df)
    print()
    corr_jp_sales_to_other(clean_df)

def corr_jp_sales_to_other(df):
    correlation = df['Other_Sales'].corr(df['JP_Sales'])
    print("=" * 70)
    print(f"Correlation between Other_Sales and JP_Sales: {correlation:.4f}")


def jp_sales_groupby_genre(df):
    jp_sales_by_genre = df.groupby('Genre')['JP_Sales'].agg([
        ('Total_Sales', 'sum'),
        ('Average_Sales', 'mean'),
        ('Number_of_Games', 'count'),
        ('Max_Sales', 'max'),
        ('Median_Sales', 'median')
    ]).sort_values('Total_Sales', ascending=False).round(5)

    print("Japanese Sales by Genre:")
    print("=" * 70)
    print(jp_sales_by_genre)
    print("=" * 70)

    jp_sales_by_genre['Percentage'] = (jp_sales_by_genre['Total_Sales']/ jp_sales_by_genre['Total_Sales'].sum() *100)
    print()
    print("Genre preferences (% of total JP sales):")
    print(jp_sales_by_genre[['Total_Sales', 'Percentage']].round(2))

    print("Plotting data")
    plt.figure(figsize=(12,6))
    plt.xlabel('Genre')
    plt.ylabel('Total JP Sales (in millions)')
    plt.title('Total Japan Sales by Genre')
    plt.bar(jp_sales_by_genre.index, jp_sales_by_genre['Total_Sales'])    

    #Pie chart
    plt.figure()
    plt.title('Sales Percentage by Genre in Japan')
    y_pie = jp_sales_by_genre['Total_Sales']
    pie_labels = jp_sales_by_genre.index
    plt.pie(y_pie, labels = pie_labels )


if __name__ == "__main__":
    df = pd.read_csv("vgsales.csv")
    run(df)
    plt.show()