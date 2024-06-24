from llstack import LLStack
from node import Node

class InvalidCoordinateError(Exception):
    pass
'''
class maze
creates the maze with the grid size and the entry location and exit location
also has a solver to solve the maze
'''
class Maze:
    
    '''
    initalized everything need for the maze to be made and for it to be solved
    '''
    def __init__(self, grid: list[list[str]], entry_loc: tuple, exit_loc: tuple):
        
        # checks if rows is a list if its not returns a type error
        for row in grid:
            if not isinstance(row, list):
                raise TypeError
            
            # makes sire the values in the rows is a string
            for stri in row:
               if not isinstance(stri, str):
                   raise TypeError
               
        # sets nrows and ncols to a int the size of the grid
        self.__nrows = len(grid)
        self.__ncols = len(grid[0])
        
        # makes sure that the grid is atleast a 3x3
        if self.__nrows < 3 or self.__ncols < 3:
           raise ValueError
       
        # sets grid to the atribution grid
        self._grid = grid 
       
       
        # sets the entry location to the atribution
        self.__entry = entry_loc 

        # checks if __entry is tuple and raises type error
        if not isinstance(self.__entry, tuple):
            raise TypeError('entry isnt a tuple')
        
        # checks if cords are ints and if they arent they raises type error
        for coords in self.__entry:
            if not isinstance(coords, int):
                raise TypeError('exit isnt a tuple')
            
            if coords > self.__ncols and self.__nrows:
                raise InvalidCoordinateError('coords are out of bounds')
        
        # sets __exit to exit loc
        self.__exit = exit_loc  
        
        # checks if __exit is a tuple
        if not isinstance(self.__exit, tuple):
            raise TypeError
        
        # checks if the values in __exit are ints
        for coords in self.__exit:
            if not isinstance(coords, int):
                raise TypeError
            
            # checks if cords are vaild 
            if coords > self.__ncols and coords > self.__nrows:
                raise InvalidCoordinateError
        
        # initalizes path to None
        self.__path = None
        
        # initalizes shortest_path to None
        self.__shortest_path = None

    '''
    readable nrows    
    '''
    @property
    def nrows(self) -> int:
        return self.__nrows

    # nrows setter
    @nrows.setter
    def nrows(self, __nrows: int):

        # makes sure that nrows is greater than 3
        if __nrows < 3:
            raise ValueError("Maze dimensions must be at least 3x3")
        self.__nrows = __nrows

    '''
    readable ncols
    '''
    @property
    def ncols(self) -> int:
        return self.__ncols
    
    '''
    ncols setter 
    '''
    @ncols.setter
    def ncols(self, __ncols: int):

        # makes sure that ncols is greater than 3
        if __ncols < 3:
            raise ValueError("Maze dimensions must be at least 3x3")
        self.__ncols = __ncols
    

    '''
    readable entry cords
    '''
    @property
    def entry_coords(self):
        return self.__entry
    
    '''
    entry coords setter
    ''' 
    @entry_coords.setter
    def entry_coords(self, __entry):

        # checks if entry is a tuple
        if not isinstance(__entry, tuple):
            raise TypeError
        
        # check if the coords is an int
        for coords in __entry:
            if not isinstance(coords, int):
                raise TypeError
            
            # makes sure that the coords are not out of bounds
            if coords > self.__ncols and self.__nrows:
                raise InvalidCoordinateError
        
    '''
    readable exit coords
    '''
    @property
    def exit_coords(self):
        return self.__exit
    
    # writable exit coords 
    @exit_coords.setter
    def exit_coords(self, __exit):

        # checks if entry is a tuple
        if not isinstance(__exit, tuple):
            raise TypeError
        
        # check if the cords is an int
        for coords in __exit:
            if not isinstance(coords, int):
                raise TypeError
            
            # makes sure that the cords are not out of bounds
            if coords > self.__ncols and coords > self.__nrows:
                raise InvalidCoordinateError
    
    # readable path
    @property
    def path(self):
        return self.__path
    
    # readable shortest path 
    @property
    def shortest_path(self):
        return self.__shortest_path
    
    # solves the maze 
    def solve(self):
        self.__path = LLStack()
        row, col = self.__entry
        exit_row, exit_col = self.__exit
        visted  = self.__path
        visited = []
        if self.__solve_helper(row, col, exit_row, exit_col, visited):
            return self.__path
        else:
            print("No valid path found.")
        self.__path = None
        return self.__path
        
    '''
    helper for solve
    '''
    def __solve_helper(self, row, col, exit_row, exit_col, visited):
        cur_coords = (row,col)
        if (row, col) == (exit_row, exit_col):
            self.__path.push(cur_coords)
            return True

    
        if not (0 <= row < self.__nrows) or not (0 <= col < self.__ncols) or self._grid[row][col] == 'x':
            return False


        # adds coords to a stack
        self.__path.push(cur_coords)
        visited.append(cur_coords)

        # Checks down
        if (row + 1, col) not in visited:
            if self.__solve_helper(row + 1, col, exit_row, exit_col, visited):
                return True
        
        # Checks right
        if (row, col + 1) not in visited:
            if self.__solve_helper(row, col + 1, exit_row, exit_col, visited):
                return True

        # Checks up
        if (row - 1, col) not in visited:
            if self.__solve_helper(row - 1, col, exit_row, exit_col, visited):
                return True

        # Checks left
        if (row, col - 1) not in visited:
            if self.__solve_helper(row, col - 1, exit_row, exit_col, visited):
                return True

        
        # removes last node if it doesnt work and keeps trying
        self.__path.pop()
        return False
            
       
       
    '''
    finds the shortest possibe path
    '''
    def solve_shortest(self):
        
        # sets shortest path to a stack from the llstack class
        self.__shortest_path = LLStack()
        
        # sets rows and cols to the entry coords
        row, col = self.__entry
        
        # sets the exits rows and cols from th exit cords
        exit_row, exit_col = self.__exit
        
        # visted is a list
        visited = []
        
        # run the shortest help and if its solved it returns the shortest path
        if self.__solve_shortest_distance(row, col, exit_row, exit_col, visited):
            return self.__shortest_path
        
        # no vaild path was found and sets shortest path back to none as per intructions
        else:
            print("No valid path found.")
        self.__shortest_path = None
        return self.__shortest_path
    
        
    '''
    actually does the work the shortest path and returns true if its possible
    '''
        
    def __solve_shortest_distance(self, row, col, exit_row, exit_col, visited):
        
        #sets coords to the row and col
        cur_coords = (row,col)
        
        # base case and sees if the maze is solved
        if (row, col) == (exit_row, exit_col):
            self.__shortest_path.push(cur_coords)
            return True

        # makes sure eveything is in bounds 
        if not (0 <= row < self.__nrows) or not (0 <= col < self.__ncols) or self._grid[row][col] == 'x':
            return False

        # adds coords to shortest path stack
        self.__shortest_path.push(cur_coords)
        
        # adds coords to visted list
        visited.append(cur_coords)

        # Checks down
        if (row + 1, col) not in visited:
            if self.__solve_shortest_distance(row + 1, col, exit_row, exit_col, visited):
                return True
        
        # Checks right
        if (row, col + 1) not in visited:
            if self.__solve_shortest_distance(row, col + 1, exit_row, exit_col, visited):
                return True

        # Checks up
        if (row - 1, col) not in visited:
            if self.__solve_shortest_distance(row - 1, col, exit_row, exit_col, visited):
                return True

        # Checks left
        if (row, col - 1) not in visited:
            if self.__solve_shortest_distance(row, col - 1, exit_row, exit_col, visited):
                return True


        # backtracks if needed
        self.__shortest_path.pop()
        return False

        
        
    
    
#testing    
entry = (0,0)
exit = (4,4)

grid1 = [['o','x','o','o','o'],
         ['o','x','o','x','o'],
         ['o','o','o','x','o'],
         ['o','x','x','x','o'],
         ['o','o','o','o','o']]

mazze = Maze(grid1, entry, exit)

mazze.solve()
print(mazze.path)