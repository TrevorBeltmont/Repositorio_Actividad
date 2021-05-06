

# %%
import pandas as pd
import numpy as np
lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)
# %%
print(lista * 10)
#%%
print(nplista * 2)
#%%
print(pdlista * 2)
# %%
df = pd.read_csv("insurance.csv")
print(df)
# %%
df.head()
# %%
df.tail()
# %%
df.sample(10)
# %%
df.describe() # Estadística descriptiva
# %%
df.info()
# %%
df['age']
# %%
df[['age']]
# %%
df[['age']].head()
# %%
df[['age','bmi']].head()
# %%
df[['age','bmi']].info()
# %%
df[:3]
# %%
df.tail(3)
# %%
df[['age','bmi']].head(2)
# %%
df[10:11]
# %%
df.iloc[[10]]
# %%
