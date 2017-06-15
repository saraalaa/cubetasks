def date(a,b,c):
    d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    dk={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if c%4==0:
        if b>=1 and b<=12:
            rang=dk[b]
            if a<=rang and a>=1:
                return True
            else:
                return False
        else:
            return False
    elif c%4!=0:
        if b>=1 and b<=12:
            rang=d[b]
            if a<=rang and a>=1:
                return True
            else:
                return False
        else:
            return False

print(date(28,2,2001))
