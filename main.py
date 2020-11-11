import os


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
    print("Version 0.0.2")
    wait()


def GetSimulationsList():
    return os.listdir("simulations")


def GetSimulations():
    return "\n".join(GetSimulationsList())


class Plot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = "empty"


class Grid:
    def __init__(self):
        self.plotList = []

    def PlotInList(self, plot):
        if plot in self.plotList:
            return True
        return False

    def AddPlot(self, plot):
        if self.PlotInList(plot):
            raise Exception("Attempted to add a plot that was already in the plot list")
        else:
            self.plotList.append(plot)

    def RemovePlot(self, plot):
        if self.PlotInList(plot):
            del self.plotList[self.plotList.index(plot)]
        else:
            raise Exception("Attempted to remove a plot that does not exist")


def run():
    menu()


if __name__ == "__main__":
    run()
