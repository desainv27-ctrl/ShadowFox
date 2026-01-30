import pandas as pd
import plotly.express as px

data = pd.read_csv("Sentiment.csv")
fig = px.box(
    data,
    x="sentiment_label",
    y="compound",
    title="Distribution of VADER Compound Scores by Sentiment Category",
    labels={
        "sentiment_label": "Sentiment Category",
        "compound": "VADER Compound Score"
    }
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

fig.show()