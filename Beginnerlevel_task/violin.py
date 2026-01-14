import plotly.express as px

scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
groups = ["Team 1", "Team 1", "Team 1", "Team 1",
           "Team 2", "Team 2","Team 2", "Team 2",
             "Team 3", "Team 3", "Team 3", "Team 3", ]


fig = px.violin(
    x = groups,
    y = scores,
    title = "MATCH",
    labels = {
        "x" : "Team",
        "y" : "Score"
    }
)


fig.update_layout(
    title={
        "x": 0.5,
        "xanchor": "center"
    }
)
fig.show()



