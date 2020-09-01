# on line we have whats called an import. This is how you add features to your script from the python feature set. 
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your scond variable is:", second)
print("Your third variable is:", third)