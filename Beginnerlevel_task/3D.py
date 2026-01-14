import plotly.express as px

x = [1, 5, 9]
y = [2, 6, 10]
z = [3, 7, 11]

fig = px.scatter_3d(
    x=x,
    y=y,
    z=z,
    size=[10, 20, 30],   
    color=[1, 2, 3],     
    title= "3D Scatter Plot"
)

fig.show()
