import numpy as np
x = np.arange(0,3,0.1)
y = x**2

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y=x^2')
plt.show()
