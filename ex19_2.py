from sys import argv

filename, cheese, crackers = argv

def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("Run using argv")
cheese_and_crackers(cheese,crackers)

print("Run using user input")
cheesePrompt = input("How much cheese? ")
crackerPrompt = input("How many crackers? ")
cheese_and_crackers(cheesePrompt,crackerPrompt)