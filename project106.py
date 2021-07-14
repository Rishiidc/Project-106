import pandas as pd
import plotly.express as pex
import numpy as np

data = pd.read_csv("data1.csv")
graph1 = pex.scatter(data, x = "Roll No", y = "Marks In Percentage")
correlation = np.corrcoef(data["Roll No"],data["Marks In Percentage"])

data1 = pd.read_csv("data2.csv")
graph2 = pex.scatter(data1, x = "week", y = "Coffee in ml") 
correlation2 = np.corrcoef(data1["week"], data1["Coffee in ml"])

print(correlation)
print(correlation2)
graph1.show()
graph2.show()