
from math import *
x_value1 = int(input("enter x value 1 "))
x_value2 = int(input("enter x value 2 "))
x_value3 = int(input("enter x value 3 "))
x_value4 = int(input("enter x value 4 "))
x_value5 = int(input("enter x value 5 "))
y_value1 = x_value1**2 + 5
y_value2 = x_value2**2 + 5
y_value3 = x_value3**2 + 5
y_value4 = x_value4**2 + 5
y_value5 = x_value5**2 + 5
step_value = x_value2 - x_value1
print("start x value", + x_value1)
print("end x value", + x_value5)
table_of_values = [
    ["X value   ,Y value"],
    [x_value1   ,y_value1],
    [x_value2   ,y_value2],
    [x_value3   ,y_value3],
    [x_value4   ,y_value4],
    [x_value5   ,y_value5],
]
print(table_of_values)