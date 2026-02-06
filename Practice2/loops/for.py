#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex5
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#ex6
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#ex7
for x in [0, 1, 2]:
  pass