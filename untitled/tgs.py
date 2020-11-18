
start_x_value = int(input("Enter starting x value = "))
End_x_value = int(input("Enter end x value = "))
step_value = int(input("Enter step value = "))

x_value = (range(start_x_value, End_x_value, step_value))
print("")

print("x value    y value")
for int in range(start_x_value, End_x_value + 1, step_value):
    print(" ", int, "        ", int**2 + 5)

print(""
      "TYFMP")