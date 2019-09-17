#latihan python
name = int(input("banyak baris = "))
for i in range(1,name+1):
    #print(i)
    for j in range(name-i,0,-1):
        print("#", end="")
    for j in range(0,2*i-1):
        print("*", end="")
    print()

# for i in range(1,2):
#     print(i)
