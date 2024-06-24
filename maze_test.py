import unittest
from llstack import LLStack
from node import Node

from maze import Maze, InvalidCoordinateError

class TestMaze(unittest.TestCase):
    def setUp(self):
        entry = (0, 0)
        exit = (4, 4)

        grid = [['o', 'x', 'o', 'o', 'o'],
                ['o', 'x', 'o', 'x', 'o'],
                ['o', 'o', 'o', 'x', 'o'],
                ['o', 'x', 'x', 'x', 'o'],
                ['o', 'o', 'o', 'o', 'o']]

        self.maze = Maze(grid, entry, exit)

    def test_vaild_entry(self):
        self.assertEqual(self.maze.entry_coords, (0, 0))
        
    def test_vaild_exit(self):
        self.assertEqual(self.maze.exit_coords, (4, 4))
        
    
        
    def test_ncols(self):
        self.assertEqual(self.maze.ncols, 5)

    def test_nrows(self):
        self.assertEqual(self.maze.nrows, 5)
        
    def test_solve(self):
        vaild = '(4,4)->(4,3)->(4,2)->(4,1)->(4,0)->(3,0)->(2,0)->(1,0)->(0,0)'
        self.assertEqual(Maze.solve, vaild)

    def test_short_solve(self):
        vaild = '(4,4)->(4,3)->(4,2)->(4,1)->(4,0)->(3,0)->(2,0)->(1,0)->(0,0)'
        self.assertEqual(Maze.shortest_path, vaild)
        
        
        
if __name__ == '__main__':
    unittest.main()