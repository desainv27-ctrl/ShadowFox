
import plotly.express as px

scores = [65, 70, 75, 80, 85, 90, 95, 100]
groups = ["A", "A", "A","A", "B", "B", "B", "B"]

fig = px.box(
    x = groups,
    y = scores,
    title = "MATCH",
    labels = {
        "x" : "Team",
        "y" : "Score"
    }
)
fig.show()



