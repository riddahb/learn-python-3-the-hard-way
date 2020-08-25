# This is a veriable of the amount of "types of people"
types_of_people = 10
# This is a variable that contains the element f which allows this string to add the variable types_of_people within the double quotation.
x = f"There are {types_of_people} types of people"
# This is a variable that stores the word "binary" in binary 
binary = "binary"
# This is a var that stores the words 'don't' inside the variable do_not
do_not = "don't"
# This stores the string and combines the string with the variable binary which stores the word "binary", and the variable do_not, which stores the word "don't" inside this string, creating a statement "Those who know binary and those who don't." using the f element to combine the variable with the string.
y = f"Those who know {binary} and those who {do_not}"
# This presents the words in the statement in the x variable combining the variables with the initial string
print(x)
#This presents the words in the statement in the y variable combining the variables with the initial string
print(y)
# This presents the words "I said:"" alongside the variable which stores the x variable string using the f statement allowing the variable to be incorporated within the string.
print(f"I said: {x}")
# This presents the words "I also said:"" alongside the variable which stores the y variable string, using the f statement allowing the variable to be incorporated within the string.. 
print(f"I also said:{y}")
# This stores the word False inside the variable hilarious
hilarious = False
# This stores the string "Isn't that joke so funny?!" inside the variable joke_evaluation.
joke_evaluation = "Isn't that joke so funny?!"
# This presents the statement of joke evaluation alongside 'format' of hilarious = 'False' 
print(joke_evaluation,format(hilarious))
# This is a var
w = "This is the left side of..."
# This is a var
e = "a string with a right side."
# prints the variables a + e together
print (w + e)