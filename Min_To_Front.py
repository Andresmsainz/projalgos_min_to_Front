#MinToFront
def mintofront(lst):
    newlst = []
    minval = 0

    #find min value
    for i in range(0, len(lst)):
        if i == 0:
            minval = lst[i]
        if lst[i] < minval:
            minval = lst[i]

    print("minval = ", minval)
    newlst.append(minval) 

    for i in range(0, len(lst)):
        if lst[i] != minval:
            newlst.append(lst[i]) 

    return newlst

mylst = [3,-1,1,2,4]
mylst2 = [1,6,-4,-2,-7,-2]
print("mintofront",mintofront(mylst))
print("mintofront",mintofront(mylst2))

