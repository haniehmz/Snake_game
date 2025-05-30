from Utility import Node
from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def recursive_DFS(self, snake, goalstate, currentstate):
        # your code ----------------------------------------------------------------------

        if currentstate.equal(goalstate):
            return self.get_path(currentstate)

        if currentstate in self.explored_set:
            return None
        self.explored_set.append(currentstate) 

        for neighbor in self.get_neighbors(currentstate):
            if not self.inside_body(snake, neighbor) and not self.outside_boundary(neighbor) and neighbor not in self.explored_set:
                neighbor.parent = currentstate 
                result = self.recursive_DFS( snake, goalstate, neighbor)  
                if result != None:
                    return result 
        return None

        # while len(self.frontier) > 0:

        #     currentstate = self.frontier.pop()  
        #     self.explored_set.append(currentstate)

        #     for neighbor in self.get_neighbors(currentstate):
                
        #         if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
        #             self.explored_set.append(neighbor)
        #             continue  

        #         if neighbor not in self.frontier and neighbor not in self.explored_set:
        #             neighbor.parent = currentstate  
        #             self.explored_set.append(neighbor)  
        #             self.frontier.append(neighbor)

        #             if neighbor.equal(goalstate):
        #                 return self.get_path(neighbor)


    def run_algorithm(self, snake):
        # to avoid looping in the same location
        if len(self.path) != 0:
            # while you have path keep going
            path = self.path.pop()
            
            if self.inside_body(snake, path):
                self.path = [] # or calculate new path!
            else:
                return path

        # start clean
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        self.frontier.append(initialstate)

        # return path
        return self.recursive_DFS(snake, goalstate, initialstate)

