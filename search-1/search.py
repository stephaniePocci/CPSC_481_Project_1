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
  return [s, s, w, s, w, w, s, w]


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
  start_pt = problem.getStartState()  # retrieves starting node
  if problem.isGoalState(start_pt):  # if solved, return the array
    return []

  stack = util.Stack()  # stack queue for DFS
  visited = []  # nodes already visited
  stack.push((start_pt, []))  # adds starting node to stack

  while not stack.isEmpty():  # while there are still nodes left
    current_pt, moves = stack.pop()  # pops the most recent node
    if current_pt not in visited:  # if node has not been traversed
      visited.append(current_pt)  # add node to the queue
      if problem.isGoalState(
          current_pt
      ):  # if node is the goal node, then return the list of moves
        return moves
      for next_pt, action, cost in problem.getSuccessors(current_pt):
        next_move = moves + [action
                             ]  # adds an additional action for the next move
        stack.push((next_pt, next_move))  # adds the next move to the stack


def breadthFirstSearch(problem):
  """Search the shallowest nodes in the search tree first."""
  "*** YOUR CODE HERE ***"
  start_pt = problem.getStartState()  # retrieves starting node
  queue = util.Queue()  # create queue for BFS
  visited = []  # a list for previously visited nodes
  queue.push((start_pt, [], 0))  # add starting node to queue

  while not queue.isEmpty():  # while there are still nodes left
    current_pt, moves, cost = queue.pop(
    )  # pop most recent node, action, and cost
    if current_pt not in visited:  # if current node has not been traversed
      visited.append(current_pt)  # add popped node into visited list
      if problem.isGoalState(
          current_pt
      ):  # if node is in the goal state, return the list of moves
        return moves
      else:
        successors = problem.getSuccessors(
          current_pt)  # add node to list of moves
        for next_pt, action, cost in successors:  # for next node in successors list
          next_move = moves + [action]
          cost += cost  # add new cost to itself
          next_node = (next_pt, next_move, cost)  # set the next node
          queue.push(
            next_node)  # push the new node to the queue (list of moves)

  return moves  # return the list of total moves
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

  queue = util.PriorityQueue() #create a priority queue that will hold the cost and heuristic of the nodes

  visitedNodes = [] #python list will hold the visited nodes through the heuristic 

  startState = problem.getStartState() #retrieve the starting point from the given problem of pacman 


  startNode = (startState, [], 0) #set the starting node position to the first index 

  queue.push(startNode, 0) #add the starting index to the queue

  while not queue.isEmpty(): #while queue is not empty, do the following
    currentState, actions, currentCost = queue.pop() #start looking through the first node in the queue that has the lowest combined cost and heuristic 
   

    visitedNodes.append((currentState, currentCost)) #add the popped node into the visited nodes list 

    if problem.isGoalState(currentState): #if the currentState a valid goal   state, then return the actions 

      return actions

    elif not problem.isGoalState(currentState): #otherwise if not
      successors = problem.getSuccessors(currentState) #then set sucessors to the problem at the getSucessors() function with currentState as the arg. 

      for state, action, cost in successors: #iterate through the sucessors list
        game_action = actions + [action] #create Action variable that will keep track of the action from the for loop and the variable within the first node
        game_cost = problem.getCostOfActions(game_action) #set Cost to the Action from the sequence of actions needed for aStarSearch 
        Node = state, game_action, game_cost #set Node variable to the current state, action, and cost of the heuristic search 

        visited = False #visited bool variable will check if the node has been checked or not

        for visit in visitedNodes: #iterate through each visited node
          visitedState, visitedCost = visit #created visited state and lowest cost to the current visited index

          if state == visitedState and game_cost >= visitedCost: #if the current state is the same value as the already visited state in the heuristic and the Cost is graeter than or equal to the visited node with the lowest cost
            visited = True #then it has been visited 

        if not visited: #if not visited, do the following
          queue.push(Node, game_cost + heuristic(state, problem)) #push the new heuristic and lowest cost combined into the queue 
          visitedNodes.append((state, game_cost)) #update value of the visited list 

  return actions #return the valuation of actions 
  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
