import plotly.graph_objects as go 
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

data = pd.read_csv(r"C:\Users\Najuka\OneDrive\Study\Documents\Shadowfox\city_temperature_data.csv")
x = data['Longitude']
y = data['Latitude']
z = data['Temperature']

xi = np.linspace(x.min(),x.max(),100)
yi = np.linspace(y.min(),y.max(),100)

Xi, Yi = np.meshgrid(xi,yi)

Zi = griddata(
    (x,y),
    z,
    (Xi,Yi),
    method ='cubic'
)

fig = go.Figure(
    data = go.Contour(
        x = xi,
        y = yi,
        z = Zi,
        colorscale = "Blues",
        colorbar = dict(title= "Temperature")      
    )
)


fig.update_layout(
    title = "City Temperature",
    xaxis_title = "Longitude",
    yaxis_title = "Latitude"

)

fig.show()


