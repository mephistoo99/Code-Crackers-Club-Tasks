c = []
a = input("enter a string :")
b= a.upper()
for i in b :
    if i != " " :
        c.append(i) 
d = len(c)-1
e = int(len(c)/2)        
for i in range(e):
    if c[i]!=c[d]:
        print("not a palindrome.")
        break
    else :
        d = d-1
if i == e-1 :
    print("it's a palindrome.")        
     
