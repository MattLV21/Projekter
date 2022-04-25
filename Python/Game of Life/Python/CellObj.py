import pygame
import random
import sys

class cell:
  def __init__(self, race: str = "human"):
    # defind vision rules
    if race == "human":
      # from top to bottom
      self.ud = 3
      # from left to right
      self.lr = 3
      # current cell
      self.middle = [1, 1]
      # defind game rules
      # minimum before death
      self.min = 2
      # maximun before death
      self.max = 3
      # alive neighbours before revive
      self.con = 3
    
    self.race = race
    # create vision array
    #self.vision = [str("X")] * self.ud # vision from top to bottom
    #for x in range(self.ud):
    #  self.vision[x] = [str("X")] * self.lr # vision from left to right
    
  # add current cell to vision
  def raceVision(self):
    r = str(self.race).lower()
    if r == "human":
      vision = [str("X")] * self.ud
      for x in range(self.ud):
        vision[x] = [str("X")] * self.lr
        for y in range(self.lr):
          if self.middle[0] == x and self.middle[1] == y:
            vision[x][y] = str("O")
    # return vision    
    return vision
