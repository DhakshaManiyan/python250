Exercise 243 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(5, 25, 3) and return a list of its elements squared only for the elements that are less than or equal to 16.

cph = [i ** 2 for i in range(5, 25, 3) if i <= 16]
 
print(cph)
