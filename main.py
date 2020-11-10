import os


def clear():
    os.system("cls")


def wait():
    print(">>> ", end="")
    input()


def wait_return():
    print(">>> ", end="")
    return input()


def run():
    wait()
    clear()


if __name__ == "__main__":
    run()
