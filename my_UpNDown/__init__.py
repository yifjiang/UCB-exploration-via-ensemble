from gym.envs.registration import register

register(
    id='my_UpNDownEnv-v0',
    entry_point='my_UpNDown.UpNDown_env:my_UpNDownEnv',
)
