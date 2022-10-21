import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
import pandas as pd
from scipy.signal import find_peaks


def load_csv_files(file_path):
    df = pd.read_csv(filepath_or_buffer=file_path,
                     index_col=None,
                     header=None,
                     names=['theta_2', 'intensity'],
                     sep="\s+|;|:",
                     engine='python')
    return df


def smoothing_alg(y, lam = 10**3, p = 0.05, niter=10):
    """
    Source: https://stackoverflow.com/questions/29156532/python-baseline-correction-library
    """
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z

def find_XRD_peaks(df, prominence= 6000):
    peaks = find_peaks(df['intensity'], prominence= prominence)
    theta_2_peak_values = [df['theta_2'].iloc[peak] for peak in peaks[0]]
    intensity_peak_values = [df['intensity'].iloc[peak] for peak in peaks[0]]
    return theta_2_peak_values, intensity_peak_values
