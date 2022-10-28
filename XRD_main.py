from data_analysis import XRD


sample_name = "SUCROSE"
sample_name_2 = "STARCH"
sample_name_3 = "ZIRCON"
file_path = f'data/XRD/{sample_name}.PRN'
file_path_2 = f'data/XRD/{sample_name_2}.PRN'
file_path_3 = f'data/XRD/{sample_name_3}.PRN'
sucrose_xrd = XRD(file_path,
                  sample_name= sample_name,
                  smoothing_option= True,
                  baseline_corr_option=  True,
                  peak_prominence= 500)
sucrose_xrd.plot_multiple_plots(file_path_2, file_path_3,
                                sample2 = sample_name_2, sample3 = sample_name_3)
# sucrose_xrd.plot_with_peaks()

# sample_name = "STARCH"
# file_path = f'data/XRD/{sample_name}.PRN'
# sucrose_xrd = XRD(file_path,
#                   sample_name= sample_name,
#                   smoothing_option= True,
#                   baseline_corr_option=  True,
#                   peak_prominence= 50)
# sucrose_xrd.plot_with_peaks()

# sample_name = "SUCROSE"
# file_path = f'data/XRD/{sample_name}.PRN'
# sucrose_xrd = XRD(file_path,
#                   sample_name= sample_name,
#                   smoothing_option= False,
#                   baseline_corr_option=  False,
#                   peak_prominence= 6000)
# sucrose_xrd.plot_with_peaks()