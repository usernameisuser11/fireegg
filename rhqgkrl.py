for i in range(2, 10, 1):
    print(f"# {i}단 #", end="  ")
print("\n")


for j in range(1, 10):
    for i in range(2, 10):
        print(f"{i} x {j} = {i*j:<3}", end="  ")
    print()  
