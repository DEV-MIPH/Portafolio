import os
import random
import readchar

POS_X = 0
POS_Y = 1

numbers_map_objects = 6

obstacle_definition = """\
###     #####   #####
###     #####   #####
###     #####   #####
###              ### 
###              ### 
##########  ######   
##########  ######   
##########  ######   
##########  ######   
##########       #   
###########      #   
############    ##   
#####         ###    
#####  ###########   
#####  ###########   \
"""
# Create map obstacle:

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

# Random objects on the map#
end_game = False

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)
my_position = [3, 1]
map_objects = []

# main loop
while not end_game:

    while len(map_objects) < numbers_map_objects and not end_game:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

# Draw map
    print("+" + "_" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):

        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if object_in_cell == my_position:
                    map_objects.remove(object_in_cell)

            if obstacle_definition[coordinate_y][coordinate_x] == '#':
                char_to_draw = '#'

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "_" * MAP_WIDTH * 3 + "+")


# Ask user where he wants to move

# direction = input("¿Donde te quieres mover?[WASD]: ")

    direction = readchar.readchar().decode()
    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True

    os.system("cls")