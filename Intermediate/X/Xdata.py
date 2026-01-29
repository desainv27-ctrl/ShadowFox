import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#load a database
data = pd.read_csv(r"C:\Users\Najuka\OneDrive\Study\Documents\Shadowfox\Xdata.csv")

#drop a empty cells 
data = data.dropna(subset = ["clean_text"])
data = data.reset_index(drop = True)

analyzer = SentimentIntensityAnalyzer()

compound_scores = []
data[['negative', 'neutral', 'positive', 'compound']] = data['clean_text'].apply(lambda x: pd.Series(analyzer.polarity_scores(x)))

# Optional: create a label based on compound
def get_label(score):
    if score >= 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

data['sentiment_label'] = data['compound'].apply(get_label)


print(data.head())
#save the file
data.to_csv("Sentiment.csv")


