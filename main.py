"""
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

ON = 255
OFF = 0
vals = [ON, OFF]


# NO LA ESTAS USANDO
def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def liveCells(i, j, grid, N):
    neighbours = 0
    # print("inicial",i,j)
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (i + x == N or j + y == N or (i + x) < 0 or (j + y) < 0):
                continue
            elif (i + x == i and j + y == j):
                continue
            elif (grid[(i + x), (j + y)] == 255):
                neighbours += 1

    return neighbours


def figueres(grid, N, frameNum, nameFile, auxGrid):
    numBlock = 0
    numBeehive = 0
    numLoaf = 0
    numBoat = 0
    numTub = 0
    numBlink = 0
    numBlink2 = 0
    numToad = 0
    numBeacon = 0
    numGlider = 0
    numShip = 0
    tFig = 0
    pBlock = 0
    pBeehive = 0
    pLoaf = 0
    pBoat = 0
    pTub = 0
    pBlinker = 0
    pToad = 0
    pBeacon = 0
    pGlider= 0
    pShip = 0
    numOther = 0
    pOther = 0

    block = np.array([[0, 0, 0, 0],
                      [0, 255, 255, 0],
                      [0, 255, 255, 0],
                      [0, 0, 0, 0]])

    beehive = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 0, 255, 255, 0, 0],
                        [0, 255, 0, 0, 255, 0],
                        [0, 0, 255, 255, 0, 0],
                        [0, 0, 0, 0, 0, 0]])

    loaf = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 255, 255, 0, 0],
                     [0, 255, 0, 0, 255, 0],
                     [0, 0, 255, 0, 255, 0],
                     [0, 0, 0, 255, 0, 0],
                     [0, 0, 0, 0, 0, 0]])

    boat = np.array([[0, 0, 0, 0, 0, ],
                     [0, 255, 255, 0, 0],
                     [0, 255, 0, 255, 0],
                     [0, 0, 255, 0, 0],
                     [0, 0, 0, 0, 0]])

    tub = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 255, 0, 0],
                    [0, 255, 0, 255, 0],
                    [0, 0, 255, 0, 0],
                    [0, 0, 0, 0, 0]])

    blinker = np.array([[0, 0, 0],
                        [0, 255, 0],
                        [0, 255, 0],
                        [0, 255, 0],
                        [0, 0, 0]])

    blinker2 = np.array([[0, 0, 0, 0, 0],
                         [0, 255, 255, 255, 0],
                         [0, 0, 0, 0, 0]])

    toad = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 255, 0, 0],
                     [0, 255, 0, 0, 255, 0],
                     [0, 255, 0, 0, 255, 0],
                     [0, 0, 255, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]])

    toad2 = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 255, 255, 255, 0],
                      [0, 255, 255, 255, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]])

    beacon = np.array([[0, 0, 0, 0, 0, 0],
                       [0, 255, 255, 0, 0, 0],
                       [0, 255, 255, 0, 0, 0],
                       [0, 0, 0, 255, 255, 0],
                       [0, 0, 0, 255, 255, 0],
                       [0, 0, 0, 0, 0, 0]])

    beacon2 = np.array([[0, 0, 0, 0, 0, 0],
                       [0, 255, 255, 0, 0, 0],
                       [0, 255, 0, 0, 0, 0],
                       [0, 0, 0, 0, 255, 0],
                       [0, 0, 0, 255, 255, 0],
                       [0, 0, 0, 0, 0, 0]])

    glider = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 255, 0, 0],
                       [0, 0, 0, 255, 0],
                       [0, 255, 255, 255, 0],
                       [0, 0, 0, 0, 0]])

    glider2 = np.array([[0, 0, 0, 0, 0],
                       [0, 255, 0, 255, 0],
                       [0, 0, 255, 255, 0],
                       [0, 0, 255, 0, 0],
                       [0, 0, 0, 0, 0]])

    glider3 = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 0, 255, 0],
                       [0, 255, 0, 255, 0],
                       [0, 0, 255, 255, 0],
                       [0, 0, 0, 0, 0]])

    glider4 = np.array([[0, 0, 0, 0, 0],
                       [0, 255, 0, 0, 0],
                       [0, 0, 255, 255, 0],
                       [0, 255, 255, 0, 0],
                       [0, 0, 0, 0, 0]])

    ship= np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 255, 0, 0, 255, 0, 0],
                    [0, 0, 0, 0, 0, 255, 0],
                    [0, 255, 0, 0, 0, 255, 0],
                    [0, 0, 255, 255, 255, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

    ship2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 255, 255, 0, 0],
                     [0, 255, 255, 0, 255, 255, 0],
                     [0, 255, 255, 255, 255, 0, 0],
                     [0, 0, 255, 255, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])

    ship3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 255, 255, 255, 255, 0],
                      [0, 255, 0, 0, 0, 255, 0],
                      [0, 0, 0, 0, 255, 0, 0],
                      [0, 255, 0, 0, 255, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]])

    ship4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 255, 255, 0, 0, 0],
                      [0, 255, 255, 255, 255, 0, 0],
                      [0, 255, 255, 0, 255, 255, 0],
                      [0, 0, 0, 255, 255, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]])

    pGeneration = frameNum +1
    print("GENERACIÓN ", pGeneration)

    tBlock = lookBlock(grid, numBlock, block, N, auxGrid)
    tBeehive = lookBeehive(grid, numBeehive, beehive, N, auxGrid)
    tLoaf = lookLoaf(grid, numLoaf, loaf, N, auxGrid)
    tBoat = lookBoat(grid, numBoat, boat, N, auxGrid)
    tTub = lookTub(grid, numTub, tub, N, auxGrid)
    tBlinker1 = lookBlinker(grid, numBlink, blinker, N, auxGrid)
    tBlinker2 = lookBlinker2(grid, numBlink2, blinker2, N, auxGrid)
    tBlinker = tBlinker1 + tBlinker2
    tToad = lookToad(grid, numToad, toad, toad2, N, auxGrid)
    tBeacon = lookBeacon(grid, numBeacon, beacon, beacon2, N, auxGrid)
    tGlider = lookGlider(grid, numGlider, glider, glider2, glider3, glider4, N, auxGrid)
    tShip = lookShip(grid, numShip, ship, ship2, ship3, ship4, N, auxGrid)
    tOther = lookOthers(grid, numOther, auxGrid)



    tFig= tBlock + tBeehive + tLoaf + tBoat + tTub + tBlinker + tToad + tBeacon + tGlider + tShip + tOther

    if(tFig > 0):
        pBlock = (tBlock * 100) / tFig
        pBeehive = (tBeehive * 100) / tFig
        pLoaf = (tLoaf * 100) / tFig
        pBoat = (tBoat * 100) / tFig
        pTub = (tTub * 100) / tFig
        pBlinker = (tBlinker * 100) / tFig
        pToad = (tToad * 100) / tFig
        pBeacon = (tBeacon * 100) / tFig
        pGlider = (tGlider * 100) / tFig
        pShip = (tShip * 100) / tFig
        pOther = (tOther * 100) / tFig

    if(pGeneration >= 1):
        #print(tOther)
        output(tBlock, pBlock, tBeehive, pBeehive, tLoaf, pLoaf, tBoat, pBoat, tTub, pTub,
               tBlinker, pBlinker, tToad, pToad, tBeacon, pBeacon, tGlider, pGlider,
               tShip, pShip, pGeneration, tOther, pOther, nameFile)



    print("Block:", tBlock, " Block percentage:" , pBlock)
    print("Beehive: ", tBeehive, " Beehive percentage:" , pBeehive)
    print("Loaf: ", tLoaf, " Loaf percentage:" , pLoaf)
    print("Boat: ", tBoat, " Boat percentage:" , pBoat)
    print("Tub: ", tTub, " Tub percentage:" , pTub)
    print("Blinker: ", tBlinker, " Blinker percentage:" , pBlinker)
    print("Toad: ", tToad, " Toad percentage:" , pToad)
    print("Beacon: ", tBeacon, " Beacon percentage:" , pBeacon)
    print("Glider:", tGlider, " Glider percentage:" , pGlider)
    print("SpaceShip: ", tShip, " Ship percentage:" , pShip)
    print("Others: ", tOther, " Others:", pOther)

    print("-------------------------")



def lookBlock(grid, numBlock, block, N, auxGrid):

    auxGridBlock = np.ones(N * N).reshape(N, N)
    blockGrid = np.zeros(16).reshape(4, 4)

    for i in range(len(grid)- 3):
        for j in range(len(grid)- 3):
            if (auxGridBlock[i, j] == 1):
                for x in range(0, 4):
                    for y in range(0, 4):
                        blockGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(blockGrid, block)):
                    numBlock +=1
                    for x in range(0, 4):
                        for y in range(0, 4):
                            auxGridBlock[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numBlock

def lookBeehive(grid, numBeehive, beehive, N, auxGrid):
    auxGridBee = np.ones(N * N).reshape(N, N)
    beehiveGrid = np.zeros(30).reshape(5, 6)

    for i in range(len(grid)- 4):
        for j in range(len(grid)- 5):
            if (auxGridBee[i, j] == 1):
                for x in range(0, 5):
                    for y in range(0, 6):
                        beehiveGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(beehiveGrid, beehive)):
                    numBeehive +=1
                    for x in range(0, 5):
                        for y in range(0, 6):
                            auxGridBee[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numBeehive

def lookLoaf(grid, numLoaf, loaf, N, auxGrid):
    auxGridLoaf= np.ones(N * N).reshape(N, N)
    loafGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid)- 5):
        for j in range(len(grid)- 5):
            if (auxGridLoaf[i, j] == 1):
                for x in range(0, 6):
                    for y in range(0, 6):
                        loafGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(loafGrid, loaf)):
                    numLoaf +=1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGridLoaf[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numLoaf

def lookBoat(grid, numBoat, boat, N, auxGrid):
    auxGridBoat = np.ones(N * N).reshape(N, N)
    boatGrid = np.zeros(25).reshape(5, 5)

    for i in range(len(grid)- 4):
        for j in range(len(grid)- 4):
            if (auxGridBoat[i, j] == 1):
                for x in range(0, 5):
                    for y in range(0, 5):
                        boatGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(boatGrid, boat)):
                    numBoat +=1
                    for x in range(0, 5):
                        for y in range(0, 5):
                            auxGridBoat[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numBoat

def lookTub(grid, numTub, tub, N, auxGrid):
    auxGridTub = np.ones(N * N).reshape(N, N)
    tubGrid = np.zeros(25).reshape(5, 5)

    for i in range(len(grid)- 4):
        for j in range(len(grid)- 4):
            if (auxGridTub[i, j] == 1):
                for x in range(0, 5):
                    for y in range(0, 5):
                        tubGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(tubGrid, tub)):
                    numTub +=1
                    for x in range(0, 5):
                        for y in range(0, 5):
                            auxGridTub[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numTub

def lookBlinker(grid, numBlink, blinker, N, auxGrid):
    auxGridBlinker = np.ones(N * N).reshape(N, N)
    blinkGrid = np.zeros(15).reshape(5, 3)

    for i in range(len(grid)- 4):
        for j in range(len(grid)- 2):
            if (auxGridBlinker[i, j] == 1):
                for x in range(0, 5):
                    for y in range(0, 3):
                        blinkGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(blinkGrid, blinker)):
                    numBlink +=1
                    for x in range(0, 5):
                        for y in range(0, 3):
                            auxGridBlinker[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numBlink

def lookBlinker2(grid, numBlink2, blinker2, N, auxGrid):
    auxGridBlinker = np.ones(N * N).reshape(N, N)
    blinkGrid = np.zeros(15).reshape(3, 5)

    for i in range(len(grid)- 2):
        for j in range(len(grid)- 4):
            if (auxGridBlinker[i, j] == 1):
                for x in range(0, 3):
                    for y in range(0, 5):
                        blinkGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(blinkGrid, blinker2)):
                    numBlink2+=1
                    for x in range(0, 3):
                        for y in range(0, 5):
                            auxGridBlinker[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numBlink2

def lookToad(grid, numToad, toad, toad2, N, auxGrid):
    auxGridToad = np.ones(N * N).reshape(N, N)
    toadGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid)- 5):
        for j in range(len(grid)- 5):
            if (auxGridToad[i, j] == 1):
                for x in range(0, 6):
                    for y in range(0, 6):
                        toadGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(toadGrid, toad) or np.array_equal(toadGrid, toad2)):
                    numToad +=1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGridToad[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0


    return numToad

def lookBeacon(grid, numBeacon, beacon, beacon2, N, auxGrid):
    auxGridBeacon = np.ones(N * N).reshape(N, N)
    beaconGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid)- 5):
        for j in range(len(grid)- 5):
            if (auxGridBeacon[i, j] == 1):
                for x in range(0, 6):
                    for y in range(0, 6):
                        beaconGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(beaconGrid, beacon) or np.array_equal(beaconGrid, beacon2)):
                    numBeacon +=1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGridBeacon[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numBeacon

def lookGlider(grid, numGlider, glider, glider2, glider3, glider4, N, auxGrid):
    auxGridGlider = np.ones(N * N).reshape(N, N)
    gliderGrid = np.zeros(25).reshape(5, 5)

    for i in range(len(grid)- 4):
        for j in range(len(grid)- 4):
            if (auxGridGlider[i, j] == 1):
                for x in range(0, 5):
                    for y in range(0, 5):
                        gliderGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(gliderGrid, glider) or np.array_equal(gliderGrid, glider2) or np.array_equal(gliderGrid, glider3) or np.array_equal(gliderGrid, glider4)):
                    numGlider +=1
                    for x in range(0, 5):
                        for y in range(0, 5):
                            auxGridGlider[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numGlider

def lookShip(grid, numShip, ship, ship2, ship3, ship4, N, auxGrid):
    auxGridShip = np.ones(N * N).reshape(N, N)
    shipGrid = np.zeros(42).reshape(6, 7)

    for i in range(len(grid)- 5):
        for j in range(len(grid)- 6):
            if (auxGridShip[i, j] == 1):
                for x in range(0, 6):
                    for y in range(0, 7):
                        shipGrid[x, y] = (grid[i + x, j + y])

                if (np.array_equal(shipGrid, ship) or np.array_equal(shipGrid, ship2) or np.array_equal(shipGrid, ship3) or np.array_equal(shipGrid, ship4)):
                    numShip +=1
                    for x in range(0, 6):
                        for y in range(0, 7):
                            auxGridShip[x + i, y + j] = 0
                            auxGrid[x + i, y + j] = 0

    return numShip

def lookOthers(grid, numOther, auxGrid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i,j] == 255 and auxGrid[i,j] == 1):
                numOther+=1

    return numOther


def initialInput(grid, coord):
    x = []
    for i in range(len(coord)):
        x.append((coord[i].split(',')))

    for i in range(len(coord)):
        a= int(x[i][0])
        b= int(x[i][1])
        grid[a,b] = 255


def output(tBlock, pBlock, tBeehive, pBeehive, tLoaf, pLoaf, tBoat, pBoat, tTub, pTub, tBlinker, pBlinker, tToad, pToad, tBeacon, pBeacon, tGlider, pGlider, tShip, pShip, pGeneration, tOther, pOther, nameFile):
    file = open(nameFile, 'a')
    file.write('GENERATION ' + str(pGeneration) + '\n')
    file.write('Block: ' + str(tBlock) + ' - Block percentage: ' + str(pBlock) + '\n')
    file.write('Beehive: ' + str(tBeehive) + ' - Beehive percentage: ' + str(pBeehive) + '\n')
    file.write('Loaf: ' + str(tLoaf) + ' - Loaf percentage: ' + str(pLoaf) + '\n')
    file.write('Boat: ' + str(tBoat) + ' - Boat percentage: ' + str(pBoat) + '\n')
    file.write('Tub: ' + str(tTub) + ' - Tub percentage: ' + str(pTub) + '\n')
    file.write('Blinker: ' + str(tBlinker) + ' - Blinker percentage: ' + str(pBlinker) + '\n')
    file.write('Toad: ' + str(tToad) + ' - Toad percentage: ' + str(pToad) + '\n')
    file.write('Beacon: ' + str(tBeacon) + ' - Loaf percentage: ' + str(pBeacon) + '\n')
    file.write('Glider: ' + str(tGlider) + ' - Glider percentage: ' + str(pGlider) + '\n')
    file.write('Ship: ' + str(tShip) + ' - Ship percentage: ' + str(pShip) + '\n')
    file.write('Others: ' + str(tOther) + ' - Others percentage: ' + str(pOther) + '\n')
    file.write('-----------------------------------' + '\n')
    file.write('\n')
    file.close()



def update(frameNum, img, grid, N, ax, nameFile, countOutput):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()

    for i in range(len(grid)):
        for j in range(len(grid)):
            neighbours = liveCells(i, j, grid, N)
            # print(neighbours)
            if (grid[i, j] == 255 and neighbours < 2):
                newGrid[i, j] = 0
                # print("menos de 2")
            if (grid[i, j] == 255 and neighbours > 3):
                newGrid[i, j] = 0
                # print("menos de 3")
            if (grid[i, j] == 0 and neighbours == 3):
                newGrid[i, j] = 255
                # print("revivio")

    auxGrid = np.ones(N * N).reshape(N, N)
    figueres(grid, N, frameNum, nameFile, auxGrid)
    # TODO: Implement the rules of Conway's Game of Life


    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    ax.set_title("Generation = {0}".format(frameNum + 1))
    return img,


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    coord = []

    nameFile = 'output.txt'
    file = open(nameFile, 'w')
    file.write('')
    file.close()


    file = open('input.txt', 'r')
    count = 0
    countOutput = 0
    N = 0
    gen = 0

    for linea in file:
        if(count == 0):
            N = int(linea)
        elif(count == 1):
            gen = int(linea)
        else:
            x = linea.rstrip()
            coord.append(x)

        count += 1


    # set grid size

    # set animation update interval
    updateInterval = 100

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    # grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    grid = np.zeros(N * N).reshape(N, N)
    initialInput(grid,coord)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ax, nameFile, countOutput),
                                  frames=gen,
                                  interval=updateInterval,
                                  save_count=50,
                                  repeat=False)

    plt.show()


# call main
if __name__ == '__main__':
    main()
