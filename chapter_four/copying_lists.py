my_pizza = ['onion', 'marinara sauce', 'cheese', 'olives', 'capsicum', 'artichoke']

friends_pizza = my_pizza[:]

friends_pizza.append('salami')
friends_pizza.append('ham')

print('\nMy favourite pizza has:\n')
for toppings in my_pizza:
    print(toppings.title())

print("\nMy friend's favourte pizza has:\n")
for toppings in friends_pizza:
    print(toppings.title())