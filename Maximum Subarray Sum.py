array = []
a = int(input("enter the number of elements :"))
for i in range(a):
    b = int(input(f"enter the element {i+1}:"))
    array.append(b)
c = array[0] 
for i in range(len(array)):
    d = 0
    for e in range(i,len(array)):
        d += array[e]
        if d > c :
            c = d 
print(c)            