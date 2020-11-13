from collections import Counter

def checkMagazine(magazine, note):
    mag_c = Counter(magazine)
    note_c = Counter(note)
    if mag_c & note_c == note_c :
        print('Yes')
    else :
        print('No')
