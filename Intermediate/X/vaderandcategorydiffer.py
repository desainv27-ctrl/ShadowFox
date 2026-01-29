import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("Sentiment.csv")

label_map = {
    -1 : "Negative",
    0 : "Netural",
    1: "Positive"
}
data ["true_label"] = data ["category"].map(label_map)

comparison_pct = (
    pd.crosstab(data["true_label"], data["sentiment_label"],normalize = "index")* 100

)
plt.figure()
plt.imshow(comparison_pct)
plt.title("Dataset Category VS VADER Sentiment")
plt.xlabel("VADER Sentiment")
plt.ylabel("Dataset Category")

plt.xticks(range(3), ["Negative", "Netural", "Positive"])
plt.yticks(range(3), ["Negative", "Netural", "Positive"])
plt.colorbar(label = "Percenatage")

for i in range (len(comparison_pct.index)):
    for j in range(len (comparison_pct.columns)):
        value = comparison_pct.iloc[i,j]
        plt.text(j,i, f"{value:.1f}%", ha = "center", va = "center")

plt.show()