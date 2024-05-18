trees = ["pine", "cyprus", "beech", "oak"]
print(trees)
print(f"The forests of New Zealand are full of {trees[2]} trees.")
not_native = trees.pop()
print(trees)
print(f"{not_native.title()} trees were introduced into New Zealand.")
evergreen = "pine"
trees.remove("pine")
print(trees)
print(f"{evergreen.title()} trees stay green thoughout the winter.")
del trees[1]
print(trees)