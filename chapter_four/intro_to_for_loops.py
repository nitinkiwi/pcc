songs = ['happy', 'beyond', 'sledgehammer', 'murmuration', 'man of colours']
song_number = 0
print()
for song in songs:
    print(f"{song.title()} is an excellent song!")
    if song_number == 4:
        break
    else:
        song_number = song_number + 1
    print(f"The next song is {songs[song_number].title()}.\n")

print('That is the end of the playlist.\n')
    
