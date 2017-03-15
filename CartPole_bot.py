import gym
import sys
import numpy as np

method = sys.argv[1]

print method



if(method == "Random_Search"):
	
	#make function to call any gym game environment
	env = gym.make('CartPole-v0')

	for i_episode in range(50):

		observation = env.reset() #obtain all the observations from the environment using reset function

		for t in range(100):
			env.render() # render/display the environment
			print(observation) # Just display the observations obtained (cart and pole velocities and position in this case)

			action = env.action_space.sample() # take any random action

			observation, reward, done, info = env.step(action) # do the action, take a step a further and obtain new observations, reward, bool of game over or not , debug info

			if done:
				print("episode finish after timesteps -", t)
				break

elif(method == "Hill_Climbing"):
	def run_episode(env,parameters):
		observation = env.reset()
		totalreward = 0

		for _ in xrange(200):
			env.render()
			#initialize random weights
			action = 0 if np.matmul(parameters, observation)<0 else 1
			observation, reward, done, info = env.step(action)
			totalreward +=reward
			if done:
				break
		return totalreward

	#hill climbing
	def train():
		env = gym.make('CartPole-v0')

		episodes_per_update = 5
		noise_scaling = 0.1
		parameters = np.random.rand(4)*2-1
		bestreward = 0

		#2000 episodes
		for _ in xrange(2000):
			newparams = parameters + np.random.rand(4)*2-1 * noise_scaling
			reward = run_episode(env,newparams)
			print "reward %d best %d" %(reward,bestreward)
			if reward > bestreward:
				bestreward = reward
				parameters = newparams
				if reward ==200:
					break

	train()
else:
	print "Select appropriate method!"
	