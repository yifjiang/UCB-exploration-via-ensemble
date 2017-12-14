from gym.envs.registration import register

register(
    id='my_UpNDownNoFrameskip-v0',
    entry_point='my_UpNDown.UpNDown_env:my_UpNDownEnv',
#    kwargs={'game': 'up_n_down', 'obs_type': 'image', 'frameskip': 1, 'repeat_action_probability': 0.25},
    max_episode_steps = 4 * 100000,
    nondeterministic=False,
)
