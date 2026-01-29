import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Sentiment.csv")

plt.figure()
plt.hist(data["compound"], bins=30)
plt.title("Distribution of VADER Compound Scores")
plt.xlabel("Compound Score")
plt.ylabel("Frequency")
plt.show()