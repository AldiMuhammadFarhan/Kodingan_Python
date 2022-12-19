import matplotlib.pyplot as plt
import plotnine as p9
import pandas as pd
from plotnine import positions
from plotnine.positions.position import position

df_penduduk = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv")
df_inflasi = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/inflasi.csv")

p9.options.figure_size = (10, 3.6)
(p9.ggplot(data=df_penduduk)
 + p9.aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH', fill='JENIS KELAMIN')
 + p9.geom_col()
 + p9.coord_flip()
 + p9.labs(title='Jumlah penduduk per kabupaten/kota di DKI Jakarta (2013)',
           x='Kabupaten/Kota',
           y='Jumlah Penduduk')
 ).draw()
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()

p9.options.figure_size = (10, 3.6)
(p9.ggplot(data=df_penduduk[df_penduduk['NAMA KECAMATAN'] == 'CENGKARENG'])
 + p9.aes(x='NAMA KELURAHAN', y='JUMLAH', fill='JENIS KELAMIN')
 + p9.geom_col(position='position.dodge')
 + p9.coord_flip()
 + p9.labs(title='Jumlah penduduk per kelurahan di DKI Jakarta (2013)',
           x='Kelurahan', y='Jumlah Penduduk')
 ).draw()
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()
