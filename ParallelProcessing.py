""" Represents
    parallel solutions
    for nxn puzzles
"""
import threading, time
from Node import Node

class ParallelProcessing:
    # Global Variable #
    mutex = threading.Lock()
    startNode = None;
    finishNode = None;

    def __init__(self, sNode, fNode):
        self.startNode = sNode
        self.finishNode = fNode
        threading.Thread.__init__(self)

    def solution_4_left(self):
        with ParallelProcessing.mutex:
            print("Start Solution For Left Tree.")
            self.startNode.Left.BFS_Serial(self.finishNode)
            print("End Solution for Left Tree.")


    def solution_4_right(self):
        with ParallelProcessing.mutex:
            print("Start Solution For Right Tree.")
            self.startNode.Right.BFS_Serial(self.finishNode)
            print("End Solution for Right Tree.")


    def solution_4_up(self):
        with ParallelProcessing.mutex:
            print("Start Solution For Up Tree.")
            self.startNode.Up.BFS_Serial(self.finishNode)
            print("End Solution for Up Tree.")


    def solution_4_down(self):
        with ParallelProcessing.mutex:
            print("Start Solution For Down Tree.")
            self.startNode.Down.BFS_Serial(self.finishNode)
            print("End Solution for Down Tree.")



def main():
    # startNode = Node(2, 8, 3, 1, 6, 4, 7, 0, 5)
    # finishNode = Node(1, 2, 3, 8, 0, 4, 7, 6, 5)
    startNode = Node(0, 2, 3, 1, 4, 5, 8, 7, 6)
    finishNode = Node(1, 2, 3, 8, 0, 4, 7, 6, 5)

    #startNode.BFS_Serial(finishNode)


    PP = ParallelProcessing(startNode, finishNode)

    startNode.constructNeighbours()
    if startNode.Left is not None:
        print("Left Node exists.")
        startNode.Left.puzzle.printTable()
        threading.Thread(name='solution_4_left', target=PP.solution_4_left()).start()
    if startNode.Right is not None:
        print("Right Node exists.")
        startNode.Right.puzzle.printTable()
        threading.Thread(name='solution_4_right', target=PP.solution_4_right()).start()
    if startNode.Up is not None:
        print("Up Node exists.")
        startNode.Up.puzzle.printTable()
        threading.Thread(name='solution_4_up', target=PP.solution_4_up()).start()
    if startNode.Down is not None:
        print("Down Node exists.")
        startNode.Down.puzzle.printTable()
        threading.Thread(name='solution_4_down', target=PP.solution_4_down()).start()


main()



