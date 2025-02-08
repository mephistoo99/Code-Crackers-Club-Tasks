array = []
a = int(input("Enter the number of integers: "))
for i in range(a):
    integer = int(input(f"Enter integer {i + 1}: "))
    array.append(integer)
target = int(input("Enter the target number: "))

def indice(array, target):
    for i in range(len(array)):
        y = target - array[i]
        for a in range(i + 1, len(array)):
            if array[a] == y:
                return [i, a]
    
print(indice(array, target))
