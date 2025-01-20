instruments = ['piano', 'guitar', 'drums', 'saxophone']
print(f"Here is the origional list: {instruments}.")
print(f"Here is the alphabetically sorted list: {sorted(instruments)}.")
print(f"Here is the origional list again: {instruments}.")
print()
instruments.reverse()
print(f'Here is the list in reverse order: {instruments}.')
instruments.reverse()
print(f'Here is the length of the list: {len(instruments)}.')
print(f'Instruments: {", ".join(instruments)}.')

*instruments, sep=", "