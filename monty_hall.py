import random
switch = 0
for i in range(100000):
    lst = [1,0,0]           
    random.shuffle(lst)     
    
    ran = random.randrange(3) 

    user = lst[ran]  

    del(lst[ran]) 

    huh = 0
    for i in lst: 
        if i == 0:
            del(lst[huh]) 
            break
        huh += 1
    if lst[0] == 1: 
        switch += 1
print("Switch =", switch)
