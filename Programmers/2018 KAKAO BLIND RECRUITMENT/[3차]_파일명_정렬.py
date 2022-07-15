def solution(files):
    f_dict = dict()
    for idx, f in enumerate(files):
        tmp = []
        head, num = '', -1
        for char in f:
            if char.isalpha() or char in [' ', '-', '.']:
                if head == '':
                    tmp.append(char)
                else:
                    num = int(''.join(tmp))
                    break
            elif char.isdigit():
                if head == '':
                    head = ''.join(tmp).lower()
                    tmp = [char]
                else:
                    tmp.append(char)
        if num == -1:
            num = int(''.join(tmp))
        
        f_dict[f] = dict({'head':head, 'num':num, 'idx':idx})

    files = sorted(files, key=lambda x: (f_dict[x]['head'], f_dict[x]['num'], f_dict[x]['idx']))
    return files

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))