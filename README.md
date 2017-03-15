# First-Game-Bot
One of the simplest decision making problem is to balance a Pole straight either by moving left or right. In this, I have used OpenAI's Gym library to train a bot in the CartPole enviroment to get better over time via reinforcement learning.

# Dependecies
* Gym
* Numpy


# Installation
```
git clone https://github.com/openai/gym
cd gym
pip install -e gym[all]
```
# Usage

The ```CartPole_bot.py``` script is the bare minimum example of using OpenAI's Gym library. It will run an instance of the
CartPole-v0 enviroment for 1000 timestep, rendering the environment at each step.
I tried to solve the problem by:
1. Random Search
2. Hill-Climbing
```
python CartPole_bot.py Random_Search
```

In Hill-Climbing the script will start with some randomly chosen initial wieghts and in every episode, add some noise to the weights. Keep the new weights if the agent improves.
```
python CartPole_bot.py Hill_Climbing
```

# Credits & Future
I learnt this technique and code from this [article](http://kvfrans.com/simple-algoritms-for-solving-cartpole/).
I will shortly add Policy Gradient method to solve this problem.
