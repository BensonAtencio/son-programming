def add_it_up(x):
    try:
        result = sum(range(x + 1))

    except TypeError:
        result = 0

    return result

x = int(input("Enter Number: "))

print(add_it_up(x))