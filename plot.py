import sys
import matplotlib.pyplot as plt
import numpy as np
import pickle

file = open(sys.argv[1],'rb')
returns = pickle.load(file)
plt.plot(returns, label = "learning curve")
plt.legend()
plt.show()