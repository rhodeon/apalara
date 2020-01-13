import sys

from apalara import Environment


def display_instructions(grid):
    """
    Prints instructions and initial state of world to screen
    :param grid: Environment object
    :return: None
    """

    print("""
            This is a Robot Arm Simulation
            Controls:
            X LEFT Y: Move box X right Y steps 
            X RIGHT Y - Move box X right Y steps
            X ON Y - Place box X on box Y 
            Q - Quit

            Sample:
            B RIGHT 2: Moves B to the right 2 steps
            C ON D: Places C on D
          """)

    grid.display_grid()


def gameplay(grid):
    """
    Requests user input for movement of robot arm
    :param grid: Environment object
    :return: None
    """

    while True:     # loop until the user quits
        command = input("Enter your command: ")

        if command == "q":
            sys.exit()

        else:
            grid.commands(command)

# create an Environment object
cells = Environment([" "] * 16)

# create boxes in world
cells.grid[0] = "D"
cells.grid[4] = "C"
cells.grid[8] = "B"
cells.grid[12] = "A"

display_instructions(cells)
gameplay(cells)
