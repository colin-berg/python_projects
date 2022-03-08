"""
This program computes the area of a Circle and Triangle 
"""

print "The Calculator is starting up"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Input radius: "))
  area = 3.14159 * radius ** 2 
  print str(area)
elif option == "T":
  base = float(raw_input("Input base: "))
  height = float(raw_input("Input height: "))
  area = 0.5 * base * height
  print str(area)
else:
  print "You have entered an invalid shape"

print "The program is exiting"
