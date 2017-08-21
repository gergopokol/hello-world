import pandas as pd
import os

os.chdir("A:\9github\hello-world\PH526XHWCS5")

birddata = pd.read_csv("bird_tracking.csv")
birddata.info()

import numpy as np
import matplotlib.pyplot as plt

ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]

plt.figure()
plt.plot(x, y, "b.")

bird_names = pd.unique(birddata.bird_name)
plt.figure()
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")