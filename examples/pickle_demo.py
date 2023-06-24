import pickle
class Testing():
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
a=[]
b=[]

a.append(Testing(50,"Greg"))
a.append(Testing(48,"Jenn"))

with open ('test.pkl','wb') as out_file:
    for p in range(0,len(a)):
        pickle.dump (a[p],out_file)

with open ('test.pkl','rb') as in_file:
    while True:
        try:
            b.append(pickle.load(in_file))
        except EOFError:
            break

for x in range(0,2):
    print (b[x].name,b[x].age)