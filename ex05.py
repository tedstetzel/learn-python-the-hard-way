name = 'Ted Stetzel'
age = 35 
height = 70 #inches
weight = 180 #lbs
weightKilos = round(weight * 0.453592,2)
heightCentimeters = height * 2.54
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That is {heightCentimeters} centimeters tall.")
print(f"He's {weight} pounds")
print(f"That is {weightKilos} kilograms")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teetch are usually {teeth} depending on the coffee.")

#this line is tricky
total = age + height + weight
print(f"If I ad {age}, {height}, and {weight} I get {total}.")

