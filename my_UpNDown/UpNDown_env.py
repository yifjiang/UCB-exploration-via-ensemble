from gym.envs.atari.atari_env import AtariEnv
from gym import spaces
import numpy as np
class my_UpNDownEnv(AtariEnv):
    def __init__(self):
        super(my_UpNDownEnv, self).\
            __init__(game = 'up_n_down', obs_type = 'image', frameskip = 0)
        self.observation_space = spaces.Box(low = 0, high = 255, shape = (840, 160, 3))

    def _step(self, action):
        ob_list = np.array([])
        for i in range(4):
            observation, reward, done, info = \
                super(my_UpNDownEnv, self)._step(action)
            if i == 0:
                ob_list = observation
            else:
                ob_list = np.append(ob_list, observation, axis = 0)
            if done:
                break

        return ob_list, reward, done, info
