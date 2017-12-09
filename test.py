import gym
import my_UpNDown

env = gym.make('my_UpNDownNoFrameskip-v0').unwrapped
ob, r, done, info = env.step(3)
print(env.observation_space)
