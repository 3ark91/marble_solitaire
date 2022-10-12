import numpy as np


class MS_Node:

    def __init__(self, state):
        self.state = state
        self.parent = None
        self.moves = None
        self.children = []
        self.num_marbles = 50
        self.last_move = None

        self.set_valid_moves()
        self.set_num_marbles()

    def get_state(self):
        return self.state

    def set_state(self, s):
        self.state = s

    def get_last_move(self):
        return self.last_move

    def set_last_move(self, m):
        self.last_move = m

    def get_parent(self):
        return self.parent

    def set_parent(self, p):
        self.parent = p

    def get_moves(self):
        return self.moves

    def set_moves(self, m):
        self.moves = m

    def get_children(self):
        return self.children

    def add_child(self, c):
        self.children.append(c)

    def get_num_marbles(self):
        return self.num_marbles

    def set_valid_moves(self):
        valid_moves = []

        rows, cols = np.shape(self.state)

        for y in range(cols):
            for x in range(rows):
                if self.state[y][x] == 1:

                    # detect edge
                    try:  # move right
                        if x + 2 > 6 or self.state[y][x + 2] == 0:
                            pass
                        else:
                            if self.state[y][x + 1] == 1 and self.state[y][x + 2] == 2:
                                valid_moves.append(((y, x), (y, x + 1), (y, x + 2)))
                    except IndexError:
                        pass
                    try:  # move left
                        if x - 2 < 0 or self.state[y][x - 2] == 0:
                            pass
                        else:
                            if self.state[y][x - 1] == 1 and self.state[y][x - 2] == 2:
                                valid_moves.append(((y, x), (y, x - 1), (y, x - 2)))
                    except IndexError:
                        pass
                    try:  # move down
                        if y + 2 > 6 or self.state[y + 2][x] == 0:
                            pass
                        else:
                            if self.state[y + 1][x] == 1 and self.state[y + 2][x] == 2:
                                valid_moves.append(((y, x), (y + 1, x), (y + 2, x)))
                    except IndexError:
                        pass
                    try:  # move up
                        if y - 2 < 0 or self.state[y - 2][x] == 0:
                            pass
                        else:
                            if self.state[y - 1][x] == 1 and self.state[y - 2][x] == 2:
                                valid_moves.append(((y, x), (y - 1, x), (y - 2, x)))
                    except IndexError:
                        pass

        self.set_moves(valid_moves)

    def set_num_marbles(self):
        num_marbles = 0
        rows, cols = np.shape(self.state)

        for y in range(cols):
            for x in range(rows):
                if self.state[y][x] == 1:
                    num_marbles += 1
        self.num_marbles = num_marbles

    def print_state(self):
        print("----------------------------------------")
        for row in self.state:
            print(row)
        print("----------------------------------------")