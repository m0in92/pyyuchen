import pandas as pd
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


class XRD:
    """
    Creator: Moin
    Contributors: Moin/
    """
    def __init__(self, file_path, sample_name,
                 smoothing_option = False,
                 baseline_corr_option = False,
                 peak_prominence  = 6000):
        self.file_path = file_path
        self.sample_name = sample_name
        self.baseline_corr_option = baseline_corr_option
        self.smoothing_option = smoothing_option
        self.theta_2, self.intensity = XRD.load_csv_files(self.file_path)
        if self.smoothing_option:
            self.intensity = XRD.smoothing_alg(self.intensity)
        if self.baseline_corr_option:
            self.intensity = self.intensity - XRD.baseline(self.intensity)
        self.peak_prominence = peak_prominence

    @staticmethod
    def load_csv_files(file_path):
        df = pd.read_csv(filepath_or_buffer=file_path,
                         index_col=None,
                         header=None,
                         names=['theta_2', 'intensity'],
                         sep="\s+|;|:",
                         engine='python')
        return df['theta_2'].to_numpy(), df['intensity'].to_numpy()

    @staticmethod
    def smoothing_alg(y, lam=10 ** 3, p=0.005, niter=10):
        """
        Source: https://stackoverflow.com/questions/29156532/python-baseline-correction-library
        """
        L = len(y)
        D = sparse.diags([1, -2, 1], [0, -1, -2], shape=(L, L - 2))
        w = np.ones(L)
        for i in range(niter):
            W = sparse.spdiags(w, 0, L, L)
            Z = W + lam * D.dot(D.transpose())
            z = spsolve(Z, w * y)
            w = p * (y > z) + (1 - p) * (y < z)
        return z

    @staticmethod
    def baseline(y):
        return XRD.smoothing_alg(y, lam=10**9, p = 0.005, niter=10)

    def find_peak_indices(self):
        return find_peaks(self.intensity, prominence= self.peak_prominence)

    @property
    def theta2_peak_values(self):
        peaks = self.find_peak_indices()
        return [self.theta_2[peak] for peak in peaks[0]]

    @property
    def intensity_peak_values(self):
        peaks = self.find_peak_indices()
        return [self.intensity[peak] for peak in peaks[0]]

    @staticmethod
    def scaled_intensity_values(intensity):
        return (intensity - np.min(intensity))/(np.max(intensity) - np.min(intensity))

    def simple_plot(self):
        axis_label_fontsize = 12.5
        fig = plt.figure(figsize=(1.2 * 6.8, 1.2 * 4.8), dpi=100)
        ax1 = fig.add_subplot(1, 1, 1)  # ax1 is for the original plot
        ax1.plot(self.theta_2, self.intensity, linewidth=3)
        ax1.set_xlabel(r'2$\theta$ [degrees]', fontsize=axis_label_fontsize, weight='bold')
        ax1.set_ylabel('intensity [a.u.]', fontsize=axis_label_fontsize, weight='bold')
        ax1.set_title(f'XRD of {self.sample_name}', fontsize=15, weight='bold')
        plt.grid(linestyle='--')
        plt.show()

    def plot_with_peaks(self):
        axis_label_fontsize = 12.5
        fig = plt.figure(figsize=(1.2 * 6.8, 1.2 * 4.8), dpi=100)
        ax1 = fig.add_subplot(1, 1, 1)  # ax1 is for the original plot
        ax1.plot(self.theta_2, self.intensity, linewidth=3)
        ax1.set_xlabel(r'2$\theta$ [degrees]', fontsize=axis_label_fontsize, weight='bold')
        ax1.set_ylabel('intensity [a.u.]', fontsize=axis_label_fontsize, weight='bold')
        ax1.set_title(f'XRD of {self.sample_name}', fontsize=15, weight='bold')
        for i, txt in enumerate(self.theta2_peak_values):
            ax1.annotate(txt, (self.theta2_peak_values[i], self.intensity_peak_values[i]),
                         textcoords='offset points', xytext=(30, 0),
                         arrowprops=dict(arrowstyle="->, head_width = 0.3",
                                         color='red', lw=1.5,
                                         connectionstyle="angle",
                                         relpos=(0, 0)),
                         bbox=dict(pad=1, facecolor="none", edgecolor="none"),
                         horizontalalignment='center', verticalalignment='center',
                         fontsize=10, weight='bold')
        plt.grid(linestyle='--')
        ax1.set_yticklabels([])
        ax1.tick_params('y', left = False)
        plt.show()

    def plot_multiple_plots(self, *file_paths, **sample_names):
        plot_color_list = ['red', 'black', 'cyan', 'green','orange']
        axis_label_fontsize = 12.5
        fig = plt.figure(figsize=(1.2 * 6.8, 1.2 * 4.8), dpi=100)
        ax1 = fig.add_subplot(1, 1, 1)  # ax1 is for the original plot
        ax1.plot(self.theta_2, XRD.scaled_intensity_values(self.intensity), linewidth=3, label=self.sample_name)
        ax1.set_xlabel(r'2$\theta$ [degrees]', fontsize=axis_label_fontsize, weight='bold')
        ax1.set_ylabel('intensity [a.u.]', fontsize=axis_label_fontsize, weight='bold')
        ax1.set_title(f'XRD of Various Samples', fontsize=15, weight='bold')
        for num_fig, (data_path, plot_color, sample_name) in enumerate(zip(file_paths, plot_color_list, sample_names.values())):
            x,y = XRD.load_csv_files(data_path)
            y = XRD.scaled_intensity_values(y)
            y = y + num_fig * 1.5 + 1.5
            ax1.plot(x, y, plot_color, linewidth = 3, label = sample_name)
        ax1.set_xlim(5,90)
        plt.grid(linestyle='--')
        ax1.set_yticklabels([])
        ax1.tick_params('y', left=False)
        ax1.legend(loc = 'upper right')
        plt.show()