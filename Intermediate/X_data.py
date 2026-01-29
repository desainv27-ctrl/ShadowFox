import pandas as pd
import numpy as np
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
#load a dataset
data = pd.read_csv(r"C:\Users\Najuka\OneDrive\Study\Documents\Shadowfox\Xdata.csv")

data = data.dropna(subset=["clean_text"]).reset_index(drop=True)

# Load model & tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create sentiment pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer,
    truncation=True
)

# Apply sentiment analysis
results = sentiment_pipeline(data["clean_text"].tolist())

# Extract labels and scores
data["hf_sentiment"] = [r["label"] for r in results]
data["hf_score"] = [r["score"] for r in results]

print(data.head())

