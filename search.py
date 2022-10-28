# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    cur_node = problem.getStartState()
    if (cur_node == problem.isGoalState):
        return []
    stack = util.Stack()
    stack.push((cur_node, []))
    visited = []
    while(not stack.isEmpty()): 
        cur_node, path = stack.pop()
        if(problem.isGoalState(cur_node)):
            return path
        if cur_node not in visited:
            visited.append(cur_node)
            for successor in problem.getSuccessors(cur_node):
                new_path_list = path + [successor[1]]
                stack.push((successor[0], new_path_list))
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState((1,1))
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    startPosition = problem.getStartState()
    visitedPositions = []
    q = util.Queue()
    q.push((startPosition,[]))
    pacmanPath =[]
    currentPosition = startPosition
    while not problem.isGoalState(currentPosition):
        currentPosition, pacmanPath = q.pop()
        if problem.isGoalState(currentPosition):
                return pacmanPath
        if currentPosition not in visitedPositions:
            for nextPosition, way, cost in problem.getSuccessors(currentPosition):
                    newPacmanPath = pacmanPath + [way]
                    q.push((nextPosition,newPacmanPath))
            visitedPositions.append(currentPosition)
    return pacmanPath
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    path = []
    visited = []
    queue = util.PriorityQueue()
    queue.update((problem.getStartState(),path),0) # initialize the queue with start state
    while not queue.isEmpty():
        current_state, current_path = queue.pop()
        if problem.isGoalState(current_state):
            return current_path
        if current_state not in visited:
            potential_paths = problem.getSuccessors(current_state)
            for potential_path in potential_paths:
                new_state = potential_path[0]
                if new_state not in visited:
                    new_direction = potential_path[1]
                    new_path = current_path + [new_direction]
                    queue.push((new_state, new_path), problem.getCostOfActions(new_path))
            visited.append(current_state)
    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startPosition = problem.getStartState()
    visitedPositions = []
    q = util.PriorityQueue()
    q.push((startPosition,[],0),0)
    pacmanPath =[]
    currentPosition = startPosition
    while not problem.isGoalState(currentPosition):
        currentPosition, pacmanPath, currentCost = q.pop()
        if problem.isGoalState(currentPosition):
            return pacmanPath
        if currentPosition not in visitedPositions:
            for nextPosition, way, cost in problem.getSuccessors(currentPosition):
                    newPacmanPath = pacmanPath + [way]
                    newCost = currentCost + cost
                    q.push((nextPosition,newPacmanPath,newCost),newCost+heuristic(nextPosition,problem))
            visitedPositions.append(currentPosition)
    return pacmanPath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
