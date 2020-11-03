import numpy as np
from chillmax.Analytical1D import disk_system
from chillmax.sim import boost


def test_boost():
    frequencies = np.linspace(22, 22.05, 10) * 1e9

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

    ref, ax = disk_system(
        frequencies,
        tand=0,
        num_disk=19,
        disk_epsilon=24,
        mirror=True,
        spacings=spacings,
    )

    boost = abs(ax * ax)
    target = np.array(
        [
            1124.09238126,
            4812.00518748,
            70174.37858119,
            30235.07430247,
            6398.26703308,
            2977.98507494,
            1824.50789595,
            1280.588185,
            973.30813528,
            778.93087653,
        ]
    )
    assert np.prod(np.isclose(boost, target)).astype(bool)


def test_boost2():
    boost()
