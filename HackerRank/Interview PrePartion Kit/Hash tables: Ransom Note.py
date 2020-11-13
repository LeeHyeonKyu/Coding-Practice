def checkMagazine(magazine, note):
    for note_str in note :
        if not note_str in magazine :
            print('No')
            return
        else :
            magazine.remove(note_str)
    print('Yes')
