import numpy as np
from time import time


puzzle = [[5,3,0, 0,7,0, 0,0,0],
          [6,0,0, 1,9,5, 0,0,0],
          [0,9,8, 0,0,0, 0,6,0],

          [8,0,0, 0,6,0, 0,0,3],
          [4,0,0, 8,0,3, 0,0,1],
          [7,0,0, 0,2,0, 0,0,6],

          [0,6,0, 0,0,0, 2,8,0],
          [0,0,0, 4,1,9, 0,0,5],
          [0,0,0, 0,8,0, 0,7,9]]


def get_possible(board, x, y) :
	which_square = (x//3, y//3)
	possible = [i for i in range(1, 10)]
	if board[y][x] != 0 :
		return True

	for i in range(which_square[1]*3, which_square[1]*3+3) :
		for j in range(which_square[0]*3, which_square[0]*3+3) :
			if board[i][j] in possible :
				possible.pop(possible.index(board[i][j]))
	for e in board[y]:
		if e in possible :
			possible.pop(possible.index(e))
	for i in range(9) :
		if board[i][x] in possible :
			possible.pop(possible.index(board[i][x]))


	return possible


def predictionBoardSetup(puzzle) :
	predictions = [[0 for __ in range(9)] for _ in range(9)]
	
	for i in range(9) :
		for j in range(9) :
			predictions[i][j] = get_possible(puzzle, j, i)
	return predictions

def solve(puzzle) :

	z = True

	i = 0

	while z:
		pred = predictionBoardSetup(puzzle)
		
		
		for x in range(9) :
			for c in range(9) : 
				if type(pred[x][c]) == list :
					if len(pred[x][c]) == 1 :
						puzzle[x][c] = pred[x][c][0]
						pred = predictionBoardSetup(puzzle)

		r = True
		for x in puzzle :
			for e in x :
				if e == 0: 
					r = False
		if r :
			z = False
	for el in puzzle :
		print(el)
		
		


solve(puzzle)

