import matplotlib.pyplot as plt
import plotnine as p9
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')

(p9.ggplot(data=df_penduduk)
+ p9.aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
+ p9.geom_boxplot()
+ p9.coord_flip()
).draw()
plt.tight_layout()
plt.show()