import os
from msvcrt import getch
import time
import copy


def clear(): 
    os.system("cls")


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
    print("Version 0.2.1")
    wait()


def GetSimulationsList():
    return os.listdir("simulations")


def GetSimulationsString():
    return "\n".join(GetSimulationsList())


class XCoordinate:
    def __init__(self):
        self.type = "empty"
        self.character_type = " "


def getEmptyXRow(width):
    return [XCoordinate() for i in range(width)]


def getPlotList(width, height):
    return [getEmptyXRow(width) for i in range(height)]


class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0
        
        self.listIndexX = 0 
        self.listIndexY = 0 

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setUnit(self, x, y):
        self.setX(x)
        self.setY(y)


class Grid:

    def __init__(self):
        self.plotList = []
        self.height = 0
        self.width = 0
        self.character_input = ""

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getGridSize(self):
        return self.height * self.width

    def plotListConstruction(self, height, width):
        self.plotList = getPlotList(width, height)

    def constructGrid(self, width, height):
        self.setHeight(height)
        self.setWidth(width)
        self.plotListConstruction(self.height, self.width)

    def getPlotListLength(self):
        return len(self.plotList)

    def isPlotListEmpty(self):
        if self.getPlotListLength() == 0:
            return True
        else:
            return False

    def printGrid(self):
        if self.isPlotListEmpty():
            raise Exception("Attempted to print an empty grid.")
        else:
            for y_unit in range(len(self.plotList)):
                for x_unit in range(len(self.plotList[y_unit])):
                    print(self.plotList[y_unit][x_unit].character_type, end="")
                print("")

    def setPlotEmpty(self, x, y):
        self.plotList[y][x].type = "empty"
        self.plotList[y][x].character_type = " "
        # print("", end=' ', flush=True)

    def setPlotFull(self, x, y):
        self.plotList[y][x].type = "full"
        self.plotList[y][x].character_type = "."
        # print("", end='.', flush=True)

    def isCharInEmpty(self):
        if self.character_input == " " or self.character_input == "" or self.character_input == "\n":
            return True
        else:
            return False

    def printGridUnitAndChangeUnit(self, x, y):
        self.getUserInputPlot()
        if self.character_input == " ":
            self.setPlotEmpty(x, y)
        else:
            self.setPlotFull(x, y)

    def getUserInputPlot(self):
        self.character_input = getch().decode("utf-8")

    def getGrid(self):
        for y_unit in range(len(self.plotList)):
            for x_unit in range(len(self.plotList[y_unit])):
                for unit in self.plotList[y_unit][x_unit]:
                    self.printGridUnitAndChangeUnit(x_unit, y_unit)
                print("", flush=True)

    def getUnitType(self, x, y):
        try:
            return self.plotList[y][x].type
        except IndexError:
            raise Exception(
                "Attempted to get a plot that was not in proper bounds - Plot(%s , %s) - PlotListSize(%s , %s )" % (x, y, len(self.plotList[y]), len(self.plotList)))

    def getUnit(self, x, y):
        try:
            return self.plotList[y][x]
        except IndexError:
            raise Exception(
                "Attempted to get a plot that was not in proper bounds - Plot(%s , %s) - PlotListSize(%s , %s )" % (x, y, len(self.plotList[y]), len(self.plotList)))

    def setUnitType(self, x, y, unit_type):
        try:
            if unit_type == "full":
                self.plotList[y][x].type = unit_type
                self.plotList[y][x].character_type = "."
            else:
                self.plotList[y][x].type = unit_type
                self.plotList[y][x].character_type = " "
        except IndexError:
            raise Exception(
                "Attempted to change a plot that was not in proper bounds - PlotGiven(%s , %s) - PlotListSize(%s , %s )" % (x, y, len(self.plotList[y]), len(self.plotList)))

    @staticmethod
    def getUnitBoolean(unit):
        if unit.type == "full":
            return True
        else:
            return False

    def getUnitBelow(self, x, y):
        try:
            return self.getUnit(x, y + 1)
        except IndexError:
            raise Exception(
                "Attempted to get a plot that was not in proper bounds - PlotGiven(%s , %s) - PlotListSize(%s , %s ) - PlotProcessed(%s , %s)" % (x, y, len(self.plotList[y]), len(self.plotList), x, y + 1))

    def getUnitAbove(self, x, y):
        try:
            return self.getUnit(x, y - 1)
        except IndexError:
            raise Exception(
                "Attempted to get a plot that was not in proper bounds - PlotGiven(%s , %s) - PlotListSize(%s , %s ) - PlotProcessed(%s , %s)" % (x, y, len(self.plotList[y]), len(self.plotList), x, y - 1))

    def getUnitRight(self, x, y):
        try:
            return self.getUnit(x + 1, y)
        except IndexError:
            raise Exception(
                "Attempted to get a plot that was not in proper bounds - PlotGiven(%s , %s) - PlotListSize(%s , %s ) - PlotProcessed(%s , %s)" % (x, y, len(self.plotList[y]), len(self.plotList), x + 1, y))

    def getUnitLeft(self, x, y):
        try:
            return self.getUnit(x - 1, y)
        except IndexError:
            raise Exception(
                "Attempted to get a plot that was not in proper bounds - PlotGiven(%s , %s) - PlotListSize(%s , %s ) - PlotProcessed(%s , %s)" % (x, y, len(self.plotList[y]), len(self.plotList), x - 1, y))

    def getTouchingUnits(self, x, y):
        units_touching = []
        if not y >= self.height - 1:
            units_touching.append([self.getUnitBelow(x, y), [x, y + 1]])
        if not y <= 0:
            units_touching.append([self.getUnitAbove(x, y), [x, y - 1]])
        if not x <= 0:
            units_touching.append([self.getUnitLeft(x, y), [x - 1, y]])
        if not x >= self.width - 1:
            units_touching.append([self.getUnitRight(x, y), [x + 1, y]])
        return units_touching

    def tic(self):
        new_grid = copy.deepcopy(self)
        for y in range(len(self.plotList)):
            for x in range(len(self.plotList[y])):
                if self.getUnit(x, y).type == "full":
                    for touching_units in self.getTouchingUnits(x, y):
                        new_grid.setPlotFull(touching_units[1][0], touching_units[1][1])
        self.plotList = new_grid.plotList


def getWidthFixed():
    clear()
    print("That was not a proper value, please input the proper width you'd like the grid to be.")
    return wait_return()


def is_less_than_one(value):
    if value < 1:
        return True
    else:
        return False


def getWidth():
    print("What would you like the width of the grid to be?")
    try:
        width = int(wait_return())
        if is_less_than_one(width):
            return False
        else:
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
    grid.constructGrid(200, 100)
    grid.setPlotFull(100, 75)
    grid.printGrid()
    wait()
    for i in range(100):
        clear()
        grid.tic()
        grid.printGrid()
        time.sleep(.1)
    wait()


if __name__ == "__main__":
    run()
