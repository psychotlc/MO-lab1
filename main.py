
from simplex import *

if __name__ == '__main__':
    problem = Simplex("input_data.json")

    print(problem)

    problem.reference_solution()

    problem.optimal_solution()