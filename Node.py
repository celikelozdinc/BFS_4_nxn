""" Represents
    tree structure
    for each of puzzles"""
from Table import Table
import datetime

class Node:
    Left = None; Right = None; Up = None;Down = None;
    Parent = None;
    visited = False;


    def __init__(self, k, l, m, n, o, p, r, s, t):
        self.puzzle = Table(a=k, b=l, c=m, d=n, e=o, f=p, g=r, h=s, j=t)

    def insertLeft(self, dictionary):
        print("A new node will be created and inserted to left.")
        self.Left = Node \
                (
                k=dictionary[0, 0], l=dictionary[0, 1], m=dictionary[0, 2],
                n=dictionary[1, 0], o=dictionary[1, 1], p=dictionary[1, 2],
                r=dictionary[2, 0], s=dictionary[2, 1], t=dictionary[2, 2]
                 )

    def insertRight(self, dictionary):
        print("A new node will be created and inserted to right.")
        self.Right = Node \
                (
                k=dictionary[0, 0], l=dictionary[0, 1], m=dictionary[0, 2],
                n=dictionary[1, 0], o=dictionary[1, 1], p=dictionary[1, 2],
                r=dictionary[2, 0], s=dictionary[2, 1], t=dictionary[2, 2]
                )

    def insertDown(self, dictionary):
        print("A new node will be created and inserted to down.")
        self.Down = Node \
                (
                k=dictionary[0, 0], l=dictionary[0, 1], m=dictionary[0, 2],
                n=dictionary[1, 0], o=dictionary[1, 1], p=dictionary[1, 2],
                r=dictionary[2, 0], s=dictionary[2, 1], t=dictionary[2, 2]
                )

    def insertUp(self, dictionary):
        print("A new node will be created and inserted to up.")
        self.Up = Node \
                (
                k=dictionary[0, 0], l=dictionary[0, 1], m=dictionary[0, 2],
                n=dictionary[1, 0], o=dictionary[1, 1], p=dictionary[1, 2],
                r=dictionary[2, 0], s=dictionary[2, 1], t=dictionary[2, 2]
                )

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def constructNeighbours(self):
        if self.puzzle.canLeft():
            print("Node can be shifted to left")
            leftDict = dict(self.puzzle.shiftLeft())
            self.insertLeft(leftDict)
            self.Left.Parent = self
            print("Left Node:")
            self.Left.puzzle.printTable()
        if self.puzzle.canRight():
            print("Node can be shifted to right")
            rightDict = dict(self.puzzle.shiftRight())
            self.insertRight(rightDict)
            self.Right.Parent = self
            print("Right Node:")
            self.Right.puzzle.printTable()
        if self.puzzle.canDown():
            print("Node can be shifted to down")
            downDict = dict(self.puzzle.shiftDown())
            self.insertDown(downDict)
            self.Down.Parent = self
            print("Down Node:")
            self.Down.puzzle.printTable()
        if self.puzzle.canUp():
            print("Node can be shifted to up")
            upDict = dict(self.puzzle.shiftUp())
            self.insertUp(upDict)
            self.Up.Parent = self
            self.Up.puzzle.printTable()

    def findPathToRoot(self, startNode):
        rootOfCurrent = self.Parent
        # Find relation with its parent #
        if rootOfCurrent.Left is not None and rootOfCurrent.Left is self:
            print("LEFT ", u'\N{BLACK LEFT-POINTING TRIANGLE}')
            if rootOfCurrent is startNode:
                print("ACHIEVED START STATE!")
                return ;
            else:
                rootOfCurrent.findPathToRoot(startNode)
        if rootOfCurrent.Right is not None and rootOfCurrent.Right is self:
            print("RIGHT ", u'\N{BLACK RIGHT-POINTING TRIANGLE}')
            if rootOfCurrent == startNode:
                print("ACHIEVED START STATE!")
                return;
            else:
                rootOfCurrent.findPathToRoot(startNode)
        if rootOfCurrent.Up is not None and rootOfCurrent.Up == self:
            print("UP", u'\N{BLACK UP-POINTING TRIANGLE}')
            if rootOfCurrent == startNode:
                print("ACHIEVED START STATE!")
                return;
            else:
                rootOfCurrent.findPathToRoot(startNode)
        if rootOfCurrent.Down is not None and rootOfCurrent.Down == self:
            print("DOWN", u'\N{BLACK DOWN-POINTING TRIANGLE}')
            if rootOfCurrent == startNode:
                print("ACHIEVED START STATE!")
                return;
            else:
                rootOfCurrent.findPathToRoot(startNode)



def main():
    """Python's built-in List data structure
    comes bundled with methods to simulate both stack and queue operations."""
    PQ = []
    #startNode = Node(2, 8, 3, 1, 6, 4, 7, 0, 5)
    #finishNode = Node(1, 2, 3, 8, 0, 4, 7, 6, 5)
    startNode = Node(0, 2, 3, 1, 4, 5, 8, 7, 6)
    finishNode = Node(1, 2, 3, 8, 0, 4, 7, 6, 5)
    PQ.append(startNode)
    startNode.visited = True
    startNode.puzzle.printTable()

    """ Store Timestamp When We Started To BFS Traversal"""
    startTS  = datetime.datetime.now()
    while len(PQ) is not 0:
        removedFromQueue = PQ.pop(0)
        removedFromQueue.puzzle.appendToVisitedPuzzles(removedFromQueue.puzzle.matrix)
        removedFromQueue.puzzle.printTable()
        if removedFromQueue == finishNode:
            print("ACHIEVED GOAL STATE!")
            finishTS = datetime.datetime.now()
            print("Start Time: {}:{}.{}.{} ".format(startTS.hour, startTS.minute, startTS.second, startTS.microsecond))
            print("Finish Time: {}:{}.{}.{} ".format(finishTS.hour, finishTS.minute, finishTS.second, finishTS.microsecond))
            print("Processing Time: {}".format(finishTS.microsecond - startTS.microsecond))
            removedFromQueue.findPathToRoot(startNode)
            return ;

        removedFromQueue.constructNeighbours()
        if removedFromQueue.Left is not None:
            print("Left node exists.")
            if removedFromQueue.Left.visited is False:
                print("Left node is not traversed.")
                removedFromQueue.Left.visited = True
                PQ.append(removedFromQueue.Left)
        if removedFromQueue.Right is not None:
            print("Right node exists.")
            if removedFromQueue.Right.visited is False:
                print("Right node is not traversed.")
                removedFromQueue.Right.visited = True
                PQ.append(removedFromQueue.Right)
        if removedFromQueue.Up is not None:
            print("Up node exists.")
            if removedFromQueue.Up.visited is False:
                print("Up node is not traversed.")
                removedFromQueue.Up.visited = True
                PQ.append(removedFromQueue.Up)
        if removedFromQueue.Down is not None:
            print("Down node exists.")
            if removedFromQueue.Down.visited is False:
                print("Down node is not traversed.")
                removedFromQueue.Down.visited = True
                PQ.append(removedFromQueue.Down)






main()