import random

machine_movements = [
    "cable",
    "leg press",
    "chest press",
    "hip adductor",
    "leg extension",
]


def move():
    print(random.choice(machine_movements))


if __name__ == "__main__":
    move()  # leg press


"""
When we run
>>> python3 machine.exercise.py
move() function gets invoked and a random machine movement prints out.

namemain block helps Python understand if the program is being directly run
from the command-line (as entry point to the Python program) instead of being
imported as a module.

"""
