formatter = "{} {} {} {}"

#take the formatter string binding and use the format method
#the format method places the item from the 
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#since there is nothing being passed, the {}s are returned. 
#Formatter is called 4 times for 16 total {}s
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your", 
    "Own text here", 
    "Maybe a poem", 
    "Or a song about fear"
))