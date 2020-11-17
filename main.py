from PyQt5.QtWidgets import *
import sys

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
        self.lowerAddSemesterButton = AddSemesterButton()
        self.layout.addWidget(self.lowerAddSemesterButton, 4, 1)
        self.lowerAddSemesterButton.clicked.connect(self.addSemester)
        self.setLayout(self.layout)

        # Show window
        self.show()



    #addSemester will add a semester widget to the app layout. Is intended for .clicked event
    #on the AddSemesterButton QPushButton.
    def addSemester(self):


        self.semesters[self.semestersAdded] = SemesterItem()
        # Row count
        self.semesters[self.semestersAdded].setRowCount(1)
        # Column count
        self.semesters[self.semestersAdded].setColumnCount(2)


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
        self.setFixedWidth(100)
        self.setFixedHeight(20)
        self.setText('Add a course')
class DelCourseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Delete Last Course")

#each semester should be its own custom QTableWidget
class SemesterItem(QTableWidget):
    def __init__(self):
        super().__init__()
        self.numberOfCols = 2
        self.numberOfRows = INITIAL_COLUMNS
        self.layout = QGridLayout()
        self.addCourseButton = AddCourseButton()
        self.delCourseButton = DelCourseButton()
        self.layout.addWidget((self.delCourseButton))
        self.layout.addWidget(self.addCourseButton)
        self.addCourseButton.clicked.connect(self.addCourseEvent)
        self.delCourseButton.clicked.connect(self.delCourseEvent)
        self.setLayout(self.layout)

    def addCourseEvent(self):
        self.insertRow(self.numberOfRows)

    def delCourseEvent(self):
        self.removeRow(self.numberOfRows)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())














