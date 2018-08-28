numbers = []

def ex33Loop(n, increment):
    i = 0
    while i < n: 
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

ex33Loop(100, 5)