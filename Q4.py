first = input()
second = input()
third = input()

if third != first and second != first:
  print('BOTH MISMATCH')
elif second != first:
  print('ENTRY 2 MISMATCH')
elif third != first:
  print('ENTRY 3 MISMATCH')
else:
  print('OK')
