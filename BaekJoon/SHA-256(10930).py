import hashlib

def main(S):
    return hashlib.sha256(S.encode()).hexdigest()

S = input()
print(main(S))