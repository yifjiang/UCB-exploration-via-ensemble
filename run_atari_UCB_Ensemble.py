import gym

from UCB_Ensemble import models
from UCB_Ensemble import simple
from UCB_Ensemble import wrap_atari_dqn
from baselines.common import set_global_seeds
from baselines import bench
import argparse
from baselines import logger
from baselines.common.atari_wrappers import make_atari
import my_UpNDown

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--env', help='environment ID', default='my_UpNDownNoFrameskip-v0')
    parser.add_argument('--seed', help='RNG seed', type=int, default=0)
    parser.add_argument('--prioritized', type=int, default=1)
    parser.add_argument('--dueling', type=int, default=1)
    parser.add_argument('--num-timesteps', type=int, default=int(1e7))
    parser.add_argument('--exploration_weight', type=float, default=float(1))
    args = parser.parse_args()
    logger.configure()
    set_global_seeds(args.seed)
    env = make_atari(args.env)
    env = bench.Monitor(env, logger.get_dir())
    env = wrap_atari_dqn(env)
    model = models.cnn_to_mlp(
        convs=[(32, 8, 4), (64, 4, 2), (64, 3, 1)],
        hiddens=[256],
        dueling=bool(args.dueling),
    )
    act = simple.learn(
        env,
        batch_size=32,
        q_func=model,
        lr=1e-4,
        max_timesteps=args.num_timesteps,
        buffer_size=10000,
        train_freq=1,
        learning_starts=10000,
        target_network_update_freq=10000,
        gamma=0.99,
        prioritized_replay=bool(args.prioritized),
        exploration_weight=args.exploration_weight
    )
    env.close()


if __name__ == '__main__':
    main()
