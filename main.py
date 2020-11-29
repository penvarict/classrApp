#from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
import sys, logging,math
# Boilerplate configuration for logging debugger.

logging.basicConfig(format='%(message)s',level='DEBUG')

# Basic Debug enable/diable functionality. If there is no command line argument, then there is no debugging
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
WINDOW_MINIMUM_HEIGHT = 506
WINDOW_MINIMUM_WIDTH = 900
INITIAL_COLUMNS = 1

# Initialize UI, Clickable Items Constants.
PUSH_BUTTON_WIDTH = 150
PUSH_BUTTON_HEIGHT = 40

# This is our main window, the parent widget. Our App class inherits from QWidget not QWindow since QWidget offers
# additional flexibility.
class App(QWidget):
    def __init__(self):
        super().__init__()
        #--semesters will be a dictionary of semesters, which will soon be custom widgets
        self.semestersAdded = 0
        self.semesters = {}
        #--set our window parameters
        self.setMinimumHeight(WINDOW_MINIMUM_HEIGHT)
        self.setMinimumWidth(WINDOW_MINIMUM_WIDTH)
        self.setWindowTitle(APPLICATION_WINDOW_TITLE)
        self.setGeometry(DEFAULT_WINDOW_POSITION_LEFT,DEFAULT_WINDOW_POSITION_RIGHT,WINDOW_MINIMUM_WIDTH,WINDOW_MINIMUM_HEIGHT)

        #--initialize our layout to grid layout
        self.layout = QGridLayout()

        #--populate with elements
        self.lowerAddSemesterButton = AddSemesterButton()
        self.layout.addWidget(self.lowerAddSemesterButton, 4, 1)
        self.lowerAddSemesterButton.clicked.connect(self.addSemester)
        self.setLayout(self.layout)

        self.addingSave = Example()
        self.layout.addWidget(self.addingSave, 1, 1)

        self.show()

    # addSemester is a clicked event intended for the AddSemesterButton QPushButton.
    def addSemester(self):
        #--upon the call of the function, set the newest item in semester dict to SemesterItem().
        #---SemesterItem() is a custom class that inherits from QWidgets.
        self.semesters[self.semestersAdded] = SemesterItem()
        #add the semester widget accordingly
        if self.semestersAdded % 2 == 0:
            self.layout.addWidget(self.semesters[self.semestersAdded], self.semestersAdded / 2, 0)
        else:
            self.layout.addWidget(self.semesters[self.semestersAdded], (self.semestersAdded- 1) / 2, 1)
        self.semestersAdded +=1


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        openFile = QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        self.show()

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')

    def file_save(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')

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

        #--Configure UI, set helper variables
        self.setMinimumWidth(self.frameGeometry().width())
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

# Boiler plate runner code.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())
