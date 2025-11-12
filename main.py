import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import sys

import na_sales as na
import jp_sales as jp
import eu_sales as eu
import global_sales as gl

if __name__ == "__main__":
    df = pd.read_csv("vgsales.csv")

    og_stdout = sys.stdout

    with open("output.txt", "w") as file:
        sys.stdout = file

        print("North America")
        na.run(df)
        print()
        print()
        print()
        print()
        print("Japan")
        jp.run(df)
        print()
        print()
        print()
        print()
        print("Europe")
        eu.run(df)
        print()
        print()
        print()
        print()
        print("Global")
        gl.run(df)

        plt.show()
    
    sys.stdout = og_stdout

