for i in range(100000):
    lst = [1,0,0]           # one car and two goats
    random.shuffle(lst)     # shuffles the list randomly
    
    ran = random.randrange(3) # gets a random number for the random guess

    user = lst[ran] #storing the random guess 

    del(lst[ran]) # deleting the random guess

    huh = 0
    for i in lst: # getting a value 0 and deleting it
        if i ==0:
            del(lst[huh]) # deletes a goat when it finds it
            break
        huh+=1
