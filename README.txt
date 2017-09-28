2017/9/21
1.
a.Step 7:
The Pac Man takes moves randomly. It might take a long time to finish without ghost, since its legalactions include 'STOP', and chooses actions randomly.
It always gets food without crashing under tinyMaze and does it relatively faster than under mediumMaze. And it takes a long time for Pacman to even get out the corner of mediumMaze it started at, so we didn't finish running after -2000 scores. Yet we think it will get to the food if given sufficient time.  
The average score for tinyMaze is: 359.3
The average score for MediumMaze is:(didn't finish running, takes too long)
The average score for myLayout is: -280
The avergae score for Opensearch is: -408
c.Step 9:
The Pac Man moves relatively faster than it moves in Step 7, since it does not take 'STOP' action. When we use Opensearch layout, it scores higher without taking 'STOP' actions. And we guess that it is because the score takes the time into account, and for a shorter game it returns a higher score. But for myLayout it scores lower, maybe it is because that the Pac Man does not stop so it takes longer for ghosts to 'find' it and makes the game longer.
The average score for myLayout is : -415
The average score for Opensearch is : 282.3

d.Step 10:
The Pac Man will be lead to actions that will gain immediate food. Once its neighbourhood is free of food, it will move randomly. When running under the OpenSearch layout, its score improves drastically, since the food are densely distributed in this layout. For myLayout, its score improves a little bit, since myLayout has walls and ghost and food are not everywhere, so it is hard for Reflex Agent to find ways to eat foods quickly without encountering ghosts.
The average score for myLayout is: 26
The average score for Opensearch: 1177

e.
His position: gameState.getPacmanPosition()
The position of all the ghost: gameState.getGhostPositions()
The location of the walls: gameState.getWalls()
The position of the capsules: gameState.getcapsules()
The position of each food pellet: gameState.getFood()
The total number of food pellets still available: gameState.getNumFood()
Whether he has won or lost the game: gameState.isWin() gameState.isLose()
His current score in the game: gameState.getScore()

2.
After running both the random and reflec agent under several different layouts, we observed that even a simple reflex agent behaves much better than agent that takes totally random actions. 
When we ran the game under myLayout that has ghost and capsules, we found that the reflex agent cannot successfully avoid ghost and has no initiative to eat capsules. We may 'motivate' our agent to eat capsules by checking scores after generating the successor state. However, without knowning which direction ghosts are moving toward, it is hard for us to find a effective way to avoid them.

2017/09/21

There is a trade-off between the number of node explored(time spent) and whether we can definitely find the optimal solution.
BFS always returns the optimal solution but the number of nodes it explores is significantly more than DFS dose.
DFS does not always return the optimal solution but it explores less node than BFS does, thus spending less time.
Thus, depending on what the user want to achieve, to find a solution quickly or to find an optimal solution without considering time, he/she should choose accordingly as discussed above.
