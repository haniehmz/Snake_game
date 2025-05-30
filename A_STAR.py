from Algorithm import Algorithm


class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # clear everything
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(initialstate)

        # while we have states in open list
        while len(self.frontier) > 0:
            # your code ----------------------------------------------------------------------
            lowest = 0
            for i in range(len(self.frontier)):
                if self.frontier[i].f < self.frontier[0].f:
                    lowest = i
                   
            current = self.frontier.pop(lowest)

            if current.equal(goalstate):
                return self.get_path(current)

            self.explored_set.append(current) 

            for neighbor in self.get_neighbors(current) :

                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor) or neighbor in self.explored_set:
                    continue 

                best = False  
                if neighbor not in self.frontier: 
                    neighbor.h = self.manhattan_distance(goalstate, neighbor)
                    self.frontier.append(neighbor)
                    best = True
                elif current.g < neighbor.g:  
                    best = True 

                if best:
                    neighbor.parent = current
                    neighbor.g = current.g + 1
                    neighbor.f = neighbor.g + neighbor.h
        return None
