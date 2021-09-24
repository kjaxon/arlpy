import arlpy.uwapm as pm
import arlpy.plot as plt
import numpy as np


bathy = [
    [0, 30],    # 30 m water depth at the transmitter
    [300, 20],  # 20 m water depth 300 m away
    [1000, 25]  # 25 m water depth at 1 km
]

ssp = [
    [ 0, 1540],  # 1540 m/s at the surface
    [10, 1530],  # 1530 m/s at 10 m depth
    [20, 1532],  # 1532 m/s at 20 m depth
    [25, 1533],  # 1533 m/s at 25 m depth
    [30, 1535]   # 1535 m/s at the seabed
]

env = pm.create_env2d(
    depth=bathy,
    soundspeed=ssp,
    bottom_soundspeed=1450,
    bottom_density=1200,
    bottom_absorption=1.0,
    tx_depth=15
)

#env['rx_range'] = np.linspace(0, 1000, 1001)
#env['rx_depth'] = np.linspace(0, 30, 301)

pm.print_env(env)

#tloss = pm.compute_transmission_loss(env, mode='incoherent')

erays = pm.compute_eigenrays(env)
rays = pm.compute_rays(env, debug=True)
print(erays.ray)
open("/eigenValues.txt", 'w+')

#print(rays)
#pm.plot_rays(erays, env=env, width=1000)