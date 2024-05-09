total=0
number=0

for i in range(1,101,2):
    print(i)
    total+=i
    if i%7 ==0:
        number+=i
    
print("總和",total)

print(number)

for i in range(1,101,2):
    if i%5 ==0 and i%15 ==0:
        print(i)
      


    
        

    