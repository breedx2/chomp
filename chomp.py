#!/usr/bin/python

import sys
import re

DEFAULT_WIDTH = 4
DEFAULT_HEIGHT = 3

class Board(object):
	@staticmethod
	def of_size(width, height):
		rows = []
		for row in range(height):
			cols = ['o' for i in range(width)]
			if(row == 0):
				cols[0] = '*'
			rows.append(cols)
		return Board(rows)
	def __init__(self, rows):
		self.rows = rows
	def __eq__(self, other):
		return self.rows == other.rows
	def display(self):
		for row in self.rows:
			print " ".join(row)
	def width(self):
		return len(self.rows[0])
	def height(self):
		return len(self.rows)
	def cell_at(self, x, y):
		return self.rows[y][x]
	def is_cell_open(self, x, y):
		return self.rows[y][x] == 'o'

def move(board, x, y):
	""" Take a board and a move position and return a new board.
	"""
	if([x,y] == [0,0]): # deathwish
		return board
	if((x >= board.width()) or (y >= board.height())):
		print("Out of bounds!")
		return board
	if(not board.is_cell_open(x, y)):
		print("You can't eat that! (already nommed)")
		return board	
	new_rows = []
	for r in range(board.height()):
		new_row = ['o' for i in range(board.width())]
		for c in range(len(new_row)):
			new_row[c] = board.cell_at(c, r)
			if((r >= y) and (c >= x)):
				new_row[c] = '.'
		new_rows.append(new_row)
	return Board(new_rows)

def negamax(board, depth = 0):
	rx = 0
	cx = 0
	for r in range(board.height()):
		for c in range(board.width()):
			if board.is_cell_open(c, r) and (r + c > 0):
				rx = r
				cx = c
				new_board = move(board, c, r)
				if(negamax(new_board, depth+1)[0]):
					continue
				if(depth == 0):
					board = move(board, c, r)
					print("I choose %d,%d (you're done for!)" %(c, r))
				return [True, board]
	if(depth == 0):
		board = move(board, cx, rx)
		print("I choose %d,%d" %(cx,rx))
		if((rx == 0) and (cx == 0)):
			print "I have lost. :-("
			return None
		else:
			print "I am losing.  :-/"
	return [False, board]

def get_user_move(board):
	while(True):
		user_input = re.sub(r'\s+', '', raw_input('chomp> ').strip())
		if(len(user_input)):
			[x,y] = map(lambda x: int(x), user_input.split(","))
			print("You picked (%d,%d)" %(x,y))
			if([x,y] == [0,0]):
				return [x,y]
			new_board = move(board, x, y)
			if(board != new_board):
				return [x,y]
		board.display()

def main(argv):
	print("Let's play chomp!")
	[width, height] = [DEFAULT_WIDTH, DEFAULT_HEIGHT]
	if(len(argv) > 0):
		width = int(argv[0])
	if(len(argv) > 1):
		height = int(argv[1])
	board = Board.of_size(width, height)
	while(True):
		board.display()
		[x,y] = get_user_move(board)
		if([x,y] == [0,0]):
			print "You're poisoned!  I win!"
			return
		board = move(board, x, y)
		board.display()
		das_komputer_mov = negamax(board)
		if(das_komputer_mov == None):
			break
		board = das_komputer_mov[1]

if __name__ == "__main__":
    main(sys.argv[1:])
