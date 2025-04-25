# Import OR-Tools wrapper for linear programming
from ortools.linear_solver import pywraplp

# Create a solver using the GLOP backend
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Create the variables we want to optimize
swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

# Add constraints for each resource
solver.Add(swordsmen*60 + bowmen*80 + horsemen*140 <= 1200) # Food
solver.Add(swordsmen*20 + bowmen*10 <= 800)                 # Wood
solver.Add(bowmen*40 + horsemen*100 <= 600)                 # Gold