from sys import argv

#get filename as a paramater
script, filename = argv

#create the txt binding and point it to an instance of the filename e.g. create file object
txt = open(filename)

#print filename and contents of file object named txt
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

#Do it again using prompt instead of argv
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

#use the read method of the fileobject to print the contents
print(txt_again.read())
txt_again.close()