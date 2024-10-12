a=int(input())
b=int(input())
c=int(input())
if a>b>c or a>c>b:
    print("большее:", a)
elif b>=a>=c or b>=c>=a:
    print("большее:", b)
elif c>=a>=b or c>=b>=a:
    print("большее:", c)
