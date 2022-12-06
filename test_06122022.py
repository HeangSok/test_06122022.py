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
