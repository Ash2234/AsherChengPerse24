amount = int(input())
if amount <= 5:
  print(amount)
else:
  remainder = amount % 5
  amount -= remainder
  
  days = amount // 5
  total = 0
  i = 1
  while i <= days:
    total += (i * 5)
    i += 1
    
  total += (i - 1) * 5
  total += remainder
  print(total)
