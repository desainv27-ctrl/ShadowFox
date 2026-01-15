import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Najuka\Downloads\csvfile\studentdata.csv")
print(df)

df.plot( x = "StudentName", y = "GGA") 

plt.show()

