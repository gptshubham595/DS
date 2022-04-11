import math
x = [2, 3, -1, 2, 2, -1, -2, 1, 4, 0]
y = [4, 9, 1, 4, 4, 1, 4, 1, 16, 0]

def mean_val(a):
    s = 0
    for i in range(len(a)):
        s+=a[i]
    return s/float(len(a))

def sig_xiyi(a, b):
    s = 0
    for i in range(len(a)):
        s+=a[i]*b[i]
    return s

def pear_corr(a, b):
    n = len(a)
    s = (sig_xiyi(a, b) - len(a)*mean_val(a)*mean_val(b))
    t = math.sqrt(sig_xiyi(a, a) - n*mean_val(a)*mean_val(a))*math.sqrt(sig_xiyi(b, b) - n*mean_val(b)*mean_val(b))
    return s/float(t)

def get_rank(a):
    n = len(a)
    l = []
    pos = 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if(a[j]<a[i]):
                pos+=1
            elif(a[j]==a[i]):
                cnt+=1
        p = pos + float(cnt-1)/2
        l.append(p)
        pos = 1
        cnt = 0
    return l

def spear_corr(a, b):
    r1 = get_rank(a)
    r2 = get_rank(b)
    return pear_corr(r1, r2)
print(spear_corr(x, y))
