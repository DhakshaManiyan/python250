#Exercise 116 - Conditionals
#Considering the code below, write code that prints out True! if x has at least 8 elements and the element positioned at index 6 is a floating-point number and prints out False! otherwise.
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
 
if len(x) >= 8 and type(x[6]) is float:
    print("True!")
else:
    print("False!")
