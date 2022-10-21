from data_analysis import XRD


sample_name = "STARCH"
file_path = f'data/XRD/{sample_name}.PRN'
sucrose_xrd = XRD(file_path,
                  sample_name= sample_name,
                  smoothing_option= True,
                  baseline_corr_option=  True,
                  peak_prominence= 50)
sucrose_xrd.plot_with_peaks()