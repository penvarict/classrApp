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
        self.semesters[self.semestersAdded].setRowCount(5)
        # Column count
        self.semesters[self.semestersAdded].setColumnCount(2)

        #create the columns and rows of QTableWidgetItems. This is where the user types in classes and credits.
        for i in range(5):
            for j in range(2):
                self.semesters[self.semestersAdded].setItem(i, j, QTableWidgetItem(""))

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


#each semester should be its own custom QTableWidget
class SemesterItem(QTableWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.layout.addWidget(AddCourseButton())
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())














