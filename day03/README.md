# Code golf

Copy this line of 196 chararacters into a Python REPL
```python
d=open("i").readlines();[sum([c-38-58*(c>97)for c in map(ord,map(max,b))])for b in[[set(r[:len(r)//2])&set(r[len(r)//2:])for r in d],[set(d[i])&set(d[i+1])&set(d[i+2])for i in range(0,len(d),3)]]]
```

Once encoded into UTF-16 it is 123 characters long.
```python
exec(bytes('㵤灯湥∨≩⸩敲摡楬敮⡳㬩獛浵嬨ⵣ㠳㔭⨸挨㤾⤷潦⁲⁣湩洠灡漨摲洬灡洨硡戬⤩⥝潦⁲⁢湩孛敳⡴孲氺湥爨⼩㈯⥝猦瑥爨汛湥爨⼩㈯崺昩牯爠椠⁮嵤嬬敳⡴孤嵩☩敳⡴孤⭩崱☩敳⡴孤⭩崲昩牯椠椠⁮慲杮⡥ⰰ敬⡮⥤㌬崩嵝','u16')[2:])
```
