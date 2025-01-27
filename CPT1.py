mostocc = 0
def Most_Occurring_Element(a) :
    b=0
    for i in a:
        c = a.count(i)
        if c > b :
            b = c
            mostocc = i
    return mostocc

arr = []
a=int(input("entrer le nombre des elements :"))
for i in range(a):
    b=input(f"entrer l'element {i+1}:")
    arr.append(b)
print(Most_Occurring_Element(arr))   
