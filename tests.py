import unittest
from game_of_life import Board

def get_next_state(init_state):
	board = Board(3, 3, init_state)
	board.next_state()
	return board.board

class TestLife(unittest.TestCase):
	
	def test_dead_stay_dead(self):
		"""
		Test 1: Dead cells with no live neighbors stay dead.
		. . .				. . .
		. . .		=>		. . .
		. . .				. . .
		"""
		init_state = [['.' for j in range(3)] for i in range(3)]
		expected_next_state = [['.' for j in range(3)] for i in range(3)]
		actual_next_state = get_next_state(init_state)
		self.assertEqual(actual_next_state, expected_next_state)
	
	def test_reproduction(self):
		"""
		Test 2: Dead cells with exactly 3 neighbors come to life.
		O . .				O O .
		O O .		=>		O O .
		. . .				. . .
		"""
		init_state = [
			['O','.','.'],
			['O','O','.'],
			['.','.','.']
		]
		expected_next_state = [
			['O','O','.'],
			['O','O','.'],
			['.','.','.']
		]
		actual_next_state = get_next_state(init_state)
		self.assertEqual(actual_next_state, expected_next_state)
		
	def test_underpopulation(self):
		"""
		Test 3: Live cells with 0 or 1 live neighbors die.
		O . .				. . .
		O . .		=>		. . .
		. . .				. . .
		"""
		init_state = [
			['O','.','.'],
			['O','.','.'],
			['.','.','.']
		]
		expected_next_state = [
			['.','.','.'],
			['.','.','.'],
			['.','.','.']
		]
		actual_next_state = get_next_state(init_state)
		self.assertEqual(actual_next_state, expected_next_state)
		
	def test_overpopulation(self):
		"""
		Test 4: Live cells with more than 3 live neighbors die.
		O O O				O . O
		O O O		=>		. . .
		O O O				O . O
		"""
		init_state = [
			['O','O','O'],
			['O','O','O'],
			['O','O','O']
		]
		expected_next_state = [
			['O','.','O'],
			['.','.','.'],
			['O','.','O']
		]
		actual_next_state = get_next_state(init_state)
		self.assertEqual(actual_next_state, expected_next_state)
	
	def test_alive_stay_alive(self):
		"""
		Test 5: Any live cell with 2 or 3 live neighbors stays alive.
		O O .				O O .
		O . O		=>		O . O
		. O .				. O .
		"""
		init_state = [
			['O','O','.'],
			['O','.','O'],
			['.','O','.']
		]
		expected_next_state = [
			['O','O','.'],
			['O','.','O'],
			['.','O','.']
		]
		actual_next_state = get_next_state(init_state)
		self.assertEqual(actual_next_state, expected_next_state)
		
if __name__ == '__main__':
	unittest.main()