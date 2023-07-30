import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image
plt.style.use('dark_background')

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.savefig('my_figure.png')
plt.show()
#Image('my_figure.png')