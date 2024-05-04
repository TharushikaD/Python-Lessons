x = [5,6,7]

for val in x:
    print(val)


for index,val in enumerate(x):
    if 6 == val:
        print("index- ",index)

# range(start,stop,step)  

for x in range (2,10,2):
    print(x)


# while loops

x = "python"
count = 1

while True:
    if count < 100:
        print(x *count)
    else:
        break
    count = count+1    
      