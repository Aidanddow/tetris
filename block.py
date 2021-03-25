#A Class for a block
import random
from shapes import *

class Block:

    def __init__(self,shape_name,colour=(255,255,255)):
        self.default_shape = shapes[shape_name]
        self.shape = shapes[shape_name]
        self.offset_values = offset_values[shape_name]
        self.colour = colour
        self.direction = 0

    def rotate0(self):
        pass

    def rotate90(self):
        #Returns a list of four lists, each containing the element which
        #was at index x for each of the original y-lists
        self.shape = [[self.shape[y-1][x] for y in range(4,0,-1)] for x in range(4)]

    def rotate180(self):
        #Reverse each column and row
        self.shape = [x[::-1] for x in self.shape][::-1]
        

    def rotate270(self):
        #Reverse each column and row
        self.rotate90()
        self.shape = [x[::-1] for x in self.shape][::-1]
        

    def rotate(self):
        self.direction = self.direction % 4
        self.shape = self.default_shape
        rotator_funcs = [self.rotate0, 
                         self.rotate90, 
                         self.rotate180, 
                         self.rotate270]
        rotator = rotator_funcs[self.direction]
        rotator()
        self.correct()
        
    def correct(self): #L is a list
        dy,dx = self.offset_values[self.direction]
        l = self.shape #Make the lines more legible

        if dy == -1:
            self.shape = l[1:] + [l[0]] #Put the first row at the end
        elif dy == 1:
            self.shape = [l[-1]] + l[:3] #Put the last row first

        if dx == -1:
            self.shape = [x[1:] + [x[0]] for x in self.shape] #Put the first column last
        elif dx == 1:
            self.shape = [[x[-1]] + x[:3] for x in self.shape] #Put the last column first

    def display(self):
        print()
        for i in self.shape:
            print(' '.join([str(j) for j in i]))



        
