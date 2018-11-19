from Maze import Maze
## todo: 创建迷宫并展示
maze = Maze(maze_size=(9, 11))
print(maze.valid_actions)
from Robot import Robot
robot = Robot(maze) # 记得将 maze 变量修改为你创建迷宫的变量名
robot.set_status(learning=True,testing=False)
print(robot.update())

maze