import pygame
import random
from WorldObj import world

# make grid and life cycle 
grids = world(width = 800, height = 800, grid_size = 30)
LifeCycle = grids.createNewLifeCycle()
new_state = grids.updateLifeCycle(LifeCycle)
#print(new_state)
print(grids.gridDimensions())
print(grids.cellSize())
print(grids.screenSize())

def main():
  pygame.init()

  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((grids.SCREEN_WIDTH, grids.SCREEN_HEIGHT), 0, 32)

  surface = pygame.Surface(screen.get_size())
  surface = surface.convert()

  LifeCycle = grids.createNewLifeCycle()
  new_state = grids.updateLifeCycle(LifeCycle)  
  grids.drawGrid(surface, LifeCycle)

  while(True):
    clock.tick(5)

    LifeCycle = grids.updateLifeCycle(LifeCycle, False)
    grids.drawGrid(surface, LifeCycle)

    # handle events
    screen.blit(surface, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

if __name__ == "__main__":
  main()