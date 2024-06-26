import numpy as np
import rl_tree
import extra.animate as animate

import tensorflow as tf
from tf_agents.environments import tf_py_environment

max_actions = 4
episodes = 3
env = rl_tree.ParkingEnvironment(size=6, max_actions=max_actions)
tf_env = tf_py_environment.TFPyEnvironment(env)
tf_env.reset()

init_frame = tf_env.render()

frames = [init_frame]
actions = [1, 1, 1, 1] # remember to update max_actions when changing the actions array

for _ in range(episodes):
    time_step = tf_env.reset()
    count = 0
    for _ in range(max_actions+1):
        if time_step.is_last():
            print("Episode terminated")
            break
        action = actions[count]
        print(action)
        time_step = tf_env.step(action)
        frame = tf_env.render()
        frames.append(frame)
        count += 1
tf_env.close()
actions_arr = env.last_terminated_number_actions()
print(actions_arr)
animate.animate_frames(frames, actions_per_episode=actions_arr)
 

