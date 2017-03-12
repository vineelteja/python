                ########## Decision Making
# Most Important Thing to Remember in Python "INDENTATION", if you miss the indentation your code will not work.
# Instead of { } as block, Indentation keeps your code aligned and maintains the block
# Decision Making, we are going to learn if, if-else, else-if
# lets declare a statement
year = 2017                                 # year = 2017

# if statement used to check if the statement is meeting our specified condition, use if and condition with ':'

if (year > 2000):
    print("You are in 2017")

# if (condition) is true the if block will get executed, or statements outside if blocks will get executed

if (year < 2020):
    print("You are living in present 2017")
else:
    print("You are living in future")

# if (condition) is true then if block will get executed, or else Block will get executed

if (year < 2020):
    print("You are living in present 2017")
elif(year > 2017):
    print("you are living in future")
else:
    print("You are living in 2017")

# if (condition) is true then if block will get executed or next condition in elif is checked if elif is true, then that block is executed
# there can be any number of elif statements if all the elif statements are false.  else Block will get executed