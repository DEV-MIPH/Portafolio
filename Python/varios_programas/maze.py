import readchar
import os
import random 

POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJETS = 11
obstacle_definitions = """\
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
#####  ##############
#####################\
"""

my_posicition = [6, 7]
map_objects = []
tail_length = 0
tail = []
lose = False

obstacle_definitions = [list(row) for row in obstacle_definitions.split("\n")]
MAP_WIDTH = len(obstacle_definitions[0])
MAP_HEIGHT = len(obstacle_definitions[1])



while len(map_objects) < NUM_OF_MAP_OBJETS:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
    if new_position not in map_objects and new_position != my_posicition:
        map_objects.append(new_position)
    



while lose == False:
    print( "+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            
            char_to_draw = " "

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                elif map_object[POS_X] == my_posicition[POS_X] and map_object[POS_Y] == my_posicition[POS_Y]:
                    delete = [map_object[POS_X], map_object[POS_Y]]
                    map_objects.remove(delete)
                    tail_length += 1
                    if len(map_objects) < 11:
                        while len(map_objects) < 11:
                            new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
                            if new_position not in map_objects and new_position != my_posicition and new_position not in tail:
                                map_objects.append(new_position)
                        
                        
                        
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                elif tail_piece[POS_X] == my_posicition[POS_X] and tail_piece[POS_Y] == my_posicition[POS_Y]:
                    
                    lose = True
            
                    
            if coordinate_x == my_posicition[POS_X] and coordinate_y == my_posicition[POS_Y]:
                char_to_draw = "@"
            
            if obstacle_definitions[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
                
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print( "+" + "-" * MAP_WIDTH * 3 + "+")
    print(f"El largo de la cola es {tail_length}")
    print(f"La cantidad de objetos es {len(map_objects)}")

    #direction = input("Donde te quieres mover? (W/A/S/D): ")
    direction = readchar.readchar().decode()

    if direction == "w":
        tail.insert(0, my_posicition.copy())
        tail = tail[:tail_length]
        my_posicition[POS_Y] -= 1
        my_posicition[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_posicition.copy())
        tail = tail[:tail_length]
        my_posicition[POS_Y] += 1
        my_posicition[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_posicition.copy())
        tail = tail[:tail_length]
        my_posicition[POS_X] -= 1
        my_posicition[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_posicition.copy())
        tail = tail[:tail_length]
        my_posicition[POS_X] += 1
        my_posicition[POS_X] %= MAP_WIDTH
        

    '''
    if my_posicition[POS_X] < 0:
        my_posicition[POS_X] = MAP_WIDTH -1
    if my_posicition[POS_Y] < 0:
        my_posicition[POS_Y] = MAP_HEIGHT - 1
    if my_posicition[POS_X] > MAP_WIDTH - 1:
        my_posicition[POS_X] = 0
    if my_posicition[POS_Y] > MAP_HEIGHT - 1:
        my_posicition[POS_Y] = 0
    '''

    os.system("cls")
print("Game Over")