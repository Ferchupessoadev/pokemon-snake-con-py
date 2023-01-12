import random
import time
import readchar
import os
import platform




POS_NAME_TRAINER = 0
POS_X_TRAINER = 1
POS_Y_TRAINER = 2
POS_NAME_POKEMON = 3
POS_LIFE_POKEMON = 4
POS_ATTACKS = 5
POS_ATTACK_1 = 0
POS_ATTACK_2 = 1
POS_ATTACK_3 = 2

TAMANIO_BARRA_VIDA = 10

POS_X = 0
POS_Y = 1

command_to_clear_the_screen = None
if platform.system() == "Linux" : command_to_clear_the_screen = "clear"
else : command_to_clear_the_screen = "cls"

trainers_and_coordinates = [["Lucas",17,4,"squirtle",80,["placaje","burbuja","pistola agua"]],["Marcos",4,7,"Caterpie",60,["araniazo","placaje","pistola veneno"]],["Juan",15,0,"Starmie",100,["rapidez","burbuja","pistola agua"]],["Javier",2,4,"riolu",90,["At.rapido","ultrapunio","esfera aural"]]]
trainer_ash_position = [4,0]

def create_map_dimensions():
    # create map\\\
    map = '''\     
###                    
###     ###############
###     ###############
                       
                       
###                    
###     ###############
###     ###############
###     ###############
#######################\
    '''
    map = [list(row) for row in map.split("\n")]
    map.pop(0)
    # create map\\\

    MAP_WIDTH = len(map[0])
    MAP_HEIGHT = len(map)
    return [map,MAP_WIDTH,MAP_HEIGHT];


def show_map(map,MAP_WIDTH,MAP_HEIGHT):
    objects = []
    char_to_draw = " "
    print("+"+ "-"*MAP_WIDTH + "+")   
    for coordinate_y in range(MAP_HEIGHT):
        print("|",end="")
        char_to_draw = " "
        for coordinate_x in range(MAP_WIDTH):
            trainer_in_cell = None
            if map[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"            
            elif map[coordinate_y][coordinate_x] == " ":
                char_to_draw = " "

            for trainers in trainers_and_coordinates:
                if trainers[POS_X_TRAINER] == coordinate_x and trainers[POS_Y_TRAINER] == coordinate_y:
                    char_to_draw = "*"
                    trainer_in_cell = trainers
            
            if coordinate_x == trainer_ash_position[POS_X] and coordinate_y == trainer_ash_position[POS_Y]:
                char_to_draw = "@"
                if trainer_in_cell:
                    trainer = trainer_in_cell
                    objects.append(trainer)
                    trainers_and_coordinates.remove(trainer_in_cell)
        
            print("{}".format(char_to_draw),end="")
        print("|")
    print("+"+ "-"*MAP_WIDTH + "+")

    return objects



def show_life(vida_pikachu,life_pokemon_trainer,VIDA_INCIAL_PIKACHU,VIDA_INCIAL_POKEMON,trainer):
    barra_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INCIAL_PIKACHU)
    barra_vida_pokemon = int(life_pokemon_trainer * TAMANIO_BARRA_VIDA / VIDA_INCIAL_POKEMON)
    cantidad_de_vida_pikachu = "*" * barra_vida_pikachu
    cantidad_de_espacios_pikachu = " " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu )
    print("pikachu:  [{}{}] ({}/{})".format(cantidad_de_vida_pikachu ,cantidad_de_espacios_pikachu ,vida_pikachu,VIDA_INCIAL_PIKACHU))
    cantidad_de_vida_pokemon = "*" * barra_vida_pokemon
    cantidad_de_espacios_pokemon = " " * (TAMANIO_BARRA_VIDA - barra_vida_pokemon)
    print("{}:  [{}{}] ({}/{})\n".format(trainer[POS_NAME_POKEMON],cantidad_de_vida_pokemon,cantidad_de_espacios_pokemon,life_pokemon_trainer,VIDA_INCIAL_POKEMON))



def start_pokemon_battle(trainer):
    os.system(command_to_clear_the_screen)
    print("el entrenado {} te reta a un lucha".format(trainer[POS_NAME_TRAINER]))
    print("El entrenador saca a {} ".format(trainer[POS_NAME_POKEMON]))
    print("ve por el pikachu\n")
    VIDA_INCIAL_PIKACHU = 120
    VIDA_INCIAL_POKEMON = trainer[POS_LIFE_POKEMON]
    vida_pikachu = VIDA_INCIAL_PIKACHU
    life_pokemon_trainer = trainer[POS_LIFE_POKEMON]
    while vida_pikachu > 0 and life_pokemon_trainer > 0:
        attack_trainer = random.randint(0,2)
        if attack_trainer == 0:
            vida_pikachu -= 10
            print("{} usa {}".format(trainer[POS_NAME_POKEMON],trainer[POS_ATTACKS][POS_ATTACK_1]))
        
        elif attack_trainer == 1:
            vida_pikachu -= 9
            print("{} usa {}".format(trainer[POS_NAME_POKEMON],trainer[POS_ATTACKS][POS_ATTACK_2]))
        
        elif attack_trainer == 2:
            vida_pikachu -= 12
            print("{} usa {}".format(trainer[POS_NAME_POKEMON],trainer[POS_ATTACKS][POS_ATTACK_3]))
        if vida_pikachu < 0:
            vida_pikachu = 0
        
        show_life(vida_pikachu,life_pokemon_trainer,VIDA_INCIAL_PIKACHU,VIDA_INCIAL_POKEMON,trainer)

        input("enter para continuar...") 
        if vida_pikachu > 0:
            my_attack = None
            while my_attack not in ["a","A","b","B","c","C","d","D"]:
                my_attack = input("Elige un ataque.\n"
                            "A - Onda voltio\n"
                            "B - Bola voltio\n"
                            "C - Rayo\n"
                            "D - MegaTrueno\n")
            if my_attack in ["a","A"]:
                life_pokemon_trainer -= 10  
                print("pikachu usa onda voltio")
            elif my_attack in ["b","B"]:
                life_pokemon_trainer -= 12
                print("pikachu usa Bola voltio")
            elif my_attack in ["c","C"]:
                life_pokemon_trainer -= 15
                print("pikachu usa rayo")
            elif my_attack in ["d","D"]:
                life_pokemon_trainer -= 25 
                print("pikachu usa Mega Trueno")
            if life_pokemon_trainer < 0:
                life_pokemon_trainer = 0
            
            print("")

            show_life(vida_pikachu,life_pokemon_trainer,VIDA_INCIAL_PIKACHU,VIDA_INCIAL_POKEMON,trainer)
            input("enter para continuar...")
            os.system(command_to_clear_the_screen)    
            if life_pokemon_trainer <= 0:       
                print("El entranador ash gana la pelea")
                time.sleep(2)
                os.system(command_to_clear_the_screen)
            elif vida_pikachu <= 0:
                end_game = True
                print("el entrador {} gana la batalla".format(trainer[POS_NAME_TRAINER]))   
                return end_game

def move_player(letter_for_move,map,MAP_HEIGHT):
    end_game = False
    if letter_for_move == "d":
        trainer_ash_position[POS_X] += 1
        
        if trainer_ash_position[POS_X] > 22:
            trainer_ash_position[POS_X] -= 1
        if map[trainer_ash_position[POS_Y]][trainer_ash_position[POS_X]] == "#":
            trainer_ash_position[POS_X] -= 1
    
    elif letter_for_move == "a":
        trainer_ash_position[POS_X] -= 1
        if map[trainer_ash_position[POS_Y]][trainer_ash_position[POS_X]] == "#" or trainer_ash_position[POS_X] < 0:
            trainer_ash_position[POS_X] += 1
    
    
    elif letter_for_move == "w":
        trainer_ash_position[POS_Y] -= 1

        if map[trainer_ash_position[POS_Y]][trainer_ash_position[POS_X]] == "#" or trainer_ash_position[POS_Y] < 0:
            trainer_ash_position[POS_Y] += 1
    
    
    elif letter_for_move == "s":
        trainer_ash_position[POS_Y] += 1

        if map[trainer_ash_position[POS_Y]][trainer_ash_position[POS_X]] == "#" or trainer_ash_position[POS_Y] > MAP_HEIGHT:
            trainer_ash_position[POS_Y] -= 1
    elif letter_for_move in ["q","Q"]:
        end_game = True
    return end_game

def main():
    dimensions_and_map = create_map_dimensions()
    map = dimensions_and_map[0]
    MAP_WIDTH = dimensions_and_map[1]
    MAP_HEIGHT = dimensions_and_map[2]
    end_game = False
    while not end_game:
        os.system(command_to_clear_the_screen)
        objects = show_map(map,MAP_WIDTH,MAP_HEIGHT)
        if objects:
            trainer = objects[0]
            end_game = start_pokemon_battle(trainer)
            os.system(command_to_clear_the_screen) 
            if len(trainers_and_coordinates) == 0:
                end_game = True
                print("\t\t\tFelicidades has ganado a todos los entrenadores pokemon")
                print("\t\t\tGame over")
                time.sleep(4)
            elif end_game:
                print("\t\t\tAsh se desmayo del susto por perder")
                print("\t\t\tGame over")
        else:
            letter_for_move = readchar.readchar()
            end_game = move_player(letter_for_move,map,MAP_HEIGHT)
            
    if end_game:
        os.system("clear")

if __name__ == "__main__":
    main()
