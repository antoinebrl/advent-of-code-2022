c=sorted([sum(map(int,e.split("\n")))for e in open("i").read().strip().split("\n\n")])
print(c[0],sum(c[:3]))