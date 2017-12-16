This repository includes two algorithms to run on atari environments.

# How to Run

Clone this repository:
```bash
git clone https://github.com/yifjiang/UCB-review.git
cd UCB-review
```
You may also need to install openai-gym and openai-baseline.

To run the UCB-ensemble algorithm, type:
```
python run_atari_UCB_Ensemble.py [--env $(AnAtariEnvironmentNoFrameSkip-v0)]
```

To run the Double-DQN algorithm, type:
```
python run_atari_double.py [--env $(AnAtariEnvironmentNoFrameSkip-v0)]
```

    @misc{baselines,
      author = {Hesse, Christopher and Plappert, Matthias and Radford, Alec and Schulman, John and Sidor, Szymon and Wu, Yuhuai},
      title = {OpenAI Baselines},
      year = {2017},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/openai/baselines}},
    }
