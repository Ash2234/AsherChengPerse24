encrypted = str(input())
front = encrypted[:2]
back = encrypted[2:]

decrypted = back + front
print(decrypted)
