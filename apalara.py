class Environment:
    def __init__(self, grid):
        """
        :param grid: list which contains all boxes
        """

        self.grid = grid
        self.initialize = 0

    def display_grid(self):
        """
        Displays current layout of the grid
        :return: None
        """

        self.gravity()
        print(self.grid[0] + "|" + self.grid[1] + "|" + self.grid[2] + "|" + self.grid[3])
        print("-+-+-+-")
        print(self.grid[4] + "|" + self.grid[5] + "|" + self.grid[6] + "|" + self.grid[7])
        print("-+-+-+-")
        print(self.grid[8] + "|" + self.grid[9] + "|" + self.grid[10] + "|" + self.grid[11])
        print("-+-+-+-")
        print(self.grid[12] + "|" + self.grid[13] + "|" + self.grid[14] + "|" + self.grid[15])
        print()

    @staticmethod
    def column(index):
        """
        :param index: position of box on grid
        :return: column of index
        """

        if index in [0, 4, 8, 12]:  # far left
            return 1

        elif index in [1, 5, 9, 13]:
            return 2

        elif index in [2, 6, 10, 14]:
            return 3

        elif index in [3, 7, 11, 15]:   # far right
            return 4

    @staticmethod
    def row(index):
        """
        :param index: position of box on grid
        :return: row of index
        """

        if index in [0, 1, 2, 3]:   # top
            return 1

        elif index in [4, 5, 6, 7]:
            return 2

        elif index in [8, 9, 10, 11]:
            return 3

        elif index in [12, 13, 14, 15]:     # bottom
            return 4

    def gravity(self):
        """
        Mimics gravity to make boxes fall if nothing is beneath them
        :return: None
        """

        count = 0

        while count < 4:
            length = len(self.grid)
            for i in range(length - 1, -1, -1):   # iterate backwards from 15 to 0 in order to emulate gravity
                if i < 12:  # not bottom row
                    if self.grid[i + 4] == " ":  # no box directly below current cell
                        # move the box to the cell underneath
                        self.grid[i + 4] = self.grid[i]
                        self.grid[i] = " "
            count += 1

    def check_clear(self, x):
        """
        :param x: specified box
        :return: True if no box is on x
        """

        x_index = self.grid.index(x)
        above_x = x_index - 4

        if self.row(x_index) == 1:  # top row
            return True

        if self.grid[above_x] != " ":   # a box is on x
            return False
        else:
            return True

    def check_empty(self, index):
        """
        :param index: specified box
        :return: True if no box occupies that index of the grid
        """

        if self.grid[index] == " ":     # no box occupies it
            return True

    def move_left(self, x, distance):
        """
        Moves x left by the specified distance
        :param x: specified box
        :param distance: distance to move x left
        :return: None
        """

        # check if x is an existing box
        if x not in self.grid:
            print("Box", x, "does not exist")

        else:
            x_index = self.grid.index(x)    # current location of x
            next_x_location = x_index - distance    # potential next location of x

            if not self.check_clear(x):
                print("A box is on", x + ", remove it to continue.")

            elif self.column(x_index) == 1:
                print("Box", x, "is at the left extreme, it cannot be moved further.")

            elif self.row(x_index) != self.row(next_x_location):    # distance is out of bounds
                print("Box", x, "cannot be moved to the left", distance, "steps.")

            elif not self.check_empty(next_x_location):
                print("That position is already occupied by another box.")

            else:
                self.grid[next_x_location] = x
                self.grid[x_index] = " "

        print()
        self.display_grid()

    def move_right(self, x, distance):
        """
        Moves x right by the specified distance
        :param x: specified box
        :param distance: distance to move x right
        :return: None
        """

        # check if x is an existing box
        if x not in self.grid:
            print("Box", x, "does not exist")

        else:
            x_index = self.grid.index(x)    # current location of x
            next_x_location = x_index + distance    # potential next location of x

            if not self.check_clear(x):
                print("A box is on", x + ", remove it to continue.")

            elif self.column(x_index) == 4:
                print("Box", x, "is at the right extreme, it cannot be moved further.")

            elif self.row(x_index) != self.row(next_x_location):    # distance is out of bounds
                print("Box", x, "cannot be moved to the right", distance, "steps.")

            elif not self.check_empty(next_x_location):
                print("That position is already occupied by another box.")

            else:
                self.grid[next_x_location] = x
                self.grid[x_index] = " "

        print()
        self.display_grid()

    def place_on(self, x, y):
        """
        Places x on y if there are no obstacles
        :param x: specified box
        :param y: specified box
        :return: None
        """

        # check x and y are existing boxes
        if x not in self.grid:
            print("Box", x, "does not exist")

        elif y not in self.grid:
            print("Box", y, "does not exist")

        else:
            x_index = self.grid.index(x)
            above_y = self.grid.index(y) - 4    # the cell directly above y

            if not self.check_clear(x):
                print("A box is on", x + ", remove it to continue.")

            elif not self.check_clear(y):
                print("Another box is on", y + ".")

            elif x_index == above_y:
                print(x, "is already at that position.")

            else:
                self.grid[above_y] = x
                self.grid[x_index] = " "

        print()
        self.display_grid()

    def commands(self, command):
        """
        :param command: command for operation of robot arm
        :return: None
        """

        # split command into a list to obtain indexes of arguments
        command = command.split(" ")

        if len(command) != 3:   # for an invalid command
            print("Command not recognized.")
            print()

        else:
            first = command[0]     # specified box
            action = command[1]      # LEFT, RIGHT, ON
            second = command[2]     # distance or specified box

            # check if LEFT is the action specified
            if action.lower() == "left":
                # ensure the distance is an integer
                try:
                    second = int(second)
                except ValueError:
                    print("The distance has to be an integer.")
                    print()
                else:
                    self.move_left(first, second)

            # check if RIGHT is the action specified
            elif action.lower() == "right":
                # ensure the distance is an integer
                try:
                    second = int(second)
                except ValueError:
                    print("The distance has to be an integer.")
                    print()
                else:
                    self.move_right(first, second)

            # check if ON is the action specified
            elif action.lower() == "on":
                self.place_on(first, second)

            else:   # for invalid commands
                print("Command not recognized.")
                print()
