"""PyCalc is a simple calculator built with Python and PyQt."""

import sys
import time
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6 import QtTest
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import (
    QTimer
)

ERROR_MSG = "ERROR"
WINDOW_SIZE = 535
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
M = 9

class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku")
        #self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refreshUI)

    def _createDisplay(self):
        self.solveButton = QPushButton("Solve it!")
        self.solveButton.clicked.connect(self._solveIt) 
        self.generalLayout.addWidget(self.solveButton)
        
    def _solveIt(self):
        self.timer.start(10)
        if (Suduko(self.keyBoard, 0, 0)):
            self.puzzle(self.keyBoard)
        else:
            print("Solution does not exist:(")
        self.timer.stop()

    def _refreshUI(self):
        self.puzzle(self.keyBoard)

    def puzzle(self, a):
        for i in range(M):
            for j in range(M):
                answer = self.keyBoard[i][j]
                self.buttonMap[i * 10 + j].setText(str(answer) if answer > 0 else "")

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        self.keyBoard = [
            [2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]
            ]

        for row, keys in enumerate(self.keyBoard):
            for col, key in enumerate(keys):
                buttonKey = row*10 + col
                textColor = "black" if key > 0 else "blue"
                self.buttonMap[buttonKey] = QPushButton(str(key) if key > 0 else "")
                self.buttonMap[buttonKey].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                self.buttonMap[buttonKey].setStyleSheet("color: " + textColor + "; font: bold 16px;")
                buttonsLayout.addWidget(self.buttonMap[buttonKey], row, col)

        self.generalLayout.addLayout(buttonsLayout)

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
            
    for x in range(9):
        if grid[x][col] == num:
            return False

    # QtTest.QTest.qWait(1)
    
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):

    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
    
        if solve(grid, row, col, num):
        
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    #PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()