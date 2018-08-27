from sys import argv
#get file name in argv form

script, filename = argv
#text explaining application
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")
#open a delete contents
print("Opening the file...")
target = open(filename, 'w')
target.truncate()
#repace with new lines
print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#print contents 
target.write(f"{line1} \n {line2} \n {line3} \n")

print("And finally, we close it.")
target.close()