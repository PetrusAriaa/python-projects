import matplotlib.pyplot as plt
from statsmodels.api import qqplot_2samples
import pandas as pd

dataset = "department_store_dataset.csv"
store_data = pd.read_csv(dataset)

data1 = store_data["Margem Realizada"] # Achieved Gross Profit Margin by Salesman
data2 = store_data["Objetivo de Margem"] # Profit Margin Goal by Salesman

fig = qqplot_2samples(
    data1=data1,
    data2=data2,
    line='45',
    xlabel="Gross profit margin achieved",
    ylabel="profit margin goal")

plt.show()
