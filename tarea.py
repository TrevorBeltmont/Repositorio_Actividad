# %%
import numpy as np
import pandas as pd
import seaborn as sns

nombres = ["customer", "order","total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
# %%
print("Caja de bigotes", nombres[0])
sns.boxplot(x=nombres[0], data=df)
# %%
print("Histograma", nombres[0])
sns.histplot(x=nombres[0], data = df)
# %%
print("Caja de bigotes", nombres[1])
sns.boxplot(x=nombres[1], data=df)
# %%
print("Histograma", nombres[1])
sns.histplot(x=nombres[1], data = df)
# %%
print("Caja de bigotes", nombres[2])
sns.boxplot(x=nombres[2], data=df)
# %%
print("Histograma", nombres[2])
sns.histplot(x=nombres[2], data = df)
# %%
print("Caja de bigotes", nombres[3])
sns.boxplot(x=nombres[3], data=df)
# %%
print("Histograma", nombres[3])
sns.histplot(x=nombres[3], data = df)
# %%
print("Caja de bigotes", nombres[4])
sns.boxplot(x=nombres[4], data=df)
# %%
print("Histograma", nombres[4])
sns.histplot(x=nombres[4], data = df)
# %%
print("Caja de bigotes", nombres[5])
sns.boxplot(x=nombres[5], data=df)
# %%
print("Histograma", nombres[5])
sns.histplot(x=nombres[5], data = df)
# %%
print("Caja de bigotes", nombres[6])
sns.boxplot(x=nombres[6], data=df)
# %%
print("Histograma", nombres[6])
sns.histplot(x=nombres[6], data = df)
# %%
print("Caja de bigotes", nombres[7])
sns.boxplot(x=nombres[7], data=df)
# %%
print("Histograma", nombres[7])
sns.histplot(x=nombres[7], data = df)
# %%
print("Caja de bigotes", nombres[8])
sns.boxplot(x=nombres[8], data=df)
# %%
print("Histograma", nombres[8])
sns.histplot(x=nombres[8], data = df)
# %%
print("Caja de bigotes", nombres[9])
sns.boxplot(x=nombres[9], data=df)
# %%
print("Histograma", nombres[9])
sns.histplot(x=nombres[9], data = df)
# %%
print("Caja de bigotes", nombres[10])
sns.boxplot(x=nombres[10], data=df)
# %%
print("Histograma", nombres[10])
sns.histplot(x=nombres[10], data = df)
# %%
print("Caja de bigotes", nombres[11])
sns.boxplot(x=nombres[11], data=df)
# %%
print("Histograma", nombres[11])
sns.histplot(x=nombres[11], data = df)
# %%
print("Caja de bigotes", nombres[12])
sns.boxplot(x=nombres[12], data=df)
# %%
print("Histograma", nombres[12])
sns.histplot(x=nombres[12], data = df)
# %%
print("Caja de bigotes", nombres[13])
sns.boxplot(x=nombres[13], data=df)
# %%
print("Histograma", nombres[13])
sns.histplot(x=nombres[13], data = df)