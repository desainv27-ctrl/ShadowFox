import plotly.express as px
import pandas as pd
import numpy as np

file = pd.read_csv(r"C:\Users\Najuka\OneDrive\Study\Documents\Shadowfox\Website_visit.csv")

file_long = file.melt(id_vars ="Day", var_name = "Website",value_name = "Visits")

fig =  px.density_heatmap(
    file_long,
    x = "Website",
    y = "Day",
    z = "Visits",
    color_continuous_scale = "YlOrRd",
    title = "Weekly Website Visit Data"
)

fig.show()
