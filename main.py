"""Marble Solitaire Solver
Author - Mark Hay
Contact - mjhay91@gmail.com
Date - 11/10/2022
"""
import copy

import numpy as np
from MS_Node import MS_Node
from tkinter import *

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


def display_and_exit(solution_node):
    solution_sequence = []

    print(f"found solution")
    traverse_state = solution_node

    while traverse_state.get_parent():
        traverse_state.print_state()
        solution_sequence.append(traverse_state.get_last_move())
        traverse_state = traverse_state.get_parent()


    solution_sequence.reverse()
    for step in solution_sequence:
        print(step)
    exit()


def build_tree(node):

    if node.get_num_marbles() == 1:
        solution_node = node
        display_and_exit(solution_node)

    if len(node.get_moves()) == 0:
        return

    for move in node.get_moves():
        start, eliminated, finish = move[0], move[1], move[2]
        new_state = make_move(node.get_state(), start, eliminated, finish)
        new_node = MS_Node(new_state)
        new_node.set_parent(node)
        new_node.set_last_move(move)
        node.add_child(new_node)
        build_tree(new_node)



def main():

    root = MS_Node(start_state)


    build_tree(root)
    print("Tree built")






if __name__ == '__main__':
    main()


