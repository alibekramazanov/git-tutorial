#ex1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#ex2
print(bool("Hello"))
print(bool(15))

#ex3
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))