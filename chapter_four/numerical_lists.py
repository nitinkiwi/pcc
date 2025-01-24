for value in range(1,6):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []

for value in range(1,11):
    squares.append(value**2)

print(squares)

numbers = [1,2,3,4,5,6,7,8,9,0]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

cubes = [value**3 for value in range(1,11)]

print(cubes)

many_numbers = [value for value in range(1,10000001)]

print(sum(many_numbers))

one_to_twenty = [value for value in range(33,21,2)]

print(one_to_twenty)