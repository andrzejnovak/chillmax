import numpy as np
from chillmax.Analytical1D import disk_system


def boost(freqs=None, spacings=None):
    """Generate boost factor curve

    Args:
        freqs (float, array): [Freqency or array of frequencies (GHz)]
        spacings (array): [Array of disk spacings]

    Returns:
        [array]: [Boost factor]
    """
    if freqs is None:
        freqs = np.linspace(22, 22.05, 20) * 1e9

    # if isinstance(freqs, float):
    #     freqs = np.array(freqs) * 1e9
    # else:
    #     freqs = freqs * 1e9

    if spacings is None:
        spacings = (
            np.array(
                [
                    1.00334,
                    6.94754,
                    7.1766,
                    7.22788,
                    7.19717,
                    7.23776,
                    7.07746,
                    7.57173,
                    7.08019,
                    7.24657,
                    7.21708,
                    7.18317,
                    7.13025,
                    7.2198,
                    7.45585,
                    7.39873,
                    7.15403,
                    7.14252,
                    6.83105,
                    7.42282,
                ]
            )
            * 1e-3
        )

    # print("X", freqs)
    # print("Y", spacings)

    ref, ax = disk_system(
        freqs,
        tand=0,
        num_disk=len(spacings) - 1,
        disk_thickness=0.001,
        disk_epsilon=24,
        mirror=True,
        spacings=spacings,
    )
    return abs(ax)**2


def generate():
    pass
