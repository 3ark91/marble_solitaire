"""Marble Solitaire Solver
Author - Mark Hay
Contact - mjhay91@gmail.com
Date - 11/10/2022
"""
import copy

import numpy as np

# 0 invalid, 1 marble, 2 empty
start_state = [[0, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 1, 1, 0, 0],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [0, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 1, 1, 0, 0]]

test_state = [[0, 0, 2, 2, 2, 0, 0],
               [0, 0, 2, 2, 2, 0, 0],
               [2, 1, 2, 2, 2, 2, 2],
               [2, 1, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 2],
               [0, 0, 2, 2, 2, 0, 0],
               [0, 0, 2, 2, 2, 0, 0]]


def print_state(state):
    print("----------------------------------------")
    for row in state:
        print(row)
    print("----------------------------------------")

def count_marbles(state):
    num_marbles = 0
    rows, cols = np.shape(start_state)

    for y in range(cols):
        for x in range(rows):
            if state[y][x] == 1:
                num_marbles += 1
    return num_marbles

def get_valid_moves(state):
    valid_moves = []

    rows, cols = np.shape(state)

    for y in range(cols):
        for x in range(rows):
            if state[y][x] == 1:

                # detect edge
                try: #move right
                    if x+2 > 6 or state[y][x+2] == 0:
                        pass
                    else:
                        if state[y][x+1] == 1 and state[y][x+2] == 2:
                            valid_moves.append(((y, x), (y, x+1), (y, x+2)))
                except IndexError:
                    pass
                try: # move left
                    if x-2 < 0 or state[y][x-2] == 0:
                        pass
                    else:
                        if state[y][x-1] == 1 and state[y][x-2] == 2:
                            valid_moves.append(((y, x), (y, x-1), (y, x-2)))
                except IndexError:
                    pass
                try: #move down
                    if y+2 > 6 or state[y+2][x] == 0:
                        pass
                    else:
                        if state[y+1][x] == 1 and state[y+2][x] == 2:
                            valid_moves.append(((y, x), (y+1, x), (y+2, x)))
                except IndexError:
                    pass
                try: # move up
                    if y-2 < 0 or state[y-2][x] == 0:
                        pass
                    else:
                        if state[y-1][x] == 1 and state[y-2][x] == 2:
                            valid_moves.append(((y, x), (y-1, x), (y-2, x)))
                except IndexError:
                    pass

    return valid_moves


def make_move(state, start, eliminated, finish):

    next_state = np.array(state)

    next_state[start[0]][start[1]] = 2
    next_state[eliminated[0]][eliminated[1]] = 2
    next_state[finish[0]][finish[1]] = 1

    return next_state


def main():

    queue = []
    visited = []

    possible_moves = {}

    queue.append(np.array(start_state))

    while queue:
        state = queue.pop()
        visited.append(np.array(state))

        moves = get_valid_moves(state)

        # if len(moves) == 0:
        #     print("deadend")
        #     print_state(state)

        for move in moves:
            start, eliminated, finish = move[0], move[1], move[2]
            new_state = np.array(make_move(state, start, eliminated, finish))
            queue.append(new_state)


            if count_marbles(new_state) == 1:
                print("found the solution")
                print("final state")
                print_state(new_state)
                quit()

        if len(visited) % 10000 == 0:
            print(f'{len(visited)}: {len(moves)} possible moves, {count_marbles(state)} marbles remain')
            print_state(state)



if __name__ == '__main__':
    main()


