# Tutaj pisz swój kod, młody padawanie ;-)
import sys , time ,copy
from random import randint
width, height = int(input("podaj szerokość ")), int(input("podaj wysokość "))
nextCells = []
for x  in range(width):
    column = []
    for y in range(height):
        if randint(0,2)== 1 or randint(0,2)== 0:
            column.append("#")
        else:
            column.append(" ")
    nextCells.append(column)
while True:
    print("\n\n\n")
    currentCell = copy.deepcopy(nextCells)
    for y in range(height):
        for x  in range(width):
            print(currentCell[x][y],end="")
        print()
    for x in range(width):
        for y in range(height):
            left=  (x+1)% width
            right = (x-1)% width
            above= (y+1)% height
            under = (y-1)% height
            numNeighbour = 0
            if currentCell[left][above]=="#":
                numNeighbour +=1
            if currentCell[x][above]=="#":
                numNeighbour +=1
            if currentCell[right][above]=="#":
                numNeighbour +=1
            if currentCell[left][y]=="#":
                numNeighbour +=1
            if currentCell[right][y]=="#":
                numNeighbour +=1
            if currentCell[left][under]=="#":
                numNeighbour +=1
            if currentCell[x][under]=="#":
                numNeighbour +=1
            if currentCell[right][under]=="#":
                numNeighbour +=1
            if currentCell[x][y] == "#" and (numNeighbour ==3 or numNeighbour==2):
                nextCells[x][y] ="#"
            elif currentCell[x][y] == " " and numNeighbour==3:
                nextCells[x][y]="#"
            else:
                nextCells[x][y] = " "
    time.sleep(1.2)
