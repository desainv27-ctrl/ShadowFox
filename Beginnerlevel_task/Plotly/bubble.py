import plotly.express as px

x = [1, 2, 3, 4, 5]
y = [60, 70, 75, 85, 90]
size = [10, 20, 30, 40, 50]

fig = px.scatter(
    x=x,
    y=y,
    size=size,
    title="Bubble Plot Example",
    labels={"x": "Study Hours", "y": "Score"}
)
fig.update_layout(
    title={
        "x" : 0.5,
        "xanchor" :"center"
    }
)

fig.show()



