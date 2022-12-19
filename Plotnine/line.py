import matplotlib.pyplot as plt
import plotnine as p9
import pandas as pd 
df_inflasi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/inflasi.csv')

(p9.ggplot(data=df_inflasi)
+ p9.aes(x='Bulan', y='Inflasi', color='Negara')
+ p9.geom_line()
+ p9.theme(figure_size=(10, 5))
).draw()
plt.show()