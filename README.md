![advent of code banner](https://camo.githubusercontent.com/45e775d95451f2bda211ee757d1a959671cf4c762feb1e7ccaca59925704e333/68747470733a2f2f626c6f67732e7361702e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f31312f456b616f5151545845414d4134424e2e6a7067)

# Advent of Code - 2022

## Installation

Recommended python version: 3.10
- Day 3, 5 and 21 use the walrus operator `:=` introduced in Python 3.8.
- Day 7 solution leverages the `match` statement introduced in Python 3.10.
- Day 11 and 20 need Python 3.9 for type annotations.

```shell
virtualenv -p python3 .venv --prompt aoc-2022
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```shell
python dayXX/main.py
```

## Code Golf

> Code golf is a type of recreational computer programming competition in which participants strive to achieve the shortest possible source code that solves a certain problem - [Wikipedia](https://en.wikipedia.org/wiki/Code_golf)

### Instruction
Move into the folder: `cd dayXX`. For the shortest solution, open a python shell and copy the code snippet.
You can also run `python golfing.py`. The benefit of the python shell is that you don't need to call `print()`
to display the computed values.

Do you know you can encode your code in UTF-16? The solution is a bit less readable but way shorter.
As this is controversal in the code golfing community I reported the length of both the raw code and the encoded version.

### Solutions
- Day 1 - 94/76 chars:
    ```Python
    c=sorted([sum(map(int,e.split("\n")))for e in open("i").read().split("\n\n")])
    c[0],sum(c[:3])
    ```
    ```Python
    exec(bytes('㵣潳瑲摥嬨畳⡭慭⡰湩ⱴ⹥灳楬⡴尢≮⤩昩牯攠椠⁮灯湥∨≩⸩敲摡⤨献汰瑩∨湜湜⤢⥝瀊楲瑮挨せⱝ畳⡭季㌺⥝ ','u16')[2:])
    ```
- Day 2 - 122/90 chars
    ```Python
    [*map(sum,zip(*[[b+1+(b-a+1)%3*3,b*3+(a+b-1)%3+1]for a,b in[[ord(l[0])-65,ord(l[2])-88]for l in open("i").readlines()]]))]
    ```
    ```Python
    exec(bytes('牰湩⡴⩛慭⡰畳Ɑ楺⡰嬪扛ㄫ⠫ⵢ⭡⤱㌥㌪戬㌪⠫⭡ⵢ⤱㌥ㄫ晝牯愠戬椠孮潛摲氨せ⥝㘭ⰵ牯⡤孬崲⴩㠸晝牯氠椠⁮灯湥∨≩⸩敲摡楬敮⡳崩⥝崩 ','u16')[2:])
    ```
- Day 3 - 196/127 chars
    ```Python
    d=open("i").readlines()
    [sum([c-38-58*(c>97)for c in map(ord,map(max,b))])for b in[[set(r[:len(r)//2])&set(r[len(r)//2:])for r in d],[set(d[i])&set(d[i+1])&set(d[i+2])for i in range(0,len(d),3)]]]
    ```
    ```Python
    exec(bytes('㵤灯湥∨≩⸩敲摡楬敮⡳਩牰湩⡴獛浵嬨ⵣ㠳㔭⨸挨㤾⤷潦⁲⁣湩洠灡漨摲洬灡洨硡戬⤩⥝潦⁲⁢湩孛敳⡴孲氺湥爨⼩㈯⥝猦瑥爨汛湥爨⼩㈯崺昩牯爠椠⁮嵤嬬敳⡴孤嵩☩敳⡴孤⭩崱☩敳⡴孤⭩崲昩牯椠椠⁮慲杮⡥ⰰ敬⡮⥤㌬崩嵝 ','u16')[2:])
    ```
- Day 4 - 218/138 chars
    ```Python
    import re
    [*map(sum,zip(*[[r[0]<=r[2]<=r[3]<=r[1]or r[2]<=r[0]<=r[1]<=r[3],r[0]<=r[2]<=r[1]or r[2]<=r[0]<=r[3]]for r in[list(map(int,re.search(r"(\d+)-(\d+),(\d+)-(\d+)",l).groups()))for l in open("i").readlines()]]))]
    ```
    ```Python
    exec(bytes('浩潰瑲爠੥牰湩⡴⩛慭⡰畳Ɑ楺⡰嬪牛せ㱝爽㉛㱝爽㍛㱝爽ㅛ潝⁲孲崲㴼孲崰㴼孲崱㴼孲崳爬せ㱝爽㉛㱝爽ㅛ潝⁲孲崲㴼孲崰㴼孲崳晝牯爠椠孮楬瑳洨灡椨瑮爬⹥敳牡档爨⠢摜⤫⠭摜⤫⠬摜⤫⠭摜⤫Ⱒ⥬朮潲灵⡳⤩昩牯氠椠⁮灯湥∨≩⸩敲摡楬敮⡳崩⥝崩 ','u16')[2:])
    ```
- Day 6 - 114/86 chars
    ```Python
    f=lambda d,m:min(i+m for i in range(len(d))if len(d[i:i+m])==len(set(d[i:i+m])))
    d=open("i").read()
    f(d,4),f(d,14)
    ```
    ```Python
    exec(bytes('㵦慬扭慤搠洬洺湩椨洫映牯椠椠⁮慲杮⡥敬⡮⥤椩⁦敬⡮孤㩩⭩嵭㴩氽湥猨瑥搨楛椺洫⥝⤩搊漽数⡮椢⤢爮慥⡤਩牰湩⡴⡦Ɽ⤴昬搨ㄬ⤴ ','u16')[2:])
    ```
- Day 10 - 218/134 chars
    ```Python
    from itertools import*
    a,b=zip(*[[(i+1)*x*(i%40==19),"\n"*(i%40==0)+".#"[x-2<i%40<x+2]]for i,x in enumerate(accumulate([1]+[int(x)if x[-1].isdigit()else 0 for x in open("i").read().split()]))])
    print(sum(a),"".join(b))
    ```
    ```Python
    exec(bytes('牦浯椠整瑲潯獬椠灭牯⩴愊戬氽獩⡴楺⡰嬪⡛⭩⤱砪⠪╩〴㴽㤱Ⱙ尢≮⠪╩〴㴽⤰∫⌮嬢⵸㰲╩〴砼㈫嵝潦⁲Ⱪ⁸湩攠畮敭慲整愨捣浵汵瑡⡥ㅛ⭝楛瑮砨椩⁦學ㄭ⹝獩楤楧⡴攩獬⁥‰潦⁲⁸湩漠数⡮椢⤢爮慥⡤⸩灳楬⡴崩⤩⥝਩牰湩⡴畳⡭⥡∬⸢潪湩戨⤩','u16')[2:])
    ```
