import matplotlib.pyplot as plt
import plotnine as p9
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')

(p9.ggplot(data=df_penduduk)
+ p9.aes(x='LUAS WILAYAH (KM2)', y='stat(count/max(count))')
+ p9.geom_histogram()
).draw()
plt.show()