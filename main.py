from PyQt5.QtWidgets import *
import sys

#app = QApplication([])
#label = QLabel('Hello World!')
#label.show()
#app.exec_()

#app2 = QApplication(sys.argv)

#tableWidget = QTableWidget(5, 2)

#print("Input a class name.")
#test = input()
#tableWidget.setItem(0, 0, QTableWidgetItem(test))

#print("Enter the credit hours of that class.")


#app2.exec_()
#Initialize Application Constants
APPLICATION_WINDOW_TITLE = 'classr - College Career Planner'
DEFAULT_WINDOW_POSITION_LEFT = 0
DEFAULT_WINDOW_POSITION_RIGHT = 0
WINDOW_MINIMUM_HEIGHT = 506
WINDOW_MINIMUM_WIDTH = 900


# Main Window, our App class inherits from QWidget, which is the base class
# for UI objects.
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = APPLICATION_WINDOW_TITLE
        self.left = DEFAULT_WINDOW_POSITION_LEFT
        self.top = DEFAULT_WINDOW_POSITION_RIGHT
        self.width = WINDOW_MINIMUM_WIDTH
        self.height = WINDOW_MINIMUM_HEIGHT
        self.tables = {}
        self.setMinimumHeight(self.height)
        self.setMinimumWidth(self.width)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.layout = QGridLayout()
        self.layout.addWidget(QPushButton("Add Semester"),1,1)
        self.createSemesterTables()
        for k in range(8):
            if k % 2 == 0:
                self.layout.addWidget(self.tables[k], k / 2, 0)
            else:
                self.layout.addWidget(self.tables[k], (k - 1) / 2, 1)

       
        self.setLayout(self.layout)

        # Show window
        self.show()

    def createSemesterTables(self):

        for k in range(8):
            self.tables[k] = QTableWidget()

            # Row count
            self.tables[k].setRowCount(5)

            # Column count
            self.tables[k].setColumnCount(2)

            #create the columns and rows of qTableWidgetItems
            for i in range(5):
                for j in range(2):
                    self.tables[k].setItem(i, j, QTableWidgetItem(""))

        #self.tableWidget2 = QTableWidget()

        # Row count
        #self.tableWidget2.setRowCount(5)

        # Column count
        #self.tableWidget2.setColumnCount(2)

        #for i in range(5):
        #    for j in range(2):
        #        self.tableWidget2.setItem(i, j, QTableWidgetItem(""))



        #self.tableWidget.setItem(0, 0, QTableWidgetItem(""))
        #elf.tableWidget.setItem(0, 1, QTableWidgetItem(""))
        #self.tableWidget.setItem(1, 0, QTableWidgetItem(""))
        #self.tableWidget.setItem(1, 1, QTableWidgetItem(""))
        #self.tableWidget.setItem(2, 0, QTableWidgetItem(""))
        #self.tableWidget.setItem(2, 1, QTableWidgetItem(""))
        #self.tableWidget.setItem(3, 0, QTableWidgetItem(""))
        #self.tableWidget.setItem(3, 1, QTableWidgetItem(""))
        #self.tableWidget.setItem(4, 0, QTableWidgetItem(""))
        #self.tableWidget.setItem(4, 1, QTableWidgetItem(""))

        # Table will fit the screen horizontally
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(
        #    QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())














