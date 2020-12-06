#from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import pickle
from PyQt5.QtCore import Qt
import sys, logging,math
# Boilerplate configuration for logging debugger.
logging.basicConfig(format='%(message)s',level='DEBUG')

# Basic Debug enable/disable functionality. If there is no command line argument, then there is no debugging
try:
    DEBUG_FLAG = sys.argv[1]
except IndexError:
    logging.debug("Application Logging disabled. No logging command line args given.")
    DEBUG_LEVEL = 10
    logging.disable(DEBUG_LEVEL)


# todo: implement persist functionality
# todo: implement universal color theming such that it is not just white and grey

# Initialize Application Constants for window (Parent Widget)
APPLICATION_WINDOW_TITLE = 'classr - College Career Planner'
DEFAULT_WINDOW_POSITION_LEFT = 0
DEFAULT_WINDOW_POSITION_RIGHT = 0
WINDOW_MINIMUM_HEIGHT = 675
WINDOW_MINIMUM_WIDTH = 1900
INITIAL_COLUMNS = 1

# Initialize UI, Clickable Items Constants.
PUSH_BUTTON_WIDTH = 150
PUSH_BUTTON_HEIGHT = 40

# This is our main window, the parent widget. Our App class inherits from QWidget not QWindow since QWidget offers
# additional flexibility.
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        #--semesters will be a dictionary of semesters, which will soon be custom widgets
        self.semestersAdded = 0
        self.semesters = {}

        #--initialize the main widget and scrolling area
        self.scrollable = QScrollArea()
        self.centralWidget = QWidget()

        #--set our window parameters
        self.setMinimumHeight(WINDOW_MINIMUM_HEIGHT)
        self.setMinimumWidth(WINDOW_MINIMUM_WIDTH)
        self.setWindowTitle(APPLICATION_WINDOW_TITLE)
        self.setGeometry(DEFAULT_WINDOW_POSITION_LEFT,DEFAULT_WINDOW_POSITION_RIGHT,WINDOW_MINIMUM_WIDTH,WINDOW_MINIMUM_HEIGHT)

        #--initialize our layout to grid layout and set it
        self.centralLayout = QGridLayout()
        self.centralWidget.setLayout(self.centralLayout)

        #--initialize our AddSemesterButton (extends QPushButton)
        #--and populate centralLayout with elements
        self.lowerAddSemesterButton = AddSemesterButton()
        self.centralLayout.addWidget(self.lowerAddSemesterButton, 4, 1)

        #--define clicked event.
        self.lowerAddSemesterButton.clicked.connect(self.addSemester)

        #--configure scrollable
        self.scrollable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollable.setWidget(self.centralWidget)
        self.scrollable.setWidgetResizable(True)

        #-set the central widget to the scrollable area. Note that the scrollable area
        #-- is central widget.
        self.setCentralWidget(self.scrollable)

        #--Define a QAction for opening previous save
        openFile = QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.fileOpen)

        #--Define QAction for saving a current plan
        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.fileSave)

        #--Define the menubar and add the actions to fileMenu.
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(True)
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        #--Show the window
        self.show()
        # End Init

    #-addSemester is a clicked event intended for the AddSemesterButton QPushButton.
    def addSemester(self):
        #--upon the call of the function, set the newest item in semester dict to SemesterItem().
        #---SemesterItem() is a custom class that inherits from QWidgets.
        self.semesters[self.semestersAdded] = SemesterItem()
        #add the semester widget accordingly
        if self.semestersAdded % 2 == 0:
            self.centralLayout.addWidget(self.semesters[self.semestersAdded], self.semestersAdded / 2, 0)
        else:
            self.centralLayout.addWidget(self.semesters[self.semestersAdded], (self.semestersAdded- 1) / 2, 1)
        self.semestersAdded +=1

    #-file_open is an action for opening a previous save file
    def fileOpen(self):
        #print(self.semesters[0].semesterTable.numberOfRows)

        name = QFileDialog.getOpenFileName(self, 'Open File')[0]
        file = open(name, 'r')
        totalRows = int(file.readline())
        totalColumns = int(file.readline())

        self.semesters[0].semesterTable.setNumberOfRows(totalRows)
        print("x")

        i = 0

        while (i <= totalRows):
            j = 0
            while (j <= totalColumns):
                inputLine = file.readline()
                self.semesters[0].semesterTable.writeCell(i, j, inputLine)
                print("Y")
                j = j + 1
            i = i + 1

        file.close()

    #-file_save is an action for saving a given plan.
    def fileSave(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')[0]
        file = open(name, 'w')
        #file.write(str(self.semesters[0].semesterTable.numberOfRows) + "\n")
        file.write(str(self.semestersAdded) + "\n")
        #-loop through all the semesters and add their information to the file
        for semester in self.semesters.values():
            totalRows = semester.semesterTable.rowCounter() - 2
            print(totalRows)
            totalColumns = semester.semesterTable.columnCounter() - 1
            semesterTitle =semester.getSemesterTitle() #type str
            #in the save file: the first line is the semester's title
            file.write(semesterTitle+"\n")
            #-in the save file the 2nd line is the semester's number
            file.write(str(self.semestersAdded)+"\n")
            #-in the save file the #st line is the number of rows (courses)
            file.write(str(totalRows) + "\n")
            #-in the save file the # line is the number of columns
            file.write(str(totalColumns) + "\n")


            i = 0
            while(i <= totalRows):
                j = 0
                while(j <= totalColumns):
                    file.write(str(semester.semesterTable.readCell(i, j)) + "\n")
                    j = j + 1
                i = i + 1

        file.write("-EndOfFileKey- \n")

        file.close()


class AddSemesterButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Add A Semester')
        self.setFixedWidth(150)
        self.setFixedHeight(40)

class AddCourseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Add a course')
class DelCourseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(150)
        self.setFixedHeight(40)
        self.setText("Delete Last Course")

class SemestertitleBox(QLineEdit):
    def __init__(self):
        super().__init__()

# SemesterItem inherits from QWidget. This is the 'container' widget that holds the table, title, and Delete button.
# Beware that Add Course button belongs to the SemesterItemTable.
class SemesterItem(QWidget):
    number_of_semesters = 0
    def __init__(self):
        super().__init__()
        self.number_of_semesters +=1 #debug variable

        #--Initialize UI objects
        self.layout = QVBoxLayout()
        self.semesterTitle = SemestertitleBox()
        self.delCourseButton = DelCourseButton()
        self.semesterTable = SemesterItemTable() #initialize the SemesterItemTable (extends QTableWidget)

        #--Configure UI, and layout set helper variables
        self.setMinimumWidth(self.frameGeometry().width())
        self.setMinimumHeight(self.frameGeometry().height())
        self.courseColumnWidth = math.floor(self.frameGeometry().width())

        #--Configure table properties
        self.semesterTable.horizontalHeader().setVisible(True) # We want a horizontal header on our table
        self.semesterTable.setColumnWidth(0, self.courseColumnWidth)
        self.semesterTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.semesterTable.setHorizontalHeaderLabels(['Course','Hours']) #set the column labels
        self.semesterTable.verticalHeader().setVisible(False) # We do not want vertical row headers
        self.semesterTable.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        #--Add widgets to our layout.
        #---(Reminder: For each semester item we use a Vertical box layout
        self.layout.addWidget(self.delCourseButton)
        self.layout.addWidget(self.semesterTitle)
        self.layout.addWidget(self.semesterTable)
        self.setLayout(self.layout)

        #--Define clicked event for delete course button
        self.delCourseButton.clicked.connect(self.semesterTable.delCourseEvent)

        #--Debugging code. Logging console out for DEBUG level
        logging.debug(f"Course Column Width = {self.courseColumnWidth}")
        logging.debug(f"Semester widget width = {self.frameGeometry().width()}")
        logging.debug(f"Semester widget height = {self.frameGeometry().height()}")

    def getSemesterTitle(self):
        return self.semesterTitle.text()


# SemesterItemTable extends QTableWidget. This is the UI elt where the user can input the
# courses and credit hours.
class SemesterItemTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.numberOfRows = INITIAL_COLUMNS
        self.setRowCount(1)
        self.setColumnCount(2)
        self.addCourseButton = AddCourseButton()
        self.addCourseButton.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        self.setCellWidget(self.rowCount() - 1,0,self.addCourseButton)
        self.addCourseButton.clicked.connect(self.addCourseEvent)

    #--define what heppens when the user clicks on Add Course
    def addCourseEvent(self):
        self.insertRow(self.numberOfRows-1)
        self.numberOfRows += 1
        logging.debug("The number of rows: " + str(self.numberOfRows))

    #--define what happends when the user clicks on Delete last Course
    def delCourseEvent(self):
        if self.numberOfRows > 1:
            self.removeRow(self.numberOfRows-2)
            self.numberOfRows -= 1
        logging.debug("The number of rows: " + str(self.numberOfRows))

    def setNumberOfRows(self, input):
        print("z")
        while(input < self.numberOfRows - 2):
            self.delCourseEvent()
        while(input > self.numberOfRows - 2):
            self.addCourseEvent()

    def readCell(self, row, column):
        return self.item(row, column).text()

    def writeCell(self, row, column, textToEnter):
        print("a")
        #self.item(row, column).setText(textToEnter)
        self.setItem(row, column, QTableWidgetItem(textToEnter))

    def rowCounter(self):
        return self.rowCount()

    def columnCounter(self):
        return self.columnCount()

# Boilerplate runner code.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())
