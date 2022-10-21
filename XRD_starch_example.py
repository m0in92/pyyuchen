import matplotlib.pyplot as plt
from XRD_helper_funcs import load_csv_files, smoothing_alg


file_path = 'data/XRD/STARCH.PRN'
df = load_csv_files(file_path= file_path)

df['baseline_corr_intensity'] = smoothing_alg(df['intensity'])

axis_label_fontsize = 12.5
fig = plt.figure(figsize=(6.8,10), dpi=100)
ax1 = fig.add_subplot(2,1,1) # ax1 is for the original plot
ax1.plot(df['theta_2'], df['intensity'], linewidth = 3)
ax1.set_xlabel(r'2$\theta$ [degrees]', fontsize = axis_label_fontsize, weight = 'bold')
ax1.set_ylabel('intensity [a.u.]', fontsize = axis_label_fontsize, weight = 'bold')
ax1.set_title('XRD of starch original data', fontsize = 15,weight = 'bold')

ax2 = fig.add_subplot(2,1,2) # ax2 is for the smoothed intensity plot
ax2.plot(df['theta_2'], df['baseline_corr_intensity'], linewidth = 3)
ax2.set_xlabel(r'2$\theta$ [degrees]', fontsize = axis_label_fontsize, weight = 'bold')
ax2.set_ylabel('intensity [a.u.]', fontsize = axis_label_fontsize, weight = 'bold')
ax2.set_title('XRD of starch w. smoothing', fontsize = 15,weight = 'bold')
plt.tight_layout()
plt.show()