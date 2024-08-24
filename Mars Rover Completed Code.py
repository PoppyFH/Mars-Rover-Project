class Rover:
    def __init__(self, x, y, direction, roverDisplayValue):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__roverDisplayValue = roverDisplayValue
        

    def move(self):
        if self.__direction == "N":
            self.__y += 1
        elif self.__direction == "E":
            self.__x += 1
        elif self.__direction == "S":
            self.__y -= 1
        elif self.__direction == "W":
            self.__x -= 1

    def lettersToNum(self, directions, direction):
        counter = 0
        found = False
        while counter < 4 and found == False:
            if directions[counter] == direction:
                found = True
            else:
                counter = counter + 1
        return counter

    def numToLetters(self, directions, direction):
        direction = directions[direction]
        return direction
        

    def turnLeft(self):
        directions = ["N", "E", "S", "W"]
        current_direction = self.lettersToNum(directions,self.__direction)
        self.__direction = current_direction - 1
        if self.__direction == -1:
            self.__direction = 3
        self.__direction = self.numToLetters(directions, self.__direction)


    def turnRight(self):
        directions = ["N", "E", "S", "W"]
        current_direction = self.lettersToNum(directions,self.__direction)
        self.__direction = current_direction + 1
        if self.__direction == 4:
            self.__direction = 0
        self.__direction = self.numToLetters(directions, self.__direction)
        

    def getRoverPosition(self):
        return [self.__x, self.__y, self.__direction]

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getDirection(self):
        return self.__direction

    def getRoverDisplayValue(self):
        return self.__roverDisplayValue

    def setX(self,new_x):
        self.__x = new_x

    def setY(self,new_y):
        self.__y = new_y

    def setDirection(self,new_direction):
        self.__direction = new_direction
    

class Plateau:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__rover_positions = []

    def addRover(self, rover):
        valid_position = True
        if self.isValid(rover.getX(), rover.getY()) == True and self.isOccupied(rover.getX(), rover.getY()) == False:
            self.__rover_positions.append([rover, rover.getX(), rover.getY(), rover.getDirection(), rover.getRoverDisplayValue()])
            return valid_position
        else:
            print("ERROR : You entered an invalid position on the plateau, nothing has been changed.")
            valid_position = False
            return valid_position
            

    def isValid(self, x, y):
        if x <= self.__width and x >= 0 and y <= self.__height and y >= 0:
            return True
        else:
            return False
        

    def isOccupied(self, x, y):
        if len(self.__rover_positions) == 1:
            return False
        else:
            counter = 0
            found = False
            while counter < len(self.__rover_positions) and found == False:
                if self.__rover_positions[counter][1] == x and self.__rover_positions[counter][2] == y:
                    found = True
                else:
                    counter += 1
            return found
                

    def checkMoveValid(self, rover):
        next_x = rover.getX()
        next_y = rover.getY()
        direction = rover.getDirection()
        if direction == "N":
            next_y += 1
        elif direction == "E":
            next_x += 1
        elif direction == "S":
            next_y -= 1
        elif direction == "W":
            next_x -= 1          

        if self.isValid(next_x, next_y) == True and self.isOccupied(next_x, next_y) == False:
            return True
        else:
            return False

    def updateRoverPosition(self, rover):

        current_x = rover.getX()
        current_y = rover.getY()
        counter = 0
        found = False
        
        while counter <len(self.__rover_positions) and found == False:
            if self.__rover_positions[counter][1] == current_x and self.__rover_positions[counter][2] == current_y:
                found = True
                
            else:
                counter += 1
        self.__rover_positions[counter-1] = [rover, rover.getX(), rover.getY(), rover.getDirection(), rover.getRoverDisplayValue()]
        

    def getRoverPositions(self):
        return self.__rover_positions
        
    def displayPlateau(self):
        plateau = []
        for i in range(-1,self.__height+ 2):
            row = []
            if i == -1:
                row.append("." + " ")
            else:
                row.append(str(i) + " ")
            for j in range(1,self.__width + 2):
                if i != -1:
                    row.append("0" + " ")
                else:
                    for num in range(0,self.__width + 2):
                        num = str(num)
                        row.append(num + " ")
            plateau.append(row)
        

        for k in range(0, len(self.__rover_positions)):
            x = self.__rover_positions[k][1]
            y = self.__rover_positions[k][2]
            roverDisplayValue = self.__rover_positions[k][4]

            plateau[y+ 1][x + 1] = roverDisplayValue + " "

        for l in range(self.__height + 1, 0 - 1, -1):
            string = ""
            for m in range(0, self.__width + 2):
                string = string + plateau[l][m]
            print(string)

###### MAIN CODE STARTS HERE #######
import time

def digitInList(ListLength, Digit):
    List = []
    for i in range(0,ListLength + 1):
        List.append(str(i))

    found = False
    counter = 0
    while counter < len(List) and found == False:
        if List[counter] == Digit:
            found = True
        else:
            counter += 1
    return found

def enterMovementCommands():
    print("")
    print("Please enter the path that you want the rover to take, use this format: LMLMLMRMM (L = turn left, R = turn right, M = move in the direction you are facing")
    unsplit_movement = input()
    movement = []
    for i in range(0, len(unsplit_movement)):
            movement.append(unsplit_movement[i])
                        
    valid = isEntryValid(movement, 0)
                
    while valid == False:
        print("One of the movement instructions you entered was invalid.")
        print("Please enter the path you want the rover to take again, using the designated format: LMLMLMRMM (L = turn left, R = turn right, M = move in the direction you are facing")
        unsplit_movement = input()
        movement = []
        for i in range(0, len(unsplit_movement)):
            movement.append(unsplit_movement[i])
                    
        valid = isEntryValid(movement, 0)

    completeMovement(movement)

def completeMovement(movement):
    currentX = rover.getX()
    currentY = rover.getY()
    currentDirection = rover.getDirection()
    m = 0
    available = True
    while m < len(movement) and available == True:
        if movement[m] == "L":
            rover.turnLeft()
        elif movement[m] == "R":
            rover.turnRight()
        elif movement[m] == "M":
            if plateau.checkMoveValid(rover) == True:
                rover.move()
            else:
                available = False
                print("")
                print("You sent your rover on an unavailable path, your rover has now been reset to its origional position. Please enter a valid path for the rover to take.")
                print("")
                rover.setX(currentX)
                rover.setY(currentY)
                rover.setDirection(currentDirection)
                enterMovementCommands()
        m += 1
    coordinates = rover.getRoverPosition()
    print("The final coordinates and heading of rover", rover_display_value, "are shown below:")
    print(" ", coordinates[0], " ", coordinates[1], " ", coordinates[2])
    plateau.updateRoverPosition(rover)


def isEntryValid(movement,counter):
    valid = True
    while valid == True and counter < len(movement):
        if movement[counter] == "L" or movement[counter] == "R" or movement[counter] == "M":
            valid = True
        else:
            valid = False
        counter += 1
    return valid


done = False
plateauCreated = False
roverList = []

while done == False:
    if plateauCreated == False:
        print("")
        print("Please start by creating a plateau, use this format (Make sure that X and Y are both integers) : X Y")
        values = input().split(" ")

        correctValues = False
        while correctValues == False:
            if len(values) == 2:
                correctValues = True
            else:
                print("")
                print("The values you entered were not in the correct format")
                time.sleep(1)
                print("Please start by creating a plateau, use this format : X Y")
                values = input().split(" ")

        width = int(values[0])
        height = int(values[1])       
        plateau = Plateau(width, height)
        plateauCreated = True
        display_values = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    else:
        print("")
        print("------Mars Rover Menu------")
        print("What would you like to do?")
        print("--------------------------")
        time.sleep(1)
        print("1. Add a new rover to the plateau")
        time.sleep(1)
        print("2. View the plateau")
        time.sleep(1)
        print("3. Quit")
        print("")

        chosen= int(input())

        if chosen == 1:
            print("")
            print("Enter the coordinates and direction of the new rover in this format: x y direction  (direction should be represented as N = North, E = East, S = South, W = West)")
            values = input().split(" ")

            correct = False

            while correct == False:
                if len(values) == 3:
                    confirmed1 = digitInList(width, values[0])
                    confirmed2 = digitInList(height, values[1])
                    if values[2].upper() == "N" or values[2].upper() == "E" or values[2].upper() == "S" or values[2].upper() == "W":
                        confirmed3 = True
                    else:
                        confirmed3 = False
                    if confirmed1 == True and confirmed2 == True and confirmed3 == True:
                        correct = True
                    else:
                        print("")
                        print("One of the rover values you entered was not valid. Please enter some valid coordinates using the designated format")
                        print("")
                        print("")
                        print("Enter the coordinates and direction of the new rover in this format: x y direction")
                        values = input().split(" ")
                else:
                    print("")
                    print("You entered the rover values using an incorrect format. Please enter some valid coordinates using the designated format")
                    print("")
                    print("")
                    print("Enter the coordinates and direction of the new rover in this format: x y direction")
                    values = input().split(" ")
            
            
            x = int(values[0])
            y = int(values[1])
            direction = values[2].upper()
            
            roverNumber = len(roverList)
            if roverNumber < 26:
                rover_display_value = display_values[roverNumber]
            else:
                display_values.append(str(roverNumber - 26))
                rover_display_value = display_values[roverNumber]
                
            
            rover = Rover(x, y, direction, rover_display_value)
            go_or_no = plateau.addRover(rover)

            if go_or_no == True:
                roverList.append(roverNumber)
                print("")
                print("This rover will be represented by the value", rover_display_value, "on your plateau.")
                enterMovementCommands()
            else:
                print("")
                print("Please try to add that rover again, within the specified plateau coordinates.")

        elif chosen == 2:
            print("")
            print("Your plateau is shown below:")
            print("")
            plateau.displayPlateau()

        else:
            done = True
