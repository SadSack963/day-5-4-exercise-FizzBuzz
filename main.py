#Write your code below this row 👇

for x in range(1, 101):
    if x % 3 != 0 and x % 5 != 0:
        print(x, end='')
    if x % 3 == 0:
        print("Fizz", end='')
    if x % 5 == 0:
        print("Buzz", end='')
    print("")
