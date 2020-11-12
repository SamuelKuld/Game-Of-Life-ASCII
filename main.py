import os
from msvcrt import getch
import time


def clear(): 
    print("\n" * 10)


def wait():
    print(">>> ", end="")
    input()


def wait_return():
    print(">>> ", end="")
    return input()


def menu():
    print("Samuel's Game Of Life")
    print("_____________________")
    # TODO Update This Version Per Git Commit
    print("Version 0.0.3")
    wait()


def GetSimulationsList():
    return os.listdir("simulations")


def GetSimulations():
    return "\n".join(GetSimulationsList())


class XCoordinate:
    def __init__(self, position):
        self.type = "empty"
        self.position = position


class YCoordinate:
    def __init__(self):
        self.XCoordinates = []


def getEmptyXRow(width):
    return [XCoordinate(i) for i in range(width)]


def getEmptyYColumns(height, width):
    return [getEmptyXRow(width) for i in range(height)]


class Grid:
    def __init__(self):
        self.plotList = []
        self.plotListLength = len(self.plotList)
        self.height = 0
        self.width = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getGridSize(self):
        return self.height * self.width

    def constructGrid(self, height, width):
        self.setHeight(height)
        self.setWidth(width)
        self.plotList.append(getEmptyYColumns(height, width))

    def isPlotListEmpty(self):
        if self.plotListLength > 0:
            return True
        return False

    def printGrid(self):
        if self.isPlotListEmpty():
            raise Exception("Attempted to print an empty grid.")
        else:
            for y_coordinate in self.plotList:
                for x_coordinate in y_coordinate:
                    for unit in x_coordinate:
                        print(unit.type, end=" ")
                    print("")

    def printGridUnitAndChangeUnit(self, value, x, y, unit, position):
        if value == " ":
            # print(position)
            self.plotList[y][x][position].type = "empty"
            print("", end=' ', flush=True)
        else:
            # print(position)
            self.plotList[y][x][position].type = "full"
            print("", end='.', flush=True)

    def getGrid(self):
        char_in = ""
        for y_unit in range(len(self.plotList)):
            for x_unit in range(len(self.plotList[y_unit])):
                for unit in self.plotList[y_unit][x_unit]:
                    char_in = getch().decode("utf-8")
                    self.printGridUnitAndChangeUnit(char_in, x_unit, y_unit, unit, unit.position)
                print("", flush=True)


def getWidthFixed():
    clear()
    print("That was not a proper value, please input the proper width you'd like the grid to be.")
    return wait_return()


def is_less_than_one(value):
    if value < 1:
        return True
    return False


def getWidth():
    print("What would you like the width of the grid to be?")
    try:
        width = int(wait_return())
        if is_less_than_one(width):
            return False
        return width
    except ValueError:
        return False


def getHeight():
    print("What would you like the height of the grid to be?")
    try:
        height = int(wait_return())
        if is_less_than_one(height):
            return False
        else:
            return height
    except ValueError:
        return False


class Timer:

    def __init__(self):
        self.startTime = 0
        self.end = 0
        self.total = 0

    def start(self):
        self.startTime = time.time()

    def stop(self):
        self.total = time.time() - self.startTime

    def readTime(self):
        return self.total


class TimerList:
    def __init__(self):
        self.timer = Timer()
        self.timeTotals = []

    def start(self):
        self.timer.start()

    def end(self):
        self.timer.stop()

    def iterateTimer(self):
        self.timeTotals.append(self.timer.readTime())

    def totalIterations(self):
        total = 0
        for i in self.timeTotals:
            total += i
        return total

    def averageIterations(self):
        return self.totalIterations() / len(self.timeTotals)


def run():
    grid = Grid()
    grid.constructGrid(10, 20)
    grid.getGrid()
    grid.printGrid()
    input()


if __name__ == "__main__":
    run()
