from lib.logger import Log
from lib.planner import Planner

startState = input("Enter the start state :: ")
goalState = input("Enter the goal state :: ")

planner = Planner(verbose=False)
plan = planner.getPlan(startState=startState, goalState=goalState)
Log.i(f"Final plane derived ::")
for p in plan:
    Log.i(p)

#
# on : stack clear
# ontable: putdown, hold
# clear: putdown, hold; unstack, on, clear
# hold: pickup,ontable, ae; unstack on clear
# ae: putdown hold
#

