import pygame
import sys
from collections import deque

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the game clock
clock = pygame.time.Clock()
fps = 60

# Maze layout
maze = [
    "****************************************",
    "*O                              ********",
    "******* *********************** ********",
    "******* *********************** ********",
    "******* *********************** ********",
    "******* ********************************",
    "******* ********************************",
    "******* ********************************",
    "******* ********************************",
    "*******                   **************",
    "******* ****** *************************",
    "******* ****** *************************",
    "******* ****** *************************",
    "***     ****** *************************",
    "******* ****** *************************",
    "******* ******               ***********",
    "******* ****** ************* ***********",
    "******* ****** ************* ***********",
    "******* ****** ************* ***********",
    "******* ******************** ***********",
    "******* ******************** ***********",
    "******* **                            X*",
    "******* ** *****************************",
    "******* ** *****************************",
    "******* ** *****************************",
    "***     ** *****************************",
    "********** *****************************",
    "********** *****************************",
    "********** *****************************",
    "****************************************"
]
visited = set()
def DFS(maze, start):
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        if maze[current[1]][current[0]] == 'X':
            return path  # Return the path to the exit

        if current not in visited:
            visited.add(current)
            x, y = current
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):  # Check if within maze bounds
                    if maze[ny][nx] != '*' and neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

    return None  # If no path to exit is found

visited2 = set()
def BFS(maze, start):
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if maze[current[1]][current[0]] == 'X':
            return path  # Return the path to the exit

        if current not in visited2:
            visited2.add(current)
            x, y = current
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):  # Check if within maze bounds
                    if maze[ny][nx] != '*' and neighbor not in visited2:
                        queue.append((neighbor, path + [neighbor]))

    return None  # If no path to exit is found

def UpdateMaze1(maze, visited):
    visited = list(visited)
    for i in range(len(visited)):
        x, y = visited[i]
        row = list(maze[y])  # Convert the string to a list
        row[x] = "+"  # Modify the list
        maze[y] = ''.join(row)  # Convert the list back to a string

def UpdateMaze2(maze, path):
    for i in range(len(path)):
        x, y = path[i]
        row = list(maze[y])  # Convert the string to a list
        row[x] = "-"  # Modify the list
        maze[y] = ''.join(row)  # Convert the list back to a string

# DFS(maze, (1, 1))
path = BFS(maze, (1, 1))

# UpdateMaze(maze, visited)
UpdateMaze1(maze, visited2)
UpdateMaze2(maze, path)

# Function to draw the maze
def draw_maze():
    block_size = 20  # Set the size of the maze block
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            if char == '*':
                pygame.draw.rect(screen, BLACK, rect)
            elif char == '+':
                pygame.draw.rect(screen, BLUE, rect)
            elif char == '-':
                pygame.draw.rect(screen, RED, rect)
            elif char == 'O' or char == 'X':
                pygame.draw.rect(screen, GREEN, rect)
            elif char == ' ':
                pygame.draw.rect(screen, WHITE, rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    draw_maze()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()