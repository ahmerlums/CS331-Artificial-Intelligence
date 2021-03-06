'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates a grid as a 2D array of True/False values (True =  traversable). Also returns the dimensions of the grid as a (columns, rows) list.
def myCreateGrid(world, cellsize):
	grid = None
	a = world.getPoints()[2][0]
	b = world.getPoints()[2][1]
	CellsX = int(a/cellsize)
	CellsY = int (b/cellsize)
	grid = numpy.zeros((CellsX+1,CellsY+1))
	for i in range(CellsX):
		for j in range(CellsY):
			grid[i][j]=True
	dimensions = (CellsX, CellsY)

	ListofObstacles = world.getObstacles();
	print len(ListofObstacles)
	for x in range(len(ListofObstacles)):
		for i in range(a):
			for j in range(b):
				if ListofObstacles[x].pointInside((i,j)):
					grid[int((i/cellsize))][int((j/cellsize))]=False
				

	###	ListofObstacles[2]
	### YOUR CODE GOES BELOW HERE ###



	### YOUR CODE GOES ABOVE HERE ###
	return grid, dimensions

