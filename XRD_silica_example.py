import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(filepath_or_buffer='data/XRD/SILICA.PRN',
                  index_col= None,
                  header=None,
                 names= ['theta_2','intensity'],
                  sep= "\s+|;|:",
                  engine= 'python')


axis_label_fontsize = 12.5
fig = plt.figure(figsize=(10,4.8), dpi=500)
ax = fig.add_subplot(1,1,1)
ax.plot(df['theta_2'], df['intensity'], linewidth = 0.5)
ax.set_xlabel(r'2$\theta$ [degrees]', fontsize = axis_label_fontsize, weight = 'bold')
ax.set_ylabel('intensity [a.u.]', fontsize = axis_label_fontsize, weight = 'bold')
ax.set_title('XRD of silica', fontsize = 15,weight = 'bold')
plt.show()