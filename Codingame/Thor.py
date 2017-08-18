mport sys 
import math

original_x = int(raw_input)
original_y = int(raw_input)
aim_x = int(raw_input)
aim_y = int(raw_input)


while 1:
    dir = ""

    if original_x < aim_x:
    oringinal_x += 1
    dir += 'E'
    elif original_x > aim_x:
    original_x -= 1
    dir = 'W'

    if original_y < aim_y:
    original_y += 1
    dir = 'N'
    else:
    original_y -= 1
    dir = 'S'

    print 'The direction is:' + dir
