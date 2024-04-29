# Appending list elements
friends = ["George", "Dan", "Sean", "Sam"]
print(friends)
friends.append("Daniel")
print(friends)
# Inserting a value in a list
friends.insert(0, "Tim")
print(friends)
friends.insert(2, "Emma")
print(friends)
# Deleting a value from a list
del friends[0]
print(friends)
# Adding Tim in again (he is still my friend)
friends.insert(0, "Tim")