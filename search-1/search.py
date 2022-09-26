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

    def getCostOfmoves(self, moves):
        """
         moves: A list of moves to take

        This method returns the total cost of a particular sequence of moves.
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

    Your search algorithm needs to return a list of moves that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start_pt = problem.getStartState() # retrieves starting node
    if problem.isGoalState(start_pt): # if solved, return the array
        return []
    
    stack = util.Stack() # stack queue for DFS
    visited = [] # nodes already visited
    stack.push((start_pt, [])) # adds starting node to stack
    
    while not stack.isEmpty(): # while there are still nodes left
        current_pt, moves = stack.pop() # pops the most recent node
        if current_pt not in visited: # if node has not been traversed
            visited.append(current_pt) # add node to the queue
            if problem.isGoalState(current_pt): # if node is the goal node, then return the list of moves
                return moves
            for next_pt, action, cost in problem.getSuccessors(current_pt):
                next_move = moves + [action] # adds an additional action for the next move
                stack.push((next_pt, next_move)) # adds the next move to the stack

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_pt = problem.getStartState() # retrieves starting node
    queue = util.Queue() # create queue for BFS
    visited = [] # a list for previously visited nodes
    queue.push((start_pt, [], 0)) # add starting node to queue 
    
    while not queue.isEmpty(): # while there are still nodes left
        current_pt, moves, cost = queue.pop() # pop most recent node, action, and cost
        if current_pt not in visited: # if current node has not been traversed
            visited.append(current_pt) # add popped node into visited list
            if problem.isGoalState(current_pt): # if node is in the goal state, return the list of moves
                return moves
            else:
                successors = problem.getSuccessors(current_pt) # add node to list of moves
                for next_pt, action, cost in successors: # for next node in successors list
                    next_move = moves + [action] 
                    cost += cost # add new cost to itself
                    next_node = (next_pt, next_move, cost) # set the next node
                    queue.push(next_node) # push the new node to the queue (list of moves)

    return moves # return the list of total moves
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
