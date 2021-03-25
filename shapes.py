#This file contains all of the default information for the blocks

shapes = {'I':      [[0,1,0,0],  #RED
                     [0,1,0,0],
                     [0,1,0,0],
                     [0,1,0,0]],

          'O':      [[0,0,0,0],  #YELLOW
                     [0,5,5,0],
                     [0,5,5,0],
                     [0,0,0,0]],

          'L':      [[4,4,0,0],  #BLUE
                     [0,4,0,0],
                     [0,4,0,0],
                     [0,0,0,0]],
          
          'J':      [[0,3,3,0],
                     [0,3,0,0],
                     [0,3,0,0],
                     [0,0,0,0]],
          
          'T':      [[0,6,0,0],
                     [6,6,6,0],
                     [0,0,0,0],
                     [0,0,0,0]],
          
          'S':      [[0,0,0,0],
                     [0,2,2,0],
                     [2,2,0,0],
                     [0,0,0,0]],

          'Z':      [[0,7,0,0],
                     [7,7,0,0],
                     [7,0,0,0],
                     [0,0,0,0]]}
            
# These values dictate the offset which the shapes obtain when they rotate
default_offset = [(0,0),(0,-1),(-1,-1),(-1,0)]

offset_values = {'T':default_offset,'L':default_offset,'S':default_offset,
                 'Z':default_offset,'J':default_offset,
                 'I':[(0,0),(0,-1),(0,0),(0,0)],
                 'O':[(0,0),(0,0),(0,0),(0,0)]}
