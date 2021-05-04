[![DOI](https://zenodo.org/badge/364381948.svg)](https://zenodo.org/badge/latestdoi/364381948)

# 15-puzzle

The 15 puzzle (also called Game of Fifteen or Mystic Square) is a game where 15
square tiles numbered from 1 to 15 are placed in a frame that is 4 by 4 tiles.
There is one tile that is left unoccupied where it is possible to slide one
orthogonally adjacent tile. The goal of the player is, starting in a position
where tiles are shuffled, to sort the tiles on the frame by sliding one tile at
a time.

This repository contains code to play the game but more importantly it
implements an A* game solver.

Example grid:

	 1 |  5 |  2 |  3
	---+----+----+---
	 4 | 12 |  6 |  7
	---+----+----+---
	 8 |  9 | 14 | 11
	---+----+----+---
	10 | 13 |    | 15

Solution found by the solver:

	13, 9, 12, 4, 8, 12, 9, 10, 12, 9, 10, 13, 14, 10, 9, 8, 4, 5, 1
