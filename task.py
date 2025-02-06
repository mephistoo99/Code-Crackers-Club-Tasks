array = []
a = int(input("enter the number of integers:"))
for i in range(a):
    integer = float(input(f"enter integer {i+1}:"))
    array.append(integer)
target = int(input("enter the target number :"))

def indice(x,y):
    for a in x :
        for i in range(1,len(x)):
            if a+x[i]==y :
                return([x.index(a),i])   
    
print(indice(array, target))   

