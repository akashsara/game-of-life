import random
import time
from platform import system as system_name
from os import system as system_call   
import argparse

class Board:
	def __init__(self, width, height, board=''):
		"""
		Create a random soup if the board hasn't been given by the user.
		Save the width & height.
		"""
		self.width = width
		self.height = height
		self.board = board
		if board == '':
			self.board = [[self.create_cell() for w in range(width)] for h in range(height)]
		
	def create_cell(self):
		"""
		Feel free to experiment with this value here. 
		"""
		if random.random() > 0.7:
			return 'O'
		return '.'
	
	def clear(self):
		"""
		Helpful code to clear the screen from StackOverflow
		https://stackoverflow.com/questions/18937058/clear-screen-in-shell/31871439
		"""
		command = "cls" if system_name().lower()=="windows" else "clear"
		system_call(command)
		
	def render(self):
		"""
		Clear the screen and display the board.
		"""
		self.clear()
		for row in self.board:
			for cell in row:
				print(cell, end=' ')
			print('')
	
	def find_neighbors(self, cell_x, cell_y):
		"""
		Find the number of neighbors for a given cell.
		"""
		neighbors = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue
				x = cell_x + i
				y = cell_y + j
				if -1 < x < self.width and -1 < y < self.height:
					if self.board[x][y] == 'O':
						neighbors += 1
		return neighbors
	
	def neighbor_matrix(self):
		"""
		Call the find_neighbors() function for every cell in the board.
		"""
		return [[self.find_neighbors(row, col) for col in range(self.height)] for row in range(self.width)]
	
	def next_state(self):
		"""
		Calculate the next state of the board based on the 5 rules of life.
		"""
		neighbor_matrix = self.neighbor_matrix()
		for i in range(self.width):
			for j in range(self.height):
				if self.board[i][j] == 'O':
					if neighbor_matrix[i][j] in [0, 1]:
						self.board[i][j] = '.'
					if neighbor_matrix[i][j] > 3:
						self.board[i][j] = '.'
				elif neighbor_matrix[i][j] == 3:
					self.board[i][j] = 'O'
    
def get_board_from_file(file):
	"""
	Open a file and copy any 0s and 1s to the board. 
	Will not work if there are errors in the file.
	"""
	f = open(file, 'r')
	board = [[char for char in line if char in ['.', 'O']] for line in f.readlines()]
	return board

def run_game(rounds, height, width, board):
	"""
	Run the game a set number of times.
	"""
	board = Board(width, height, board)
	for i in range(rounds):
		board.render()
		board.next_state()
		time.sleep(0.5)
		
if __name__ == '__main__':
	# Setting up our parser. Included default values for each argument.
	parser = argparse.ArgumentParser(description="Akash Saravanan's implementation of Conway's Game of Life. Check it out at github.com/akashsara")
	parser.add_argument('--h', dest='height', action='store', default=10, type=int, help="Enter the height of the board.")
	parser.add_argument('--w', dest='width', action='store', default=10, type=int, help="Enter the width of the board.")
	parser.add_argument('--rounds', dest='rounds', action='store', default=8, type=int, help="Enter the number of rounds.")
	parser.add_argument('--file', dest='file', action='store', default='', help="Enter the location of a file for the intial state.")
	
	# Setting up initial variables from parsed values
	args = parser.parse_args()
	rounds = args.rounds
	height = args.height
	width = args.width
	if args.file == '':
		board = ''
	else:
		board = get_board_from_file(args.file)
		height = len(board)
		width = len(board[0])
	run_game(rounds, width, height, board)