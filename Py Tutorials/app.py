from math import *
xvalue1 =  int(input("enter x value 1 "))
xvalue2 =  int(input("enter x value 2 "))
xvalue3 =  int(input("enter x value 3 "))
xvalue4 =  int(input("enter x value 4 "))
xvalue5 =  int(input("enter x value 5 "))
yvalue1 = xvalue1**2 + 5
yvalue2 = xvalue2**2 + 5
yvalue3 = xvalue3**2 + 5
yvalue4 = xvalue4**2 + 5
yvalue5 = xvalue5**2 + 5
step_value = xvalue2 - xvalue1
print("start x value ", + xvalue1)
print("end x value", + xvalue5)
X_value = {xvalue5, xvalue4, xvalue3, xvalue2, xvalue1}
Y_value = {yvalue5, yvalue4, yvalue3, yvalue2, yvalue1}
table_of_values = [
    ["Xvalue  ,Yvalue"],
    [xvalue1  ,yvalue1],
    [xvalue2  ,yvalue2],
    [xvalue3  ,yvalue3],
    [xvalue4  ,yvalue4],
    [xvalue5  ,yvalue5],
]
print(table_of_values)