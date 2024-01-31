count = 0
valid = 0
while count in range(12):
  word = input()
  difference = int(word[0]) - int(word[-1])
  if difference == 1 or difference == -1:
    valid += 1
  count += 1
print(valid)
