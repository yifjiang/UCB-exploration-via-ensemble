import gym

from bootstrapped_DQN import models
from bootstrapped_DQN import simple
from bootstrapped_DQN import wrap_atari_dqn
from baselines.common import set_global_seeds
from baselines import bench
import argparse
from baselines import logger
from baselines.common.atari_wrappers import make_atari
import my_UpNDown

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--env', help='environment ID', default='CartPole-v0')
    parser.add_argument('--seed', help='RNG seed', type=int, default=0)
    parser.add_argument('--prioritized', type=int, default=1)
    parser.add_argument('--dueling', type=int, default=1)
    parser.add_argument('--num-timesteps', type=int, default=int(1e7))
    parser.add_argument('--exploration_weight', type=float, default=float(1))
    args = parser.parse_args()
    logger.configure()
    set_global_seeds(args.seed)
    env = gym.make(args.env)
    # env = bench.Monitor(env, logger.get_dir())
    # env = wrap_atari_dqn(env)
    model = models.cnn_to_mlp(
        convs=[],
        hiddens=[256],
        dueling=bool(args.dueling),
    )
    act = simple.learn(
        env,
        batch_size=32,
        # buffer_size=1000000,
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
    # act.save("pong_model.pkl") XXX
    env.close()


if __name__ == '__main__':
    main()
