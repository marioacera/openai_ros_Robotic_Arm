
from openai_ros.task_envs.fetch import fetch_reach
import rospy
env = fetch_reach.FetchReachEnv()

from stable_baselines import HER, DQN, SAC, DDPG, TD3
from stable_baselines.her import GoalSelectionStrategy, HERGoalEnvWrapper

model_class = DDPG  # works also with SAC, DDPG and TD3
rospy.init_node("train_fetch_her")
env = fetch_reach.FetchReachEnv()

# Available strategies (cf paper): future, final, episode, random
goal_selection_strategy = 'future' # equivalent to GoalSelectionStrategy.FUTURE

# Wrap the model
model = HER('MlpPolicy', env, SAC, n_sampled_goal=4,
            goal_selection_strategy='future',
            verbose=1, buffer_size=int(1e6),
            learning_rate=1e-3,
            gamma=0.95, batch_size=256,
            policy_kwargs=dict(layers=[256, 256, 256]))
# Train the model
rospy.init_node("train_fetch_her")
model.learn(1000)

model.save("./her_fetch_env")

# WARNING: you must pass an env
# or wrap your environment with HERGoalEnvWrapper to use the predict method
model = HER.load('./her_bit_env', env=env)

obs = env.reset()
episode_reward = 0
for _ in range(1000):
	action, _ = model.predict(obs)
	obs, reward, done, info = env.step(action)
	episode_reward += reward
	if done or info.get('is_success', False):
		print("Reward:", episode_reward, "Success?", info.get('is_success', False))
		episode_reward = 0.0
		obs = env.reset()
