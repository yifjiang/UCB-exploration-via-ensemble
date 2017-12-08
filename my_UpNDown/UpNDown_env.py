from gym.envs.atari.atari_env import AtariEnv
import numpy as np
class my_UpNDownEnv(AtariEnv):

    def __init__(self):
        super(my_UpNDownEnv, self).\
            __init__(game = 'up_n_down', obs_type = 'image', frameskip = 0)

    def _step(self, action):
        ob_list = np.array([])
        for i in range(4):
            observation, reward, done, info = \
                super(my_UpNDownEnv, self)._step(action)
            if i == 0:
                ob_list = observation
            else:
                ob_list = np.append(ob_list, observation, axis = 0)

        return ob_list, reward, done, info
