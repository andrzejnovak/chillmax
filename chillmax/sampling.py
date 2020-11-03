import numpy as np
import matplotlib.pyplot as plt
import chillmax as cm
import scipy
from scipy.signal import chirp, find_peaks, peak_widths

def get_spans(cfg, freq=(21, 24), plot=False, size_parameter=0.5):
    if len(freq) != 2:
        freqs = freq  # passed linspace i guess
    else:
        freqs = np.linspace(freq[0], freq[1], 2000)

    boost = cm.sim.boost(freqs * 1e9, spacings=cfg)

    if plot:
        fig, axs = plt.subplots(figsize=(7, 5))
        axs.plot(freqs, boost)

    peaks, _ = find_peaks(boost, prominence=np.max(boost) * 0.1)
    results_full = peak_widths(boost, peaks, rel_height=0.98)

    if peaks.size==0:
        return 0

    if plot:
        axs.plot(freqs[peaks], boost[peaks], "x", label="Peaks")

    def find(peak, freqs, size_parameter):
        rmin, rmax = np.floor(peak[0]).astype(int), np.ceil(peak[1]).astype(int)
        fmin, fmax = freqs[rmin], freqs[rmax]
        scale = 0.1
        size = fmax - fmin
        extra = max(0.005, size * size_parameter)
        return fmin - extra, fmax + extra

    peaks = np.array(results_full[2:]).T
    spans = []
    for i, peak in enumerate(peaks):
        if plot:
            axs.axvspan(*find(peak, freqs, size_parameter), alpha=0.5, label=f'Peak {i}', color=f'C{i}')
        spans.append(find(peak, freqs, size_parameter))

    np.min(np.array(spans))

    if plot:
        axs.legend()
        plt.xlim(np.min(np.array(spans)), np.max(np.array(spans)))
    return np.array(spans)


def get_spans_overlap(spans):
    sorted_by_lower_bound = sorted(spans, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return np.array(merged)


def find_sampling(spans, bounds=(21, 24)):
    """Find sampling for each peak span passed.

    Parameters
    ----------
    spans : list
        List of spans in which to find sampling
    bounds : tuple, optional
        Boundaries for baseline sampling, by default (21, 24)

    Returns
    -------
    2D array
        arays of sampling points for each span
    """
    pts = []
    for i, span in enumerate(spans):
        pts.append(np.linspace(*span, 200))
    pts.append(np.arange(*bounds, 0.1))
    return np.sort(np.hstack(pts), kind='heapsort')


def find_split_sampling(spans, cfgs):
    """Find sampling for each peak span passed.

    Parameters
    ----------
    spans : 2D arrays or list of arrays
        Peak spans
    cfgs : 2D arrays or list of arrays
        Disk configurations

    Returns
    -------
    tuple(sampling points, matched configs)
    """
    pts = []
    for i, span in enumerate(spans):
        pts.append(np.linspace(*span, 200))
    cfgs = np.tile(cfgs, (len(pts), 1))
    return np.array(pts), cfgs
