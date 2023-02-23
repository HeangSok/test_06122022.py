**Task**: 

Using Python 3.6 and Qt4, please prepare a GUI based SMPTE timecode Calculator. 
You can leverage active projects on the Internet to assist in your development. Please prepare the calculator so it runs as a standalone program. 
You can use this online TC Calculator as an example of the functionality: https://robwomack.com/timecode-calculator/ 
Useful Resource Projects that you can leverage for your test. 
SMPTE Time code projects 
https://github.com/eoyilmaz/timecode 
https://gist.github.com/manneohrstrom/8033e178cd38589b0226b45cef1dfe30 
Python Qt Calculator Project 
https://realpython.com/python-pyqt-gui-calculator/ 
Ideally I would like to see a working “Time Code Calculator” where I can input various time codes and see the correct output if I change the frame rate. As per the online example above. 
It will need to support at least the following frame rates: 23.976, 23.98, 24, 25, 29.97, 30, 50, 59.94, 60 fps (frames per second) 
Once completed (or much as you can achieve in an hour) then post the project to your personal github account or equivalent for us to review. 
Hint: We will be reviewing your code, so well commented code will be advantageous. 
P.S. The test will last one hour and it doesn’t need to be concluded (if you don't have time), but try to do as much as possible. 
Good Luck!


**Solution:**

**Step1:** Install PyQt4 package
You can use pip to install PyQt4 package.
````python
pip install PyQt4
````

**Step2:** Design the user interface

The first step is to design the user interface of the calculator. You can use Qt Designer tool to create the interface. In the interface, you should include the following:

- A combo box to select the frame rate
- Text boxes to input the hours, minutes, seconds, and frames
- A button to calculate the timecode
- A label to display the timecode result

**Step3:** Convert the UI file to Python

Once the user interface is designed, you need to convert the UI file to a Python file. You can use the pyuic4 tool that comes with PyQt4 package to do this.

````Python
pyuic4 -o ui_timecode_calculator.py timecode_calculator.ui
````

**Step4:** Write the application code
In the Python file, you need to write the application code to calculate the timecode based on the user input. You can use the timecode module to perform the calculation. Here's an example code snippet that shows how to calculate the timecode:

````Python
import timecode

def calculate_timecode(frame_rate, hours, minutes, seconds, frames):
    tc = timecode.Timecode(frame_rate, hours=hours, minutes=minutes, seconds=seconds, frames=frames)
    return str(tc)
````

In the above code, frame_rate is the selected frame rate from the combo box, and hours, minutes, seconds, and frames are the input values from the text boxes.

**Step5**: Connect UI elements to application code

Finally, you need to connect the UI elements to the application code. You can use the QtCore and QtGui modules from PyQt4 package to do this. Here's an example code snippet that shows how to connect the UI elements to the application code:

````Python
import sys
from PyQt4 import QtCore, QtGui
from ui_timecode_calculator import Ui_TimecodeCalculator

class TimecodeCalculator(QtGui.QMainWindow):
    def __init__(self):
        super(TimecodeCalculator, self).__init__()
        self.ui = Ui_TimecodeCalculator()
        self.ui.setupUi(self)

        self.ui.btn_calculate.clicked.connect(self.calculate)

    def calculate(self):
        frame_rate = float(self.ui.cmb_frame_rate.currentText())
        hours = int(self.ui.txt_hours.text())
        minutes = int(self.ui.txt_minutes.text())
        seconds = int(self.ui.txt_seconds.text())
        frames = int(self.ui.txt_frames.text())

        timecode = calculate_timecode(frame_rate, hours, minutes, seconds, frames)

        self.ui.lbl_result.setText(timecode)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TimecodeCalculator()
    window.show()
    sys.exit(app.exec_())
 ````
 
In the above code, TimecodeCalculator is the main application class that inherits from QtGui.QMainWindow class. It creates an instance of the UI class Ui_TimecodeCalculator and connects the clicked signal of the Calculate button to the calculate method. The calculate method reads the input values from the UI elements, calls the calculate_timecode function to perform the calculation, and updates the result label.

