import sys
import matplotlib.pyplot as plt
import numpy as np
import pickle

file = open("./reward_stats.bin",'rb')
mean_frame100_rewards, mean_episode100_rewards, episode_rewards, frame_rewards = pickle.load(file)
l = []
l[0] = frame_rewards[0]
for i in range(1, len(frame_rewards)):
	l[i] = l[i-1] + frame_rewards[i]
plt.plot(l, label = "learning curve")
plt.legend()
plt.show()