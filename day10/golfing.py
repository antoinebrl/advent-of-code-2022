from itertools import*
a,b=list(zip(*[[(i+1)*x*(i%40==19),"\n"*(i%40==0)+".#"[x-2<i%40<x+2]]for i,x in enumerate(accumulate([1]+[int(x)if x[-1].isdigit()else 0 for x in open("i").read().split()]))]))
print(sum(a),"".join(b))