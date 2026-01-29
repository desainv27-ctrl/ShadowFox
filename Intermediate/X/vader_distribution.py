import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Sentiment.csv")

sentiment_counts = data["sentiment_label"].value_counts()

plt.figure()
sentiment_counts.plot(kind="bar")
plt.title("VADER Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.show()