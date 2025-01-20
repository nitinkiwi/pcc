friends = []
more_friends = True
more_friends = input('Do you have any friends? (yes/no) ')
if more_friends == 'no':
    more_friends = False
else:
    more_friends = True

while more_friends == True:
    friends.append(input('Who is a good friend of yours? '))
    print(f'Your friend(s) are {", ".join(friends)}.')
    more_friends = input('Do you have any more friends? (yes/no) ')
    if more_friends == 'yes':
        more_friends = True
    else:
        more_friends = False
if len(friends) == 0:
    print("I'm sorry you don't have any friends.")
else:
    print(f'Your final list of friend(s) is {", ".join(friends)}.')