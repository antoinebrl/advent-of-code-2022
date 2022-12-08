f=lambda d,m:min(i+m for i in range(len(d))if len(d[i:i+m])==len(set(d[i:i+m])))
d=open("i").read()
print(f(d,4),f(d,14))