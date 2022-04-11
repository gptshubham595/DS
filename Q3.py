x = [23, 14, 17, 16, 24, 13, 15, 11, 32, 20]
y = [10, 6, 12, 11, 12, 5, 15, 9, 11, 12]
nc2 = 45    #calculate manually
def kendall_corr(a, b):
    nc = 0
    nd = 0
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if((a[i]-a[j])*(b[i]-b[j])>0):
                nc+=1
            else:
                nd+=1
    return (nc-nd)/float(nc2)

print(kendall_corr(x, y))