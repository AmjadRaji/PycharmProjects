print("welcome to my program")
print("")
start_x_value = int(input("enter starting x value = "))
end_x_value = int(input("enter ending y value = "))
step_value = int(input("enter step value = "))

x_value = (range(start_x_value, end_x_value, step_value))
print("")

print("x value     y value")
for int in range(start_x_value, end_x_value + 1, step_value ):
    print(" ", int, "     ", int**2 + 5)

print(" ")
print(" ")
print("Thank You For Using My Program")