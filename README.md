#Maze Solver

This is a maze solver program written in python using pygame. 

pygame should be installed in your system.

enter python main.py to run the code.

It uses BFS and DFS to parse through the maze to find the path, the path might not be optimal though. The solved path is colored using red and the explored path which does not lie on the main path is colored in blue the unexplored path is colored in white while walls are colored in black.

To change from DFS to BFS or vice versa just change the DFS() function to BFS() and in UpdateMaze() function change the visited argument to visited2.

There are 5 pre built mazes in the text file in it '*' denotes the wall, 'O' denotes the starting point and 'X' denotes the ending point.

To make your own custom maze please keept these things in mind the total maze size should be 40 * 29 for best results the 'O' symbol should be at the index (1,1). The outermost layer of the whole maze should be covered in star such that now free path is at the end of the array. Place your custom maze in place of the maze variable. 