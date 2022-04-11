x = [25, 26, 27, 28, 29, 30]
y = [101.75, 105.75, 109.75, 113.75, 117.75, 121.75]

b1 = 2.982
b0 = 1.252

y_hat = []
n = len(y)
for i in range(n):
    y_hat.append(b0+b1*float(x[i]))

def mean_val(a):
    s = 0
    for i in range(len(a)):
        s+=a[i]
    return s/float(len(a))

e = 0
f = 0
y_mean = mean_val(y)
for i in range(n):
    e+=(y[i]-y_hat[i])*(y[i]-y_hat[i])
    f+=(y[i]-y_mean)*(y[i]-y_mean)

r2 = 1-(e/float(f))
print(r2)