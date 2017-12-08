import gym
import my_UpNDown

env = gym.make('my_UpNDownEnv-v0').unwrapped
print(env.observation_space.shape)
