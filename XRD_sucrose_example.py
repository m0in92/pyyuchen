import matplotlib.pyplot as plt
from XRD_helper_funcs import load_csv_files, smoothing_alg, find_XRD_peaks


file_path = 'data/XRD/SUCROSE.PRN'
df = load_csv_files(file_path= file_path)

df['baseline_corr_intensity'] = smoothing_alg(df['intensity'])
theta_2_peak_values, intensity_peak_values = find_XRD_peaks(df)

axis_label_fontsize = 12.5
fig = plt.figure(figsize=(1.2*6.8,1.2*4.8), dpi=100)
ax1 = fig.add_subplot(1,1,1) # ax1 is for the original plot
ax1.plot(df['theta_2'], df['intensity'], linewidth = 3)
ax1.set_xlabel(r'2$\theta$ [degrees]', fontsize = axis_label_fontsize, weight = 'bold')
ax1.set_ylabel('intensity [a.u.]', fontsize = axis_label_fontsize, weight = 'bold')
ax1.set_title('XRD of sucrose', fontsize = 15,weight = 'bold')
# ax1.scatter(theta_2_peak_values, intensity_peak_values, s=200, marker = 'x', color="red")
for i, txt in enumerate(theta_2_peak_values):
    ax1.annotate(txt, (theta_2_peak_values[i], intensity_peak_values[i]),
                 textcoords='offset points', xytext=(30, 0),
                 arrowprops=dict(arrowstyle="->, head_width = 0.3",
                                 color='red', lw=1.5,
                                 connectionstyle = "angle",
                                 relpos=(0, 0)),
                 bbox=dict(pad= 1, facecolor="none", edgecolor="none"),
                 horizontalalignment = 'center', verticalalignment = 'center',
                 fontsize = 10, weight = 'bold')
    # ax1.text(theta_2_peak_values[i], intensity_peak_values[i], theta_2_peak_values[i],
    #          fontsize = 10, weight = 'bold')
plt.grid(linestyle = '--')
plt.show()