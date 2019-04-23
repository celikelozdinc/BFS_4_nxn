""" Represent
    puzzle schema
    in nxn skeleton"""

class Table:
    """static variables"""
    visitedPuzzles = []
    numberOfPuzzles = 0

    def __init__(self, **kwargs):
        self.matrix = dict()
        self.matrix[0,0] = kwargs.get('a')
        self.matrix[0,1] = kwargs.get('b')
        self.matrix[0,2] = kwargs.get('c')
        self.matrix[1,0] = kwargs.get('d')
        self.matrix[1,1] = kwargs.get('e')
        self.matrix[1,2] = kwargs.get('f')
        self.matrix[2,0] = kwargs.get('g')
        self.matrix[2,1] = kwargs.get('h')
        self.matrix[2,2] = kwargs.get('j')
        """ Store current situation"""
        self.increasePuzzleSize()

    @staticmethod
    def increasePuzzleSize():
        Table.numberOfPuzzles = Table.numberOfPuzzles + 1

    @staticmethod
    def appendToVisitedPuzzles(dictionary):
        Table.visitedPuzzles.append(dictionary)

    def __eq__(self, other):
        return  (self.matrix[0,0] == other.matrix[0,0] and
                self.matrix[0,1] == other.matrix[0,1] and
                self.matrix[0,2] == other.matrix[0,2] and
                self.matrix[1,0] == other.matrix[1,0] and
                self.matrix[1,1] == other.matrix[1,1] and
                self.matrix[1,2] == other.matrix[1,2] and
                self.matrix[2,0] == other.matrix[2,0] and
                self.matrix[2,1] == other.matrix[2,1] and
                self.matrix[2,2] == other.matrix[2,2])

    def printTable(self):
        print("Total number of puzzles: {}".format(self.numberOfPuzzles))
        print ("{:_^30}".format("Puzzle Situation"))
        print("{:<12s}{:<6s}{:<6s}{:<6s}".format("", "Col0", "Col1","Col2"))
        print("{:<12s}{:^6s}{:^6s}{:^6s}".format("Row0", str(self.matrix[0,0]), str(self.matrix[0,1]),str(self.matrix[0,2])))
        print("{:<12s}{:^6s}{:^6s}{:^6s}".format("Row1", str(self.matrix[1,0]), str(self.matrix[1,1]),str(self.matrix[1,2])))
        print("{:<12s}{:^6s}{:^6s}{:^6s}".format("Row2", str(self.matrix[2,0]), str(self.matrix[2,1]),str(self.matrix[2,2])))

    def shiftLeft(self):
        """Create new dictionary"""
        # Copy to new dictionary #
        shiftedMatrix = {**self.matrix}
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        leftRow = row; leftColumn = column -1; leftCell = self.matrix[leftRow, leftColumn]
        """ Swap values of the cells"""
        shiftedMatrix[row, column] = leftCell
        shiftedMatrix[leftRow, leftColumn] = 0
        return shiftedMatrix

    def canLeft(self):
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        if column is 0:
            print("Empty cell is in the position: " , row , "," , column)
            print("Can not change puzzle position. Can not go left.")
            return False
        elif column is not 0:
            shiftedMatrix = self.shiftLeft()
            if shiftedMatrix in Table.visitedPuzzles:
                print("Visited cells contains duplicate information. Prohibited.")
                #print("Left row: {} Left col: {}"  .format(leftRow, leftColumn))
                #print("Visited cells: ")
                #print(self.visitedCells)
                return False
            else:
                return True

    def shiftRight(self):
        """Create new dictionary"""
        shiftedMatrix = {**self.matrix}
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        rightRow = row; rightColumn = column +1; rightCell = self.matrix[rightRow, rightColumn]
        """ Swap values of the cells"""
        shiftedMatrix[row, column] = rightCell
        shiftedMatrix[rightRow, rightColumn] = 0
        return shiftedMatrix

    def canRight(self):
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        if column is 2:
            print("Empty cell is in the position: " , row , "," , column)
            print("Can not change puzzle position. Can not go right.")
            return False
        elif column is not 2:
            shiftedMatrix = self.shiftRight()
            if shiftedMatrix in Table.visitedPuzzles:
                print("Visited cells contains duplicate information. Prohibited.")
                #print("Right row: {} Right col: {}".format(rightRow, rightColumn))
                #print("Visited cells: ")
                #print(self.visitedCells)
                return False
            else:
                return True

    def shiftUp(self):
        """Create new dictionary"""
        shiftedMatrix = {**self.matrix}
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        upRow = row -1 ; upColumn = column ; upCell = self.matrix[upRow, upColumn]
        """ Swap values of the cells"""
        shiftedMatrix[row, column] = upCell
        shiftedMatrix[upRow, upColumn] = 0
        return shiftedMatrix

    def canUp(self):
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        if row is 0:
            print("Empty cell is in the position: " , row , "," , column)
            print("Can not change puzzle position. Can not go up.")
            return False
        elif row is not 0:
            shiftedMatrix = self.shiftUp()
            if shiftedMatrix in Table.visitedPuzzles:
                #print("Visited cells contains duplicate information. Prohibited.")
                #print("Up row: {} Up col: {}".format(upRow, upColumn))
                #print("Visited cells: ")
                #print(self.visitedCells)
                return False
            else:
                return True

    def shiftDown(self):
        """Create new dictionary"""
        shiftedMatrix = {**self.matrix}
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        downRow = row +1 ; downColumn = column ; downCell = self.matrix[downRow, downColumn]
        """ Swap values of the cells"""
        shiftedMatrix[row, column] = downCell
        shiftedMatrix[downRow, downColumn] = 0
        return shiftedMatrix

    def canDown(self):
        l = self.findEmptyCell(); row = l[0]; column = l[1]
        if row is 2:
            print("Empty cell is in the position: " , row , "," , column)
            print("Can not change puzzle position. Can not go down.")
            return False
        elif row is not 2:
            shiftedMatrix = self.shiftDown()
            if shiftedMatrix in Table.visitedPuzzles:
                #print("Visited cells contains duplicate information. Prohibited.")
                #print("Down row: {} Down col: {}".format(downRow, downColumn))
                #print("Visited cells: ")
                #print(self.visitedCells)
                return False
            else:
                return True

    def findEmptyCell(self):
        """ Returns the list
            that contains row and column information
            of the empty cell"""
        return list(self.matrix.keys())[list(self.matrix.values()).index(0)]

    """
    table = Table()
    table.printTable()
    table.shiftLeft()
    table.shiftUp()
    table.shiftRight()
    table.shiftRight()
    table.shiftDown()
    table.shiftDown()
    table.printTable()
    print(table.visitedCells)
    """