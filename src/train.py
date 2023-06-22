from stable_baselines3 import PPO

import gymnasium as gym
import malware_gym

env = gym.make("malware-v0")
print("env:", env)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000, progress_bar=True)
model.save("../models/ppo_malware")
