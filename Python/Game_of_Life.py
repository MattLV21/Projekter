import pygame
import numpy as np
from enum import Enum
import random

class race(Enum):
  HUMAN = 0
  DOG = 1

  def rules(race):
    if race == race.HUMAN:
      print("this is a human")

class cell:
  def __init__(self, state: int = 0, r: int = 0):
    self.state = random.randint(0,1)
    self.r = race(r)

  def draw(self):
    # race.rules(self.r)
    pass

class world:
  def __init__(self, width: int = 480, height: int = 480, grid_size: int = 20):
    self.SCREEN_WIDTH = width
    self.SCREEN_HEIGHT = height
    self.GRIDSIZE = grid_size
    self.GRID_WIDTH = width / grid_size
    self.GRID_HEIGHT = height / grid_size

    # Make empty grid
    # self.grid = np.array([])
    self.grid = [cell()] * int(self.GRID_WIDTH)
    for x in range(int(self.GRID_WIDTH)):
      self.grid[x] = [cell()] * int(self.GRID_HEIGHT)
      #self.grid.resize((int(self.GRID_WIDTH), int(self.GRID_HEIGHT)), refcheck=False)
    print(self.grid)


  def drawGrid(self, surface):
    for x in range(0, int(self.GRID_WIDTH)):
      for y in range(0, int(self.GRID_HEIGHT)):
        # draw dead or alive cells
        # not this

        if self.grid[x][y] == 0:
          r = pygame.Rect((x * self.GRIDSIZE, y * self.GRIDSIZE), (self.GRIDSIZE, self.GRIDSIZE))
          pygame.draw.rect(surface, (0, 0, 0), r)
        else:
          rr = pygame.Rect((x * self.GRIDSIZE, y * self.GRIDSIZE), (self.GRIDSIZE, self.GRIDSIZE))
          pygame.draw.rect(surface, (255, 255, 255), rr)

        # if (x + y) % 2 == 0:
        #   r = pygame.Rect((x * self.GRIDSIZE, y * self.GRIDSIZE), (self.GRIDSIZE, self.GRIDSIZE))
        #   pygame.draw.rect(surface, (93, 216, 228), r)
        # else:
        #   rr = pygame.Rect((x * self.GRIDSIZE, y * self.GRIDSIZE), (self.GRIDSIZE, self.GRIDSIZE))
        #   pygame.draw.rect(surface, (84, 194, 205), rr)
  

grids = world(width = 600, height = 600, grid_size = 30)

def main():
  pygame.init()

  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((grids.SCREEN_WIDTH, grids.SCREEN_HEIGHT), 0, 32)

  surface = pygame.Surface(screen.get_size())
  surface = surface.convert()
  grids.drawGrid(surface)

  while(True):
    clock.tick(10)
    grids.drawGrid(surface)

    # handle events
    screen.blit(surface, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)


main()