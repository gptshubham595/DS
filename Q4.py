x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4.04, 6.56, 10.67, 13.73, 16.14, 19.14, 21.94, 25.67, 27.98, 30.64]

def mean_val(a):
    s = 0
    for i in range(len(a)):
        s+=a[i]
    return s/float(len(a))

def calculate_para(a, b):
    n = len(a)
    s = 0
    t = 0
    a_mean = mean_val(a)
    b_mean = mean_val(b)
    for i in range(n):
        s+=(a[i]-a_mean)*(b[i]-b_mean)
    for i in range(n):
        t+=(a[i]-a_mean)*(a[i]-a_mean)
    b1 = s/float(t)
    b0 = b_mean-b1*a_mean
    print(b1)
    print(b0)

calculate_para(x,y)