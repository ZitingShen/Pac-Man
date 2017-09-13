from game import Agent
from game import Directions

class DumbAgent(Agent):
    "An agent that goes West until it can't"

    def getAction(self.state):
        return Directions.WEST
