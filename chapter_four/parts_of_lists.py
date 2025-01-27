animals = ['dogs', 'cats', 'birds', 'lizards', 'snakes', 'insects', 'spiders', 'monkeys', 'fish']

print('Here are three animals from the start of the list:')
for animal in animals[:3]:
    print(animal.title())

print('Here are three animals from the middle of the list:')
for animal in animals[3:6]:
    print(animal.title())

print('Here are three animals from the end of the list:')
for animal in animals[-3:]:
    print(animal.title())