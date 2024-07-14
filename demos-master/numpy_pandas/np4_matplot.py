import numpy as np
from matplotlib import pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

plt.title("Matplotlib demo")
plt.xlabel("Days")
plt.ylabel("Steps Walked")
plt.plot(days, steps_walked, color='green', marker='o',
         linestyle='dashed', linewidth=2, markersize=12)
plt.show()
