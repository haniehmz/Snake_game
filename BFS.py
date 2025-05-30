from collections import deque
from Utility import Node
from Algorithm import Algorithm

class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # start clean
        self.frontier = deque([])
        self.explored_set = []
        self.path = []
        
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        # open list
        self.frontier.append(initialstate)
        
        # while we have states in open list
        while len(self.frontier) > 0:
            # your code ----------------------------------------------------------------------
            current = self.frontier.popleft()  
            self.explored_set.append(current)

            for neighbor in self.get_neighbors(current):
                
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
                    self.explored_set.append(neighbor)
                    continue  

                if neighbor not in self.frontier and neighbor not in self.explored_set:
                    neighbor.parent = current  
                    self.explored_set.append(neighbor)  
                    self.frontier.append(neighbor)

                    if neighbor.equal(goalstate):
                        return self.get_path(neighbor)
            
        return None
    