from random import randint, random
from re import S
from typing import List


class Environement:
    def __init__(self) -> None:
        self.steps_left=10

    
    def get_observation(self) -> List[float]:
        return [0,0,0]

    def get_actions(sefl) -> List[int]:
        return [0,1]

    def is_done(self) ->bool:
        return self.steps_left==0
    def action(self, action : int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        
        self.steps_left-=1
        return random.random()