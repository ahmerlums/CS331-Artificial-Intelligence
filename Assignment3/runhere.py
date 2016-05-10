# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions 
import random, util
import math
from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        distancefromGhost = manhattanDistance(currentGameState.getGhostPosition(1),newPos)
        

        if distancefromGhost <=4 :
           score =  4 + successorGameState.getScore()
        else:
           score =  distancefromGhost + successorGameState.getScore()


        
        min = 1000;

        for pos in newFood.asList():
          if (manhattanDistance(pos, newPos) < min):
              min = manhattanDistance(pos, newPos)
        score = score-2*min
        if (currentGameState.getNumFood() > successorGameState.getNumFood()):
              score = score + 50
        if action == Directions.STOP:
              score = score - 30
        
        campsules = currentGameState.getCapsules()
        if successorGameState.getPacmanPosition() in campsules:
            score = score + 50
        
        
        if successorGameState.isWin():
          return 10000
        else:
          return score
def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (TASK 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        return self.getAction1(gameState,2,1,self.depth)
    def getAction1(self, gameState,flag,i,d):
        numghosts = gameState.getNumAgents() - 1
        result = Directions.STOP
        if flag == 1:
            if gameState.isWin() or gameState.isLose() or d == 0:
               return self.evaluationFunction(gameState)
            legalActions = gameState.getLegalActions(i)
            
            score = 99999
            if i == numghosts:
              for action in legalActions:
                   successorGameState = gameState.generateSuccessor(i, action)
                   lowLevel = d - 1
                   score = min(score,self.getAction1(successorGameState, 0,i,lowLevel))
            else:
               for action in legalActions:
                   successorGameState = gameState.generateSuccessor(i, action)
                   nextIndex = i+1
                   score = min(score,self.getAction1(successorGameState, 1,nextIndex,d))


            return score

            
        elif flag == 2:
            
            legalActions = gameState.getLegalActions()
            score = -99999
            for action in legalActions:
                 successorGameState = gameState.generateSuccessor(0, action)
                 prevresult = score
                 score = max(score,self.getAction1(successorGameState, 1, 1,d))
                 if score > prevresult:
                    result = action
            return result

        else: 
            if gameState.isWin() or gameState.isLose() or d == 0:
                return self.evaluationFunction(gameState)
            legalActions = gameState.getLegalActions(0)
            score = -99999
            i=1
            for action in legalActions:
                 successorGameState = gameState.generateSuccessor(0, action)
                 lowLevel = d-1
                 score = max(score, self.getAction1(successorGameState, 1,1,lowLevel))
            return score



class ExpectiminimaxAgent(MultiAgentSearchAgent):
    """
      Your expeciminimax agent (TASK 4)
    """

    def getAction(self, gameState):
      """
        Returns the expectimax action using self.depth and self.evaluationFunction
        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
      """
      "*** YOUR CODE HERE ***"
      def expectedvalue(gameState, i, d):
            if gameState.isWin() or gameState.isLose() or d == 0:
                return self.evaluationFunction(gameState)
            total= 0
            numghosts = gameState.getNumAgents() - 1
            legalActions = gameState.getLegalActions(i)
            min = 99999
            for action in legalActions:
                successorGameState = gameState.generateSuccessor(i, action)
                if (i <> numghosts):
                    total = total + expectedvalue(successorGameState,i+1, d)
                else:
                    total = total + maxvalue(successorGameState, d-1)
                if total < min:
                  min = total
            
            if i==1:
              rval = min
            else:
              rval=total/len(legalActions)
            return rval
      def maxvalue(gameState, d):
          if gameState.isWin() or gameState.isLose() or d == 0: 
              return self.evaluationFunction(gameState) 

          legalActions = gameState.getLegalActions(0)
          score = -99999
          for action in legalActions:
              successorGameState = gameState.generateSuccessor(0, action)
              prev = score
              expval = expectedvalue(successorGameState, 1, d)
              if score < expval:
                 score = expval
          return score
      legalActions = gameState.getLegalActions(0)
      score = -99999
      for action in legalActions:
          successorGameState = gameState.generateSuccessor(0, action)
          prevresult = score
          expval = expectedvalue(successorGameState, 1, self.depth)
          if score < expval:
              score = expval
          if prevresult < score:
              result = action
      return result
      util.raiseNotDefined()

       
    
     

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction
      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    def expectedvalue(gameState, i, d):
        if gameState.isWin() or gameState.isLose() or d == 0:
            return self.evaluationFunction(gameState)
        total= 0
        numghosts = gameState.getNumAgents() - 1
        legalActions = gameState.getLegalActions(i)
        
        for action in legalActions:
            successorGameState = gameState.generateSuccessor(i, action)
            if (i <> numghosts):
                total = total + expectedvalue(successorGameState,i+1, d)
            else:
                total = total + maxvalue(successorGameState, d-1)
        rval=total/len(legalActions)
        return rval
    def maxvalue(gameState, d):
        if gameState.isWin() or gameState.isLose() or d == 0: 
            return self.evaluationFunction(gameState) 

        legalActions = gameState.getLegalActions(0)
        score = -99999
        for action in legalActions:
            successorGameState = gameState.generateSuccessor(0, action)
            prev = score
            expval = expectedvalue(successorGameState, 1, d)
            if score < expval:
	             score = expval
        return score
    legalActions = gameState.getLegalActions(0)
    score = -99999
    for action in legalActions:
        successorGameState = gameState.generateSuccessor(0, action)
        prevresult = score
        expval = expectedvalue(successorGameState, 1, self.depth)
        if score < expval:
            score = expval
        if prevresult < score:
            result = action
    return result
    
    util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function.

      DESCRIPTION: <write something here so we know what you did>
    """
    
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
      
        util.raiseNotDefined()

