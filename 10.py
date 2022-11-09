#create a list where each element of the list is a digit of a given number
num=input("Enter any number=")
l=[]
for i in num:
    l.append(i)
print([int(e) for e in l ])
