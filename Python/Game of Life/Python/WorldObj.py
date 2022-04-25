import pygame
import random
import sys
from CellObj import cell

# create a object of a grid using the class world
class world:
  # color codes
  green = '\033[95m'
  black = '\033[0m'
  def __init__(self, width: int = 480, height: int = 480, grid_size: int = 20):
    # defind base paramiters of grid 
    self.SCREEN_WIDTH = width
    self.SCREEN_HEIGHT = height
    self.GRIDSIZE = grid_size
    self.GRID_WIDTH = width / grid_size
    self.GRID_HEIGHT = height / grid_size

    # Make grid of object cell
    self.grid = [cell()] * int(self.GRID_WIDTH)
    # control struckture if, while og for
    for x in range(int(self.GRID_WIDTH)):
      self.grid[x] = [cell()] * int(self.GRID_HEIGHT)
  
  # create an arr grid of 0 or 1 (new life cycle state)
  def createNewLifeCycle(self):
    # make array of grid
    arr = [int] * int(self.GRID_WIDTH)
    for x in range(int(self.GRID_HEIGHT)):
      arr[x] = [int] * int(self.GRID_HEIGHT)
    # loop throuh grid
    for x in range(int(self.GRID_WIDTH)):
      for y in range(int(self.GRID_HEIGHT)):
        # give evevy cell a random int of 0 or 1
        arr[x][y] = random.randint(0, 1)
    # return LifeCycle grid array
    return arr

  # update the game based of current Life cycle state
  def updateLifeCycle(self, LifeCycle, changes = False):
    arr = [int] * int(self.GRID_WIDTH) # vision of cells
    neighbours = [int(0)] * int(self.GRID_WIDTH) # number of alive neighbours to cells
    newLifeCycle = [int] * int(self.GRID_WIDTH) # new LifeCycle
    for x in range(int(self.GRID_WIDTH)):

      arr[x] = [int] * int(self.GRID_HEIGHT)
      neighbours[x] = [int(0)] * int(self.GRID_HEIGHT)
      newLifeCycle[x] = [int] * int(self.GRID_HEIGHT)
      for y in range(int(self.GRID_HEIGHT)):
        # in cell
        # load cell race vision rules
        r = self.grid[x][y].raceVision()
        mid = self.grid[x][y].middle
        # add array of vision to grid array
        arr[x][y] = [int] * int(self.grid[x][y].ud)
        # loop throuh every cell in vision
        for n in range(int(self.grid[x][y].ud)):
          arr[x][y][n] = [int] * int(self.grid[x][y].lr)
          for p in range(int(self.grid[x][y].lr)):
            # array i array i array i array aka multidimensional array
            # in vision for cell
            # if viewing cell is equal to this cell do nothing
            if n == mid[0] and p == mid[1]:
              # current cell
              arr[x][y][n][p] = [None, None]
            else:
              # surrounding cells 
              grid_x_value = x - (n - mid[0])
              grid_y_value = y - (p - mid[1])
              # arr[x][y][n][p] = [grid_x_value, grid_y_value]
              # check every surround cell to se if there LifeCycle is active or not
              try:
                # number of alive neighbours
                if LifeCycle[grid_x_value][grid_y_value] == 1:
                  # print(grid_x_value, grid_y_value)
                  neighbours[x][y] += 1
              except:
                # edges
                # top and bottom edges
                if grid_x_value == int(self.GRID_WIDTH):
                  grid_x_value = 0
                if grid_y_value == int(self.GRID_HEIGHT):
                  grid_y_value = 0

                # left and right edges
                if grid_x_value == -1:
                  grid_x_value = int(self.GRID_WIDTH) - 1
                if grid_y_value == -1:
                  grid_y_value = int(self.GRID_HEIGHT) - 1
                
                # number of alive neighbours 
                if LifeCycle[grid_x_value][grid_y_value] == 1:
                  neighbours[x][y] += 1
        
        # checks the cells death, live and revive rules conditions
        if (neighbours[x][y] <= self.grid[x][y].max and neighbours[x][y] >= self.grid[x][y].min) and LifeCycle[x][y] == 1:
          newLifeCycle[x][y] = 1 # cell stays alive
        elif (neighbours[x][y] == self.grid[x][y].con) and LifeCycle[x][y] == 0:
          newLifeCycle[x][y] = 1 # cell revives
          if changes:
            # prints changes to console
            print(f"{self.green}{x} {y} : {LifeCycle[x][y]} {self.black}")
            print(neighbours[x][y])
            print("Revives \n")
        else:
          newLifeCycle[x][y] = 0 # cell dies or was dead
          if LifeCycle[x][y] == 1 and changes: # checks if cell was alive in past LifeCycle
              #  prints changes to console
              print(f"{self.green}{x} {y} : {LifeCycle[x][y]} {self.black}")
              print(neighbours[x][y])
              print("Dies \n")
        
    # return the value of new active LifeCycle 
    return newLifeCycle #temp
        
  # draw the LifeCycle in grid
  def drawGrid(self, surface, LifeCycle):
    # loop throuh grid
    for x in range(0, int(self.GRID_WIDTH)):
      for y in range(0, int(self.GRID_HEIGHT)):
        # draw every cell based on cells LifeCycle on surface
        if LifeCycle[x][y] == 0:
          r = pygame.Rect((x * self.GRIDSIZE - 1, y * self.GRIDSIZE - 1), (self.GRIDSIZE - 2, self.GRIDSIZE - 2))
          pygame.draw.rect(surface, (0, 0, 0), r)
        else:
          rr = pygame.Rect((x * self.GRIDSIZE - 1, y * self.GRIDSIZE - 1), (self.GRIDSIZE - 2, self.GRIDSIZE - 2))
          pygame.draw.rect(surface, (255, 255, 255), rr)
  
  # return the dimensions of grid
  def gridDimensions(self):
    return self.GRID_WIDTH, self.GRID_HEIGHT
  # return the size of a single cell
  def cellSize(self):
    return self.GRIDSIZE
  # return the screen size
  def screenSize(self):
    return self.SCREEN_WIDTH, self.SCREEN_HEIGHT