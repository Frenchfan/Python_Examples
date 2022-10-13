def dif_max_min(mylist):
    min = 1
    max = 0
    for i in mylist:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)  
    print(f"Разница составила: {max-min}")
mylist = [1.1, 1.2, 3.1, 5, 10.01]
dif_max_min(mylist)