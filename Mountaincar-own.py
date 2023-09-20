import gym
import pygame
from gym.utils.play import play

# 定义案件的映射
# 0往左，1不动（我没放），2往右
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 2}

# 直接玩这个游戏
env = gym.make('MountainCar-v0', render_mode='rgb_array')

play(env, keys_to_action=mapping)
