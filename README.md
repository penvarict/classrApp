# Classr Application
**Main Contributors: Ryan Wisniewski & Charlie Penvari**

Classr is a light weight desktop app that will track college credits and will allow users to plan out their college career. 

**Current Project Status**

The project is stable with minimal bugs. See project board to see known bugs.

**Where to Find Information**

Inside the \Planning Resources\ directory is the original proposal for the project. Currently, that document is a good starting point to understanding what the end result might look like and what features can be implemented.  

Also, on GitHub we are using the project boards to track bugs and things that need to be done. 

**Dependencies**

- **Python 3.7 or later, Virtual Environment is included but not configured with PyQt5**

- PyQt5.QtWidgets
  - We import all (*) currently
- PyQt5.QtCore
  - Qt (we need Qt package for scroll bar policies)
- sys (included in Python 3)
- logging (included in Python 3)
- math (included in Python 3)



**Contribution Guide**

Clone the repository. Off of the main branch, create a working branch that is named 'GitHubUsername-FeatureName'.

In pull requests, please specify the files that were changed and why they were changed in the pull request description. 

If you have ideas for features, you may add to the project board on this Github Repository. You may also create your own branch and then add drawings for UI improvements to the Planning Resources directory. From there, put in a pull request and we will get to reviewing it as soon as possible.

## User Guide

**Basic use case: (see README.PDF for user guide with images)** 

1. Click 'Add Semester' to get your first semester table.

<img src="C:\Users\Charlie\Desktop\UseGuide1.png" alt="UseGuide1" style="zoom:67%;" />

2. You can name your semester in the line edit box above the table.![UseGuide2](C:\Users\Charlie\Desktop\UseGuide2.png)

3. Click "Add Course" to add a row in the table.![UseGuide3](C:\Users\Charlie\Desktop\UseGuide3.png)

4. Input course and credit hours in the respective columns.<img src="C:\Users\Charlie\Desktop\UseGuide4.png" alt="UseGuide4" style="zoom: 200%;" />

5. Double click any cell to sum credit hours.<img src="C:\Users\Charlie\Desktop\UseGuide5.png" alt="UseGuide5" style="zoom:200%;" />

6. To delete the last added course, click "Delete Last Course"![UseGuide6](C:\Users\Charlie\Desktop\UseGuide6.png)
7. To add another semester click the "Add Semester" button at the lower right hand side.

![UseGuide7](C:\Users\Charlie\Desktop\UseGuide7.png)

8. To save, click file.![UseGuide8](C:\Users\Charlie\Desktop\UseGuide8.png)

9. Click save.![UseGuide9](C:\Users\Charlie\Desktop\UseGuide9.png)
10. Input save name, saves are formatted in .txt only. ![UseGuide10](C:\Users\Charlie\Desktop\UseGuide10.png)



### Other Use Cases

To open a previous save, launch the program -> click File -> click Open -> select the save file -> click open. The application should open up that previously made plan. 

To create a new plan, save the current working plan, exit program, open program, then create the new plan using steps in the section above. 

### Known Bugs

See Projects on the Classr repository, go to,  Project Features and Organization board. Currently, there is no delete semester function in the code, so a know bug is that if you create a plan with more semesters than the plan you want to open, the program crashes.
