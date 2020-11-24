from PyQt5.QtWidgets import *
import sys, logging,math
logging.basicConfig(format='%(message)s',level='DEBUG')

#Basic Debug enable/diable functionality. If there is no command line argument, then there is no debugging
try:
    DEBUG_FLAG = sys.argv[1]
except IndexError:
    logging.debug("Application Logging disabled. No logging command line args given.")
    DEBUG_LEVEL = 10
    logging.disable(DEBUG_LEVEL)


# todo: implement persist functionality
# todo: implement universal color theming such that it is not just white and grey
#Initialize Application Constants - WINDOW
APPLICATION_WINDOW_TITLE = 'classr - College Career Planner'
DEFAULT_WINDOW_POSITION_LEFT = 0
DEFAULT_WINDOW_POSITION_RIGHT = 0
WINDOW_MINIMUM_HEIGHT = 506
WINDOW_MINIMUM_WIDTH = 900
INITIAL_COLUMNS = 1

#Initialize UI, Clickable Items Constants
# todo: extract the constants used for button size and pos to here. Scope is global fyi


# Main Window, our App class inherits from QWidget, which is the base class
# for UI objects.
class App(QWidget):
    def __init__(self):
        super().__init__()
        #semesters will be a dictionary of semesters, which will soon be custom widgets
        self.semestersAdded = 0
        self.semesters = {}
        #set our window parameters
        self.setMinimumHeight(WINDOW_MINIMUM_HEIGHT)
        self.setMinimumWidth(WINDOW_MINIMUM_WIDTH)
        self.setWindowTitle(APPLICATION_WINDOW_TITLE)
        self.setGeometry(DEFAULT_WINDOW_POSITION_LEFT,DEFAULT_WINDOW_POSITION_RIGHT,WINDOW_MINIMUM_WIDTH,WINDOW_MINIMUM_HEIGHT)

        #initialize our layout to grid layout
        self.layout = QGridLayout()
        #populate with elements
        self.lowerAddSemesterButton = AddSemesterButton()
        self.layout.addWidget(self.lowerAddSemesterButton, 4, 1)
        self.lowerAddSemesterButton.clicked.connect(self.addSemester)
        self.setLayout(self.layout)

        # Show window
        self.show()



    #addSemester is a clicked event intended for the AddSemesterButton QPushButton.
    def addSemester(self):

        self.semesters[self.semestersAdded] = SemesterItem()
        #add the semester widget accordingly
        if self.semestersAdded % 2 == 0:
            self.layout.addWidget(self.semesters[self.semestersAdded], self.semestersAdded / 2, 0)
        else:
            self.layout.addWidget(self.semesters[self.semestersAdded], (self.semestersAdded- 1) / 2, 1)
        self.semestersAdded +=1


class AddSemesterButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Add A Semester')

class AddCourseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Add a course')
class DelCourseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(100)
        self.setFixedHeight(20)
        self.setText("Delete Last Course")

#each semester should be its own custom QTableWidget
class SemesterItem(QWidget):
    number_of_semesters = 0
    def __init__(self):
        super().__init__()
        self.number_of_semesters +=1
        self.layout = QVBoxLayout()
        self.semesterWidgetWidth = self.frameGeometry().width()
        self.courseColumnWidth = math.floor(self.semesterWidgetWidth) - 20

        # initialize our buttons and elts
        self.semesterTable = SemesterItemTable()
        self.semesterTable.setMinimumWidth(639)
        self.semesterTable.horizontalHeader().setVisible(False)
        self.semesterTable.verticalHeader().setVisible(False)
        self.semesterTable.setColumnWidth(0, self.courseColumnWidth)
        self.semesterTable.setColumnWidth(1, self.courseColumnWidth/4)
        self.delCourseButton = DelCourseButton()
        #add buttons to the layout
        self.layout.addWidget(self.delCourseButton)
        self.delCourseButton.clicked.connect(self.semesterTable.delCourseEvent)
        self.layout.addWidget(self.semesterTable)
        self.setLayout(self.layout)
        logging.debug("Semester widget width: "+ str(self.semesterWidgetWidth))


class SemesterItemTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.numberOfRows = INITIAL_COLUMNS
        self.setRowCount(1)
        self.setColumnCount(2)
        self.addCourseButton = AddCourseButton()
        self.setCellWidget(self.rowCount() - 1,0,self.addCourseButton)
        self.addCourseButton.clicked.connect(self.addCourseEvent)


    def addCourseEvent(self):
        self.insertRow(self.numberOfRows-1)
        self.numberOfRows += 1
        logging.debug("The number of rows: " + str(self.numberOfRows))

    def delCourseEvent(self):
        if self.numberOfRows > 1:
            self.removeRow(self.numberOfRows-2)
            self.numberOfRows -= 1
        logging.debug("The number of rows: " + str(self.numberOfRows))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())














