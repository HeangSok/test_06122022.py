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


````python3
#!/bin/python3

# ------------note---------------
# Started: 10:20 am. Ended: 11:02 am 

# frame_rate = [23.976, 23.98, 24, 25, 29.97, 30, 50, 59.94, 60]

# Tool: timcode (pip3 install timecode)

# Alternative Soluction: Using lambda (ex: result = lambda x, y : x + y)


# ------------end-of-note---------------

from timecode import Timecode

try:
    time_operand1, fps_operand1 = input("Please input your time using this format (HH:MM:SS:FF): "), input("Your fps is: ")

    time_operand2,fps_operand2 = input("Please input your time using this format (HH:MM:SS:FF): "), input("Your fps is: ")

    operator = input("Please select (add | sub | mul | div): ") 

    def timecode_calculator(operator, time_operand1, time_operand2, fps_operand1, fps_operand2):
        """Simple math operations like, addition, subtraction, multiplication or division with an integer value or with a timecode is possible. """
        
        timecode1 = Timecode(fps_operand1, time_operand1)
        timecode2 = Timecode(fps_operand2, time_operand2)

        if operator == "add":
            timecode_after_cal = timecode1 + timecode2
            return timecode_after_cal.frames
        elif operator == "sub":
            timecode_after_cal = timecode1 - timecode2
            return timecode_after_cal.frames
        elif operator == "mul":
            timecode_after_cal = timecode1 * timecode2
            return timecode_after_cal.frames
        elif operator == "div":
            timecode_after_cal = timecode1 / timecode2
            return timecode_after_cal.frames   
            

    result = timecode_calculator(operator, time_operand1, time_operand2, fps_operand1, fps_operand2)

    print(result)

except:
    print("Something went wrong!")

````
