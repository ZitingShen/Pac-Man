from game import Agent
from game import Directions
import random as ran

class DumbAgent(Agent):
    "An agent that goes West until it can't"

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)"
        print 'Location:', state.getPacmanPosition()
        print 'Actions available:', state.getLegalPacmanActions()
        if Directions.WEST in state.getLegalPacmanActions():
            print 'Going West'
            return Directions.WEST
        else:
            print "STOP."
            return Directions.STOP
        

class RandomAgent(Agent):
    "An agent that picks random legal action"

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)"
        print 'Location:', state.getPacmanPosition()
        print 'Actions available:', state.getLegalPacmanActions()
        action = ran.choice(state.getLegalPacmanActions())
        print "Going" + action
        return action
