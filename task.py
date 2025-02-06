array = []
a = int(input("enter the number of integers:"))
for i in range(a):
    integer = float(input(f"enter integer {i+1}:"))
    array.append(integer)
target = int(input("enter the target number :"))

def indice(x,y):
    for i in range(len(x)) :
        d =i+1
        for a in range(d,len(x)):
            if x[i]+x[a]==y :
                return([i,a])   
    
print(indice(array, target))   


