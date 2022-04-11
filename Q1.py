import math
x = [1, 3, 10, 2, 9, 6, 10, 1, 5, 2]
y1 = [3, 9, 30, 6, 27, 18, 30, 3, 15, 6]
y2 = [4, 12, 103, 7, 84, 39, 103, 4, 28, 7]
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

print(pear_corr(x, y1))
print(pear_corr(x, y2))
print(pear_corr(e, f))