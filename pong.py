
import os
import time
import random
import msvcrt



class Yard():
    def __init__(self, yard):
        self.yard = yard


    def create_yard(self, yard, size_x, size_y):
        counter = 0
        for x in range(size_y):
            for y in range(size_x):
                yard.append(" ")
                counter += 1


        return yard


    def create_ball(self):
        self.yard[295] = '@'
        return 295

    def move_ball_on_yard(self, index):

        for i in range(len(yard)):
            if yard[i] == "@":
                self.yard[i] = ' '

            self.yard[index] = '@'
        return self.yard

    def create_bats(self, yard, width, bat):
        half_yard = round(len(yard)/2)
        bat_start_index = []

        if (bat == "player_bat"):
            bat_start_index.append(round(half_yard - (width / 2) - width))
            bat_start_index.append(round(half_yard - width / 2))
            bat_start_index.append(round(half_yard - (width / 2) + width))
            bat_start_index.append(round(half_yard - (width / 2) + width*2))

        if(bat == "enemy_bat"):
            bat_start_index.append(round(half_yard+(width/2)-width-1))
            bat_start_index.append(round(half_yard+(width/2))-1)
            bat_start_index.append(round(half_yard+(width/2) + width)-1)
            bat_start_index.append(round(half_yard+ (width / 2) + width*2)-1)

        return bat_start_index

    def move_bat_on_yard(self, index_bat, index_another_bat):

        for i in range(len(self.yard)):
            for j in range(len(index_another_bat)):
                if(self.yard[i] != '@'):
                    self.yard[i] = ' '
                    yard[index_bat[j]] = "|"
                    yard[index_another_bat[j]] = "|"



    def print_yard(self):
        os.system('cls')

        print("$ " * (size_x + 2))
        counter = 0
        for i in range(size_y):

            print("$ ", end="")
            for j in range(size_x):
                print(yard[counter], end=" ")
                counter += 1
            print("$")

        print("$ " * (size_x + 2))




class Ball:
    def __init__(self, arr, index):
        self.index = index
        self.max_size = len(arr)
        self.dir = random.choice(['wa', 'as', 'sd', 'dw'])
        self.arr = arr

    def respawn_ball(self, width):
        for i in range(len(self.arr)):
            if(self.arr[i] == "@" and i % width == 0):
                self.arr[i] = " "
                self.index = 165

        return index_ball

    def increase_ball(self, bat1_index, bat2_index, bat_dir, width):

        for i in range(len(bat1_index)):

            if (self.index-1 == bat1_index[i]):
                self.dir = random.choice(['a', 'dw', 'sd'])
                if (self.dir == 'dw'):
                    self.index -= width - 1
                if (self.dir == 'sd'):
                    self.index += width + 1
                if (self.dir == 'a'):
                    self.dir = 'd'
                    self.index += 1

            elif (self.index+1 == bat2_index[i]):
                self.dir = random.choice(['a', 'wa', 'as'])
                if (self.dir == 'wa'):
                    self.index -= width - 1
                if (self.dir == 'as'):
                    self.index += width - 1
                if (self.dir == 'd'):
                    self.dir = 'a'
                    self.index -= 1

            if(self.index-width+1 == bat1_index[i]):

                if(bat_dir == 'w'):
                    self.dir = 'dw'
                if (bat_dir == 's'):
                    self.dir = 'sd'

            elif(self.index+width+1 == bat2_index[i]):

                if (self.dir == 'w'):
                    self.dir = 'wa'
                if (self.dir == 's'):
                    self.dir = 'as'


        return self.dir

    def move(self, width):
        if (self.index > width):
            if (self.dir == 'w'):
                self.index = self.index - width
        if (self.index < self.max_size - width):
            if (self.dir == 's'):
                self.index = self.index + width
        if (self.index % width != 0):
            if (self.dir == 'a'):
                self.index = self.index - 1
        if(self.index % width != width-1):
            if (self.dir == 'd'):
                self.index = self.index + 1
        logic = self.index >= width and self.index < self.max_size - width and self.index % width != 0 and self.index % width != width-1

        if (logic):
            if (self.dir == 'wa'):
                self.index = self.index - width - 1
            if (self.dir == 'as'):
                self.index = self.index + width - 1
            if (self.dir == 'sd'):
                self.index = self.index + width + 1
            if (self.dir == 'dw'):
                self.index = self.index - width + 1
        else:
            if(self.index == 0 or self.index == width-1 or self.index == self.max_size - width or self.index == self.max_size-1):

                if(self.index == 0):

                    self.dir = 'sd'
                    self.index = self.index + width + 1
                if(self.index == width-1):
                    self.dir = 'as'
                    self.index = self.index + width - 1
                if(self.index == self.max_size - width):
                    self.dir = 'dw'
                    self.index = self.index - width + 1
                if(self.index == self.max_size-1):
                    self.dir = 'wa'
                    self.index = self.index - width - 1

            else:

                if(self.index < width):

                    if (self.dir == 'wa'):
                        self.dir = 'as'
                        self.index = self.index + width - 1
                    if (self.dir == 'dw'):
                        self.dir = 'sd'
                        self.index = self.index + width + 1


                elif(self.index > self.max_size - width):

                    if (self.dir == 'as'):
                        self.dir = 'wa'
                        self.index = self.index - width - 1
                    if (self.dir == 'sd'):
                        self.dir = 'dw'
                        self.index = self.index - width + 1

                elif(self.index % width == 0):

                    if (self.dir == 'wa'):
                        self.dir = 'dw'
                        self.index = self.index - width + 1
                    if (self.dir == 'as'):
                        self.dir = 'sd'
                        self.index = self.index + width + 1
                elif(self.index % width == width-1):

                    if (self.dir == 'dw'):
                        self.dir = 'wa'
                        self.index = self.index - width - 1

                    if (self.dir == 'sd'):
                        self.dir = 'as'
                        self.index = self.index + width - 1


        return self.index
class Bat:
    def __init__(self, yard, bat_start_index, mode):
        self.max_size = len(yard)
        self.bat_index = bat_start_index

        self.mode = mode
    def move(self, dir, width, bat_index):


        if(dir == 'w'  and self.mode == "player_bat"):
            if(not (bat_index[0] == 0)):
                for i in range(len(bat_index)):
                    bat_index[i] -= width
        if (dir == 'w' and self.mode == "enemy_bat"):
            if (not (bat_index[0] == width - 1)):
                for i in range(len(bat_index)):
                    bat_index[i] -= width

        if(dir == 's' and self.mode == "player_bat"):
            if (not (bat_index[len(bat_index)-1] == self.max_size - width)):
                for i in range(len(bat_index)):
                    bat_index[i] += width
        if (dir == 's' and self.mode == "enemy_bat"):
            if (not (bat_index[len(bat_index)-1] == self.max_size-1)):
                    for i in range(len(bat_index)):
                        bat_index[i] += width


        return bat_index



yard = []
size_x, size_y = 30, 11

yard1 = Yard(yard)
yard = yard1.create_yard(yard, size_x, size_y)
ball_index = yard1.create_ball()
ball1 = Ball(yard, ball_index)

bat1_start_index = yard1.create_bats(yard, size_x, "player_bat")
bat2_start_index = yard1.create_bats(yard, size_x, "enemy_bat")

bat1 = Bat(yard, bat1_start_index, "player_bat")
bat2 = Bat(yard, bat2_start_index, "enemy_bat")

bat2_index = bat2_start_index
bat1_index = bat1_start_index

while True:
    time.sleep(0.1)

    while msvcrt.kbhit():
        dir = str(msvcrt.getch())[2]



    ball1.increase_ball(bat1_index, bat2_index, dir, size_x)

    index_ball = ball1.move(size_x)

    yard1.move_ball_on_yard(index_ball)
    ball1.respawn_ball(size_x)
    bat1_index = bat1.move(dir, size_x, bat1_index)
    bat2_index = bat2.move(dir, size_x, bat2_index)
    print(bat2_index)

    yard1.move_bat_on_yard(bat2_index, bat1_index)

    yard1.print_yard()
    print(index_ball)





