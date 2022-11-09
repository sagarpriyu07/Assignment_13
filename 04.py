#change values in a list
thislist=['Java','SQL','C','Reactnative','Javascript','Python']
thislist[thislist.index('Reactnative')]='Flutter'
thislist.insert(thislist.index('SQL'),'NoSQL')
print(thislist)