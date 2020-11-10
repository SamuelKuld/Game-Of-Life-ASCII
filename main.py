import os


def clear():
    os.system("cls")


def wait():
    print(">>> " , end="")
    input()
    clear()


def run():
    print("Completed")
    clear()


if __name__ == "__main__":
    run()
