x1, v1, x2, v2 = map(int, input().split(" "))


try:
    # Arithmetic Progression
    n = ((x2 - x1) / (v1 - v2)) + 1
    if n > 0 and n.is_integer():
        print("YES")
    else: 
        print("NO")
except:
    # devision by zero
    print("NO")