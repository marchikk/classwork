elements = []

while True : 
    a=input("enter element type or quit :")
    if a != "quit":
        elements += [a]
    else:
        break

print("Elements:" , elements )